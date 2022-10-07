---

copyright:
  years:  2022
lastupdated: "2022-10-06"

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

This document outlines the process for using context-based restrictions (CBR) to protect your {{site.data.keyword.databases-for}} resources. This process is not yet in production. Use this document to prepare your resources for context-based restrictions.{: .important}

# Protecting {{site.data.keyword.databases-for}} resources with context-based restrictions
{: #cbr}

Context-based restrictions (CBR) give account owners and administrators the ability to define and enforce access restrictions for {{site.data.keyword.cloud}} resources based on the context of access requests. Access to {{site.data.keyword.databases-for}} resources can be controlled with CBR and identity and access management (IAM) policies.
{: shortdesc}

These restrictions work with traditional IAM policies, which are based on identity, to provide an extra layer of protection. Unlike IAM policies, CBR doesn't assign access. CBR checks that an access request comes from an allowed context that you configure. Since both IAM access and CBR enforce access, CBR offers protection even in the face of compromised or mismanaged credentials. For more information, see [What are context-based restrictions](/docs/account?topic=account-context-restrictions-whatis).

A user must have the Administrator role on the {{site.data.keyword.databases-for}} service to create, update, or delete rules. A user must also have either the Editor or Administrator role on the CBR service to create, update, or delete network zones. A user with the Viewer role on the CBR service can only add network zones to a rule. 
{: note}

Any {{site.data.keyword.cloudaccesstraillong_notm}} or audit log events generated come from the context-based restrictions service, not {{site.data.keyword.databases-for}}. For more information, see [Monitoring context-based restrictions](/docs/account?topic=account-cbr-monitor).

To get started protecting your {{site.data.keyword.databases-for}} resources with context-based restrictions, see the tutorial for [Leveraging context-based restrictions to secure your resources](/docs/account?topic=account-context-restrictions-tutorial).

## How {{site.data.keyword.databases-for}} integrates with context-based restrictions
{: #cbr-overview}

You can create context-based restrictions (CBR) for {{site.data.keyword.databases-for}} resources or for specific APIs.

### Protecting {{site.data.keyword.databases-for}} resources
{: #cbr-overview-protect-services}

You can create CBR rules to protect specific **regions**, **namespaces**, and **instances**.

**Region**
   Protects {{site.data.keyword.databases-for}} resources in a specific region. If you include a region in your CBR rule, resources in the network zones that you associate with the rule can interact only with resources in that region.
   If you use the CLI, you can specify the `--region REGION` option to protect resources in a specific region.
   If you use the API, you can specify `"name": "region","value": "REGION"` field in the resource attributes. 

**Namespace**
   Protects a specific namespace. If you include a namespace in your CBR rule, resources in the network zones that you associate with the rule can interact only with resources in that namespace. Note that scoping a rule to a specific namespace is available only for rules that protect the cluster API type.
   If you use the CLI, you can specify the `--resource-attributes namespace=NAMESPACE` option to protect resources in a specific resource group.
   If you use the UI, you can specify `"name": "namespace","value": "NAMESPACE"` field in the resource attributes.

**Instance**
   Protects a specific instance. If you include an instance in your CBR rule, resources in the network zones that you associate with the rule can interact only with resources in that instance. Note that scoping a rule to a specific instance is available only for rules that protect the cluster API type.
   If you use the CLI, you can specify the `--service-instance` option to protect instances in a specific resource group.
   If you use the UI, you can specify the Service instance in the resource attributes.

## Creating network zones 
{: #network-zone}

A network zone represents an allowlist of IP addresses where an access request is created. It defines a set of one or more network locations that are specified by the following attributes:

* IP addresses, which include individual addresses, ranges, or subnets.
* VPCs
* Service references, which allow access from other {{site.data.keyword.cloud_notm}} services.

Make sure to add {{site.data.keyword.databases-for}} to network zones for rules that target other {{site.data.keyword.cloud_notm}} resources, or some operations in your workflow might fail.
{: important}

### Creating network zones from the CLI
{: #network-zone-cli}

To create network zones from the CLI, [install the CBR CLI plug-in](/docs/account?topic=cli-cbr-plugin#install-cbr-plugin). You can use the `cbr-zone-create` command to add resources to network zones. For more information, see the [CBR CLI reference](https://test.cloud.ibm.com/docs/account?topic=cli-cbr-plugin#cbr-zones-cli). 

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

   Updating requires the `ZONE-ID`, not the zone name. Use the following command to list your zones and retrieve the revelant `ZONE-ID`:
   ```sh
   ibmcloud cbr zones
   ```
   {: .pre}

Delete a zone using a command like:
```sh
ibmcloud cbr zone-delete <ZONE-ID>
```
{: .pre}

### Creating network zones in the UI
{: #network-zone-ui}

1. Navigate to *Context-based restrictions* in the *Manage* section of the {{site.data.keyword.cloud}} Dashboard.
1. Select *Create a network zone*.
1. Name your network zone.
1. Enter your *Allowed IP adresses.* You can enter a single IP address, a range of IP addresses, or a single CIDR. **The *Denied IP addresses* field is optional and should only include exceptions contained within the IP ranges you provide in the allowed IP adresses field.**
1. Choose your *Allowed VPCs*, selecting as many as you like. 

{{site.data.keyword.databases-for}} does not support *Reference a service*. Selecting a service will result in an error when you create a rule.{: .note}

## Creating rules 
{: #rules}

Rules restrict access to specific cloud resources based on resource attributes and contexts.

### Creating rules from the CLI
{: #rules-cli}

To create rules from the CLI, [install the CBR CLI plug-in](/docs/account?topic=cli-cbr-plugin#install-cbr-plugin).

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
ibmcloud cbr rule-update <RULE-ID> --enforcement-mode disabled --context-attributes="networkZoneId=b0ceb852f281b489343bae8c574b219e" --resource-group-id   <RESOURCE_GROUP_ID> --service-name <SERVICE_NAME> --api-types crn:v1:bluemix:public:context-based-restrictions::::api-type:data-plane --description    <DESCRIPTION>
```
{: .pre}

Updating requires the `RULE-ID`, not the rule name. Use the following command to list your rules and retrieve the revelant `RULE-ID`:
```sh
ibmcloud cbr rules
```
{: .pre}

Delete a rule using a command like:
```sh
ibmcloud cbr zone-delete <RULE-ID>
```
{: .pre}

### Creating rules from the UI
{: #rules-ui}

#### Step 1: Select your resources
{: #rules-ui-select-resources}

**Service** - Select which resources to target from the list provided.

**APIs** - Select **Specific APIs**, then **Data plane**.

{{site.data.keyword.databases-for}} does not currently support **Control plane** as an option.{: .note}

**Resources** - Choose the scope of your restrictions, either *All resources* or *Specific resources*. If you choose *Specific resources*, you have the option of specifying *Region*, *Resource group*, or *Service instance*.

#### Step 2: Add a context
{: #rules-ui-add-context}

Contexts define from where your resources can be accessed, effectively linking your network zone to your rule.

* Select a network zone from the list provided, then click *Add*. You will see the Context added to the righthand menu. 

* **Endpoint types** To specify public, private, or direct endpoints, select *Yes* to allow only specific endpoint types, then choose from the available list. 

#### Step 3: Describe your rule
{: #rules-ui-describe-rule}

While naming your rule is optional, it's recommended. 

* Enforce your rule by selecting *Enabled*.

* Click **Create** and your rule is now enforced in your designated network zone.

### Verifying your rule
{: #rules-ui-verify}

To verify that your rule has been applied, go to the {{site.data.keyword.cloud}} Dashboard and select the relevant instance from your *Resource List*. Within the **Recent Tasks** panel, you will see your rule's status.

The task of creating or modifying a rule goes into your instance's task queue. Depending on workload, it may take some time for your rule enforcement to complete.{: .note}
