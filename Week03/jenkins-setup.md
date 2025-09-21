# Jenkins Installation & Setup
## Pulling and running the Docker image
1. Pull the Jenkins docker image using `docker pull jenkins/jenkins:jdk21`. If you choose to use a different jdk, specify it in place of *21* after the jdk.
2. Create a jenkins-specific volume and port mapping using `docker run -p 8080:8080 -p 50000:50000 --restart=on-failure -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk21`. You can modify the port mappings and jdk version here as well if there are conflicts.
Jenkins should now be running on your machine at (http://localhost:8080) or your specified port.
## Jenkins setup
1. To unlock jenkins using the admin account, access the password by running `docker exec <jenkins_container_id_or_name> cat /var/jenkins_home/secrets/initialAdminPassword` or in Docker Desktop, visit Volumes -> jenkins_home/secrets/initialAdminPassword.
2. On the 'Customize Jenkins' page install the suggested plugins or select the plugins for this project by searching for *Gihub, Pipeline, Docker, JUnit*. If you installed the suggested plugins, take note of those not automatically added during installation. 
3. Complete the first admin user and the jenkins url setup as you wish, or skip them.
4. From the Jenkins dashboard, click the settings icon or search `manage jenkins`. Verify the installed plugins, and search for the missing plugins under the `available plugins`.
### Configuring Tools
1. To setup JDK, Git, and Docker, under 'Manage Jenkins' select 'Tools' > 'Add JDK', type JAVA_HOME as the 'Name' > add the Java path in the JAVA_HOME text box.
2. Git installations should remain as the default for now
3. Scroll to the bottom of the page. Click 'Add Docker' > Install automatically > latest > Save
### Configuring Credentials
1. You should now be back at 'Manage Jenkins'. Select 'Credentials' > System > Global credentials > Add Credentials
2. Enter your GitHub username in the textbox. Use username as secret if you choose. Next, is to add a password, but we'll be using tokens.
3. Visit your GitHub page > click your profile image > settings > Developer settings (at the bottom of the left panel)
4. To add tokens, 'Personal access tokens' > Tokens (classic) > Generate new token > Generate new token (classic). *You may generate a scope-specific token for the organization if you choose*
5. Enter a note, expiration, and check the boxes for your preferred access. Click 'Generate token'
6. Copy/paste the generated token into the Password textbox in Jenkins and enter "senior_project_token" for easy future identification and configuration with current *Jenkinsfile.ci* for this project. Click 'Create'
### Pipeline configuration
1. Navigate back to the landing dashboard by clicking the Jenkins icon on the top left of your screen and select `New Item`. Enter a name for the project. *Choose a name with no spaces for Jenkins backend compatibility. For example, SeniorCapstoneTeam1 or project_team1* Select the 'Pipeline' option and click 'OK' to proceed
2. Check 'GitHub project' and paste in our project url at `https://github.com/P31CI-CD/CI-CD-Pipeline.git` Check any other preferred settings, for example 'Discard old builds'.
3. Under the 'Triggers' section, check 'GitHub hook trigger for GITScm polling'. We will be using webhooks for our project.
4. Under the 'Pipeline' section, select the dropdown in the top-right of the 'Script' textbox and try a sample pipleine like 'Hello World'. The 'Pipeline Syntax' hyperlink leads to location that helps guide you through constructing the correct syntax for the pipeline; you may explore this later. Click 'Save' and run your first build by clicking 'Build Now' in the next screen that shows up for the project's pipeline. Watch the bottom left corner of the screen for the build to complete, click on it to see the console output. You should see the 'Hello World' sample.
5. Click or hover over'SeniorCapstoneTeam1' beside the Jenkins icon to navigate back to the home directory for the pipeline. Select 'Configure' and copy/paste the pipeline definition in Week03/ops/Jenkinsfile.ci into the Script textbox. You may also configure using the pipeline script from SCM if you choose. Now run another build.