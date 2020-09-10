---

copyright:
  years: 2018, 2020
lastupdated: "2020-08-31"

subcollection: cloud-databases

keywords: HA for cloud-databases, DR for cloud-databases, high availability for cloud-databases, disaster recovery for cloud-databases, failover for cloud-databases

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}

# Understanding high availability and disaster recovery for {{site.data.keyword.databases-for}}
{: #ha-dr}

{{site.data.keyword.cloud}} Databases use global load balancing to ensure a redundant, highly available platform is available for you to host your workloads and applications.
{: shortdesc}

This document covers all the {{site.data.keyword.cloud}} Databases, which include {{site.data.keyword.databases-for-cassandra}}, {{site.data.keyword.databases-for-elasticsearch}}, {{site.data.keyword.databases-for-enterprisedb}}, {{site.data.keyword.databases-for-etcd}}, {{site.data.keyword.databases-for-mongodb}}, {{site.data.keyword.databases-for-postgresql}}, {{site.data.keyword.databases-for-redis}}, and {{site.data.keyword.messages-for-rabbitmq}}.
{: .note}

--------
Specifically, the service MUST clearly state/document:

1) If the service replicates the data (and where)
   
Each {{site.data.keyword.cloud}} Databases service instance is a highly available product. The data is replicated on one or more servers making the data highly available during normal operations. In the case of a complete zone failure, your data is still accessible on  other fully functioning servers, as the {{site.data.keyword.cloud}} Databases servers are setup in separate zones. In addition, the data is backed up and pushed to Object Storage on a daily schedule and per clients' requests. In the case of a complete region failure, all of the database servers will not be accessible, but the backup data will remain accessible. You can access this backup and restore into a new region and new service instance.

1) If the Clients need to replicate the data (and how)
You do not need to replicate the data manually. You do, however, have to restore your old service's backup into a new service and region.

3) What data are backed-up /replicated (and by who)
Your entire service instance is snapshotted and backed up daily by the {{site.data.keyword.cloud}} Databases platform. Furthermore, you can initiate a backup manually whenever you want. {{site.data.keyword.cloud}} Databases can then use the latest backup for the restoration into a new service instance into a new region. Again, this restoration process is initiated by you.

4) If IBM Cloud replicates the service (and where)
No.

5) If the Clients need to replicate the service (and how).
You do need to initiate the restoration of a backup of a failed service into a new service in a new region.  
--------


## High availability and disaster recovery

High Availability (HA) means providing the best possible continuous data availability after hardware failure to avoid impact on operations. Disaster Recovery (DR) means the ability to make all the data available on an alternative system as quickly as possible after a severe or extensive hardware failure.

All {{site.data.keyword.cloud}} Databases general availability (GA) offerings conform to the {{site.data.keyword.cloud_notm}} [SLA terms](/docs/overview?topic=overview-slas). 

The {{site.data.keyword.cloud}} Databases are GA services that are offered in _Chennai, Dallas, Frankfurt, London, Oslo, Seoul, Sydney, Tokyo, and Washington_. 

{{site.data.keyword.cloud}} Databases are deployed in either a multi-zone region (for example, Dallas, Frankfurt, London, Sydney, Tokyo, and Washington), or a single zone region (for eaxmple, Oslo, Seoul, and Chennai). 

Your data is backed up to cross-regional object storage instances, but steps must be taken to make those backups restorable after regional failure. The purpose of the regional policy is to make backups from the failed region available for you to restore - not to automatically recover database instances from the failed region.  

To prepare for the disaster scenario where the entire region fails (broken network, for example) and the service in that region becomes unavailable, you need to define your own cross-region backup policy to restore your data in another available region. 

See [How do I ensure zero downtime?](/docs/overview?topic=overview-zero-downtime#zero-downtime) to learn more about the high availability and disaster recovery standards in {{site.data.keyword.Bluemix_notm}}. You can also find information about [Service Level Agreements](/docs/overview?topic=overview-zero-downtime#SLAs).  

## Automatic in-region data redundancy and failover

{{site.data.keyword.cloud}} Databases provide automatic in-region data redundancy and failover by default. The services are offered in Multi-Zone [regions](/docs/cloud-databases?topic=cloud-databases-regions) each with three availability zones for redundancy.

You can create {{site.data.keyword.cloud}} Database service instances in one of the supported IBM Cloud regions, which represent the geographic area where your service requests are handled and processed. By default, your {{site.data.keyword.cloud}} Database service instance consists of three nodes, one primary and two secondary nodes in three different availability zones in the IBM Cloud region.

The data in your primary node is automatically replicated to secondary nodes (replicas) with low latency. You don't need to do anything to enable the replication. When your primary node fails, a secondary node in the cluster is elected as the primary to prevent your applications from being affected. In this way, you have automatic high availability within one region for your data.

If a failure is encountered, the {{site.data.keyword.cloud}} Databases team will take the necessary steps to restore service access. Once service is restored, you will be instructed to locate and restore backups of any database instances that you need access to during the outage. You can then restore databases from the failed region to a region of your choice. You are responsible for selecting and restoring appropriate backups as needed to regain access to your database instances. 

## Manual cross-region backups

To protect your data across more than one region against the disaster scenario where the entire region fails, you need to define your own cross-region backup policy. To create cross-region data redundancy, you need to have regular backups of your complete databases from your service instance in a region. When the region is unavailable, you can provision a new service instance in another available region to restore your database manually (except where replicating cross-region data into or outside of `eu-de` is disallowed). 

Time of restoration varies, depending on the size of your data and network condition. For your reference, it takes about 45 minutes to restore data of 10G from Poughkeepsie to a service instance deployed in Dallas. Therefore, to minimize the impact of region-wide failures, you need to plan ahead. For example, plan ahead by having a service instance in a second region as a cold standby.
{: .tip}

