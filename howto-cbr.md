---

copyright:
  years:  2022
lastupdated: "2022-09-19"

keywords: restricting access to cloud databases, restricting access to ICD

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

This document outlines the process for using context-based restrictions to protect your {{site.data.keyword.databases-for}} resources. This process is not yet in production. Use this document to prepare your resources for context-based restrictions.{: experimental}

# Protecting {{site.data.keyword.databases-for}} resources with context-based restrictions
{: #cbr}

Context-based restrictions give account owners and administrators the ability to define and enforce access restrictions for {{site.data.keyword.cloud}} resources based on the context of access requests. Access to {{site.data.keyword.databases-for}} resources can be controlled with context-based restrictions and identity and access management (IAM) policies.
{: shortdesc}

These restrictions work with traditional IAM policies, which are based on identity, to provide an extra layer of protection. Unlike IAM policies, context-based restrictions don't assign access. Context-based restrictions check that an access request comes from an allowed context that you configure. Since both IAM access and context-based restrictions enforce access, context-based restrictions offer protection even in the face of compromised or mismanaged credentials. For more information, see [What are context-based restrictions](/docs/account?topic=account-context-restrictions-whatis).

A user must have the Administrator role on the {{site.data.keyword.databases-for}} service to create, update, or delete rules. A user must also have either the Editor or Administrator role on the Context-based restrictions service to create, update, or delete network zones. A user with the Viewer role on the Context-based restrictions service can only add network zones to a rule. 
{: note}

Any {{site.data.keyword.cloudaccesstraillong_notm}} or audit log events generated come from the context-based restrictions service, not {{site.data.keyword.databases-for}}. For more information, see [Monitoring context-based restrictions](/docs/account?topic=account-cbr-monitor).

To get started protecting your {{site.data.keyword.databases-for}} resources with context-based restrictions, see the tutorial for [Leveraging context-based restrictions to secure your resources](/docs/account?topic=account-context-restrictions-tutorial).

<!-- Most services can include only the content above this comment. If your service has limitations, stipulations as to how rules and network zones are enforced, or other use cases specific to your service, then review the following section to include additional information. -->

## How {{site.data.keyword.databases-for}} integrates with context-based restrictions
{: #cbr-overview}

_If context-based restrictions don't apply holistically to all components of your service's resources, provide a paragraph that categorizes the scope of what’s enforced or impacted and what isn't. Also, consider the following use cases to determine what you need to document for your service:_

_1. Include common examples across all interface types (UI, CLI, API). See platform task topics, but if there's something specific in CLI/API as far as scoping a rule, then you might want to include those here--similar to examples for fine-grained access by using the interfacer switcher._

_2. Consider the different access patterns for your service's APIs, if any. How does a customer use the APIs? How does your service have it set up for creating context-based restriction rules and how does that impact operations a customer can perform (for example, scoping a rule to protect specific APIs)? Think about a user creating a rule. When you select and scope resources for a rule, you must select the service, resources, and then you might have the option to scope protection to APIs. Depending on what level of this your service supports, you might need to document what's available and how this works for your service. Name this section "Protecting specific APIs". Include information about each API or API type, such as the actions and action descriptions that map to each._

   _Tip: Ask your development team for the CBR service registration json file to help you get started. In the file, you'll find the APIs that customers can use to scope a rule._

_3. Document resource attributes. Check the UI for the resource attributes that customers can use to scope the rule to specific resources. Documenting these resource attributes can help customers that are using the CLI or API because there is currently no programmatic way to retreive the available resource attributes for a given service. Name this section "Protecting specific resources"._ 

_4. If you use private endpoints, private endpoints might already have an allowlist concept, so how would integration with context-based restrictions work? Honor both, honor one over the other, an intersection of these, how will this work if you have a legacy system in place?_

_5. State any limitations on how the context-based restrictions work with your service's resources when it's working with another service or generally within the platform. You can use a note format if this is only a sentence or two. For example, "Context-based restrictions are not supported in Object Storage for Satellite."_

_6. Are there service to service authorizations required to be in place? If so, you would want to create rules to allow for those service to service authorizations to continue working once a rule is in place._ 

   _Example:_
   1. There is an existing IAM S2S authorization to allow COS to access key protect.
   2. Someone creates a CBR rule on key protect.
   3. For the rule in step 2, a CBR zone would need to specify a service reference allowing COS to access key protect. Without this step network access would be blocked.

_For an example of how to document your service's intrgration with context-based restrictions, see the [Protecting IBM Cloud Kubernetes Service resources with context-based restrictions](https://test.cloud.ibm.com/docs/containers?topic=containers-cbr&interface=api#api-types-cbr)._

## Creating network zones 
{: #network-zone}

A network zone represents an allowlist of IP addresses where an access request is created. It defines a set of one or more network locations that are specified by the following attributes:

* IP addresses, which include individual addresses, ranges, or subnets.
* VPCs
* Service references, which allow access from other {{site.data.keyword.cloud_notm}} services.

Make sure to add {{site.data.keyword.databases-for}} to network zones for rules that target other {{site.data.keyword.cloud_notm}} resources, or some operations in your workflow might fail.
{: important}


### Creating network zones in the console
{: #network-zone-ui}
{: ui}

*Insert your examples here.*

### Creating network zones by using the API
{: #network-zone-api}
{: api}

You can create network zones by using the `create-zone` command. For more information, see the [API docs](/apidocs/context-based-restrictions#create-zone). You can add _serviceName_ to network zones as a service reference to allow {{site.data.keyword.databases-for}} to access resources and services in your account that are the subject of a rule.

The `serviceRef` attribute for {{site.data.keyword.databases-for}} is `your-service`.
{: tip}

*Insert your examples here.*

### Creating network zones by using the CLI
{: #network-zone-cli}
{: cli}

You can use the `cbr-zone-create` command to add network locations, VPCs, and service references to network zones. For more information, see the CBR [CLI reference](/docs/account?topic=cli-cbr-plugin#cbr-zones-cli). Add {{site.data.keyword.databases-for}} to network zones as a service reference to allow _serviceName_ to access resources and services in your account that are the subject of a rule.
    
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
