---

copyright:
   years: 2022
lastupdated: "2022-05-09"

keywords: IBM Cloud Databases, ICD, terraform

subcollection: cloud-databases

content-type: tutorial
account-plan: paid
completion-time: 2h

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
{: toc-completion-time="2h"} 

In this tutorial, you learn how to use Terraform to provision an {{site.data.keyword.databases-for-postgresql}}. For more information, see [IBM Cloud in the Terraform Registry.](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}
{: shortdesc}

## Before you begin
{: #tutorial-provision-postgres-tf-prereqs}

* [You need to have an {{site.data.keyword.cloud_notm}} account.](https://cloud.ibm.com/registration)
* [Understand the basics of Terraform.](https://www.terraform.io/intro){: external}
* [Install {{site.data.keyword.cloud_notm}} CLI.](/docs/cli?topic=cli-install-ibmcloud-cli)

## Step 1: Install the Terraform CLI
{: #tutorial-provision-postgres-install-cli}
{: step}

Follow the steps at [Installing the Terrafom CLI](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-getting-started) to install the Terraform CLI.

## Step 2: Configure the {{site.data.keyword.cloud}} Provider plug-in
{: #tutorial-provision-postgres-install-cli}
{: step}

Once you have installed the command-line, set up and configure the {{site.data.keyword.cloud}} Provider Plug-in. For more information, see [Configuring the IBM Cloud Provider plug-in](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-getting-started#install_provider)

1. Create a `versions.tf` file with the following content. In this file, specify the {{site.data.keyword.cloud}} Provider plug-in version that you want to use with the version parameter for {{site.data.keyword.cloud}} Provider plug-in, and `required_version` to specify the Terraform template version. If no version parameter is specified, {{site.data.keyword.cloud}} Provider automatically uses the latest version of the provider. For a list of supported {{site.data.keyword.cloud}} Provider versions, see [{{site.data.keyword.cloud}} Provider plug-in releases](https://github.com/IBM-Cloud/terraform-provider-ibm/releases){: external}.

   PostgreSQL Example
   ```shell
   terraform {
     required_providers {
       ibm = {
         source = "IBM-CLoud/ibm"
         version = "-> 9.6"
       }
     }
   }
   ```
   {: pre}

1. [Create or retrieve an IBM Cloud API key](/docs/account?topic=account-userapikey#create_user_key) The API key is used to authenticate with the {{site.data.keyword.cloud}} platform and to determine your permissions for {{site.data.keyword.cloud}} services.
1. Create a variables file that is named `terraform.tfvars` and specify the {{site.data.keyword.cloud}} API key that you retrieved. In addition, specify the region where you want your {{site.data.keyword.cloud}} resources to be created. If no region is specified, Terraform on {{site.data.keyword.cloud}} automatically creates your resources in the `us-south` region. Variables that are defined in the `terraform.tfvars` file are automatically loaded by Terraform when the {{site.data.keyword.cloud}} Provider plug-in is initialized and you can reference them in every Terraform configuration file that you use.

Because the terraform.tfvars file contains confidential information, do not push this file to a version control system. This file is meant to be on your local system only.
{: .important}

Example of terraform.tfvarsfile
```shell
ibmcloud_api_key = "<ibmcloud_api_key>"
region = "<region>"
```
{: pre}

```shell
provider "ibm" {
  region = "us-south" # The deployment's region
  ibmcloud_api_key = "<API_KEY>"
}
data "ibm_resource_group" "default" { # The resource group is "Default", unless specified by you.
  is_default = true
}
resource "ibm_database" "mongodb_enterprise_helen" {
  resource_group_id = data.ibm_resource_group.default.id #
  name              = "<your_database_name>" # The name can be any string and is the name that is used on the web and in the CLI to identify the new deployment.
  service           = "databases-for-postgresql" # The service you will be using for deployment.
  plan              = "enterprise" # Your service plan
  location          = "<LOCATION>" # Your desired instance location, for example, "us-south".
  adminpassword     = "<PASSWORD>" 
  group {
    group_id = "member"
    memory {
      allocation_mb = 57344
    }
    disk {
      allocation_mb = 573440
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
output "Mongodb_connection_string" {
  value = "http://${ibm_database.mongodb_enterprise_helen.connectionstrings[0].composed}"
}
```
