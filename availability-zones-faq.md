---
copyright:
  years: 2023
lastupdated: "2023-07-31"

subcollection: cloud-databases

keywords: 

---

{{site.data.keyword.attribute-definition-list}}

# Availability zones FAQ
{: #faq-availability-zones}
{: faq}
{: support}

You can create a {{site.data.keyword.databases-for}} instance on {{site.data.keyword.cloud_notm}} in a multi-zone or single-zone region.
{: shortdesc}

See the documentation for provisioning a specific service {{site.data.keyword.databases-for}} instance: 

- 

## What is an availability zone?
{: #what-availability-zone}
{: faq}

When you create an instance, after you select the {{site.data.keyword.cloudant_short_notm}} tile, you must select a region. These locations are called availability zones. An availability zone is an {{site.data.keyword.cloud}} Public location that hosts your data. All Lite and Standard plans automatically deploy into a multi-zone region. Dedicated Hardware plan instances can be deployed in most [{{site.data.keyword.IBM_notm}} data center locations](https://www.ibm.com/cloud/data-centers/){: external}.


## What is the difference between a single-zone and a multi-zone region?
{: #multi-zone-region}
{: faq}

A multi-zone region includes three availability zones that can be used by an instance that is deployed to that region. The multi-zone regions available with {{site.data.keyword.cloudant_short_notm}} include the following regions:

- Dallas
- Frankfurt
- London
- Osaka
- Sydney
- Tokyo
- Washington DC

A single-zone region offers only one availability zone for that region. The single-zone regions available with {{site.data.keyword.cloudant_short_notm}} include the following regions:

- Seoul
- Chennai

For more information, see [Plans and provisioning](/docs/services/Cloudant?topic=Cloudant-ibm-cloud-public#locations-and-tenancy).
