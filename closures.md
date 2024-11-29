---
copyright:
  years: 2018, 2022
lastupdated: "2022-05-05"

subcollection: cloud-databases

keywords: migrating cloud-databases, data center cloud-databases
---

{:external: .external target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Migrating resources to a different data center
{: #migrate-data-center}

{{site.data.keyword.cloud}}'s investments in data center infrastructure include rolling out newer data centers and multizone regions (MZRs) and closing older data centers that are unsuitable for upgrading. 

For a current list of data centers, see [Locations for resource deployment
](/docs/overview?topic=overview-locations){: external}. 

For information on data center closures, see [Data center migrations](/docs/account?topic=account-dc-closure){: external}.

## Migrating your resources
{: #migrating-your-resources}

To identify your impacted resources, take advantage of special offers, or learn about recommended configurations, use one of the following options to contact the {{site.data.keyword.IBM_notm}} 24x7 Client Success team:

- [Live chat](https://www.ibm.com/cloud/data-centers/?focusArea=WCP%20-%20Pooled%20CSM&contactmodule){: external}
- Phone: (US) 866-597-9687

To avoid any disruption to your service, please complete the following steps to migrate your resources from your current data center to your new location: 

- Restore your backup into a new database, in a new region. For more information, see [Managing Cloud Databases backups](/docs/cloud-databases?topic=cloud-databases-dashboard-backups){: .external}.
- For an {{site.data.keyword.databases-for-postgresql_full}} deployment, you can deploy [Read Replicas](/docs/databases-for-postgresql?topic=databases-for-postgresql-read-only-replicas){: .external} into a new region and turn that Read Replica into a stand-alone database.
