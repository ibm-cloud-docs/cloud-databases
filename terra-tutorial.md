---

copyright:
   years: 2022
lastupdated: "2022-05-16"

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

In this tutorial, you will provision your database using Terraform, which enables you to safely and predictably create, change, and improve infrastructure. It is an open source tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned. It is infrastructure as code. You write down what your infrastructure should look like and Terraform will create, update, remove cloud resources as needed. For more information, see [Understand the basics of Terraform.](https://www.terraform.io/intro){: external} 

To support a multi-cloud approach, Terraform works with providers. A provider is responsible for understanding API interactions and exposing resources. IBM Cloud has its provider for Terraform, enabling users of IBM Cloud to manage resources with Terraform. Although Terraform is categorized as infrastructure as code, it is not limited to Infrastructure-As-A-Service resources.

## Step 1: Install the Terraform CLI
{: #tutorial-provision-postgres-install-cli}
{: step}

1. Follow the steps at [Installing the Terrafom CLI](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-getting-started) to install the Terraform CLI.

1. After you install the command-line, set up and configure the {{site.data.keyword.cloud}} Provider plug-in. For more information, see [Configuring the IBM Cloud Provider plug-in.](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-getting-started#install_provider)

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

1. [Create or retrieve an IBM Cloud API key.](/docs/account?topic=account-userapikey#create_user_key) The API key is used to authenticate with the {{site.data.keyword.cloud}} platform and to determine your permissions for {{site.data.keyword.cloud}} services.

1. Create a variables file that is named `terraform.tfvars` and specify the {{site.data.keyword.cloud}} API key that you retrieved. In addition, specify the region where you want your {{site.data.keyword.cloud}} resources to be created. If no region is specified, Terraform on {{site.data.keyword.cloud}} automatically creates your resources in the `us-south` region. Variables that are defined in the `terraform.tfvars` file are automatically loaded by Terraform when the {{site.data.keyword.cloud}} Provider plug-in is initialized and you can reference them in every Terraform configuration file that you use

Because the `terraform.tfvars` file contains confidential information, do not push this file to a version control system. This file is meant to be on your local system only.
{: .important}
   
   Example of `terraform.tfvarsfile`
   ```terraform
   ibmcloud_api_key = "<ibmcloud_api_key>"
   region = "us-east"
   ```
   {: pre}
   {: codeblock}
   
   The `us-east` region is provided as an example, not a requirement. Use the region that works best for your instance deployment.{: .note} 
   
1. Create a provider configuration file that is named `provider.tf`. Use this file to configure the {{site.data.keyword.cloud}} Provider plug-in with the {{site.data.keyword.cloud}} API key from your `terraform.tfvars file`. The plug-in uses this key to access {{site.data.keyword.cloud}} and to work with your {{site.data.keyword.cloud}} service. To access a variable value from the `terraform.tfvars file`, you must first declare the variable in the `provider.tf file` and then reference the variable by using the `var.<variable_name>` syntax.

Example of `provider.tf` file

```terraform
variable "ibmcloud_api_key" {}
variable "region" {}
```

```terraform
provider "ibm" {
    ibmcloud_api_key   = var.ibmcloud_api_key
    region = var.region
    }
```
{: pre}
{: codeblock}

```terraform
data "ibm_resource_group" "resource_group" {
  name = "default"
}
```
{: pre}
{: codeblock}

Resource example for {{site.data.keyword.databases-for-postgresql}} instance

Setting up a deployment environment begins with creating a resource group. Its name is taken from an environment variable:

```terraform
# a resource group
resource "ibm_database" "ibm_postgres_instance" {
  resource_group_id = data.ibm_resource_group.default.id 
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

## Step 3: Test your configuration
{: #tutorial-provision-postgres-test}
{: step}

Now that you configured the IBM Cloud Provider plug-in for your resource you can start using Terraform on IBM Cloud to initialize, execute plan and apply commands to provision the resource. For more information, about Terraform commands to test your configuration, see [Provisioning IBM Cloud resources](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-manage_resources#provision_resources).

To view sample Terraform templates with the complete Terraform configuration files to test, refer to [Sample templates](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-provider-template#sample-templates).

For an overview of the Terraform resources and data sources that you can use, see the [Index of Terraform on IBM Cloud resources and data sources](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-resources-datasource-list).
