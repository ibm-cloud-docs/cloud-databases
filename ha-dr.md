---

copyright:
  years: 2020, 2023
lastupdated: "2023-03-21"

subcollection: cloud-databases

keywords: HA for cloud-databases, DR for cloud-databases, high availability for cloud-databases, disaster recovery for cloud-databases, failover for cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Understanding high availability and disaster recovery for {{site.data.keyword.databases-for}}
{: #ha-dr}

This document covers all the {{site.data.keyword.cloud}} Databases, which include {{site.data.keyword.databases-for-cassandra}}, {{site.data.keyword.databases-for-elasticsearch}}, {{site.data.keyword.databases-for-enterprisedb}}, {{site.data.keyword.databases-for-etcd}}, {{site.data.keyword.databases-for-mongodb}}, {{site.data.keyword.databases-for-postgresql}}, {{site.data.keyword.databases-for-redis}}, {{site.data.keyword.messages-for-rabbitmq}}, and {{site.data.keyword.databases-for-mysql}}. 
{: .note}

{{site.data.keyword.cloud}} Databases instances are deployed in either a multi-zone region (MZR) (for example, Dallas, Frankfurt, London, Sydney, Tokyo, and Washington), or a single-campus multizone region (for example, Chennai). Each instance is deployed in a highly available configuration; that is, data is replicated by each database onto one or more servers, making the data highly available during normal operations.

- In MZRs, database members are distributed across different data centers, or zones.  
- In single-campus multizone regions, database members are distributed across different hosts.

If a single-campus multizone region failure in an MZR or a hardware failure in any region occurs, your data is still accessible as it is replicated onto other fully functioning database servers. Such issues are addressed by {{site.data.keyword.cloud}} Specialists in place. 

You can consult your {{site.data.keyword.databases-for}} documentation for more details on how your specific database replicates data among each of its members.

In addition to the high-availability configuration, for deployments in IBM Cloud Multi-Zone Regions, your data is snapshotted and backed up daily by the {{site.data.keyword.cloud}} Databases platform and stored in [cross-region Cloud Object Storage buckets](/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints-geo). For most IBM Cloud single-campus multizone regions, your data is backed up locally in [Single-campus multizone region Cloud Object Storage buckets](/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints-zonee).

If a complete region failure occurs, the database servers in the region might not be accessible, but the backup data remains available. You can initiate a restore from these backups into an available region from the service management console. Consult your {{site.data.keyword.databases-for}} backups page for more details. 

It is your responsibility to [create a new service instance](/docs/cloud-databases?topic=cloud-databases-provisioning) in which to restore when the {{site.data.keyword.cloud}} Databases platform is restored. You are also responsible for testing the validity and restore time of your backups. For more information, see [Disaster recovery](/docs/cloud-databases?topic=cloud-databases-responsibilities-cloud-databases#disaster-recovery-responsibilities) in the *Responsibilities for Cloud Databases* page.

## Application-level high availability
{: #application-ha}

Applications that communicate over networks and cloud services are subject to transient connection failures. You want to design your applications to retry connections when errors are caused by a temporary loss in connectivity to your deployment or to {{site.data.keyword.cloud_notm}}.

Because {{site.data.keyword.databases-for}} is a managed service, regular updates and database maintenance occur as part of normal operations. Such maintenance can occasionally cause short intervals where your database is disabled.

Your applications must be designed to handle temporary interruptions to the database, implement error handling for failed database commands, and implement retry logic to recover from a temporary interruption.

Several minutes of database unavailability or connection interruptions are not expected. Open a [support ticket](https://cloud.ibm.com/unifiedsupport/cases/add) with details if you have time periods longer than a minute with no connectivity so we can investigate.

If you have deployments in more than one region, you must provision {{site.data.keyword.monitoringlong}} and enable platform metrics in each region. For more information, see {{site.data.keyword.monitoringlong_notm}}your {{site.data.keyword.databases-for}} deployment's *{{site.data.keyword.monitoringlong_notm}}* page

## SLAs
{: #sla}

See [How do I ensure zero downtime?](/docs/overview?topic=overview-zero-downtime#zero-downtime) to learn more about the high availability and disaster recovery standards in {{site.data.keyword.cloud_notm}}.

All {{site.data.keyword.cloud}} Databases general availability (GA) offerings conform to the {{site.data.keyword.cloud}} [Service Level Agreement](/docs/overview?topic=overview-slas) (SLA) terms.

For more information, see the [Responsibilities for Cloud Databases](/docs/cloud-databases?topic=cloud-databases-responsibilities-cloud-databases) page.

