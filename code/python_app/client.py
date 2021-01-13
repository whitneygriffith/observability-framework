# Creates Calls to Flask API 
import requests 
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

url = environ.get("api_url", "http://127.0.0.1:8000/jokes")
num_requests = 10

for request in range(num_requests): 
    try: 
        jokes = requests.get(url).json()
        # TODO: Log response 
    except Exception as e:
        # TODO: Log exception
        print(e)
