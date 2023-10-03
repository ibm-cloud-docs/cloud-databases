---

copyright:
  years: 2023
lastupdated: "2023-10-03"

subcollection: cloud-databases

keywords: DR for cloud-databases, high availability for cloud-databases, disaster recovery for cloud-databases, failover for cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

<!--Name your file `bc-dr.md` and include it in the **Reference** nav group in your `toc.yaml` file.-->

# Understanding business continuity and disaster recovery for {{site.data.keyword.databases-for}}
{: #bc-dr}

[Disaster recovery](#x2113280){: term} involves a set of policies, tools, and procedures for returning a system, an application, or an entire data center to full operation after a catastrophic interruption. It includes procedures for copying and storing an installed system's essential data in a secure location, and for recovering that data to restore normalcy of operation.
{: shortdesc}

## Responsibilities
{: #bc-dr-responsibilities}

<!-- If there is specific responsibility documentation for the product, do not include the next paragraph-->
To find out more about responsibility ownership for using {{site.data.keyword.cloud}} products between {{site.data.keyword.IBM_notm}} and customer see [Shared responsibilities for {{site.data.keyword.cloud_notm}} products](/docs/overview?topic=overview-shared-responsibilities).

<!-- If there is a specific responsibility topic available for the product, include the next line or remove the line and include details in this section of the topic.-->

For more information about your responsibilities when using {{site.data.keyword.databases-for}}, see [Shared responsibilities for {{site.data.keyword.databases-for}}](/docs/cloud-databases?topic=cloud-databases-responsibilities-cloud-databases).

## Disaster recovery strategy
{: #bc-dr-strategy}

{{site.data.keyword.cloud_notm}} has [business continuity](#x3026801){: term} plans in place to provide for the recovery of services within hours if a disaster occurs. You are responsible for your data backup and associated recovery of your content.

{{site.data.keyword.databases-for}} provides mechanisms to protect your data and restore service functions. Business continuity plans are in place to achieve targeted [recovery point objective](#x3429911){: term} (RPO) and [recovery time objective](#x3167918){: term} (RTO) for the service. The following table outlines the targets for {{site.data.keyword.databases-for}}.

| Disaster recovery objective | Target Value   |
|---|---|
|  RPO | < 24 hours |
|  RTO | <24 hours - for Regional failure (0 hours for Zone Failure) |
{: caption="Table 1. RPO and RTO for {{site.data.keyword.databases-for}}" caption-side="bottom"}

## Locations
{: #ha-locations}

For more information about service availability within regions and data centers, see [Service and infrastructure availability by location](/docs/overview?topic=overview-services_region).

## Backup Storage Regions
{: #bc-dr-single-region-backups}

The purpose of the {{site.data.keyword.databases-for}} regional Disaster Recovery (DR) policy is to make {{site.data.keyword.cos_full}} backups available from the downed region available for you to restore.

| **Region** |                **Backup Storage Region**               | Cross-Region Support? |
|:----------:|:------------------------------------------------------:|:---------------------:|
| us-south   | s3.private.us.cloud-object-storage.appdomain.cloud     | Yes                   |
| jp-osa     | s3.private.ap.cloud-object-storage.appdomain.cloud     | Yes                   |
| jp-tok     | s3.private.ap.cloud-object-storage.appdomain.cloud     | Yes                   |
| eu-gb      | s3.private.eu.cloud-object-storage.appdomain.cloud     | Yes                   |
| us-east    | s3.private.us.cloud-object-storage.appdomain.cloud     | Yes                   |
| ay-syd     | s3.private.ap.cloud-object-storage.appdomain.cloud     | Yes                   |
| che01      | s3.private.che01.cloud-object-storage.appdomain.cloud  | No*                   |
| ca-tor     | s3.private.mon01.cloud-object-storage.appdomain.cloud  | No*                   |
| br-sao     | s3.private.br-sao.cloud-object-storage.appdomain.cloud | No*                   |
| eu-de      | s3.private.eu.cloud-object-storage.appdomain.cloud     | Yes                   |
| par01      | s3.private.eu.cloud-object-storage.appdomain.cloud     | Yes                   |
| eu-es      | s3.private.eu.cloud-object-storage.appdomain.cloud     | Yes                   |
| eu-fr2     | s3.private.eu-fr2.cloud-object-storage.appdomain.cloud | No*                   |
{: caption="Table 2. Single Region Backups for {{site.data.keyword.databases-for}}" caption-side="bottom"}

*You should keep a local copy of data in case of region failure.

