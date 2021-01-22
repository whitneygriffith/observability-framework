# Backends for OpenTelemetry to export Observability Data 

## Prerequisites

Create `otel-exporters` namespace: `kubectl create namespace otel-exporters`

## Deployment

### Jaeger 

`kubectl apply -f jaeger.yaml`


`kubectl logs jaeger-all-in-one -n otel-exporters`

```
021/01/20 22:16:14 maxprocs: Leaving GOMAXPROCS=2: CPU quota undefined
{"level":"info","ts":1611180974.630113,"caller":"flags/service.go:117","msg":"Mounting metrics handler on admin server","route":"/metrics"}
{"level":"info","ts":1611180974.630253,"caller":"flags/service.go:123","msg":"Mounting expvar handler on admin server","route":"/debug/vars"}
{"level":"info","ts":1611180974.6307378,"caller":"flags/admin.go:121","msg":"Mounting health check on admin server","route":"/"}
{"level":"info","ts":1611180974.630785,"caller":"flags/admin.go:127","msg":"Starting admin HTTP server","http-addr":":14269"}
{"level":"info","ts":1611180974.630826,"caller":"flags/admin.go:113","msg":"Admin server started","http.host-port":"[::]:14269","health-status":"unavailable"}
{"level":"info","ts":1611180974.6450408,"caller":"memory/factory.go:61","msg":"Memory storage initialized","configuration":{"MaxTraces":0}}
{"level":"info","ts":1611180974.6592247,"caller":"server/grpc.go:76","msg":"Starting jaeger-collector gRPC server","grpc.host-port":":14250"}
{"level":"info","ts":1611180974.659261,"caller":"server/http.go:45","msg":"Starting jaeger-collector HTTP server","http host-port":":14268"}
{"level":"info","ts":1611180974.6596541,"caller":"server/zipkin.go:48","msg":"Not listening for Zipkin HTTP traffic, port not configured"}
{"level":"info","ts":1611180974.659684,"caller":"grpc/builder.go:70","msg":"Agent requested insecure grpc connection to collector(s)"}
{"level":"info","ts":1611180974.659719,"caller":"grpc@v1.29.1/clientconn.go:243","msg":"parsed scheme: \"\"","system":"grpc","grpc_log":true}
{"level":"info","ts":1611180974.6597402,"caller":"grpc@v1.29.1/clientconn.go:249","msg":"scheme \"\" not registered, fallback to default scheme","system":"grpc","grpc_log":true}
{"level":"info","ts":1611180974.6597638,"caller":"grpc@v1.29.1/resolver_conn_wrapper.go:143","msg":"ccResolverWrapper: sending update to cc: {[{:14250  <nil> 0 <nil>}] <nil> <nil>}","system":"grpc","grpc_log":true}
{"level":"info","ts":1611180974.6597745,"caller":"grpc@v1.29.1/clientconn.go:667","msg":"ClientConn switching balancer to \"round_robin\"","system":"grpc","grpc_log":true}
{"level":"info","ts":1611180974.6597805,"caller":"grpc@v1.29.1/clientconn.go:682","msg":"Channel switches to new LB policy \"round_robin\"","system":"grpc","grpc_log":true}
{"level":"info","ts":1611180974.6598,"caller":"grpc@v1.29.1/clientconn.go:1056","msg":"Subchannel Connectivity change to CONNECTING","system":"grpc","grpc_log":true}
{"level":"info","ts":1611180974.660495,"caller":"grpc@v1.29.1/clientconn.go:417","msg":"Channel Connectivity change to CONNECTING","system":"grpc","grpc_log":true}
{"level":"info","ts":1611180974.6606393,"caller":"grpc@v1.29.1/clientconn.go:1193","msg":"Subchannel picks a new address \":14250\" to connect","system":"grpc","grpc_log":true}
{"level":"info","ts":1611180974.6608727,"caller":"grpc/builder.go:108","msg":"Checking connection to collector"}
{"level":"info","ts":1611180974.6609561,"caller":"grpc/builder.go:119","msg":"Agent collector connection state change","dialTarget":":14250","status":"CONNECTING"}
{"level":"info","ts":1611180974.6614132,"caller":"command-line-arguments/main.go:218","msg":"Starting agent"}
{"level":"info","ts":1611180974.6614754,"caller":"querysvc/query_service.go:137","msg":"Archive storage not created","reason":"archive storage not supported"}
{"level":"info","ts":1611180974.6614912,"caller":"app/flags.go:159","msg":"Archive storage not initialized"}
{"level":"info","ts":1611180974.661646,"caller":"grpc@v1.29.1/clientconn.go:1056","msg":"Subchannel Connectivity change to READY","system":"grpc","grpc_log":true}
{"level":"info","ts":1611180974.6618369,"caller":"base/balancer.go:200","msg":"roundrobinPicker: newPicker called with info: {map[0xc00065fa90:{{:14250  <nil> 0 <nil>}}]}","system":"grpc","grpc_log":true}
{"level":"info","ts":1611180974.6619248,"caller":"grpc@v1.29.1/clientconn.go:417","msg":"Channel Connectivity change to READY","system":"grpc","grpc_log":true}
{"level":"info","ts":1611180974.6619947,"caller":"app/agent.go:69","msg":"Starting jaeger-agent HTTP server","http-port":5778}
{"level":"info","ts":1611180974.6618736,"caller":"app/static_handler.go:181","msg":"UI config path not provided, config file will not be watched"}
{"level":"info","ts":1611180974.6629477,"caller":"app/server.go:187","msg":"Query server started","port":16686,"addr":":16686"}
{"level":"info","ts":1611180974.6629803,"caller":"healthcheck/handler.go:128","msg":"Health Check state change","status":"ready"}
{"level":"info","ts":1611180974.662994,"caller":"app/server.go:262","msg":"Starting CMUX server","port":16686,"addr":":16686"}
{"level":"info","ts":1611180974.6630318,"caller":"app/server.go:232","msg":"Starting HTTP server","port":16686,"addr":":16686"}
{"level":"info","ts":1611180974.6630456,"caller":"app/server.go:251","msg":"Starting GRPC server","port":16686,"addr":":16686"}
{"level":"info","ts":1611180974.662007,"caller":"grpc/builder.go:119","msg":"Agent collector connection state change","dialTarget":":14250","status":"READY"}
```

View Dashboard: `kubectl port-forward pod/jaeger-all-in-one 16686:16686 -n otel-exporters`


### Prometheus 

`kubectl apply -f prometheus.yaml`

`kubectl logs prometheus-* -n otel-exporters`

```
level=info ts=2021-01-20T22:42:22.873Z caller=main.go:364 msg="Starting Prometheus" version="(version=2.24.1, branch=HEAD, revision=e4487274853c587717006eeda8804e597d120340)"
level=info ts=2021-01-20T22:42:22.874Z caller=main.go:369 build_context="(go=go1.15.6, user=root@0b5231a0de0f, date=20210120-00:09:36)"
level=info ts=2021-01-20T22:42:22.874Z caller=main.go:370 host_details="(Linux 5.4.0-1034-azure #35~18.04.1-Ubuntu SMP Thu Dec 10 09:13:52 UTC 2020 x86_64 prometheus-86c54d7459-2f4z7 (none))"
level=info ts=2021-01-20T22:42:22.874Z caller=main.go:371 fd_limits="(soft=1048576, hard=1048576)"
level=info ts=2021-01-20T22:42:22.874Z caller=main.go:372 vm_limits="(soft=unlimited, hard=unlimited)"
level=info ts=2021-01-20T22:42:22.877Z caller=web.go:530 component=web msg="Start listening for connections" address=0.0.0.0:9090
level=info ts=2021-01-20T22:42:22.878Z caller=main.go:738 msg="Starting TSDB ..."
level=info ts=2021-01-20T22:42:22.879Z caller=tls_config.go:191 component=web msg="TLS is disabled." http2=false
level=info ts=2021-01-20T22:42:22.882Z caller=head.go:645 component=tsdb msg="Replaying on-disk memory mappable chunks if any"
level=info ts=2021-01-20T22:42:22.882Z caller=head.go:659 component=tsdb msg="On-disk memory mappable chunks replay completed" duration=2.6µs
level=info ts=2021-01-20T22:42:22.882Z caller=head.go:665 component=tsdb msg="Replaying WAL, this may take a while"
level=info ts=2021-01-20T22:42:22.883Z caller=head.go:717 component=tsdb msg="WAL segment loaded" segment=0 maxSegment=0
level=info ts=2021-01-20T22:42:22.883Z caller=head.go:722 component=tsdb msg="WAL replay completed" checkpoint_replay_duration=112.801µs wal_replay_duration=197.301µs total_replay_duration=330.602µs
level=info ts=2021-01-20T22:42:22.884Z caller=main.go:758 fs_type=EXT4_SUPER_MAGIC
level=info ts=2021-01-20T22:42:22.884Z caller=main.go:761 msg="TSDB started"
level=info ts=2021-01-20T22:42:22.884Z caller=main.go:887 msg="Loading configuration file" filename=/etc/prometheus/prometheus.yml
level=info ts=2021-01-20T22:42:22.885Z caller=kubernetes.go:264 component="discovery manager scrape" discovery=kubernetes msg="Using pod service account via in-cluster config"
level=info ts=2021-01-20T22:42:22.887Z caller=kubernetes.go:264 component="discovery manager scrape" discovery=kubernetes msg="Using pod service account via in-cluster config"
level=info ts=2021-01-20T22:42:22.887Z caller=main.go:918 msg="Completed loading of configuration file" filename=/etc/prometheus/prometheus.yml totalDuration=3.870218ms remote_storage=1.4µs web_handler=300ns query_engine=700ns scrape=257.601µs scrape_sd=2.479912ms notify=14.8µs notify_sd=10.9µs rules=1.3µs
level=info ts=2021-01-20T22:42:22.889Z caller=main.go:710 msg="Server is ready to receive web requests."
```

View Dashboard: `kubectl port-forward pod/prometheus-76dbb4667b-9bndz 9090:9090 -n otel-exporters`

### Azure Monitor 


[Create Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/create-workspace-resource) and select target [Log Analytics Workspace](https://docs.microsoft.com/en-us/azure/azure-monitor/learn/quick-create-workspace)


Copy Instrumentation Key