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

A local region is a geographic area that is accessed by a dedicated [endpoint](/docs/cloud-databases?topic=cloud-databases-service-endpoints). 
The region IDs and associated locations are shown in the following table.

|Local region ID | Location |
|--------|--------|
| `che01`	|  Chennai |
| `seo01`	|  Seoul |
| `au-syd` | Sydney |
| `jp-tok`	| Tokyo |
| `eu-gb` | London |
| `eu-de`	| Frankfurt |
| `osl01`	| Oslo |
| `us-east`	| Washington |
| `us-south`	| Dallas |
{: caption="Table 1. IDs and locations of local regions for {{site.data.keyword.databases-for}}" caption-side="top"}

## Targeting a local region

If you want to use a region other than your local region, you can target the region that you want to access by running the `ibmcloud target -r` command. You can run the command with no parameters to get a list of available regions, or you can specify the region as a parameter.

1. To run the command with parameters, replace <region> with the name of the region.
```
ibmcloud target -r <region>
```
{: .pre}

For example, to target the `eu-gb` region, run the following command:
```
ibmcloud target -r eu-gb
```
{: .pre}


## Allowlists and IP subnet ranges

Review the [full list of regional subnets](/docs/cloud-databases?topic=cloud-databases-allowlisting#allowlisting-cloud-databases-in-your-environment) and associated locations to ensure your allowlists are configured with the appropriate subnet ranges. 

