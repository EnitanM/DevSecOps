# Pushing image to Azure Container Registry
**Using ACR is not mandatory, you may choose Docker or GitHub**

## Installing Plugin and adding credentials in Jenkins
1. 'Manage Jenkins' > Plugins > Available Plugins > Azure Credentials > Install
Read more about Azure Credentials here (https://plugins.jenkins.io/azure-credentials/)
2. Navigate back to the home page. Click on the pipeline 'SeniorCapstoneTeam1' > Credentials > Under "Stores scoped to SeniorCapstoneTeam1" select the pipeline folder > 'Add domain'
3. Domain Name = "Azure". Description = "add your description". *Example "credentials for azure-related services"*
4. 'Add Credentials' > Kind = 'Azure Service Principal' > Client ID = enter provided client ID > Client Secret = Enter provided secret > ID = "AZURE_CONTAINER_REGISTRY" > Description = "add your description". *Example "credentials for azure container registry"* > Create
