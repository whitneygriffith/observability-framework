# Creates Calls to Flask API 
import requests
import logging  
from os import environ 

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
)

trace.set_tracer_provider(TracerProvider())

trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)

url = environ.get("api_url", "http://127.0.0.1:800")

for request in range(10): 
    try: 
        logging.info(f"Client Request {request} started for jokes")
        jokes = requests.get(url + '/jokes')
        logging.info(f"Client Request {request} started for hello")
        hello = requests.get(url + '/hello')
        logging.info(f"Client Request {request} ended successfully for hello and jokes")
    except Exception as e:
        logging.exception(f"Client Execption Occurred {e}")
