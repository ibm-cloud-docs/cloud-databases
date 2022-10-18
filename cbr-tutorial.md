---

copyright:
  years: 2022, 2022
lastupdated: "2022-10-18"

keywords: cbr, context based restrictions, security, cbr scenario, cloud databases

subcollection: cloud-databases

content-type: tutorial
services: cloud-databases
account-plan: paid
completion-time: 30m

---

{{site.data.keyword.attribute-definition-list}}

# Example context-based restrictions scenarios
{: #cbr-tutorial}
{: toc-content-type="tutorial"}
{: toc-services="cloud-databases"}
{: toc-completion-time="30m"}

With context-based restrictions, account owners and administrators can define and enforce access restrictions for {{site.data.keyword.cloud}} resources, based on the context of access requests. Access to {{site.data.keyword.databases-for}} resources can be controlled with context-based restrictions and identity and access management policies. For more information, see [Protecting {{site.data.keyword.databases-for}} resources with context-based restrictions](/docs/cloud-databases?topic=cloud-databases-cbr).
{: shortdesc}

## Restrict traffic to your deployment by using [{{site.data.keyword.databases-for}} Allowlisting](/docs/databases-for-mysql?topic=cloud-databases-allowlisting).
{: #cbr-tutorial-scenario}

In this example scenario, you use context-based restrictions to restrict traffic to your {{site.data.keyword.databases-for-mysql_full}} cluster by allowing only an individual IP address from the [{{site.data.keyword.databases-for}} Allowlist page](/docs/databases-for-mysql?topic=cloud-databases-allowlisting) to connect to your deployment.

In the following steps, you start by creating a network zone, or allowlist, that includes a single IP address. Then, you create a context-based restrictions rule for your deployment. When you create the rule, you associate it with the network zone that contains the individual IP address.

## Prerequisites
{: #cbr-tutorial-prereqs}

Before beginning this tutorial, make sure you have created or installed the following resources and tools.

- An {{site.data.keyword.cloud_notm}} account. For more information, see [Creating an account](/docs/account?topic=account-account-getting-started).
- The [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin) - the CLI interface to interact with the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction). For more information, see [Getting started with the {{site.data.keyword.cloud_notm}} CLI](/docs/databases-cli-plugin).
- A {{site.data.keyword.databases-for}} deployment. For more information, see [Provisioning](/docs/cloud-databases?topic=cloud-databases-provisioning).
- Review the [What are context-based restrictions](/docs/account?topic=account-context-restrictions-whatis) docs to get an understanding of concepts of network zones and rules.
- Review the [Protecting {{site.data.keyword.databases-for}} resources with context-based restrictions](/docs/cloud-databases?topic=cloud-databases-cbr) docs to understand how you can leverage CBR for your {{site.data.keyword.databases-for}} resources.

## Creating your network zone
{: #cbr-tutorial-create-zone}
{: step}

[Provision your service from the {{site.data.keyword.cloud_notm}} Catalog](https://cloud.ibm.com/catalog/services/databases-for-mysql) and choose your IP address(es) from the [{{site.data.keyword.databases-for}} Allowlist page](/docs/databases-for-mysql?topic=cloud-databases-allowlisting). 
1. Run the following example command to create a network that includes only one IP address.

    ```sh
    ibmcloud cbr zone-create --addresses=169.63.121.159/27 --name=tutorial_zone
    ```
    {: pre}
    
1. Verify the network zone was created.
    ```sh
    ibmcloud cbr zones
    ```
    {: pre}



## Creating your CBR rule
{: #cbr-tutorial-create-rule}
{: step}

1. After you create your network zone (allowlist), create a CBR rule and add the network zone you created in the previous step. The following example creates a rule that uses the `cluster` API type. Replace `NETWORK-ZONE-ID` with the ID of the `allow-client-ip` network zone that you created in [Step 1](#creating-your-network-zone).

    ```sh
    ibmcloud cbr rule-create --enforcement-mode enabled --context-attributes "networkZoneId=<ZONE-ID>" --resource-group-id "<RESOURCE_GROUP_ID>" --service-name "<SERVICE-NAME>" --service-instance "<SERVICE-INSTANCE>" --api-types crn:v1:bluemix:public:context-based-restrictions::::api-type:data-plane --description "<DESCRIPTION>"
    ```
    {: pre}
    
    Understanding the command options.
    
    `--zone-id (string)`
    :   Shorthand for adding context attribute `networkZoneId` to the first context.
    
    `--resource-group-id (string)`
    :   Shorthand for creating {{site.data.keyword.cloud_notm}} resource attribute `resourceGroupId`.

    `--service-name (string)`
    :   Shorthand for creating {{site.data.keyword.cloud_notm}} resource attribute `serviceName`.
    
    `--service-instance SERVICE_INSTANCE_GUID (string)`
    :   GUID of the service instance. This option is exclusive with the `--file` option.
    
    
1. Verify the rule was created.
    ```sh
    ibmcloud cbr rules
    ```
    {: pre}
    
## Testing your context-based restrictions
{: #cbr-tutorial-create-test}
{: step}

To test your context-based restrictions setup, try connecting to your deployment  from an IP address other than the individual IP address that you allowlisted in your network zone. With this setup, only the individual IP address in your network zone can connect to your deployment.

## Additional scenarios
{: #cbr-tutorial-create-additional-scenarios}

Now that you've created a simple CBR network zone and rule, review the following more advanced examples to further control access to your {{site.data.keyword.databases-for}} resources.

### {{site.data.keyword.databases-for}} as a Service Reference for a Key Protect instance
{: #cbr-tutorial-key-protect-instance}

