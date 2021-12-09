---
copyright:
  years: 2019, 2021
lastupdated: "2021-12-09"

keywords: kubernetes, tutorial, setup, terraform, IBM Cloud Databases, ICD

subcollection: cloud-databases
---

{:external: .external target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:tip: .tip}
{:note: .note}

# Getting Started with {{site.data.keyword.databases-for}} tutorials 
{: #tutorial-getting-started}

## Getting productive 
{: #productivity-tools}

Install necessary productivity tools:

- The [{{site.data.keyword.databases-for}} CLI plug-in](https://cloud.ibm.com/docs/databases-cli-plugin) - the command line interface to interact with the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction)
- An {{site.data.keyword.cloud_notm}} account, [sign up here](https://cloud.ibm.com/registration/)
- [The Kubernetes CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/) - a command line interface for running commands against Kubernetes clusters.
- oc - manages OpenShift applications, and provides tools to interact with each component of your system
- Helm 3 - helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application
- [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) - automates your resource provisioning
- jq - a lightweight and flexible command-line JSON processor
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - a free and open source distributed version control system

To avoid the installation of these tools, you can also use the {{site.data.keyword.cloud-shell_short}} from the {{site.data.keyword.cloud_notm}} console. {: tip}

### IBM Solution Tutorials Terraform Tutorial
{: #tutorial-solutions-terraform-app}

For a detailed tutorial on creating and maintaining your databases using {{site.data.keyword.cloud_notm}} CLI and [Terraform](https://www.terraform.io/), check out [Plan, create and update deployment environments
](/docs/solution-tutorials?topic=solution-tutorials-plan-create-update-deployments) on the [IBM solution tutorials](/docs/solution-tutorials?topic=solution-tutorials-tutorials) page.

### An example {{site.data.keyword.containershort_notm}} Application
{: #tutorial-k8s-app}

The [{{site.data.keyword.databases-for}} "Hello World" Kubernetes examples](https://github.com/IBM-Cloud/clouddatabases-helloworld-kubernetes-examples) repository holds sample {{site.data.keyword.cloud}} applications that show you how to connect to a {{site.data.keyword.databases-for}} deployment to an {{site.data.keyword.containerlong_notm}} application written in a various programming languages.  

Each Git branch of the examples repository corresponds to samples in a particular programming language. For example, when you click **Branch**, a **Node** branch exists where all examples are written in JavaScript that uses Node.js. The files in each folder correspond to either a database or a message queue.  

### An example Cloud Foundry Application
{: #tutorial-cf-app}

This tutorial uses a [sample app](https://github.com/IBM-Cloud/clouddatabases-helloworld-cloudfoundry-examples) to demonstrate how to connect a Cloud Foundry application in {{site.data.keyword.cloud_notm}} to a {{site.data.keyword.databases-for}} deployment. The application creates, reads from, and writes to a database that uses data that is supplied through the app's web interface.

Each Git branch of the [repository](https://github.com/IBM-Cloud/clouddatabases-helloworld-cloudfoundry-examples) corresponds to samples in a particular programming language. For example, when you click **Branch** you see a **Node** branch, where all examples are written in JavaScript that uses Node.js. The files in each folder correspond to either a database or a message queue. 