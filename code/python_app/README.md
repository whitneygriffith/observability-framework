# Introduction 

[api.py](./api.py)
[client.py](./client.py)
## Instrumentation 

Configuration of Tracing Provider is done through [Environment Variables](#environment-variables)

TODO: 
* Data source specific configuration
* Exporter configuration
    * span processor 
    * tracer provider 
    * logger 
* Propagator configuration
* Resource configuraton


### Traces Autoinstrumentation

[api.py](./api.py) is automatically instrumented for tracing by installing the relevant instrumentation libraries for the python site-packages used in the app which can be found [here](https://opentelemetry-python.readthedocs.io/en/stable/index.html#instrumentations) or can be recommended by running `opentelemetry-bootstrap --action=requirements`

To verify instrumentation: 

[Results for Traces](#traces-autoinstrumentation-results)



### Metrics Instrumentation

TODO: Bug when running gunicorn

```
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/local/Cellar/python@3.8/3.8.6_2/Frameworks/Python.framework/Versions/3.8/lib/python3.8/threading.py", line 932, in _bootstrap_inner
    self.run()
  File "/Users/whitneygriffith/Desktop/MicrosoftProjects/pwc-osic/observability-framework/code/python_app/venv/lib/python3.8/site-packages/opentelemetry/sdk/metrics/export/controller.py", line 48, in run
    self.tick()
  File "/Users/whitneygriffith/Desktop/MicrosoftProjects/pwc-osic/observability-framework/code/python_app/venv/lib/python3.8/site-packages/opentelemetry/sdk/metrics/export/controller.py", line 57, in tick
    self.accumulator.collect()
AttributeError: 'DefaultMeter' object has no attribute 'collect'
```


[Results for Metrics](#metrics-instrumentation-results)

# Build and Run App 

## Environment Variables

Traces
```
export OTEL_EXPORTER=otlp_span
export OTEL_EXPORTER_OTLP_SPAN_ENDPOINT="TODO: ENDPOINT_ADDRESS"
export OTEL_EXPORTER_OTLP_SPAN_PROTOCOL="TODO: grpc"
export OTEL_EXPORTER_OTLP_SPAN_INSECURE="True"
export OTEL_SERVICE_NAME="jokes_generator"
```
## Locally 

Create virtualenv `python -m venv venv`

Activate virtualenv `source venv/bin/activate`

Install packages `pip install -r requirements.txt`

### API 
`opentelemetry-instrument --exporter none --service-name jokes-api --ids-generator random python api.py`


### Client

`opentelemetry-instrument --exporter none --service-name jokes-client --ids-generator random python client.py`

## Docker 

TODO: Communicate between API and Client based on network settings
### API 

`DOCKER_BUILDKIT=1 docker build -t braveheartacr.azurecr.io/api -f API.Dockerfile  .`

`docker run -it  -p 127.0.0.1:8000:8000 braveheartacr.azurecr.io/api`

### Client 


`DOCKER_BUILDKIT=1 docker build -t braveheartacr.azurecr.io/client -f Client.Dockerfile  .`

`docker run -it -p 127.0.0.1:5000:5000 braveheartacr.azurecr.io/client`

# Test


## Traces Autoinstrumentation Results

### API Traces Sample

`opentelemetry-instrument --exporter none --service-name jokes-api --ids-generator random python3 api.py`

```
{
    "name": "HTTP GET",
    "context": {
        "trace_id": "0xa1ac62936f96a1fec8ec8b6c96119c26",
        "span_id": "0xc2f81eb5b90dc13f",
        "trace_state": "{}"
    },
    "kind": "SpanKind.SERVER",
    "parent_id": null,
    "start_time": "2021-01-13T15:57:48.546998Z",
    "end_time": "2021-01-13T15:57:48.553674Z",
    "status": {
        "status_code": "ERROR"
    },
    "attributes": {
        "component": "http",
        "http.method": "GET",
        "http.server_name": "127.0.0.1",
        "http.scheme": "http",
        "host.port": 5000,
        "http.host": "127.0.0.1:5000",
        "http.target": "/",
        "net.peer.ip": "127.0.0.1",
        "http.user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "net.peer.port": 55731,
        "http.flavor": "1.1",
        "http.status_text": "NOT FOUND",
        "http.status_code": 404
    },
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "0.16b1",
        "service.name": "jokes-api"
    }
}
127.0.0.1 - - [13/Jan/2021 07:57:48] "GET / HTTP/1.1" 404 -
{
    "name": "HTTP GET",
    "context": {
        "trace_id": "0xdbc286fc00c9f56348ecab6302b38f34",
        "span_id": "0x09e447839437d7e0",
        "trace_state": "{}"
    },
    "kind": "SpanKind.CLIENT",
    "parent_id": "0x8cc56c0bce77049a",
    "start_time": "2021-01-13T15:57:58.569115Z",
    "end_time": "2021-01-13T15:57:58.684249Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "component": "http",
        "http.method": "GET",
        "http.url": "https://official-joke-api.appspot.com/random_joke",
        "http.status_code": 200,
        "http.status_text": "OK"
    },
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "0.16b1",
        "service.name": "jokes-api"
    }
}
{
    "name": "/jokes",
    "context": {
        "trace_id": "0xdbc286fc00c9f56348ecab6302b38f34",
        "span_id": "0x8cc56c0bce77049a",
        "trace_state": "{}"
    },
    "kind": "SpanKind.SERVER",
    "parent_id": null,
    "start_time": "2021-01-13T15:57:58.568122Z",
    "end_time": "2021-01-13T15:57:58.686275Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "component": "http",
        "http.method": "GET",
        "http.server_name": "127.0.0.1",
        "http.scheme": "http",
        "host.port": 5000,
        "http.host": "127.0.0.1:5000",
        "http.target": "/jokes",
        "net.peer.ip": "127.0.0.1",
        "http.user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "net.peer.port": 55740,
        "http.flavor": "1.1",
        "http.route": "/jokes",
        "http.status_text": "OK",
        "http.status_code": 200
    },
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "0.16b1",
        "service.name": "jokes-api"
    }
}
127.0.0.1 - - [13/Jan/2021 07:57:58] "GET /jokes HTTP/1.1" 200 -
```


### Client Traces Sample

`opentelemetry-instrument --exporter none --service-name jokes-client --ids-generator random python3 client.py`

```
{
    "name": "HTTP GET",
    "context": {
        "trace_id": "0x285d0d322bd17fa5e337c1f7dd5306c2",
        "span_id": "0x77e875e675aa1869",
        "trace_state": "{}"
    },
    "kind": "SpanKind.CLIENT",
    "parent_id": null,
    "start_time": "2021-01-13T19:24:59.060472Z",
    "end_time": "2021-01-13T19:24:59.191997Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "component": "http",
        "http.method": "GET",
        "http.url": "http://127.0.0.1:8000/jokes",
        "http.status_code": 200,
        "http.status_text": "OK"
    },
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "0.16b1",
        "service.name": "jokes-client"
    }
}
```


## Metrics Instrumentation Results

### API Metrics Sample 

`python api.py`

`ConsoleMetricsExporter(data="Counter(name="requests", description="number of incoming requests")", labels="(('endpoint', 'hello api'), ('environment', 'dev'))", value=1, resource={'telemetry.sdk.language': 'python', 'telemetry.sdk.name': 'opentelemetry', 'telemetry.sdk.version': '0.16b1'})`


### Client Metrics Sample 

`python client.py`

`ConsoleMetricsExporter(data="Counter(name="requests", description="number of incoming requests")", labels="(('endpoint', 'hello client'), ('environment', 'dev'))", value=1, resource={'telemetry.sdk.language': 'python', 'telemetry.sdk.name': 'opentelemetry', 'telemetry.sdk.version': '0.16b1'})`

## Requests Lifespan 

Requests: 
- Regular
- Proxy that introduces a delay 


# Additional Resources 

[OpenTelemetry Specifications](https://github.com/open-telemetry/opentelemetry-specification)

[Autoinstrumentation of Traces in Python](https://opentelemetry-python.readthedocs.io/en/stable/examples/auto-instrumentation/README.html)

[Flask Instrumentation](https://opentelemetry-python.readthedocs.io/en/stable/instrumentation/flask/flask.html)

[Python Requests Library Instrumentation](https://opentelemetry-python.readthedocs.io/en/stable/instrumentation/requests/requests.html)
