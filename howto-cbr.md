---

copyright:
  years:  2022, 2025
lastupdated: "2025-03-24"

keywords: restricting access to cloud databases, restricting access to ICD, DataStax cbr, Elasticsearch cbr, EnterpriseDB cbr, etcd cbr, mongodb cbr, postgresql cbr, redis cbr, mysql cbr, rabbitmq cbr

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

This document outlines the process for using context-based restrictions to protect your {{site.data.keyword.databases-for}} resources. Use this document to prepare your resources for context-based restrictions. {{site.data.keyword.databases-for}} doesn't offer scoping rules to the control plane in this current phase of implementation.{: .important}

# Context-based restrictions
{: #cbr}

Context-based restrictions give account owners and administrators the ability to define and enforce access restrictions for {{site.data.keyword.cloud}} resources based on the context of access requests. Access to {{site.data.keyword.databases-for}} resources can be controlled with context-based restrictions and Identity and Access Management (IAM) policies.
{: shortdesc}

These restrictions work with traditional IAM policies, which are based on identity, to provide an extra layer of protection. Unlike IAM policies, context-based restrictions don't assign access. Context-based restrictions check that an access request comes from an allowed context that you configure. Since both IAM access and context-based restrictions enforce access, context-based restrictions offer protection even in the face of compromised or mismanaged credentials. For more information, see [What are context-based restrictions](/docs/account?topic=account-context-restrictions-whatis).

A user must have the Administrator role on the {{site.data.keyword.databases-for}} service to create, update, or delete rules. A user must also have either the Editor or Administrator role on the context-based restrictions service to create, update, or delete network zones. A user with the Viewer role on the context-based restrictions service can add network zones to a rule.
{: note}

Any {{site.data.keyword.cloudaccesstraillong_notm}} or audit log events generated come from the context-based restrictions service, not {{site.data.keyword.databases-for}}. {{site.data.keyword.databases-for}} supports audit events only for customer interactions with context-based restrictions-protected platform endpoint calls. {{site.data.keyword.databases-for}} does not support audit events when you enable context-based restrictions rules on the control plane API for your instances. For more information, see [Monitoring context-based restrictions](/docs/account?topic=account-cbr-monitor).

To start protecting your {{site.data.keyword.databases-for}} resources with context-based restrictions, see the tutorial for [Leveraging context-based restrictions to secure your resources](/docs/account?topic=account-context-restrictions-tutorial).

## How {{site.data.keyword.databases-for}} integrates with context-based restrictions
{: #cbr-overview}

You can create context-based restrictions for the {{site.data.keyword.databases-for}} service, specific resources, and specific APIs.

### Protecting {{site.data.keyword.databases-for}} resources
{: #cbr-overview-protect-services}

You can create context-based restrictions rules to protect specific **regions**, **resource groups**, and **instances**.

Region
:   Protects {{site.data.keyword.databases-for}} resources in a specific region. If you include a region in your context-based restrictions rule, resources in the network zones that you associate with the rule can interact with resources only in that region. If you use the CLI, you can specify the `--region` option to protect resources in a specific region. If you use the UI, you can specify *Region* in the resource attributes.

Resource groups
:   Protects a specific resource group. If you include a resource group in your context-based restrictions rule, resources in the network zones that you associate with the rule can interact only with resources in that resource group. Scoping a rule to a specific resource group is available only for rules that protect the cluster API type. If you use the CLI, you can specify the `--resource-group-id` option to protect resources in a specific resource group. If you use the UI, you can specify the *Resource group* in the resource attributes.

Instance
:   Protects a specific instance. If you include an instance in your context-based restrictions rule, resources in the network zones that you associate with the rule can interact only with resources in that instance. Scoping a rule to a specific instance is available only for rules that protect the cluster API type. If you use the CLI, you can specify the `--service-instance` option to protect instances in a specific resource group. If you use the UI, you can specify the *Service instance* in the resource attributes.

### Using the Command Line Interface (CLI)
{: cli}

You can create and manage context-based restrictions with the IBM Cloud CLI by [installing the context-based restrictions CLI plug-in](/docs/cli?topic=cli-cbr-plugin).

## Creating network zones
{: #network-zone}

A network zone represents an allowlist of IP addresses where an access request is created. It defines a set of one or more network locations that are specified by the following attributes:

* IP addresses, which include individual addresses, ranges, or subnets.
* VPCs.

### Creating network zones in the UI
{: #network-zone-ui}
{: ui}

1. Go to **Manage** > **Context-based restrictions** in the {{site.data.keyword.cloud}} console.
1. Select **Network zones**.
1. Click **Create**.
1. Name your network zone and provide a description.
1. Enter your *Allowed IP addresses.* You can enter a single IP address, a range of IP addresses, or a single CIDR.

   The **Denied IP addresses** field is optional and should include only exceptions that are contained within the IP ranges you provide in the allowed IP addresses field.
   {: note}

1. Choose your *Allowed VPCs*, selecting as many as you like.

1. **Reference a service**: You can select {{site.data.keyword.databases-for}} as a source service for context-based restrictions, but not as a target service. For example, you can provision a {{site.data.keyword.databases-for}} instance using BYOK from {{site.data.keyword.keymanagementservicefull}}. In this example, {{site.data.keyword.databases-for}} is the source formation and {{site.data.keyword.keymanagementservicefull}} is the target formation. Then, you would create a network zone with a {{site.data.keyword.databases-for}} service reference and create a rule associated with the network zone that targets {{site.data.keyword.keymanagementservicefull}}. To add a {{site.data.keyword.databases-for}} service reference, for *Service Type*, IAM services is autoselected. In the *Service* dropdown, select a specific {{site.data.keyword.databases-for}} service. If the zone you create is associated with a rule targeting {{site.data.keyword.databases-for}}, then a service reference is not allowed.

Service references function only from {{site.data.keyword.keymanagementserviceshort}} service to {{site.data.keyword.databases-for}}.
{: important}

### Create network zones in the CLI
{: #network-zone-cli}
{: cli}

To create network zones in the CLI, use the `cbr-zone-create` command to add resources to network zones. For more information, see the [context-based restrictions CLI reference](/docs/account?topic=account-cbr-plugin#cbr-zones-cli).

Create a zone by using a command like:

```sh
ibmcloud cbr zone-create --addresses=1.1.1.1,5.5.5.5 --name=<NAME>
```
{: .pre}

### Creating network zones in Terraform
{: #zones-tf}
{: terraform}

To create zones in Terraform, follow the instructions in the [IBM Cloud Terraform provider documentation](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cbr_zone){: external}.

Example Terraform script to create a CBR zone:

```sh
resource "ibm_cbr_zone" "cbr_zone" {
  account_id = "12ab34cd56ef78ab90cd12ef34ab56cd"
  addresses {
    type = "ipAddress"
    value = "169.23.56.234"
  }
  addresses {
    type = "ipRange"
    value = "169.23.22.0-169.23.22.255"
  }
  excluded {
    type  = "ipAddress"
    value = "169.23.22.10"
  }
  excluded {
    type  = "ipAddress"
    value = "169.23.22.11"
  }
  description = "this is an example of zone"
  excluded {
        type = "ipAddress"
        value = "value"
  }
  name = "an example of zone"
}
```

### Update network zones in the CLI
{: #update-network-zone-cli}
{: cli}

Update a zone by using a command like:

```sh
ibmcloud cbr zone-update <ZONE-ID> --addresses=1.2.3.4 --name=<NAME>
```
{: .pre}

Updating requires the `ZONE-ID`, not the zone name. Use the following command to list your zones and retrieve the relevant `ZONE-ID`:

```sh
ibmcloud cbr zones
```
{: .pre}

The `zone-update` command is an overwrite. Include all of the fields that are required as if you are creating the rule from scratch. If you omit any required fields, the rule overwrites those missing fields as empty, and the rule might fail because some of those fields are required, regardless of whether they are changing the rule. {: .important}

### Delete network zones in the CLI
{: #delete-network-zone-cli}
{: cli}

Delete a zone by using a command like:

```sh
ibmcloud cbr zone-delete <ZONE-ID>
```
{: .pre}

## Creating rules
{: #rules}

Rules restrict access to specific cloud resources based on resource attributes and contexts. A created rule can accept up to 2,000 IP/CIDR values for private endpoints and up to 2,000 IP/CIDR values for public endpoints. This limit is specfic to {{site.data.keyword.databases-for}}. Other {{site.data.keyword.cloud}} service limits may vary.

{{site.data.keyword.databases-for}} does not support IPv6 addresses. If an IPv6 address is included, it will be ignored.

Full closure of access to non-allowlisted endpoints: To provide a more robust security framework, we have implemented a significant change in access control for public and private endpoints. Going forward, access to both public and private endpoints that are not explicitly allowlisted will be fully closed. This restriction ensures only authorized access to your endpoints, minimizing the risk of unauthorized access.
{: important}

### Creating rules in the UI
{: #rules-ui}
{: ui}

1. Go to **Manage** > **Context-based restrictions** in the {{site.data.keyword.cloud}} console.
1. Select **Rules**.
1. Click **Create**.
1. Under **Service**, select the service you want to target with your rule.
1. Under **APIs**, select `Data plane`. Currently any other selection results in an error. 

   0 actions are expected for the Data Plane API type.
   {: .note}

   {{site.data.keyword.databases-for}} does not currently support **Control plane** as an option.
   {: .note}

1. Under **Resources**, scope the rule to **All resources** or **Specific resources**. For more information, see [Protecting {{site.data.keyword.databases-for}} resources](/docs/cloud-databases?topic=cloud-databases-cbr#cbr-overview-protect-services).
1. Click **Continue**.
1. Define the allowed endpoint types.
   - Keep the toggle set to **No** to allow all endpoint types.
   - Set the toggle to **Yes** to allow only specific endpoint types, then choose from the list.
1. Select a network zone or zones that you have already created, or create a new network zone by clicking **Create**.

   Contexts define from where your resources can be accessed, effectively linking your network zone to your rule.
   {: tip}

1. Click **Add** to add your configuration to the summary.
1. Click **Next**.
1. Name your rule.
1. Select how you want to enforce the rule.

   *Report-only* is not available for {{site.data.keyword.databases-for}}.
   {: important}

### Create rules in the CLI
{: #rules-cli}
{: cli}

To create a rule in the CLI, you need the appropriate {{site.data.keyword.databases-for}} `service_name`:

* `databases-for-postgresql`
* `databases-for-mongodb`
* `databases-for-redis`
* `databases-for-elasticsearch`
* `database-for-mysql`
* `messages-for-rabbitmq`
* `databases-for-enterprisedb`
* `databases-for-etcd`

All the other parameters that follow are explained in the [CBR plugin reference guide](https://cloud.ibm.com/docs/account?topic=account-cbr-plugin#cbr-rules-cli).

Example command for creating a CBR Rule:

```sh
ibmcloud cbr rule-create --enforcement-mode enabled --context-attributes "networkZoneId=<ZONE-ID>" --resource-group-id <RESOURCE_GROUP_ID> --service-name <SERVICE-NAME> --service-instance <SERVICE-INSTANCE> --api-types crn:v1:bluemix:public:context-based-restrictions::::api-type:data-plane --description <DESCRIPTION>
```
{: .pre}

The only `api-type` option currently supported by {{site.data.keyword.databases-for}} is  **Data plane**.
{: .note}

*Report-only* is not available for {{site.data.keyword.databases-for}}.
{: .important}

### Update rules in the CLI
{: #update-rules-cli}
{: cli}

Example command for updating a CBR rule:

```sh
ibmcloud cbr rule-update <RULE-ID> --enforcement-mode disabled --context-attributes="networkZoneId=<ZONE-ID>" --resource-group-id   <RESOURCE_GROUP_ID> --service-name <SERVICE_NAME> --api-types crn:v1:bluemix:public:context-based-restrictions::::api-type:data-plane --description    <DESCRIPTION>
```
{: .pre}

The `rule-update` command is an overwrite. Include all of the fields that are required as if you are creating the rule from scratch. If you omit any required fields, the rule overwrites those missing fields as empty, and the rule might fail because some of those fields are required, regardless of whether they are changing the rule.
{: .important}

Updating requires the `RULE-ID`, not the rule name. Use the following command to list your rules and retrieve the relevant `RULE-ID`:

```sh
ibmcloud cbr rules
```
{: .pre}

### Delete rules in the CLI
{: #delete-rules-cli}
{: cli}

Delete a rule by using a command like:

```sh
ibmcloud cbr rule-delete <RULE-ID>
```
{: .pre}

Use `ibmcloud cbr <command> — help` for a full list of options and parameters. For example, `ibmcloud cbr rule-create — help` outputs parameters for rule creation.
{: .tip}



### Creating rules in Terraform
{: #rules-tf}
{: terraform}

To create rules in Terraform, follow the instructions in the [IBM Cloud Terraform provider documentation](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cbr_rule){: external}.

To create a rule, you need the appropriate {{site.data.keyword.databases-for}} `service_name`:

* `databases-for-postgresql`
* `databases-for-mongodb`
* `databases-for-redis`
* `databases-for-elasticsearch`
* `database-for-mysql`
* `messages-for-rabbitmq`
* `databases-for-enterprisedb`
* `databases-for-etcd`

Create a rule by using a command like:

```sh
resource "ibm_cbr_rule" "cbr_rule" {
  contexts {
        attributes {
            name = "networkZoneId"
            value = "559052eb8f43302824e7ae490c0281eb"
        }
        attributes {
               name = "endpointType"
               value = "private"
    }
  }
  description = "this is an example of a rule with one context one zone"
  enforcement_mode = "enabled"
  operations {
        api_types {
            api_type_id = "api_type_id"
        }
  }
  resources {
        attributes {
            name = "accountId"
            value = "12ab34cd56ef78ab90cd12ef34ab56cd"
        }
        attributes {
              name = "serviceName"
              value = "network-policy-enabled"
        }
        tags {
              name     = "tag_name"
              value    = "tag_value"
        }
  }
}
```
{: pre}


### Verifying your rule
{: #rules-ui-verify}

To verify that your rule is applied, go to the {{site.data.keyword.cloud}} Dashboard and select the relevant instance from your *Resource List*. Within **Recent Tasks**, you see your rule's status.

The task of creating or modifying a rule goes into your instance's task queue. Depending on workload, it might take some time for your rule enforcement to complete.
{: .note}
