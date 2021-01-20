# Kubernetes 

## Prerequisites 

Azure Kubernetes Cluster with a Service Principal with ACRPull role assigned and enabled for [HTTP application routing](https://docs.microsoft.com/en-us/azure/aks/http-application-routing#use-http-routing)

[Connect to Kubernetes Cluster](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough#connect-to-the-cluster)

## Configuration 

Create `python-app` namespace: `kubectl create namespace python-app`

[Enable LinkerD in Kubernetes cluster](https://linkerd.io/2/getting-started/#step-2-validate-your-kubernetes-cluster)

[Enable Azure Monitor for Containers](https://docs.microsoft.com/en-us/azure/azure-monitor/insights/container-insights-enable-existing-clusters) 

[Authenticate with Azure Container Registry from Azure Kubernetes Service](https://docs.microsoft.com/en-us/azure/aks/cluster-container-registry-integration#grant-aks-access-to-acr): `az aks update -n braveheart-sharing -g braveheart-sharing-rg --attach-acr braveheartacr`

## Deployments 

Create Docker images for the `api` and `cli` and deploy to target container registry
* Dockerfiles: 
    * [API Dockerfile](../../API.Dockerfile)
    * [Client Dockerfile](../../Client.Dockerfile)
* Pipelines: 
    * [Deploy API and Client to ACR](../pipelines/deploy.yaml)

Update [api.yaml](./api.yaml) and [client.yaml](./client.yaml) with target image. 

API Deployment: `kubectl apply -f api.yaml`

Client Deployment: `kubectl apply -f client.yaml`

