
from __future__ import annotations

import httpx
import json 
from datetime import datetime
import uuid
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from opentelemetry.sdk.resources import Resource
import logging

from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from presidio_analyzer import AnalyzerEngine
import boto3
from presidio_analyzer.nlp_engine import NlpEngineProvider
import time
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.metrics import get_meter


OTEL_COLLECTOR_ENDPOINT= "https://otelcol.g58o14d6u7j6c.us-east-2.cs.amazonlightsail.com"
OBEX_BUCKET="obex-config-dev"
DLP_CONFIG_PATH="dlp/dlp.json"
API_KEYS_PATH="api-keys/{0}/key.json"

class ObexConfig:
	def __init__(self, aws_session):
		if aws_session is None:
			aws_session = boto3.Session()  
		self.s3_client = aws_session.resource('s3')
		self.get_aws_user_name(aws_session)

	def get_aws_user_name(self, aws_session):
		self.user = aws_session.client('sts').get_caller_identity().get('Arn').split(":")[5]

	def read_file_from_s3(self, path):
		try:
			obj = self.s3_client.Object(OBEX_BUCKET, path).get()
			data = obj['Body'].read().decode('utf-8')
			return json.loads(data)
		except Exception as e:
			raise Exception("Error reading the Obex config file from S3: " 
				   + str(e) + ". Please check if you have the right permissions.")
	
	def get_dlp_config(self):
		dlp_config = self.read_file_from_s3(DLP_CONFIG_PATH)["dlp"]
		return dlp_config

	def get_api_key(self, provider):
		path = API_KEYS_PATH.format(provider)
		api_key = self.read_file_from_s3(path)["key"]
		return api_key
	
	def get_user(self):
		return self.user

	def get_org(self):
		return "Acme Inc."

class ObexDLPBlocker:
	def __init__(self, config_provider):
		self.config_provider = config_provider
		configuration = {
			"nlp_engine_name": "spacy",
			"models": [{"lang_code": "en", "model_name": "en_core_web_sm"}],
		}
		provider = NlpEngineProvider(nlp_configuration=configuration)
		nlp_engine = provider.create_engine()
		self.block_analyzer = AnalyzerEngine(nlp_engine=nlp_engine)

	def check(self, text):
		dlp_config = self.config_provider.get_dlp_config()
		self.block_entities = []
		for z in dlp_config['preset']:
			if z['status'] == "Block":
				self.block_entities.append(z['name'])
		if not self.block_entities: return None
		block_results = self.block_analyzer.analyze(text=text,entities=self.block_entities, language='en')
		return block_results


resource = Resource(attributes={SERVICE_NAME: "obex"})
_logger = logging.getLogger("obex")
_logger.propagate = False
p_logger = logging.getLogger("presidio-analyzer")
p_logger.propagate = False

exporter = OTLPLogExporter(endpoint=OTEL_COLLECTOR_ENDPOINT+"/v1/logs")
logger_provider = LoggerProvider(resource=resource)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
handler = LoggingHandler(level=logging.DEBUG, logger_provider=logger_provider)
_logger.addHandler(handler)
_logger.setLevel(logging.DEBUG)

otlp_exporter = OTLPMetricExporter(endpoint=OTEL_COLLECTOR_ENDPOINT+"/v1/metrics")
reader = PeriodicExportingMetricReader(otlp_exporter, export_interval_millis=1)
provider = MeterProvider(metric_readers=[reader], resource=resource)
metrics.set_meter_provider(provider)
meter = get_meter("obex-counts")
total_counter = meter.create_counter("total")


class ObexLogger:	
	def log(self, data):
		_logger.debug(json.dumps(data))

class ObexMetrics:	
	def counter(self, actrl_fail, dlp_fail):
		total_counter.add(1)


class Obex:
	def __init__(self,*, aws_session=None):
		self.config = ObexConfig(aws_session)
		self.logger = ObexLogger()
		self.metrics = ObexMetrics()
		self.dlp_blocker = ObexDLPBlocker(self.config)
	
	def get_provider(self, url):
		if "openai" in url.__str__():
			return "openai"
		elif "anthropic" in url.__str__():
			return "anthropic"
		return "unknown"
	
	def get_model(self, request_body):
		if '"model": "claude-3' in request_body:
			return "Claude-3"
		if '"model": "gpt-3.5-turbo' in request_body:
			return "GPT-3.5-turbo"
		return "unknown"

	def build_audit_object(self, request, request_body, dlp_check):
		data = {}		
		data["type"] = "obex_ai_call_event"
		data["uid"] = str(uuid.uuid4())
		data["url"] = str(request.url)
		data["timestamp"] = str(datetime.now())
		data["prompt"] = request_body
		data["user"] = self.config.get_user()
		data["org"] = self.config.get_org()
		data["provider"] = self.get_provider(request.url)
		data["model"] = self.get_model(request_body)
		data["dlp"] = str(dlp_check)
		data["status"] = "Success" if not dlp_check else "Blocked [DLP]"
		return data
	
	def set_auth_header(self, request):
		provider = self.get_provider(request.url)
		if provider == "openai":
			request.headers['authorization'] = "Bearer " + self.config.get_api_key("openai")
		if provider == "anthropic":
			request.headers['x-api-key'] =  self.config.get_api_key("anthropic")

	def protect(self, func):

		oldsend = httpx.Client.send

		def new_send(*args, **kwargs):
			request = args[1]
			request_body = request.read().decode("utf-8")
			self.set_auth_header(request)
			dlp_check = self.dlp_blocker.check(request_body)
			audit_data = self.build_audit_object(request, request_body, dlp_check)
			self.logger.log(audit_data)
			total_counter.add(1)
			if dlp_check:
				responseContent = '{"msg": "Request blocked by Obex for violating DLP rules: ' + str(dlp_check) + '"}'
				return httpx.Response(status_code=403, request=request, json=responseContent)	
			z = oldsend(*args, **kwargs)
			return z

		def wrapper(*args, **kwargs):
			httpx.Client.send = new_send
			z = func(*args, **kwargs)
			httpx.Client.send = oldsend
			return z

		return wrapper

