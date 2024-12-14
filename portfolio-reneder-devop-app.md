 

# Portfolio DevOps Project

*Automating Application Deployment with CI/CD*

**Objective**
This project focuses on setting up and implementing a CI/CD pipeline to automate the deployment of a Python Flask application. The deployment is done on the Render cloud platform, showcasing how automation can streamline application updates and hosting.

1. **Version Control**: Git and GitHub for managing code.
2. **Deployment Framework**: Render for hosting the application.
3. **CI/CD Pipeline**: Automated workflows using GitHub Actions.
4. **Python Framework**: Flask for creating the application.

------------------------------------------------------------
**Render Cloud platform Deployment Process**

<img src="Render Cloud Platform Deployment Process.png" alt="Render Cloud Platform Deployment Process" width="520" height="202">

This process outlines how the application is deployed and hosted on the Render cloud platform as part of the CI/CD pipeline:

1. **Build Initialization**
1.1 When a push is made to the main branch, the Render platform is triggered to start the deployment process.
1.2 The platform begins by setting up the build environment using the application’s linked repository (e.g., GitHub).

____________________________________________________________
**GitHub Actions dashboard**

<img src="GitHub Actions dashboard.png" alt width= "395" height="150">

**Function**

This shows the GitHub Actions dashboard where the CI/CD workflow (Test CI/CD Pipeline) is defined and triggered.
**It lists**
Workflow name
Test CI/CD pipeline.
**Status**
In progress (or other states like "Success" or "Failed").
**Branch** 
main
**Process**

Whenever a new commit is pushed to the main branch, this workflow is triggered automatically.
The workflow contains defined steps like setting up Python, installing dependencies, and deploying to Render.

**Key Takeaway for Portfolio**

This screenshot demonstrates the CI/CD pipeline setup using GitHub Actions, which automatically triggers workflows based on code changes.
_______________________________________________________________________

**Live web application**
<img src="Live Application web.png" alt width= "380">

This screen shot is  live application reflects the outcome of the automated CI/CD pipeline, 
showcasing successful deployment and hosting on Render.

**Function**

This is the final result of the CI/CD pipeline: the deployed application accessible via the Render-hosted URL (render-devops-app.onrender)
The web page confirms that the application is live and functional.

**Process**
Once the deployment is successful on Render, the application becomes publicly accessible.
The URL provided by Render can be used to access the application.
_____________________________________________________________________ 
 
 **Error logs in action github action**
 <img src= "Error Logs in GitHub Actions.png" alt width= "550">

 **Function**

This shows an error encountered during a failed GitHub Actions workflow.
The error (curl: (3) URL using bad/illegal format or missing URL) occurred during the Deploy to Render step.

**Process**
The error happened because of an incorrect or missing URL in the curl command used for deployment.

**Steps taken to resolve the error**
Identified the issue in the logs.
Corrected the URL in the deploy.yml file to ensure the proper API endpoint was used.
Re-ran the workflow after making the fix.

**Key Takeaway for Portfolio**

Encountered and resolved deployment errors by debugging logs in GitHub Actions. The fix involved correcting the API endpoint in the deployment configuration. 
____________________________________________________________________

**Successful CI/CD Pipeline**

<img src= "Successful CI CD Pipeline.png" alt width= "550">

**Function**

This shows a successful run of the CI/CD pipeline in GitHub Actions.
All steps (Setup Job, Checkout Code, Set up Python, Install Dependencies, Deploy to Render) are marked as completed.

**Process**
After fixing the error in the previous step, the pipeline was re-run, leading to a successful deployment.
Each step in the workflow is executed without any errors.

**Key Takeaway for Portfolio**
This screenshot demonstrates a successful CI/CD pipeline run, highlighting the automated workflow's efficiency and reliability.