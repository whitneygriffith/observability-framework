# OpenTelemetry Collector 

## Prerequisites 

## Configuration 

Create `otel-collector` namespace: `kubectl apply -f namespace.yaml`

### Receivers 

#### OTLP 

[OTLP](https://github.com/open-telemetry/opentelemetry-collector/tree/master/receiver/otlpreceiver)

* grpc endpoint: `0.0.0.0:4317/v1/traces` or `0.0.0.0:4317/v1/metrics` or `0.0.0.0:4317/v1/logs`

[Host metrics for OTel agent](https://github.com/open-telemetry/opentelemetry-collector/tree/master/receiver/hostmetricsreceiver)


| Endpoint | Protocol | Description | 
| -------- | ---------| ------------|
| 4317    |  GRPC    | otlp: endpoint for OpenTelemetry receiver |
| 55681    |  HTTP    | otlp: endpoint for OpenTelemetry receiver |  
| 14250   |  GRPC     | jaeger-grpc: Default endpoint for Jaeger gRPC 
receiver| 
| 14268   |  HTTP     | jaeger-thrift-http: Default endpoint for Jaeger HTTP receiver| 
| 8888   |       | metrics: Default endpoint  for querying metrics | 
| 55679    |  HTTP     | Default endpoint for ZPages | 
| 1777  |       | pprof extension | 
| 13133   |       | healthcheck extension  | 



### Exporters 

#### File 

[File Exporter for Debugging](https://github.com/open-telemetry/opentelemetry-collector/tree/master/exporter/fileexporter)


#### Jaeger

Grpc endpoint: `jaeger.otel-exporters:14250`


#### Prometheus 

Endpoint: `0.0.0.0:8889`

Where the prometheus backend will scrape from `otel-collector.otel-collector:8889`
#### Azure Monitor

Instrumentation key is needed


## Deployments 


### Collector 

`kubectl apply -f otel-collector.yaml`

`kubectl get pods -n otel-collector`

`kubectl logs otel-collector-* -n otel-collector`

```
2021-01-21T19:03:51.457Z        info    service/service.go:411  Starting OpenTelemetry Collector...     {"Version": "latest", "GitHash": "a1004bba", "NumCPU": 2}
2021-01-21T19:03:51.457Z        info    service/service.go:255  Setting up own telemetry...
2021-01-21T19:03:51.458Z        info    service/telemetry.go:101        Serving Prometheus metrics      {"address": ":8888", "level": 0, "service.instance.id": "e775fc11-359f-4d15-b953-f7b8632b5ef4"}
2021-01-21T19:03:51.459Z        info    service/service.go:292  Loading configuration...
2021-01-21T19:03:51.461Z        info    service/service.go:303  Applying configuration...
2021-01-21T19:03:51.461Z        info    service/service.go:324  Starting extensions...
2021-01-21T19:03:51.461Z        info    builder/extensions_builder.go:53        Extension is starting...        {"component_kind": "extension", "component_type": "zpages", "component_name": "zpages"}
2021-01-21T19:03:51.461Z        info    zpagesextension/zpagesextension.go:42   Register Host's zPages  {"component_kind": "extension", "component_type": "zpages", "component_name": "zpages"}
2021-01-21T19:03:51.497Z        info    zpagesextension/zpagesextension.go:55   Starting zPages extension       {"component_kind": "extension", "component_type": "zpages", "component_name": "zpages", "config": {"TypeVal":"zpages","NameVal":"zpages","Endpoint":"localhost:55679"}}
2021-01-21T19:03:51.497Z        info    builder/extensions_builder.go:59        Extension started.      {"component_kind": "extension", "component_type": "zpages", "component_name": "zpages"}
2021-01-21T19:03:51.497Z        info    builder/extensions_builder.go:53        Extension is starting...        {"component_kind": "extension", "component_type": "pprof", "component_name": "pprof"}
2021-01-21T19:03:51.531Z        info    pprofextension/pprofextension.go:49     Starting net/http/pprof server  {"component_kind": "extension", "component_type": "pprof", "component_name": "pprof", "config": {"TypeVal":"pprof","NameVal":"pprof","Endpoint":"localhost:1777","BlockProfileFraction":0,"MutexProfileFraction":0,"SaveToFile":""}}
2021-01-21T19:03:51.531Z        info    builder/extensions_builder.go:59        Extension started.      {"component_kind": "extension", "component_type": "pprof", "component_name": "pprof"}
2021-01-21T19:03:51.531Z        info    builder/extensions_builder.go:53        Extension is starting...        {"component_kind": "extension", "component_type": "health_check", "component_name": "health_check"}
2021-01-21T19:03:51.531Z        info    healthcheckextension/healthcheckextension.go:40 Starting health_check extension {"component_kind": "extension", "component_type": "health_check", "component_name": "health_check", "config": {"TypeVal":"health_check","NameVal":"health_check","Port":13133}}
2021-01-21T19:03:51.531Z        info    builder/extensions_builder.go:59        Extension started.      {"component_kind": "extension", "component_type": "health_check", "component_name": "health_check"}
2021-01-21T19:03:51.532Z        info    builder/exporters_builder.go:306        Exporter is enabled.    {"component_kind": "exporter", "exporter": "file"}
2021-01-21T19:03:51.532Z        info    builder/exporters_builder.go:235        Ignoring exporter as it is not used by any pipeline    {"component_kind": "exporter"}
2021-01-21T19:03:51.532Z        info    builder/exporters_builder.go:306        Exporter is enabled.    {"component_kind": "exporter", "exporter": "jaeger"}
2021-01-21T19:03:51.532Z        info    service/service.go:339  Starting exporters...
2021-01-21T19:03:51.532Z        info    builder/exporters_builder.go:92 Exporter is starting... {"component_kind": "exporter", "component_type": "file", "component_name": "file"}
2021-01-21T19:03:51.532Z        info    builder/exporters_builder.go:97 Exporter started.       {"component_kind": "exporter", "component_type": "file", "component_name": "file"}
2021-01-21T19:03:51.532Z        info    builder/exporters_builder.go:92 Exporter is starting... {"component_kind": "exporter", "component_type": "prometheus", "component_name": "prometheus"}
2021-01-21T19:03:51.532Z        info    builder/exporters_builder.go:97 Exporter started.       {"component_kind": "exporter", "component_type": "prometheus", "component_name": "prometheus"}
2021-01-21T19:03:51.532Z        info    builder/exporters_builder.go:92 Exporter is starting... {"component_kind": "exporter", "component_type": "jaeger", "component_name": "jaeger"}
2021-01-21T19:03:51.532Z        info    builder/exporters_builder.go:97 Exporter started.       {"component_kind": "exporter", "component_type": "jaeger", "component_name": "jaeger"}
2021-01-21T19:03:51.532Z        info    builder/pipelines_builder.go:207        Pipeline is enabled.    {"pipeline_name": "traces", "pipeline_datatype": "traces"}
2021-01-21T19:03:51.532Z        info    builder/pipelines_builder.go:207        Pipeline is enabled.    {"pipeline_name": "metrics", "pipeline_datatype": "metrics"}
2021-01-21T19:03:51.533Z        info    service/service.go:352  Starting processors...
2021-01-21T19:03:51.533Z        info    builder/pipelines_builder.go:51 Pipeline is starting... {"pipeline_name": "metrics", "pipeline_datatype": "metrics"}
2021-01-21T19:03:51.533Z        info    builder/pipelines_builder.go:61 Pipeline is started.    {"pipeline_name": "metrics", "pipeline_datatype": "metrics"}
2021-01-21T19:03:51.533Z        info    builder/pipelines_builder.go:51 Pipeline is starting... {"pipeline_name": "traces", "pipeline_datatype": "traces"}
2021-01-21T19:03:51.533Z        info    builder/pipelines_builder.go:61 Pipeline is started.    {"pipeline_name": "traces", "pipeline_datatype": "traces"}
2021-01-21T19:03:51.533Z        info    builder/receivers_builder.go:110        Ignoring receiver as it is not used by any pipeline    {"component_kind": "receiver", "component_type": "prometheus", "component_name": "prometheus", "receiver": "prometheus"}
2021-01-21T19:03:51.533Z        info    builder/receivers_builder.go:235        Receiver is enabled.    {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp", "datatype": "traces"}
2021-01-21T19:03:51.533Z        info    builder/receivers_builder.go:235        Receiver is enabled.    {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp", "datatype": "metrics"}
2021-01-21T19:03:51.533Z        info    service/service.go:364  Starting receivers...
2021-01-21T19:03:51.534Z        info    builder/receivers_builder.go:70 Receiver is starting... {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T19:03:51.534Z        info    otlpreceiver/otlp.go:93 Starting GRPC server on endpoint 0.0.0.0:4317   {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T19:03:51.534Z        info    otlpreceiver/otlp.go:130        Setting up a second GRPC listener on legacy endpoint 0.0.0.0:55680     {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T19:03:51.534Z        info    otlpreceiver/otlp.go:93 Starting GRPC server on endpoint 0.0.0.0:55680  {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T19:03:51.534Z        info    builder/receivers_builder.go:75 Receiver started.       {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T19:03:51.534Z        info    healthcheck/handler.go:128      Health Check state change       {"component_kind": "extension", "component_type": "health_check", "component_name": "health_check", "status": "ready"}
2021-01-21T19:03:51.534Z        info    service/service.go:267  Everything is ready. Begin running and processing data.
```

### Contrib Collector 

`kubectl apply -f otel-collector-contrib.yaml`

`kubectl get pods -n otel-collector`

`kubectl logs otel-collector-contrib-* -n otel-collector`

```
2021-01-22T06:16:49.748Z        info    service/service.go:411  Starting OpenTelemetry Contrib Collector...     {"Version": "latest", "GitHash": "bb44b79b", "NumCPU": 2}
2021-01-22T06:16:49.759Z        info    service/service.go:592  Using memory ballast    {"MiBs": 683}
2021-01-22T06:16:49.759Z        info    service/service.go:255  Setting up own telemetry...
2021-01-22T06:16:49.763Z        info    service/telemetry.go:101        Serving Prometheus metrics      {"address": ":8888", "level": 0, "service.instance.id": "9a8a186d-8229-4422-a9ca-73511a08f7b5"}
2021-01-22T06:16:49.766Z        info    service/service.go:292  Loading configuration...
2021-01-22T06:16:49.768Z        info    service/service.go:303  Applying configuration...
2021-01-22T06:16:49.769Z        info    service/service.go:324  Starting extensions...
2021-01-22T06:16:49.769Z        info    builder/extensions_builder.go:53        Extension is starting...        {"component_kind": "extension", "component_type": "pprof", "component_name": "pprof"}
2021-01-22T06:16:49.802Z        info    pprofextension/pprofextension.go:49     Starting net/http/pprof server  {"component_kind": "extension", "component_type": "pprof", "component_name": "pprof", "config": {"TypeVal":"pprof","NameVal":"pprof","Endpoint":"localhost:1777","BlockProfileFraction":0,"MutexProfileFraction":0,"SaveToFile":""}}
2021-01-22T06:16:49.802Z        info    builder/extensions_builder.go:59        Extension started.      {"component_kind": "extension", "component_type": "pprof", "component_name": "pprof"}
2021-01-22T06:16:49.802Z        info    builder/extensions_builder.go:53        Extension is starting...        {"component_kind": "extension", "component_type": "health_check", "component_name": "health_check"}
2021-01-22T06:16:49.802Z        info    healthcheckextension/healthcheckextension.go:40 Starting health_check extension {"component_kind": "extension", "component_type": "health_check", "component_name": "health_check", "config": {"TypeVal":"health_check","NameVal":"health_check","Port":13133}}
2021-01-22T06:16:49.802Z        info    builder/extensions_builder.go:59        Extension started.      {"component_kind": "extension", "component_type": "health_check", "component_name": "health_check"}
2021-01-22T06:16:49.802Z        info    builder/extensions_builder.go:53        Extension is starting...        {"component_kind": "extension", "component_type": "zpages", "component_name": "zpages"}
2021-01-22T06:16:49.802Z        info    zpagesextension/zpagesextension.go:42   Register Host's zPages  {"component_kind": "extension", "component_type": "zpages", "component_name": "zpages"}
2021-01-22T06:16:49.814Z        info    zpagesextension/zpagesextension.go:55   Starting zPages extension       {"component_kind": "extension", "component_type": "zpages", "component_name": "zpages", "config": {"TypeVal":"zpages","NameVal":"zpages","Endpoint":"localhost:55679"}}
2021-01-22T06:16:49.814Z        info    builder/extensions_builder.go:59        Extension started.      {"component_kind": "extension", "component_type": "zpages", "component_name": "zpages"}
2021-01-22T06:16:49.815Z        info    builder/exporters_builder.go:306        Exporter is enabled.    {"component_kind": "exporter", "exporter": "azuremonitor"}
2021-01-22T06:16:49.815Z        info    builder/exporters_builder.go:306        Exporter is enabled.    {"component_kind": "exporter", "exporter": "file"}
2021-01-22T06:16:49.815Z        info    service/service.go:339  Starting exporters...
2021-01-22T06:16:49.815Z        info    builder/exporters_builder.go:92 Exporter is starting... {"component_kind": "exporter", "component_type": "azuremonitor", "component_name": "azuremonitor"}
2021-01-22T06:16:49.815Z        info    builder/exporters_builder.go:97 Exporter started.       {"component_kind": "exporter", "component_type": "azuremonitor", "component_name": "azuremonitor"}
2021-01-22T06:16:49.815Z        info    builder/exporters_builder.go:92 Exporter is starting... {"component_kind": "exporter", "component_type": "file", "component_name": "file"}
2021-01-22T06:16:49.815Z        info    builder/exporters_builder.go:97 Exporter started.       {"component_kind": "exporter", "component_type": "file", "component_name": "file"}
2021-01-22T06:16:49.815Z        info    builder/pipelines_builder.go:207        Pipeline is enabled.    {"pipeline_name": "metrics", "pipeline_datatype": "metrics"}
2021-01-22T06:16:49.815Z        info    builder/pipelines_builder.go:207        Pipeline is enabled.    {"pipeline_name": "traces", "pipeline_datatype": "traces"}
2021-01-22T06:16:49.815Z        info    service/service.go:352  Starting processors...
2021-01-22T06:16:49.815Z        info    builder/pipelines_builder.go:51 Pipeline is starting... {"pipeline_name": "metrics", "pipeline_datatype": "metrics"}
2021-01-22T06:16:49.815Z        info    builder/pipelines_builder.go:61 Pipeline is started.    {"pipeline_name": "metrics", "pipeline_datatype": "metrics"}
2021-01-22T06:16:49.815Z        info    builder/pipelines_builder.go:51 Pipeline is starting... {"pipeline_name": "traces", "pipeline_datatype": "traces"}
2021-01-22T06:16:49.815Z        info    builder/pipelines_builder.go:61 Pipeline is started.    {"pipeline_name": "traces", "pipeline_datatype": "traces"}
2021-01-22T06:16:49.815Z        info    builder/receivers_builder.go:235        Receiver is enabled.    {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp", "datatype": "metrics"}
2021-01-22T06:16:49.815Z        info    builder/receivers_builder.go:235        Receiver is enabled.    {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp", "datatype": "traces"}
2021-01-22T06:16:49.815Z        info    builder/receivers_builder.go:235        Receiver is enabled.    {"component_kind": "receiver", "component_type": "prometheus", "component_name": "prometheus", "datatype": "metrics"}
2021-01-22T06:16:49.815Z        info    service/service.go:364  Starting receivers...
2021-01-22T06:16:49.815Z        info    builder/receivers_builder.go:70 Receiver is starting... {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-22T06:16:49.815Z        info    otlpreceiver/otlp.go:93 Starting GRPC server on endpoint 0.0.0.0:4317   {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-22T06:16:49.815Z        info    otlpreceiver/otlp.go:130        Setting up a second GRPC listener on legacy endpoint 0.0.0.0:55680     {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-22T06:16:49.815Z        info    otlpreceiver/otlp.go:93 Starting GRPC server on endpoint 0.0.0.0:55680  {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-22T06:16:49.815Z        info    builder/receivers_builder.go:75 Receiver started.       {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-22T06:16:49.815Z        info    builder/receivers_builder.go:70 Receiver is starting... {"component_kind": "receiver", "component_type": "prometheus", "component_name": "prometheus"}
2021-01-22T06:16:49.854Z        info    builder/receivers_builder.go:75 Receiver started.       {"component_kind": "receiver", "component_type": "prometheus", "component_name": "prometheus"}
2021-01-22T06:16:49.854Z        info    healthcheck/handler.go:128      Health Check state change       {"component_kind": "extension", "component_type": "health_check", "component_name": "health_check", "status": "ready"}
2021-01-22T06:16:49.855Z        info    service/service.go:267  Everything is ready. Begin running and processing data.
```
### Agent 

`kubectl apply -f otel-agent.yaml`

`kubectl get pods -n otel-collector`

`kubectl logs otel-agent-* -n otel-collector`

```
2021-01-21T20:49:21.009Z        info    service/service.go:411  Starting OpenTelemetry Collector...     {"Version": "latest", "GitHash": "a1004bba", "NumCPU": 2}
2021-01-21T20:49:21.013Z        info    service/service.go:592  Using memory ballast    {"MiBs": 165}
2021-01-21T20:49:21.013Z        info    service/service.go:255  Setting up own telemetry...
2021-01-21T20:49:21.015Z        info    service/telemetry.go:101        Serving Prometheus metrics      {"address": ":8888", "level": 0, "service.instance.id": "90573a76-a371-4361-a5f9-26f63f294484"}
2021-01-21T20:49:21.015Z        info    service/service.go:292  Loading configuration...
2021-01-21T20:49:21.017Z        info    service/service.go:303  Applying configuration...
2021-01-21T20:49:21.017Z        info    service/service.go:324  Starting extensions...
2021-01-21T20:49:21.017Z        info    builder/exporters_builder.go:306        Exporter is enabled.    {"component_kind": "exporter", "exporter": "otlp"}
2021-01-21T20:49:21.018Z        info    service/service.go:339  Starting exporters...
2021-01-21T20:49:21.018Z        info    builder/exporters_builder.go:92 Exporter is starting... {"component_kind": "exporter", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T20:49:21.018Z        info    builder/exporters_builder.go:97 Exporter started.       {"component_kind": "exporter", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T20:49:21.019Z        info    builder/pipelines_builder.go:207        Pipeline is enabled.    {"pipeline_name": "metrics", "pipeline_datatype": "metrics"}
2021-01-21T20:49:21.019Z        info    builder/pipelines_builder.go:207        Pipeline is enabled.    {"pipeline_name": "traces", "pipeline_datatype": "traces"}
2021-01-21T20:49:21.019Z        info    service/service.go:352  Starting processors...
2021-01-21T20:49:21.019Z        info    builder/pipelines_builder.go:51 Pipeline is starting... {"pipeline_name": "metrics", "pipeline_datatype": "metrics"}
2021-01-21T20:49:21.019Z        info    builder/pipelines_builder.go:61 Pipeline is started.    {"pipeline_name": "metrics", "pipeline_datatype": "metrics"}
2021-01-21T20:49:21.019Z        info    builder/pipelines_builder.go:51 Pipeline is starting... {"pipeline_name": "traces", "pipeline_datatype": "traces"}
2021-01-21T20:49:21.019Z        info    builder/pipelines_builder.go:61 Pipeline is started.    {"pipeline_name": "traces", "pipeline_datatype": "traces"}
2021-01-21T20:49:21.019Z        info    builder/receivers_builder.go:235        Receiver is enabled.    {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp", "datatype": "traces"}
2021-01-21T20:49:21.019Z        info    builder/receivers_builder.go:235        Receiver is enabled.    {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp", "datatype": "metrics"}
2021-01-21T20:49:21.019Z        info    builder/receivers_builder.go:235        Receiver is enabled.    {"component_kind": "receiver", "component_type": "hostmetrics", "component_name": "hostmetrics", "datatype": "metrics"}
2021-01-21T20:49:21.019Z        info    service/service.go:364  Starting receivers...
2021-01-21T20:49:21.019Z        info    builder/receivers_builder.go:70 Receiver is starting... {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T20:49:21.019Z        info    otlpreceiver/otlp.go:93 Starting GRPC server on endpoint 0.0.0.0:4317   {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T20:49:21.020Z        info    otlpreceiver/otlp.go:130        Setting up a second GRPC listener on legacy endpoint 0.0.0.0:55680     {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T20:49:21.020Z        info    otlpreceiver/otlp.go:93 Starting GRPC server on endpoint 0.0.0.0:55680  {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T20:49:21.021Z        info    builder/receivers_builder.go:75 Receiver started.       {"component_kind": "receiver", "component_type": "otlp", "component_name": "otlp"}
2021-01-21T20:49:21.021Z        info    builder/receivers_builder.go:70 Receiver is starting... {"component_kind": "receiver", "component_type": "hostmetrics", "component_name": "hostmetrics"}
2021-01-21T20:49:21.021Z        info    builder/receivers_builder.go:75 Receiver started.       {"component_kind": "receiver", "component_type": "hostmetrics", "component_name": "hostmetrics"}
2021-01-21T20:49:21.021Z        info    service/service.go:267  Everything is ready. Begin running and processing data.
```

## Next Steps 

[Enable Distributed Tracing with Linkerd](https://linkerd.io/2/tasks/distributed-tracing/) and update the annotations in all linkerd enabled namespaces to collect traces using the `otel-collector`, `config.linkerd.io/trace-collector: otel-collector.otel-collector:4317`


## Additional Reading 

[Choosing gRPC vs HTTP protocol](TODO)
[Using the Prometheus federation API to Export Metrics from LinkerD](https://linkerd.io/2/tasks/exporting-metrics/)