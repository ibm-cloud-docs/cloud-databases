---

copyright:
  years: 2023, 2024
lastupdated: "2024-09-13"

subcollection: cloud-databases

keywords: DR for cloud-databases, high availability for cloud-databases, disaster recovery for cloud-databases, failover for cloud-databases

---

{{site.data.keyword.attribute-definition-list}}



# Understanding business continuity and disaster recovery for {{site.data.keyword.databases-for}}
{: #bc-dr}

[Disaster recovery](#x2113280){: term} involves a set of policies, tools, and procedures for returning a system, an application, or an entire data center to full operation after a catastrophic interruption. It includes procedures for copying and storing an installed system's essential data in a secure location, and for recovering that data to restore normalcy of operation.
{: shortdesc}

## Responsibilities
{: #bc-dr-responsibilities}


- To find out more about responsibility ownership for using {{site.data.keyword.cloud}} products between **{{site.data.keyword.IBM_notm}}** and customer see [Shared responsibilities for {{site.data.keyword.cloud_notm}} products](/docs/overview?topic=overview-shared-responsibilities).

- For more information about your responsibilities when using **{{site.data.keyword.databases-for}}**, see [Shared responsibilities for {{site.data.keyword.databases-for}}](/docs/cloud-databases?topic=cloud-databases-responsibilities-cloud-databases).

## Disaster recovery strategy
{: #bc-dr-strategy}

{{site.data.keyword.cloud_notm}} has [business continuity](#x3026801){: term} plans in place to provide for the recovery of services within hours if a disaster occurs. You are responsible for your data backup and associated recovery of your content.

{{site.data.keyword.databases-for}} provides mechanisms to protect your data and restore service functions. Business continuity plans are in place to achieve targeted [recovery point objective](#x3429911){: term} (RPO) and [recovery time objective](#x3167918){: term} (RTO) for the service. The following table outlines the targets for {{site.data.keyword.databases-for}}.

| Disaster recovery objective | Target value   |
|---|---|
|  RPO | < 24 hours |
|  RTO | <24 hours - for Regional failure (0 hours for Zone Failure) |
{: caption="RPO and RTO for {{site.data.keyword.databases-for}}" caption-side="bottom"}

## Locations
{: #ha-locations}

For more information about service availability within regions and data centers, see [Service and infrastructure availability by location](/docs/overview?topic=overview-services_region).

## Backup storage regions
{: #bc-dr-single-region-backups}

The purpose of the {{site.data.keyword.databases-for}} regional Disaster Recovery (DR) policy is to make {{site.data.keyword.cos_full}} backups available from the downed region available for you to restore.

| **Region** |                **Backup storage region**               | Cross-region support |
|:----------:|:------------------------------------------------------:|:---------------------:|
| `us-south`   | US cross regional endpoint   | Yes                   |
| `jp-osa`     | Asia Pacific cross regional endpoint  | Yes                   |
| `jp-tok`     | Asia Pacific cross regional endpoint    | Yes                   |
| `eu-gb`      | Europe cross regional endpoint     | Yes                   |
| `us-east`    | US cross regional endpoint     | Yes                   |
| `au-syd`     | Asia Pacific cross regional endpoint     | Yes                   |
| `che01`      | Che01 single data center endpoint  | No*                   |
| `ca-tor`     | Mon01 single data center endpoint  | No*                   |
| `br-sao`     | Br-sao regional endpoint | No*                   |
| `eu-de`      | Europe cross regional endpoint     | Yes                   |
| `par01`      | Europe cross regional endpoint    | Yes                   |
| `eu-es`      | Europe cross regional endpoint     | Yes                   |
{: caption="Single region backups for {{site.data.keyword.databases-for}}" caption-side="bottom"}

Keep a local copy of your data.
{: important}
