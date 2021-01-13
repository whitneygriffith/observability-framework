# Introduction 

[app.py](./app.py)

# Getting Started

Create virtualenv `python -m venv venv`

Activate virtualenv `source venv/bin/activate`

Install packages `pip install -r requirements.txt`

## Instrumentation 

configuration of Tracing Provider
* Data source specific configuration
* Exporter configuration
* Propagator configuration
* Resource configuraton
exporter 
* setting credentials securely 
span processor 
tracer provider 
logger 

### Autoinstrumentation

[app.py](./app.py) is automatically instrumented for tracing by installing the relevant instrumentation libraries for the python site-packages used in the app which can be found [here](https://opentelemetry-python.readthedocs.io/en/stable/index.html#instrumentations) or can be recommended by running `opentelemetry-bootstrap --action=requirements`


To verify instrumentation: 

[Results when run with flask](#flask-sample)

[Results when run with console utils](#console-sample)

# Build and Run App 

## Environment Variables

OTEL_PYTHON_DJANGO_INSTRUMENT
## Locally 

`export FLASK_APP=app.py`
`opentelemetry-instrument --exporter none --service-name jokes-generator --ids-generator random flask run`


## Docker 

## Kubernetes 

# Test


## Autoinstrumentation 

### Flask Sample 

`opentelemetry-instrument --exporter none --service-name jokes-generator --ids-generator random flask run`

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
        "service.name": "jokes-generator"
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
        "service.name": "jokes-generator"
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
        "service.name": "jokes-generator"
    }
}
127.0.0.1 - - [13/Jan/2021 07:57:58] "GET /jokes HTTP/1.1" 200 -
```


### Console Sample 

`python app.py` 

`python console_utils/client.py`

Expected sample output from [console_utils/client.py](./console_utils/client.py): 

```
{
    "name": "client-server",
    "context": {
        "trace_id": "0x79801874915d919d157568cd9c65b8c7",
        "span_id": "0x327d460f23849113",
        "trace_state": "{}"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0x0601002a6ff832ef",
    "start_time": "2021-01-12T21:26:32.049287Z",
    "end_time": "2021-01-12T21:26:32.191381Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "0.16b1"
    }
}
{
    "name": "client",
    "context": {
        "trace_id": "0x79801874915d919d157568cd9c65b8c7",
        "span_id": "0x0601002a6ff832ef",
        "trace_state": "{}"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": null,
    "start_time": "2021-01-12T21:26:32.049205Z",
    "end_time": "2021-01-12T21:26:32.192394Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [],
    "links": [],
    "resource": {
        "telemetry.sdk.language": "python",
        "telemetry.sdk.name": "opentelemetry",
        "telemetry.sdk.version": "0.16b1"
    }
}
```

## Requests Lifespan 

Requests: 
- Regular
- Proxy that introduces a delay 


# Additional Resources 

[Autoinstrumentation in Python](https://opentelemetry-python.readthedocs.io/en/stable/examples/auto-instrumentation/README.html)
