# Prerequisites 

Azure DevOps Organization

Container Registry with a Service Principal with ACRPush role assigned

## Configuration

[Create Variable Group](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops&tabs=yaml#create-a-variable-group) named `secrets`

Add the following variables to `secrets`:
* dockerId: Client ID of Service Principal assigned to registry 
* dockerPassword: Password of Service Principal assigned to registry 
* acrName (without the `.azurecr.io`)

Create ADO Build Pipeline based on [deploy.yaml](./deploy.yaml)

## Deploy 

Run [deploy.yaml](./deploy.yaml) build pipeline to deploy Client and API to target Container Registry. 


