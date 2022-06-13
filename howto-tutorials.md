---
copyright:
  years: 2019, 2022
lastupdated: "2022-06-13"

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

The following tutorials are devised to walk you through creating and maintaining deployment environments.

## Getting productive 
{: #productivity-tools}

Before you begin, it's a good idea to install some necessary productivity tools:

- The [{{site.data.keyword.databases-for}} CLI plug-in](https://cloud.ibm.com/docs/databases-cli-plugin) - the CLI interface to interact with the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction)
- An {{site.data.keyword.cloud_notm}} account, [sign up here](https://cloud.ibm.com/registration/)
- [The Kubernetes CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/) - a CLI interface for running commands against Kubernetes clusters.
- [oc](https://docs.openshift.com/container-platform/4.7/cli_reference/openshift_cli/getting-started-cli.html) - manages Red Hat OpenShift applications, and provides tools to interact with each component of your system
- [Helm 3](https://helm.sh/) - helps you manage Kubernetes applications. Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.
- [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) - automates your resource provisioning
- [jq](https://stedolan.github.io/jq/) - a lightweight and flexible command-line JSON processor
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - an open source-distributed version control system

To avoid the installation of these tools, you can also use the [{{site.data.keyword.cloud-sh_short}}](https://cloud.ibm.com/sh) from the {{site.data.keyword.cloud_notm}} console. {: tip}

## IBM Solutions Tutorials
{: #tutorial-solutions}

### Moving a VM based app to Kubernetes
{: #tutorial-solutions-terraform-app}

For a detailed tutorial on moving a VM based app to a Kubernetes cluster by using Kubernetes Service, check out [Moving a VM based app to Kubernetes
](/docs/solution-tutorials?topic=solution-tutorials-vm-to-containers-and-kubernetes). This tutorial walks you through storing app pod data in an {{site.data.keyword.databases-for}} service, allowing {{site.data.keyword.databases-for}} to easily configure and manage your database-as-a-service (DBaaS) with built-in backups and scaling.

### Modern web application with MEAN stack
{: #tutorial-solutions-mean-stack}

Using [Databases for MongoDB](/docs/databases-for-mongodb), [create a Modern web application with MEAN stack](/docs/solution-tutorials?topic=solution-tutorials-mean-stack). You learn how to run a MEAN starter locally, create and use a managed database-as-a-service (DBasS), deploy the app to IBM Cloud, and scale the database resources.

### Scale workloads in shared and dedicated VPC environments
{: #tutorial-solutions-vpc-enviro}

Use [Databases for PostgreSQL](/docs/databases-for-postgresql) to set up isolated workloads in a shared (multi-tenant) environment and a dedicated (single-tenant) environment in the [Scale workloads in shared and dedicated VPC environments](/docs/solution-tutorials?topic=solution-tutorials-vpc-scaling-dedicated-compute) tutorial.

## {{site.data.keyword.databases-for}} Tutorials
{: #tutorial-icd}

### An example {{site.data.keyword.containershort_notm}} Application
{: #example-k8s-app}

The [{{site.data.keyword.databases-for}} "Hello World" Kubernetes tutorial](https://github.com/IBM-Cloud/clouddatabases-helloworld-kubernetes-examples) repository holds sample {{site.data.keyword.cloud}} applications that show you how to connect to a {{site.data.keyword.databases-for}} deployment to an {{site.data.keyword.containerlong_notm}} application written in various programming languages.  

Each Git branch of the examples repository corresponds to samples in a particular programming language. For example, when you click **Branch**, a **Node** branch exists where all examples are written in JavaScript that uses Node.js. The files in each folder correspond to either a database or a message queue.  