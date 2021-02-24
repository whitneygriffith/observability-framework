# Logging 

Deploys the unified logging layer for the Kubernetes Cluster. This layer is built using the following: 
* [Elasticsearch](https://www.elastic.co/): Search engine
* [Fluentd](https://www.fluentd.org/): Log Collector
* [Kibana](https://www.elastic.co/kibana): Dashboard


## Deployment 

`kubectl apply -f logging.yaml`

## Validate 

Get the kibana pod name using `kubectl get pods -n observability`

`kubectl port-forward kibana-* 5601:5601 -n observability`

Visit http://localhost:5601 and click [discover](https://www.elastic.co/guide/en/kibana/current/discover.html) 

View Logs 

## Dashboard 

Create [index pattern](https://www.elastic.co/guide/en/kibana/current/index-patterns.html) for `logstash-*` as a catch-all and any additional custom patterns

## Additional Reading 

[Fluentd vs Logstash](https://logz.io/blog/fluentd-logstash/)