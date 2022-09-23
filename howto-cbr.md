---

copyright:
  years:  2022
lastupdated: "2022-09-19"

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

These restrictions work with traditional IAM policies, which are based on identity, to provide an extra layer of protection. Unlike IAM policies, CBRs don't assign access. CBRs check that an access request comes from an allowed context that you configure. Since both IAM access and CBRs enforce access, CBRs offer protection even in the face of compromised or mismanaged credentials. For more information, see [What are context-based restrictions](/docs/account?topic=account-context-restrictions-whatis).

A user must have the Administrator role on the {{site.data.keyword.databases-for}} service to create, update, or delete rules. A user must also have either the Editor or Administrator role on the CBR service to create, update, or delete network zones. A user with the Viewer role on the CBRs service can only add network zones to a rule. 
{: note}

Any {{site.data.keyword.cloudaccesstraillong_notm}} or audit log events generated come from the context-based restrictions service, not {{site.data.keyword.databases-for}}. For more information, see [Monitoring context-based restrictions](/docs/account?topic=account-cbr-monitor).

To get started protecting your {{site.data.keyword.databases-for}} resources with context-based restrictions, see the tutorial for [Leveraging context-based restrictions to secure your resources](/docs/account?topic=account-context-restrictions-tutorial).

## How {{site.data.keyword.databases-for}} integrates with context-based restrictions
{: #cbr-overview}

You can create context-based restrictions (CBR) for {{site.data.keyword.databases-for}} resources or for specific APIs.

### Protecting IBM Cloud Kubernetes Service resources
{: #cbr-overview-protect-services}

You can create CBR rules to protect specific regions, resource groups, and instances.

**Region**
   Protects {{site.data.keyword.databases-for}} resources in a specific region. If you include a region in your CBR rule, resources in the network zones that you associate with the rule can interact only with resources in that region.
   If you use the CLI, you can specify the `--region REGION` option to protect resources in a specific region.
   If you use the API, you can specify `"name": "region","value": "REGION"` field in the resource attributes.

**Resource group**
   Protects {{site.data.keyword.databases-for}} resources in a specific resource group.
   If you use the CLI, you can specify the `--resource-group-id RESOURCE-GROUP-ID` option to protect resources in a specific resource group.
   If you use the API, you can specify `"name": "resourceGroupId","value": "RESOURCE-GROUP-ID"` field in the resource attributes.

**Namespace**
   Protects a specific namespace. If you include a namespace in your CBR rule, resources in the network zones that you associate with the rule can interact only with resources in that namespace. Note that scoping a rule to a specific namespace is only available only for rules that protect the cluster API type.
   Protects IBM Cloud Kubernetes Service resources in a specific resource group.
   If you use the CLI, you can specify the `--resource-attributes` namespace=NAMESPACE option to protect resources in a specific resource group.
   If you use the API, you can specify `"name": "namespace","value": "NAMESPACE"` field in the resource attributes.

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

1. To create network zones from the CLI, [install the CBR CLI plug-in](/docs/account?topic=cli-cbr-plugin#install-cbr-plugin).
1. You can use the `cbr-zone-create` command to add resources to network zones. For more information, see the [CBR CLI reference](https://test.cloud.ibm.com/docs/account?topic=cli-cbr-plugin#cbr-zones-cli). Note that the `service_name` for {{site.data.keyword.databases-for}} is **SERVICE_NAME**.

### Creating network zones in the console
{: #network-zone-ui}
{: ui}

*Insert your examples here.*

### Creating network zones by using the API
{: #network-zone-api}
{: api}

You can create network zones by using the `create-zone` command. For more information, see the [API docs](/apidocs/context-based-restrictions#create-zone). You can add *serviceName* to network zones as a service reference to allow {{site.data.keyword.databases-for}} to access resources and services in your account that are the subject of a rule.

The `serviceRef` attribute for {{site.data.keyword.databases-for}} is `your-service`.
{: tip}

*Insert your examples here.*

### Creating network zones by using the CLI
{: #network-zone-cli}
{: cli}

You can use the `cbr-zone-create` command to add network locations, VPCs, and service references to network zones. For more information, see the CBR [CLI reference](/docs/account?topic=cli-cbr-plugin#cbr-zones-cli). Add {{site.data.keyword.databases-for}} to network zones as a service reference to allow *serviceName* to access resources and services in your account that are the subject of a rule.
    
    To find a list of available service refs, run the `ibmcloud cbr service-ref-targets` [command](/docs/account?topic=cli-cbr-plugin#cbr-cli-service-ref-targets-command). The `service_name` for {{site.data.keyword.databases-for}} is `{{site.data.keyword.databases-for}}`.
    {: tip}
    
*Insert your examples here.*

## Creating rules
{: #create-rules}

Define restrictions to {{site.data.keyword.databases-for}} resources by creating rules. 

### Creating rules in the console
{: #rules-ui}
{: ui}

Review the following examples to learn how to create rules for {{site.data.keyword.databases-for}}.

*Insert your examples here. Include more complex use cases, like scoping a rule to protect specific APIs.*

### Creating rules by using the API
{: #rules-api}
{: api}

Review the following examples to learn how to create rules for {{site.data.keyword.databases-for}}. For more information, see the [API docs](/apidocs/context-based-restrictions#create-rule).

*Insert your examples here. Include more complex use cases, like scoping a rule to protect specific APIs.*


### Creating rules by using the CLI
{: #rules-cli}
{: cli}

Review the following examples to learn how to create rules for {{site.data.keyword.databases-for}}. For more information, see the CBR [CLI reference](/docs/account?topic=cli-cbr-plugin). 

*Insert your examples here. Include more complex use cases, like scoping a rule to protect specific APIs.*
