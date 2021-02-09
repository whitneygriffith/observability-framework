# Linkerd 
## Setup

1. Install the [linkerd CLI](https://linkerd.io/2/getting-started/#step-1-install-the-cli)

1. Generate and install the linkerd manifest

`linkerd check --pre`

`linkerd install --config config.yaml | kubectl apply -f -`

Verify setup: `linkerd check`

## View Data

View linkerd dashboard `linkerd dashboard`

Explore Jaeger `kubectl -n linkerd port-forward svc/linkerd-jaeger 16686` 

## Proxy Injection 

### Annotations 

Annotate all namespaces, deployments, pods manually with: 

```
linkerd.io/inject: enabled
config.linkerd.io/trace-collector: linkerd-collector.linkerd:55678
config.alpha.linkerd.io/trace-collector-service-account: linkerd-collector
```

### Verify 

`linkerd stat deployments -n target-namespace`

You can also check visually in the Meshed column in the `linkerd dashboard` 

## Additional Reading 

[Install Linkerd onto the cluster](https://linkerd.io/2/getting-started/)

[Enable Distributed Tracing with Linkerd](https://linkerd.io/2/tasks/distributed-tracing/)

[Adding Your Services to Linkerd](https://linkerd.io/2/tasks/adding-your-service/)