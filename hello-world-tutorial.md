---

copyright:
  years: 2021, 2022
lastupdated: "2022-10-17"

keywords: instance tutorial, provision tutorial, docker

subcollection: cloud-databases

---

{:shortdesc: .shortdesc}
{:external: .external target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:note: .note}
{:important: .important}

# Deploying and Connecting a {{site.data.keyword.databases-for}} Instance 
{: #create-instance-tutorial}

## Objectives
{: #create-instance-tutorial-objectives}

This tutorial guides you through the process of deploying a {{site.data.keyword.databases-for}} instance and connecting it to a web front end by creating a webpage that allows visitors to input a word and its definition. These values are then stored in a database running on {{site.data.keyword.databases-for}}. You install the database infrastructure by using [Terraform](https://www.terraform.io/){: external} and your web application uses the popular [Express](https://www.terraform.io/){: external} framework. The application can then be run locally, or by using [Docker](https://www.docker.com/){: external}.

## Getting productive 
{: #create-instance-tutorial-getting-started}

To begin the deployment process, install some must-have productivity tools:

* You need to have an [{{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/registration).
* [Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm){: external} - to install packages to and from public npm registries
* [Terraform](https://www.terraform.io/){: external} - to codify and deploy infrastructure
* *Optional* [Docker](https://www.docker.com/){: external} - to run your application nonlocally

## Step 1: Obtain an API key to deploy infrastructure to your account
{: #create-instance-tutorial-step-1}

Follow [these steps](https://cloud.ibm.com/docs/account?topic=account-userapikey&interface=ui#create_user_key) to create an {{site.data.keyword.cloud_notm}} API key that enables a program or script without distributing your password to the script. You can create up to 20 API keys.

For security reasons, the API key is only available to be copied or downloaded at the time of creation. If the API key is lost, you must create a new API key.{: .important}

## Step 2: Clone the project
{: #create-instance-tutorial-step-2}

Clone the project from the {{site.data.keyword.databases-for}} [Hello World project GitHub repository](https://github.com/IBM-Cloud/clouddatabases-helloworld-examples){: external}.

```sh
git clone https://github.com/IBM-Cloud/clouddatabases-helloworld-examples.git
```
{: pre}

## Step 3: Install the infrastructure
{: #create-instance-tutorial-step-2}

1. From the main GitHub project folder, navigate into the service folder of your choice, for example, MySQL.

1. On your machine, create a document named `terraform.tfvars`, with the following fields:

   ```sh
   ibmcloud_api_key = "<your_api_key_from_step_1>"
   region = "<your_region"
   admin_password  = "<make_up_a_password>"
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

## Step 4: Run your app locally
{: #create-instance-tutorial-step-3}

1. To connect to the database from your local machine, ensure that you are in your service folder, then install the node dependencies and run the service with the following command:

   ```sh
   npm install
   npm run start
   ```
   {: pre}
   
   If successful, the output shows you are connected:
   
   
   ```sh
   #Connected!
   #Server is listening on port 8080
   Open a browser and visit http://localhost:8080
   ```
   {: pre}
   
   A welcome page with a database logo will be displayed in your browser window.

1. To test the interface, enter a word and its definition. The data pair is added to the database and appears in a list at the bottom of the page.

## Step 5 (optional): Run the app from a Docker container
{: #create-instance-tutorial-step-3}

The first step toward hosting your application from a service like Code Engine is to containerize the app code inside a Docker container and run it from there.

Make sure you are logged in to your Docker account. In the database, enter the following command:

```sh
docker build -t database-hello-world:1.0 . 
docker run -p 8080:8080 database-hello-world:1.0
```
{: pre}

Visit http://localhost:8080 to see the same page from the previous step.

Congratulations, you've created an app with a front end that feeds data into your {{site.data.keyword.databases-for}} deployment!
