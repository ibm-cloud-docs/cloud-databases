---

copyright:
  years:  2022
lastupdated: "2022-10-20"

keywords: restricting access to cloud databases, restricting access to ICD, DataStax cbr, Elasticsearch cbr, EnterpriseDB cbr, etcd cbr, mongodb cbr, postgresql cbr, redis cbr, mysql cbr, rabbitmq cbr

subcollection: cloud-databases

---

{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:tip: .tip}
{:note: .note}
{:important: .important}	
{:experimental: .experimental}
{{site.data.keyword.attribute-definition-list}}

This document outlines the process for using context-based restrictions to protect your {{site.data.keyword.databases-for}} resources. Use this document to prepare your resources for context-based restrictions. {{site.data.keyword.databases-for}} doesn't offer scoping rules to the control plane API in this current phase of implementation.{: .important}

# Protecting {{site.data.keyword.databases-for}} resources with context-based restrictions
{: #cbr}

Context-based restrictions give account owners and administrators the ability to define and enforce access restrictions for {{site.data.keyword.cloud}} resources based on the context of access requests. Access to {{site.data.keyword.databases-for}} resources can be controlled with context-based restrictions and Identity and Access Management (IAM) policies.
{: shortdesc}

These restrictions work with traditional IAM policies, which are based on identity, to provide an extra layer of protection. Unlike IAM policies, context-based restrictions don't assign access. Context-based restrictions check that an access request comes from an allowed context that you configure. Since both IAM access and context-based restrictions enforce access, context-based restrictions offer protection even in the face of compromised or mismanaged credentials. For more information, see [What are context-based restrictions](/docs/account?topic=account-context-restrictions-whatis).

A user must have the Administrator role on the {{site.data.keyword.databases-for}} service to create, update, or delete rules. A user must also have either the Editor or Administrator role on the context-based restrictions service to create, update, or delete network zones. A user with the Viewer role on the context-based restrictions service can only add network zones to a rule. 
{: note}

Any {{site.data.keyword.cloudaccesstraillong_notm}} or audit log events generated come from the context-based restrictions service, not {{site.data.keyword.databases-for}}. {{site.data.keyword.databases-for}} supports audit events only for customer interactions with context-based restrictions-protected platform endpoint calls. {{site.data.keyword.databases-for}} does not support audit events when you enable context-based restrictions rules on the control plane API for your instances. For more information, see [Monitoring context-based restrictions](/docs/account?topic=account-cbr-monitor).

To get started protecting your {{site.data.keyword.databases-for}} resources with context-based restrictions, see the tutorial for [Leveraging context-based restrictions to secure your resources](/docs/account?topic=account-context-restrictions-tutorial).

## How {{site.data.keyword.databases-for}} integrates with context-based restrictions
{: #cbr-overview}

You can create context-based restrictions for the {{site.data.keyword.databases-for}} service, specific resources, and specific APIs.

### Protecting {{site.data.keyword.databases-for}} resources
{: #cbr-overview-protect-services}

You can create context-based restrictions rules to protect specific **regions**, **resource groups**, and **instances**.

Region
:   Protects {{site.data.keyword.databases-for}} resources in a specific region. If you include a region in your context-based restrictions rule, resources in the network zones that  you associate with the rule can interact only with resources in that region. If you use the CLI, you can specify the `--region` option to protect resources in a specific region. If you use the UI, you can specify *Region* in the resource attributes. 

Resource groups
:   Protects a specific resource group. If you include a resource group in your context-based restrictions rule, resources in the network zones that you associate with the rule can interact only with resources in that resource group. Note that scoping a rule to a specific resource group is available only for rules that protect the cluster API type. If you use the CLI, you can specify the `resource-group-id` option to protect resources in a specific resource group. If you use the UI, you can specify the *Resource group* in the resource attributes.

Instance
:   Protects a specific instance. If you include an instance in your context-based restrictions rule, resources in the network zones that you associate with the rule can interact only with resources in that instance. Note that scoping a rule to a specific instance is available only for rules that protect the cluster API type. If you use the CLI, you can specify the `--service-instance` option to protect instances in a specific resource group. If you use the UI, you can specify the *Service instance* in the resource attributes.

## Creating network zones
{: #network-zone}

A network zone represents an allowlist of IP addresses where an access request is created. It defines a set of one or more network locations that are specified by the following attributes:

* IP addresses, which include individual addresses, ranges, or subnets.
* VPCs
* Service references, which allow access from other {{site.data.keyword.cloud_notm}} services.

Make sure to add {{site.data.keyword.databases-for}} to network zones for rules that target other {{site.data.keyword.cloud_notm}} resources, or some operations in your workflow might fail. 
{: important}

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

   {{site.data.keyword.databases-for}} does not support *Reference a service*. Selecting a service results in an error when you create a rule.
   {: .note}

### Creating network zones in the CLI
{: #network-zone-cli}
{: cli}

To create network zones in the CLI, [install the context-based restrictions CLI plug-in](/docs/account?topic=cli-cbr-plugin#install-cbr-plugin). You can use the `cbr-zone-create` command to add resources to network zones. For more information, see the [context-based restrictions CLI reference](https://test.cloud.ibm.com/docs/account?topic=cli-cbr-plugin#cbr-zones-cli).

Create a zone using a command like:

```sh
ibmcloud cbr zone-create --addresses=1.1.1.1,5.5.5.5 --name=<NAME>
```
{: .pre}

Update a zone using a command like:
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

Delete a zone using a command like:
```sh
ibmcloud cbr zone-delete <ZONE-ID>
```
{: .pre}

## Creating rules
{: #rules}

Rules restrict access to specific cloud resources based on resource attributes and contexts.

### Creating rules in the UI
{: #rules-ui}
{: ui}

1. Go to **Manage** > **Context-based restrictions** in the {{site.data.keyword.cloud}} console.
1. Select **Rules**.
1. Click **Create**.
1. Protect **All APIs** by default, or select **Specific APIs**.
   {{site.data.keyword.databases-for}} does not currently support **Control plane** as an option.
   {: .note}

1. Click **Next**.
1. Scope the rule to **All resources** or **Specific resources**. See [Protecting Cloud Databases resources](/docs/cloud-databases?topic=cloud-databases-cbr#cbr-overview-protect-services) for more information about how you can target specific resources.
1. Click **Continue**.
1. Define the allowed endpoint types.
   - Keep the toggle set to **No** to allow all endpoint types.
   - Set the toggle to **Yes** to allow only specific endpoint types, then choose from the list.
1. Select a network zone or zones that you have already created, or create a new network zone by clicking **Create**.
   Contexts define from where your resources can be accessed, effectively linking your network zone to your rule.
   {: tip}

1. Click **Add** to add your configuraiton to the summary panel.
1. Click **Next**.
1. Name your rule.
1. Select how you want to enforce the rule.

### Creating rules in the CLI
{: #rules-cli}

To create rules in the CLI, [install the context-based restrictions CLI plug-in](/docs/account?topic=cli-cbr-plugin#install-cbr-plugin).

To create a rule in the CLI, you need the appropriate {{site.data.keyword.databases-for}} `service_name`:
* `databases-for-etcd`
* `databases-for-elasticsearch`
* `databases-for-mongodb`
* `databases-for-postgresql`
* `databases-for-redis`
* `messages-for-rabbitmq`
* `databases-for-cassandra`
* `databases-for-enterprisedb`
* `database-for-mysql`

Create a rule using a command like:

```sh
ibmcloud cbr rule-create --enforcement-mode enabled --context-attributes "networkZoneId=<ZONE-ID>" --resource-group-id <RESOURCE_GROUP_ID> --service-name <SERVICE-NAME> --service-instance <SERVICE-INSTANCE> --api-types crn:v1:bluemix:public:context-based-restrictions::::api-type:data-plane --description <DESCRIPTION>
```
{: .pre}

Update a rule using a command like:

```sh
ibmcloud cbr rule-update <RULE-ID> --enforcement-mode disabled --context-attributes="networkZoneId=<ZONE-ID>" --resource-group-id   <RESOURCE_GROUP_ID> --service-name <SERVICE_NAME> --api-types crn:v1:bluemix:public:context-based-restrictions::::api-type:data-plane --description    <DESCRIPTION>
```
{: .pre}

The `rule-update` command is an overwrite. Include all of the fields required as if you are creating the rule from scratch. If you omit any required fields, the rule overwrites those missing fields as empty, and the rule might fail because some of those fields are required, regardless of whether they are changing the rule. {: .important}

Updating requires the `RULE-ID`, not the rule name. Use the following command to list your rules and retrieve the relevant `RULE-ID`:
```sh
ibmcloud cbr rules
```
{: .pre}

Delete a rule using a command like:
```sh
ibmcloud cbr rule-delete <RULE-ID>
```
{: .pre}

### Verifying your rule
{: #rules-ui-verify}

To verify that your rule has been applied, go to the {{site.data.keyword.cloud}} Dashboard and select the relevant instance from your *Resource List*. Within the **Recent Tasks** panel, you will see your rule's status.

The task of creating or modifying a rule goes into your instance's task queue. Depending on workload, it might take some time for your rule enforcement to complete.{: .note}
