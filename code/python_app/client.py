# Creates Calls to Flask API 
import requests
import logging  
from os import environ 
from flask import Flask, render_template     

# traces 
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

# logging configuration

LOGLEVEL = environ.get("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)

app = Flask(__name__)

url = environ.get("API_URL", "http://0.0.0.0:8000")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/jokes")
def jokes(): 
    try: 
        labels["endpoint"] = "jokes client"
        incoming_requests_counter.add(1, labels)
        logging.info(f"Client Request started for jokes")
        jokes = requests.get(url + '/jokes')
        logging.info(f"Client Request ended successfully for jokes")
        return jokes.text
    except Exception as e:
        logging.exception(f"Client Execption Occurred for jokes")

@app.route("/hello")
def hello():
    try: 
        labels["endpoint"] = "hello client"
        incoming_requests_counter.add(1, labels)
        logging.info(f"Client Request started for hello")
        hello = requests.get(url + '/hello')
        logging.info(f"Client Request ended successfully for hello")
        return hello.text
    except Exception as e:
        logging.exception(f"Client Execption Occurred for hello")


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    try:
        response = requests.get(url + '/hello')
        return app.response_class(response="API is live", status=200, mimetype="application/text")
    except Exception as e:
        return app.response_class(response=str(e), status=500, mimetype="application/text")


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)