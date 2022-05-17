---

copyright:
   years: 2022
lastupdated: "2022-05-17"

keywords: IBM Cloud Databases, ICD, terraform

subcollection: cloud-databases

content-type: tutorial
account-plan: paid
completion-time: 1h

---

{:external: .external target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:tip: .tip}
{:note: .note}
{:important: .important}

# Provision a {{site.data.keyword.databases-for-postgresql}} instance with Terraform
{: #tutorial-provision-postgres-tf}
{: toc-content-type="tutorial"} 
{: toc-completion-time="1h"} 

In this tutorial, you learn how to use Terraform to provision a {{site.data.keyword.databases-for-postgresql}} instance. 
{: shortdesc}

## Overview of the available tools
{: #tutorial-provision-postgres-tf-prereqs}

Before beginning the process of provisioning a database with Terraform, [you need to have an {{site.data.keyword.cloud_notm}} account.](https://cloud.ibm.com/registration) 

In this tutorial, you provision your database by using Terraform, which enables you to safely and predictably create, change, and improve infrastructure. It is an open source tool that codifies APIs into declarative configuration files that can be shared among team members, which are treated as code, edited, reviewed, and versioned. It is infrastructure as code. You write down what your infrastructure should look like and Terraform will create, update, and remove cloud resources as needed. For more information, see [Understand the basics of Terraform.](https://www.terraform.io/intro){: external} 

To support a multi-cloud approach, Terraform works with providers. A provider is responsible for understanding API interactions and exposing resources. {{site.data.keyword.cloud}} has its provider for Terraform, enabling users of {{site.data.keyword.cloud}} to manage resources with Terraform. Although Terraform is categorized as infrastructure as code, it is not limited to Infrastructure-As-A-Service resources. For more information, see [ibm_database](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database).

## Step 1: Install the Terraform CLI
{: #tutorial-provision-postgres-install-cli}
{: step}

1. Follow the steps at [Installing the Terrafom CLI](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-getting-started) to install the Terraform CLI.

## Step 2: Configure the {{site.data.keyword.cloud}} Provider plug-in
{: #tutorial-provision-postgres-config-provider}
{: step}

1. After you install the command-line, set up and configure the {{site.data.keyword.cloud}} Provider plug-in. For more information, see [Configuring the {{site.data.keyword.cloud}} Provider plug-in.](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-getting-started#install_provider)

1. Create a `versions.tf` file with the following content. In this file, specify the {{site.data.keyword.cloud}} Provider plug-in version that you want to use with the version parameter for {{site.data.keyword.cloud}} Provider plug-in, and `required_version` to specify the Terraform template version. If no version parameter is specified, {{site.data.keyword.cloud}} Provider automatically uses the latest version of the provider. For a list of supported {{site.data.keyword.cloud}} Provider versions, see [{{site.data.keyword.cloud}} Provider plug-in releases](https://github.com/IBM-Cloud/terraform-provider-ibm/releases){: external}.

   Example

   ```terraform
   terraform {
     required_providers {
       ibm = {
         source = "IBM-CLoud/ibm"
         version = "-> 1.41.0"
       }
     }
   }
   ```
   {: pre}
   {: codeblock}

1. [Create or retrieve an {{site.data.keyword.cloud}} API key.](/docs/account?topic=account-userapikey#create_user_key) The API key is used to authenticate with the {{site.data.keyword.cloud}} platform and to determine your permissions for {{site.data.keyword.cloud}} services.

1. Create a Terraform on {{site.data.keyword.cloud_notm}} Databases project directory. The directory holds all your configuration files that you create as part of this tutorial. The directory in this tutorial is named `tf-postgres`, but you can use any name for the directory.

   ```terraform
   mkdir tf-postgres && cd tf-postgres
   ```
   {: pre}
   {: codeblock}

1. In your project directory, create a `terraform.tfvars` file and add the {{site.data.keyword.cloud}} API key that you created earlier. In addition, specify the region where you want your {{site.data.keyword.cloud}} resources to be created. If no region is specified, Terraform on {{site.data.keyword.cloud}} automatically creates your resources in the `us-south` region. The `terraform.tfvars` file is a variables file that you store on your local machine. When you initialize the CLI, all variables that are defined in this file are automatically loaded into Terraform on {{site.data.keyword.cloud}} and you can reference them in every Terraform on {{site.data.keyword.cloud}} configuration file in the same project directory.

   Because the `terraform.tfvars` file contains confidential information, do not push this file to a version control system. This file is meant to be on your local system only.
   {: .important}
   
   Example of `terraform.tfvars` file
   ```terraform
   ibmcloud_api_key = "<ibmcloud_api_key>"
   region = "us-east"
   ```
   {: pre}
   {: codeblock}
   
   The `us-east` region is provided as an example, not a requirement. Use the region that works best for your instance deployment.
   
1. In the same project directory, create a provider configuration file that is named `provider.tf`. Use this file to configure the {{site.data.keyword.cloud}} Provider plug-in with the {{site.data.keyword.cloud}} API key from your `terraform.tfvars` file. The plug-in uses this key to access {{site.data.keyword.cloud}} and to work with your {{site.data.keyword.cloud}} service. To access a variable value from the `terraform.tfvars` file, you must first declare the variable in the `provider.tf` file and then reference the variable by using the `var.<variable_name>` syntax.

   Example of `provider.tf` file
   
   ```terraform
   variable "ibmcloud_api_key" {}
   variable "region" {}
   ```
   {: pre}
   {: codeblock}
   
   ```terraform
   provider "ibm" {
       ibmcloud_api_key   = var.ibmcloud_api_key
       region = var.region
       }
   ```
   {: pre}
   {: codeblock}
   
   
   Great! Now that you completed your Terraform on {{site.data.keyword.cloud}} setup, you can go ahead and provision a {{site.data.keyword.databases-for-postgresql}} instance.

## Step 3: Provision a {{site.data.keyword.databases-for-postgresql}} instance
{: #tutorial-provision-postgres-provision-instance}
{: step}

1. To set up a deployment environment, create a resource group that organizes your account resources for access control and billing purposes. For more information, see [Using the catalog](/docs/databases-for-postgresql?topic=cloud-databases-provisioning#catalog). 

   Example
   ```terraform
   data "ibm_resource_group" "resource_group" {
     name = "postgres_resource_group_1"
   }
   ```
   {: pre}
   {: codeblock}

2. Provision your {{site.data.keyword.databases-for-postgresql}} instance

   ```terraform
   # a resource group
   resource "ibm_database" "postgresql_db" {
     resource_group_id = data.ibm_resource_group.postgres_resource_group_1.id 
     name              = "provision_terraform_postgres"
     service           = "databases-for-postgresql"
     plan              = "standard" 
     location          = "us-east" 
     adminpassword     = "password123" 
     group {
       group_id = "member"
       memory {
         allocation_mb = 1024
       }
       disk {
         allocation_mb = 5120
       }
     }
     timeouts {
       create = "120m"
       update = "120m"
       delete = "15m"
     }
   }
   ```
   {: pre}
   {: codeblock}
   
   ```terraform
   output "Postgresql" {
     value = "http://${ibm_database.postgresql_default.connectionstrings[0].composed}"
   }
   ```
   {: codeblock}
   {: pre}

   - **Resource group** - the Resource Group value you declare. 
   - **Name** - The service name can be any string and is the name that is used on the web and in the CLI to identify the new deployment.
   - **Service** - For {{site.data.keyword.databases-for-postgresql}}, the service ID is `databases-for-postgresql`. Choose the correct Service ID for your deployment.
   - **Plan** - This tutorial uses a Standard plan. For more information on pricing, see [{{site.data.keyword.cloud}} Pricing](https://www.ibm.com/cloud/pricing).
   - **Location** - Choose a suitable region for your deployment instance.
   - **Admin Password** - The {{site.data.keyword.databases-for-postgresql}} service is provisioned with an admin user, so you can manage PostgreSQL by using its command-line tool, `psql`. For more information, see [Setting the Admin Password](/docs/databases-for-postgresql?topic=databases-for-postgresql-admin-password).
   - **Group** Scaling groups represent the various resources that are allocated to a deployment. To see an example for configuring and deploying a database that uses `group` attributes, see [Sample database instance by using group attributes.](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database#sample-database-instance-by-using-group-attributes){: external}
   - **Group values** - Memory, disk, and CPU values are all based on minimum requirements for provisioning a {{site.data.keyword.databases-for-postgresql}} instance.
   - **Timeouts** - Create, update, and delete values for this resource. ICD `create` typically takes between 30-45 minutes. `delete` and `update` typically take one minute. Provisioning times are unpredictable. If the deployment fails due to a timeout, import the database resource once the `create` is complete.



## Step 4: Test your configuration
{: #tutorial-provision-postgres-test}
{: step}

Now that you configured the {{site.data.keyword.cloud}} Provider plug-in for your resource you can start using Terraform on {{site.data.keyword.cloud}} to initialize, run, plan, and apply commands to provision the resource. For more information, about Terraform commands to test your configuration, see [Provisioning {{site.data.keyword.cloud}} resources](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-manage_resources#provision_resources).

To view sample Terraform templates with the complete Terraform configuration files to test, refer to [Sample templates](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-provider-template#sample-templates).

For an overview of the Terraform resources and data sources that you can use, see the [Index of Terraform on {{site.data.keyword.cloud}} resources and data sources](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-resources-datasource-list).
