---

copyright:
  years: 2020
lastupdated: "2020-09-14"

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

## Data Replication 
  
Each {{site.data.keyword.cloud}} Databases service instance is a highly available product. The data is replicated on one or more servers making the data highly available during normal operations. For example, multi-zone regions deploy to three difference data centers, while single-zone regions deploy to three different hosts.

In the case of a complete zone failure, your data is still accessible on other fully functioning servers, as the {{site.data.keyword.cloud}} Databases servers are setup in separate zones. 

In addition, the data is backed up stored in [cross-region Cloud Object Storage buckets](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints-geo). In the case of a complete region failure, the database servers in the region may not be accessible, but the backup data will remain accessible. You can access this backup and restore into a new region and new service instance. 

### What data are backed-up /replicated (and by whom) 
Your entire service instance data is snapshotted and backed up daily by the {{site.data.keyword.cloud}} Databases platform. 

### Manual data replication  
You do not need to replicate the data manually. You do, however, have to restore your old service's backup into a new service and region. 
 
Furthermore, you can initiate a backup manually whenever you want. {{site.data.keyword.cloud}} Databases can then use the latest backup for the restoration into a new service instance into a new region. This restoration process is initiated by you in coordination with the {{site.data.keyword.cloud}} Databases team.

## Service replication 

{{site.data.keyword.cloud}} Databases does not replicate the service instance. You need to initiate the restoration of a backup of a failed service into a new service in a new region. The restoration process will require you to create a new instance in the event of a complete regional failure following the normal service create guidelines. You are not required to restore into a new region for single zone failures. The {{site.data.keyword.cloud}} Databases team will fix  single zone failures in place.


## High availability and disaster recovery

High Availability (HA) means providing the best possible continuous data availability after hardware failure to avoid impact on operations. Disaster Recovery (DR) means the ability to make all the data available on an alternative system as quickly as possible after a severe or extensive hardware failure.

All {{site.data.keyword.cloud}} Databases general availability (GA) offerings conform to the {{site.data.keyword.cloud_notm}} [SLA terms](/docs/overview?topic=overview-slas). 

The {{site.data.keyword.cloud}} Databases are GA services that are offered in _Chennai, Dallas, Frankfurt, London, Oslo, Seoul, Sydney, Tokyo, and Washington_. 

{{site.data.keyword.cloud}} Databases are deployed in either a multi-zone region (for example, Dallas, Frankfurt, London, Sydney, Tokyo, and Washington), or a single zone region (for eaxmple, Oslo, Seoul, and Chennai). 

Each {{site.data.keyword.cloud}} Databases service has its own particular methods for ensuring high availability. 

- In the event of a single zone outage, refer to the {{site.data.keyword.cloud}} Databases' high availability documentation for details on failover and recovery specific to your deployment. 

- In the event of a full region outage, IBM will recover the {{site.data.keyword.cloud}} Databases services in another region so that you can create a new instance deployment and initiate recovery from an instance's available backups into another region.

- In both cases it is your responsibility to create a new servcie instance in which to restore to once the {{site.data.keyword.cloud}} Databases services have been restored. 

See [How do I ensure zero downtime?](/docs/overview?topic=overview-zero-downtime#zero-downtime) to learn more about the high availability and disaster recovery standards in {{site.data.keyword.Bluemix_notm}}. You can also find information about [Service Level Agreements](/docs/overview?topic=overview-zero-downtime#SLAs).  


