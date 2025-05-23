---

copyright:
  years: 2023
lastupdated: "2023-12-13"

keywords: data location requirements, backup region, cross region buckets, backup locations

subcollection: cloud-databases

content-type: tutorial
services: cloud-databases
account-plan: paid
completion-time: 30m

---

{{site.data.keyword.attribute-definition-list}}

# Determine whether your deployment region and key management system support Bring Your Own Key (BYOK) for backups
{: #kms-tutorial}
{: toc-content-type="tutorial"}
{: toc-services="cloud-databases"}
{: toc-completion-time="30m"}

To determine whether your {{site.data.keyword.databases-for}} deployment region and key management system support Bring Your Own Key (BYOK) for backups, follow this procedure:

## Prerequisites
{: #kms-tutorial-prereqs}
{: step}

Before beginning this tutorial, make sure that you have created or installed the following resources and tools.

- An {{site.data.keyword.cloud_notm}} account. For more information, see [Creating an account](/docs/account?topic=account-account-getting-started){: external}.
- The [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin) - the CLI interface to interact with the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction). For more information, see [Getting started with the {{site.data.keyword.cloud_notm}} CLI](/docs/databases-cli-plugin).
- A {{site.data.keyword.databases-for}} deployment. For more information, see [Provisioning](/docs/cloud-databases?topic=cloud-databases-getting-started-cdb-provision-instance).

## Match backup region location with data location requirements
{: #kms-tutorial-match-backup-data}
{: step}

1. Ensure that the backup region location matches your data location requirements, see [Backup Locations Cloud Object chart](/docs/databases-for-postgresql?topic=databases-for-postgresql-dashboard-backups&interface=ui#backup-locations). Backup location differs per database region. Ensure that the backup region location matches your data location requirements.

1. Check whether the {{site.data.keyword.databases-for}} broker configuration permits the key region:

   | Instance location | Key region supported |
   |-------------------|----------------------|
   | `us-east`           | `us-south`             |
   | `us-south`          | `us-south`             |
   | `eu-fr2`            | `eu-de`, `eu-fr2`        |
   | `eu-de`             | `eu-de`                |
   {: caption="{{site.data.keyword.databases-for}} instance location and key region support" caption-side="top"}

## Configure failover
{: #kms-tutorial-config-failover}
{: step}

[Creating Cross region buckets](/docs/cloud-object-storage?topic=cloud-object-storage-hpcs#hpcs-cr){: external} with a root key from a Hyper Protect Crypto Services (HPCS) instance requires that instance to be [configured with failover configuration](/docs/hs-crypto?topic=hs-crypto-enable-add-failover){: external}.

Confirm that failover is properly configured for the selected HPCS instance correctly using either the {{site.data.keyword.cloud_notm}} console or CLI. For more information, see [Creating Cross region buckets](/docs/cloud-object-storage?topic=cloud-object-storage-hpcs#hpcs-cr){: external}.
