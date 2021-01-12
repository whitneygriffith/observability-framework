import requests 

from flask import Flask, request

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


app = Flask(__name__)

@app.route("/jokes", methods=["GET"])
def jokes():
    url = "https://official-joke-api.appspot.com/random_joke"
    try: 
        response = requests.get(url).json()
        return app.response_class(response=response, status=200, mimetype="application/text")
    except: 
        return app.response_class(response="Internal Server Error", status=response.status_code, mimetype="application/text")


if __name__ == "__main__":
  app.run(port=8082)