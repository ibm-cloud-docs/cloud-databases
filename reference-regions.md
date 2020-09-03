---

copyright:
  years: 2020
lastupdated: "2020-09-01"

keywords: regions for cloud-databases, ibmcloud, cluster, zone, domains

subcollection: cloud-databases

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}

# Working with regions in {{site.data.keyword.databases-for}}   
{: #regions}

{{site.data.keyword.cloud}} Databases are available in several regions. All deployments are scoped to the specific regional cluster with which you are currently working. For example, namespaces, images, quota settings, and plan settings must all be managed separately for each regional deployment.
{: shortdesc}

## Local regions

A local region is a geographic area that is accessed by a dedicated endpoint. The domain names are available in the console and the CLI. 

The region IDs and associated domain names are shown in the following table.

|Local region ID	|Domain name	|Private domain name	| Location
|--------|--------|--------|--------|
`che01`	| `che01.icr.io`	| `private.che01.icr.io` | Chennai
`seo01`	| `seo01.icr.io`	| `private.seo01.icr.io`	| Seoul
`au-syd` | `au-syd.icr.io` | `private.au-syd.icr.io` | Sydney
`jp-tok`	| `jp-tok.icr.io`	| `private.jp-tok.icr.io`	| Tokyo
`eu-gb` |`eu-gb.icr.io` | `private.eu-gb.icr.io` | London
`eu-de`	| `de.icr.io`	| `private.de.icr.io`	| Frankfurt
`osl01`	| `osl01.icr.io`	| `private.osl01.icr.io`	| Oslo
`us-east`	| `us-east.icr.io`	| `private.us-east.icr.io` | Washington
`us-south`	| `us.icr.io`	| `private.us.icr.io`	| Dallas
{: caption="Table 1. Domain names for local regions for {{site.data.keyword.databases-for}}" caption-side="top"}

## Targeting a local region

If you want to use a region other than your local region, you can target the region that you want to access by running the ibmcloud cr region-set command. You can run the command with no parameters to get a list of available regions, or you can specify the region as a parameter.

1. To run the command with parameters, replace <region> with the name of the region.
```
ibmcloud cr region-set <region>
```
{: .pre}

For example, to target the `eu-gb` region, run the following command:
```
ibmcloud cr region-set eu-gb
```
{: .pre}


## Allowlists and IP subnet ranges

Review the [full list of regional subnets](/docs/cloud-databases?topic=cloud-databases-allowlisting#allowlisting-cloud-databases-in-your-environment) and associated locations to ensure your allowlists are configured with the appropriate subnet ranges. 

