import requests 
import logging 

from flask import Flask, request

# traces
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
)
#from opentelemetry.instrumentation.flask import FlaskInstrumentor

#traces configuration
trace.set_tracer_provider(TracerProvider())

trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)

# metrics
from opentelemetry import metrics
from opentelemetry.sdk.metrics import Counter, MeterProvider
from opentelemetry.sdk.metrics.export import ConsoleMetricsExporter
from opentelemetry.sdk.metrics.export.controller import PushController


# metrics configuration
metrics.set_meter_provider(MeterProvider())
# TODO: get the global meter
meter = metrics.get_meter(__name__, True)
exporter = ConsoleMetricsExporter()
controller = PushController(meter, exporter, 5)
labels = {"environment": "dev", "endpoint" : ""}


incoming_requests_counter = meter.create_counter(
    name="requests",
    description="number of incoming requests",
    unit="1",
    value_type=int,
)

app = Flask(__name__)

# FlaskInstrumentor().instrument_app(app) TODO: responding with a Failed to detach context 

@app.route("/jokes", methods=["GET"])
def jokes():
    url = "https://official-joke-api.appspot.com/random_joke"
    try: 
        labels["endpoint"] = "jokes api"
        incoming_requests_counter.add(1, labels)
        logging.info(f"Server Request started for jokes")
        response = requests.get(url).json()
        logging.info(f"Server Request ended successfully for jokes")
        return response
    except Exception as e: 
        return app.response_class(response=str(e), status=response.status_code, mimetype="application/text")

@app.route("/hello")
def hello():
   labels["endpoint"] = "hello api"
   incoming_requests_counter.add(1, labels)
   return "hello world\n"


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000)