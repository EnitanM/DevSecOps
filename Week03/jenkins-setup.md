# Jenkins Installation & Setup

## Pulling and running the Docker image
1. Pull the Jenkins docker image using `docker pull jenkins/jenkins:jdk21`. Alternatively visit (https://www.jenkins.io/doc/book/installing/docker/) for a detailed breakdown *skip step 2 if you do*
2. Create a jenkins-specific volume and port mapping using `docker run -p 8080:8080 -p 50000:50000 --restart=on-failure -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk21`. You can modify the port mappings and jdk version here as well if there are conflicts.
Jenkins should now be running on your machine at (http://localhost:8080) or your specified port.

## Jenkins setup
1. To unlock jenkins using the admin account, access the password by running `docker exec <jenkins_container_id_or_name> cat /var/jenkins_home/secrets/initialAdminPassword` or in Docker Desktop, visit Volumes -> jenkins_home/secrets/initialAdminPassword.
2. On the 'Customize Jenkins' page install the suggested plugins or select the plugins for this project by searching for *Gihub, Pipeline, Docker, JUnit*. If you installed the suggested plugins, take note of those not automatically added during installation. 
3. Complete the first admin user and the jenkins url setup as you wish, or skip them.
4. From the Jenkins dashboard, click the settings icon or search `manage jenkins`. Verify the installed plugins, and search for the missing plugins under the `available plugins`.

### Configuring Tools
1. To setup JDK, Git, and Docker, under 'Manage Jenkins' select 'Tools' > 'Add JDK', type JAVA_HOME as the 'Name' > add the Java path in the JAVA_HOME text box.
2. Git installations can remain as the default for now
3. Scroll to the bottom of the page. Click 'Add Docker' > Install automatically from the website > latest > Save

### Configuring Credentials
1. You should now be back at 'Manage Jenkins'. Select 'Credentials' > System > Global credentials > Add Credentials
2. Enter your GitHub username in the textbox. Use username as secret if you choose. Next, is to add a password, but we'll be using tokens.
3. Visit your GitHub page > click your profile image > settings > Developer settings (at the bottom of the left panel)
4. To add tokens, 'Personal access tokens' > Tokens (classic) > Generate new token > Generate new token (classic). *You may generate a scope-specific token for the organization if you choose*
5. Enter a note, expiration, and check the boxes for your preferred access. Click 'Generate token'
6. Copy/paste the generated token into the Password textbox in Jenkins and enter "seniorprojecttoken" for easy future identification and configuration with current *Jenkinsfile.ci* for this project. Click 'Create'

### Pipeline configuration
1. Navigate back to the landing dashboard by clicking the Jenkins icon on the top left of your screen and select `New Item`. Enter a name for the project. *Choose a name with no spaces for Jenkins backend compatibility. For example, SeniorCapstoneTeam1 or project_team1* Select 'Multibranch Pipeline' option and click 'OK' to proceed. *You may also choose the 'Pipline' option but the configuration is slightly different.
2. Under 'Branch Sources' > Add source > GitHub > select *seniorprojecttoken* credentials, or the name you used > Copy/paste the repo url (https://github.com/P31CI-CD/CI-CD-Pipeline.git). Keep or modify the defaults for the other subsections.
3. Check 'GitHub project' and paste in our project's url.
4. Under the 'Build Configuration' section, keep the 'Mode' by Jenkinsfile and enter the Script path as "Week03/ops/Jenkinsfile.ci" This will be updated as the project progesses. The extension '.ci' specifies that this is the C.I. We will also use webhooks for our project, which will be integrated later.
5.  Check any other preferred settings, for example 'Discard old items'.
6. Skip the other properties for now. Configure them if you're familiar with Jenkins. Click 'Save' at the bottom of the page.
7. The Pipeline should automatically try to scan the repo. 
8. Click 'Scan Reposity Now' to run your first build for each branch. You can also run builds for specific branches.

## Webhooks configuration
1. I have added smee.io link for our project. To view this link, visit the project's repo > Settings > Webhooks *Read more about the installation here (https://www.jenkins.io/blog/2019/01/07/webhook-firewalls/)*
2. To install the smee clint, open a new terminal and run `npm install -g smee-client`
3. Then run `smee -u https://smee.io/2QAI9s8iW9oVrGGx -t http://localhost:8080/github-webhook/` *If you used a different port, remember to change it in the url*