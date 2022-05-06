---

copyright:
   years: 2022
lastupdated: "2022-05-06"

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

# Provision a {{site.data.keyword.databases-for-postgresql}} instance with Terraform
{: #tutorial-provision-postgres-tf}
{: toc-content-type="tutorial"} 
{: toc-completion-time="2h"} 

In this tutorial, you learn how to use Terraform to provision an {{site.data.keyword.databases-for-postgresql}} running on {{site.data.keyword.containershort_full}}. 
{: shortdesc}

## Before you begin
{: #tutorial-provision-postgres-tf-prereqs}

* [You need to have an {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/registration).
* [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-getting-started).
* [Understand the basics of Terraform](https://www.terraform.io/intro){: external}.
* [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli){: external}.
* [Install {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).
* [Use the console, CLI, or API to create an {{site.data.keyword.cloud}} API key](/docs/account?topic=account-userapikey&interface=ui#create_user_key)

## Establish Provider 
{: #tutorial-provision-postgres-tf-provider}
{: step}

To provision your Terraform provider, see the example 

```shell
terraform {
  required_providers {
    ibm = {
      source  = "IBM-Cloud/ibm"
      version = "~> 9.6"
    }
  }
}
```

Ensure your version number matches the latest Major version, which can be found on the [Database Versioning Policy page.](/docs/cloud-databases?topic=cloud-databases-versioning-policy#version-definitions)
{: .note}

## Configure the IBM Provider
{: #tutorial-provision-postgres-tf-sh2}
{: step}

```shell
provider "ibm" {
  region = "us-south" # The deployment's region
  ibmcloud_api_key = "<API_KEY>"
}
data "ibm_resource_group" "default" {
  is_default = true
}
resource "ibm_database" "mongodb_enterprise_helen" {
  resource_group_id = data.ibm_resource_group.default.id
  name              = "<your_database_name>" # The name can be any string and is the name that is used on the web and in the CLI to identify the new deployment.
  service           = "databases-for-postgresql" # The service you will be using for deployment.
  plan              = "enterprise" # Your service plan
  location          = "<LOCATION>" # Your desired instance location.
  adminpassword     = "<PASSWORD>" 
  group {
    group_id = "member"
    memory {
      allocation_mb = 14336
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
output "Mongodb_connection_string" {
  value = "http://${ibm_database.mongodb_enterprise_helen.connectionstrings[0].composed}"
}
```

## task-oriented title 3
{: #tutorial-provision-postgres-tf-sh3}
{: step}

## task-oriented title 4
{: #tutorial-provision-postgres-tf-sh4}
{: step}

## Next steps
{: #tutorial-provision-postgres-tf-sh5}
