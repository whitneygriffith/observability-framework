# Introduction 

[app.py](./app.py)

# Getting Started

Create virtualenv `python -m venv venv`

Activate virtualenv `source venv/bin/activate`

Install packages `pip install -r requirements.txt`

## Instrumentation 

configuration 
exporter 
span processor 
tracer provider 
logger 

### Autoinstrumentation

[app.py](./app.py) is automatically instrumented for tracing 

To verify instrumentation: 

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

# Build and Run App 

## Locally 

`export FLASK_APP=app.py`
`flask run`

## Docker 

## Kubernetes 

# Test

Requests: 
- Regular
- Proxy that introduces a delay 


# Additional Resources 

[Autoinstrumentation in Python](https://opentelemetry-python.readthedocs.io/en/stable/examples/auto-instrumentation/README.html)
