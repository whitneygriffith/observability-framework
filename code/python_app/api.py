import requests 
import logging 

from flask import Flask, request

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
)
from opentelemetry.instrumentation.flask import FlaskInstrumentor

trace.set_tracer_provider(TracerProvider())

trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)

app = Flask(__name__)

# FlaskInstrumentor().instrument_app(app) TODO: responding with a Failed to detach context 

@app.route("/jokes", methods=["GET"])
def jokes():
    url = "https://official-joke-api.appspot.com/random_joke"
    try: 
        logging.info(f"Server Request started for jokes")
        response = requests.get(url).json()
        logging.info(f"Server Request ended successfully for jokes")
        return response
    except Exception as e: 
        return app.response_class(response=str(e), status=response.status_code, mimetype="application/text")

@app.route("/hello")
def hello():
   return "hello world\n"


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000)