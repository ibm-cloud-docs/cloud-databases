---

copyright:
  years: 2021, 2025
lastupdated: "2025-01-29"

keywords: instance tutorial, provision tutorial, docker

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Deploying and connecting a {{site.data.keyword.databases-for}} instance 
{: #create-instance-tutorial}

## Objectives
{: #create-instance-tutorial-objectives}

This tutorial guides you through the process of deploying a {{site.data.keyword.databases-for}} instance and connecting it to a web front end by creating a webpage that allows visitors to input a word and its definition. These values are then stored in a database running on {{site.data.keyword.databases-for}}. You install the database infrastructure by using [Terraform](https://www.terraform.io/){: external} and your web application uses the popular [Express](https://www.terraform.io/){: external} framework. The application can then be run locally, or by using [Docker](https://www.docker.com/){: external}. 

## Getting productive 
{: #create-instance-tutorial-getting-started}

To begin the deployment process, install some must-have productivity tools:

* You need to have an [{{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/registration).
* [Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm){: external} - to install packages from public npm registries
* [Terraform](https://www.terraform.io/){: external} - to codify and deploy infrastructure
* *Optional* [Docker](https://www.docker.com/){: external} - to run your application nonlocally

## Obtain an API key to deploy infrastructure to your account
{: #create-instance-tutorial-step-1}
{: step}

Follow [these steps](https://cloud.ibm.com/docs/account?topic=account-userapikey&interface=ui#create_user_key) to create an {{site.data.keyword.cloud_notm}} API key that enables Terraform to provision infrastructure into your account. You can create up to 20 API keys.

For security reasons, the API key is only available to be copied or downloaded at the time of creation. If the API key is lost, you must create a new API key.{: .important}

## Clone the project
{: #create-instance-tutorial-step-2}
{: step}

Clone the project from the {{site.data.keyword.databases-for}} [Hello World project GitHub repository](https://github.com/IBM-Cloud/clouddatabases-helloworld-examples){: external}.

```sh
git clone https://github.com/IBM-Cloud/clouddatabases-helloworld-examples.git
```
{: pre}

## Install the infrastructure
{: #create-instance-tutorial-step-3}
{: step}

In this step, you deploy an instance of the database service you want to use. The GitHub repository contains folders for various {{site.data.keyword.databases-for}} resources.

1. From the main GitHub project folder, navigate into the `terraform` service folder of your choice, for example, `mysql/terraform`.

1. On your machine, create a document that is named `terraform.tfvars`, with the following fields:

   ```sh
   ibmcloud_api_key = "<YOUR_API_KEY_FROM_STEP_1>"
   region = "<YOUR_REGION>"
   admin_password  = "<CREATE_15_CHARACTER_PASSWORD>"
   ```
   {: pre}
   
   The `terraform.tfvars` document contains variables that you might want to keep secret so it is ignored by the GitHub repository.{: .note}

1. Install the infrastructure with the following command:

   ```sh
   terraform init 
   terraform apply --auto-approve
   ```
   {: pre}
   
   The Terraform script outputs configuration data that is needed to run the application, so copy it into the root folder:
   
   ```sh
   terraform output -json >../config.json
   ```
   {: pre}

## Run your app locally
{: #create-instance-tutorial-step-4}
{: step}

1. To connect to the database from your local machine, ensure that you are in your service folder, then install the node dependencies and run the service with the following commands:

   ```sh
   npm install
   ```
   {: pre}

   ```sh
   npm run start
   ```
   {: pre}
   
   If successful, the output shows you are connected:
   
   ```sh
   #Connected!
   #Server is listening on port 8080
   ```
   {: pre}

1. Open a browser and visit http://localhost:8080. You are greeted by a welcome page with a database logo that is displayed in your browser window.

1. To test the interface, enter a word and its definition. The data pair is added to the database and appears in a list at the bottom of the page.

## Run the app from a Docker container (optional)
{: #create-instance-tutorial-step-5}
{: step}

The first step toward hosting your application from a service like [Code Engine](https://www.ibm.com/cloud/code-engine){: .external} is to containerize the app code inside a Docker container and run it from there.

1. Make sure you are logged in to your Docker account. In the service folder of your chosen database, enter the following command:

   ```sh
   docker build -t database-hello-world:1.0 . 
   docker run -p 8080:8080 database-hello-world:1.0
   ```
   {: pre}

1. Open a browser and visit http://localhost:8080 to see the same welcome page from the [Step 4](#step-4-run-your-app-locally).

Congratulations, you've created an app with a front end that feeds data into your {{site.data.keyword.databases-for}} deployment!
