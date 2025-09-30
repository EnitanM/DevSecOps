# Pushing image to Azure Container Registry
**Using ACR is not mandatory, you may choose Docker or GitHub**

## Installing Plugin and adding credentials in Jenkins
1. 'Manage Jenkins' > Plugins > Available Plugins > Azure Credentials > Install
Read more about Azure Credentials here (https://plugins.jenkins.io/azure-credentials/)
2. Navigate back to the home page. Click on the pipeline > Credentials > Under "Stores scoped to SeniorCapstoneTeam1" select the pipeline folder > 'Add domain'
3. Domain Name = "Azure". Description = "add your description". *Example "credentials for azure-related services"*
4. 'Add Credentials' > Kind = 'Azure Service Principal' > Client ID = enter provided client ID > Client Secret = Enter provided secret > Tenant ID = Enter provided tenant ID > ID = "AZURE_CONTAINER_REGISTRY" > Description = "add your description". *Example "credentials for azure container registry"* > Create

## Suggested structure to view personal repositories
1. Create a copy of the Jenkinsfile.container file on your local machine. Rename it to Jenkinsfile-'YourName'.container
2. Change the APP_NAME to "flask-app-yourname" to ensure it does not mix in with another team member's registry. *your name must be in lowercase*
3. In Jenkins, update your pipeline configuration.
Navigate to the homepage. Click on the pipeline > Configure > Build Configuration > Script Path = Week04/snippets/Jenkinsfile-YourName.container > Save/Apply
4. Push your code changes to the GitHub repo
5. Re-run your build, and troubleshoot if necessary.