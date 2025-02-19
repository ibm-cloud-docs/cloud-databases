---

copyright:
   years: 2022, 2024
lastupdated: "2024-10-04"

keywords: IBM Cloud Databases, ICD, terraform, terraform mongodbee, mongodb, mongodbee

subcollection: cloud-databases

content-type: tutorial
account-plan: paid
completion-time: 1h

---

{{site.data.keyword.attribute-definition-list}}	

# Provision a {{site.data.keyword.databases-for-mongodb}} Enterprise Edition instance with Terraform
{: #tutorial-provision-mongodbee-tf}
{: toc-content-type="tutorial"}
{: toc-completion-time="1h"}

In this tutorial, you learn how to use Terraform to provision a {{site.data.keyword.databases-for-mongodb}} Enterprise Edition instance that includes the {{site.data.keyword.databases-for-mongodb}} Enterprise Edition Analytics Add-On. The {{site.data.keyword.databases-for-mongodb}} EE Analytics Add-On allows you to run long-running analytical queries and/or provision a [MongoDB Connector for business intelligence(BI)](https://docs.mongodb.com/bi-connector/current/){: .external} to make your query data compatible with BI tools, such as [Tableau](https://www.tableau.com/){: .external}.
{: shortdesc}

## Overview of the available tools
{: #tutorial-provision-mongodbee-tf-prereqs}

Before beginning the process of provisioning a database with Terraform, [you need to have an {{site.data.keyword.cloud_notm}} account.](https://cloud.ibm.com/registration)

In this tutorial, you provision your database by using Terraform, a service that enables you to safely and predictably create, change, and improve infrastructure. It is an open source tool that codifies APIs into declarative configuration files that can be shared among team members, which are treated as code, edited, reviewed, and versioned. It is infrastructure as code. You write down what your infrastructure should look like and Terraform will create, update, and remove cloud resources as needed. For more information, see [Understand the basics of Terraform.](https://www.terraform.io/intro){: external}

To support a multi-cloud approach, Terraform works with providers. A provider is responsible for understanding API interactions and exposing resources. {{site.data.keyword.cloud}} has its provider for Terraform, enabling users of {{site.data.keyword.cloud}} to manage resources with Terraform. Although Terraform is categorized as infrastructure as code, it is not limited to Infrastructure-As-A-Service resources. For more information, see [ibm_database](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database).

## Step 1: Install Terraform
{: #tutorial-provision-mongodbee-install-cli}
{: step}

Follow the steps at [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/docker-get-started){: external} to install Terraform.

## Step 2: Configure the {{site.data.keyword.cloud}} Provider plug-in
{: #tutorial-provision-mongodbee-config-provider}
{: step}

1. [Create or retrieve an {{site.data.keyword.cloud}} API key.](/docs/account?topic=account-userapikey#create_user_key) The API key is used to authenticate with the {{site.data.keyword.cloud}} platform and to determine your permissions for {{site.data.keyword.cloud}} services.

1. Create a Terraform on {{site.data.keyword.cloud_notm}} Databases project directory. The directory holds all your configuration files that you create as part of this tutorial. The directory in this tutorial is named `tf-mongodbee`, but you can use any name for the directory.

   ```sh
   mkdir tf-mongodbee && cd tf-mongodbee
   ```
   {: codeblock}

1. In your project directory, create a variable definition file that is named `terraform.tfvars` and specify the {{site.data.keyword.cloud_notm}} API key that you retrieved. In addition, you specify the region where you want your {{site.data.keyword.cloud_notm}} resources to be created. If no region is specified, the {{site.data.keyword.cloud}} Provider plug-in automatically creates your resources in the us-south region. Variables that are defined in the `terraform.tfvars` file are automatically loaded by Terraform when the {{site.data.keyword.cloud_notm}} Provider plug-in is initialized and you can reference them in every Terraform configuration file that you use.

   Because the variable definitions file contains confidential information, do not push this file to a version control system. This file is meant to be on your local system only.{: .important}

   **Example `terraform.tfvars` file**

   ```terraform
   ibmcloud_api_key = "<IBMCLOUD_API_KEY>"
   region = "us-east"
   ```
   {: codeblock}

   The `us-east` region is provided as an example, not a requirement. Use the region that works best for your instance deployment.

1. Create a provider configuration file that is named `provider.tf`. Use this file to configure the {{site.data.keyword.cloud_notm}} Provider plug-in with the {{site.data.keyword.cloud_notm}} API key from your `terraform.tfvars` file. The plug-in uses this key to access {{site.data.keyword.cloud_notm}} and to work with your {{site.data.keyword.cloud_notm}} service. To access a variable value from the `terraform.tfvars` file, you must first declare the variable in the `provider.tf` file and then reference the variable by using the `var.<variable_name>` syntax.

    **Example `provider.tf` file**

    ```terraform
    terraform {
      required_providers {
        ibm = {
          source  = "IBM-Cloud/ibm"
          version = ">= 1.28.0"
        }
      }
    }

    variable "ibmcloud_api_key" {}
    variable "region" {}

    provider "ibm" {
      ibmcloud_api_key = var.ibmcloud_api_key
      region           = var.region
    }
    ```
    {: codeblock}

## Step 3: Provision a {{site.data.keyword.databases-for-mongodb}} instance
{: #tutorial-provision-mongodbee-provision-instance}
{: step}

In the same project directory, create a Terraform configuration file named `mongodbee.tf`.

**Example `mongodbee.tf` file**

```terraform
data "ibm_resource_group" "mongodbee_tutorial" {
  is_default = true
}
resource "ibm_database" "mongodbee_db" {
  resource_group_id = data.ibm_resource_group.mongodbee_tutorial.id
  name              = "terraform_mongodbee"
  service           = "databases-for-mongodb"
  plan              = "enterprise"
  location          = "us-east"
  service_endpoints = "public"
  adminpassword     = "password123changeme"
  group {
    group_id = "member"
    host_flavor {
      id = "b3c.4x16.encrypted"
    }
    disk {
      allocation_mb = 20480
    }
  }

  group {
    group_id = "analytics"

    members {
      allocation_count = 1
    }
  }

  group {
    group_id = "bi_connector"

    members {
      allocation_count = 1
    }
  }

  timeouts {
    create = "120m"
    update = "120m"
    delete = "15m"
  }
}
data "ibm_database_connection" "mongodbee_conn" {
  deployment_id = resource.ibm_database.mongodbee_db.id
  user_id       = resource.ibm_database.mongodbee_db.adminuser
  user_type     = "database"
  endpoint_type = "public"
}
output "bi_connector_connection" {
  description = "BI Connector connection string"
  value       = data.ibm_database_connection.mongodbee_conn.bi_connector.0.composed.0
}
output "analytics_connection" {
  description = "Analytics Node connection string"
  value       = data.ibm_database_connection.mongodbee_conn.analytics.0.composed.0
}
```
{: codeblock}

- **Resource group** - the Resource Group value you declare.
- **Name** - The service name can be any string and is the name that is used on the web and in the CLI to identify the new deployment.
- **Service** - For {{site.data.keyword.databases-for-mongodb}}, the service ID is `databases-for-mongodb`. Choose the correct Service ID for your deployment.
- **Plan** - This tutorial uses a Standard plan. For more information, see [{{site.data.keyword.cloud}} Pricing](https://www.ibm.com/cloud/pricing).
- **Location** - Choose a suitable region for your deployment instance.
- **Service endpoints** - Choose the service endpoints for your deployment instance. _"private"_ is recommended for production use.
- **Admin password** - You must set the admin password before you can use it to connect. For more information, see [Setting the Admin password](/docs/databases-for-mongodb?topic=databases-for-mongodb-user-management&interface=ui#user-management-set-admin-password-ui).
- **Group** Scaling groups represent the various resources that are allocated to a deployment. To see an example for configuring and deploying a database that uses `group` attributes, se[Sample database instance by using group attributes.](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database#sample-database-instance-by-using-group-attributes){external}
- **Group values** - Memory, disk, and CPU values are all based on minimum requirements for provisioning a {{site.data.keyword.databases-for-mongodb}} instance.
- **Timeouts** - Create, update, and delete values for this resource. {{site.data.keyword.databases-for}} `create` typically takes between 30-45 minutes. `delete` and `update` typically take 1 minute. Provisioning times are unpredictable. If the deployment fails due to a timeout, import the database resource once the `create` is complete.

## Step 4: Test your configuration
{: #tutorial-provision-mongodb-test}
{: step}

Now that you configured the {{site.data.keyword.cloud}} Provider plug-in for your resource, you can use Terraform to initialize, run, plan, and apply commands to provision the resource. You need the following commands:

| Command Description | Command |
| -------------- | -------------- |
| [`terraform init`](https://www.terraform.io/cli/commands/init){: external} | The `terraform init` command is used to initialize a working directory containing Terraform configuration files. |
| [`terraform fmt`](https://www.terraform.io/cli/commands/fmt){: external} | The `terraform fmt` command is used to rewrite Terraform configuration files to a canonical format and style. |
| [`terraform validate`](https://www.terraform.io/cli/commands/validate){: external} | The `terraform validate` command validates the configuration files in a directory  |
| [`terraform apply`](https://www.terraform.io/cli/commands/apply){: external} | The `terraform apply` command runs the actions that are proposed in a Terraform plan. |
{: caption="Terrarform provisioning commands" caption-side="bottom"}

 For more information, see [Provisioning {{site.data.keyword.cloud}} resources](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-manage_resources#provision_resources).

 To view sample Terraform templates with the complete Terraform configuration files to test, see [Sample templates](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-provider-template#sample-templates).

For an overview of Terraform resources and data sources, see [Index of Terraform on {{site.data.keyword.cloud}} resources and data sources](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-resources-datasource-list).
