---

copyright:
  years: 2023
lastupdated: "2023-12-01"

keywords: backups, new service instance, deleted resource, undelete, pending backup

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Backups FAQ
{: #faq-backups}
{: faq}
{: support}

## What happens to the backups if I accidentally delete an instance?
{: #faq-backups-data-deletion}
{: faq}
{: support}

If an instance is deleted, the backup is deleted as well. However, {{site.data.keyword.databases-for}} waits for 3 days before it is deleted internally. Within those 3 days, you can either re-enable the instance or create a new service instance from the backup. For more information, see [Deleting your Deployment and Removing your Data](https://cloud.ibm.com/docs/cloud-databases?topic=cloud-databases-deprovisioning). You can also use {{site.data.keyword.cloud_notm}} CLI or API to restore a deleted resource. For more information, see [Using resource reclamations](/docs/account?topic=account-resource-reclamation){: external}.

## Is it possible to restore an instance from a backup in a different instance?
{: #faq-backups-restore-new-instance}
{: faq}
{: support}

{{site.data.keyword.databases-for}} backups are restored in a new service instance. For more information, see [Managing {{site.data.keyword.databases-for}} backups](/docs/cloud-databases?topic=cloud-databases-dashboard-backups).

Point-in-Time Recovery (PITR) is available for [{{site.data.keyword.databases-for-mysql}}](/docs/databases-for-mysql?topic=databases-for-mysql-pitr){: external}, [{{site.data.keyword.databases-for-postgresql}}](/docs/databases-for-postgresql?topic=databases-for-postgresql-pitr){: external}, [{{site.data.keyword.databases-for-mongodb}}](/databases-for-mongodb?topic=databases-for-mongodb-pitr){: external} and [{{site.data.keyword.databases-for-enterprisedb}}](/docs/databases-for-enterprisedb?topic=databases-for-enterprisedb-pitr){: external} but only if there is an instance that the backup is related to.

## Can I create a backup while another backup is pending?
{: #faq-backups-pending-backup}
{: faq}
{: support}

{{site.data.keyword.databases-for}} does not create additional backups if there is already a pending backup in the queue, ensuring efficiency and avoiding redundancy in our backup processes. {{site.data.keyword.databases-for}} automatically schedules a new daily backup if none is currently set up. You have the flexibility to initiate manual backups at your preferred cadence.
