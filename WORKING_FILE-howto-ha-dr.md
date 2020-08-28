---

copyright:
  years: 2018, 2020
lastupdated: "2020-08-31"

keywords: HA for cloud-databases, DR for cloud-databases, high availability for cloud-databases, disaster recovery for cloud-databases, failover for cloud-databases

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

```
_Name your file `ha-dr.md` and include it in the **How To** nav group in your `toc` file._
```

# Understanding high availability and disaster recovery for {{site.data.keyword.cloud}} Databases
{: #ha-dr}

{{site.data.keyword.cloud}} Databases use global load balancing to ensure a redundant, highly-available platform is available for you to host your workloads and applications.
{: shortdesc}

This document covers all the {{site.data.keyword.cloud}} Databases, which includes {{site.data.keyword.databases-for-cassandra}}, {{site.data.keyword.databases-for-elasticsearch}}, {{site.data.keyword.databases-for-enterprisedb}}, {{site.data.keyword.databases-for-etcd}}, {{site.data.keyword.databases-for-mongodb}}, {{site.data.keyword.databases-for-postgresql}}, {{site.data.keyword.databases-for-redis}}, and {{site.data.keyword.messages-for-rabbitmq}}.
{: .note}

All {{site.data.keyword.cloud}} Databases general availability (GA) offerings conform to the {{site.data.keyword.cloud_notm}} [SLA terms](/docs/overview?topic=overview-slas). 


The {{site.data.keyword.cloud}} Databases are GA services that are offered in _Chenai, Dallas, Frankfurt, London, Oslo, Sydney, Tokyo, and Washington_. Each location has three different data centers for redundancy. 

{{site.data.keyword.cloud}} Databases are deployed in a multi-zone region (for example, us-south, us-east, eu-fra) where the platform is designed to be resilient to the failure of any one zone in the region.

See [How do I ensure zero downtime?](/docs/overview?topic=overview-zero-downtime#zero-downtime) to learn more about the high availability and disaster recovery standards in {{site.data.keyword.Bluemix_notm}}. You can also find information about [Service Level Agreements](/docs/overview?topic=overview-zero-downtime#SLAs).  

----------
----------

Your data is backed up to cross-regional object storage instances, but steps must be taken to make those backups restorable after regional failure. The purpose of the regional policy is to make backups from the failed region available for you to restore - not to automatically recover database instances from the failed region.

In the case of a failure, the {{site.data.keyword.cloud}} Databases team will take the neccessary steps to restore service access. Once service is restored, you will be instructed to locate and restore backups of any database instances that you need access to during the outage. You may then restore databases from the failed region to a region of your choice. You will be responsible for selecting and restoring appropriate backup(s) as needed to regain access to your database instances. 

----------
----------

High Availability (HA) means providing the best possible continuous data availability after hardware failure to avoid impact on operations. Disaster Recovery (DR) means the ability to make all the data available on an alternative system as quickly as possible after a severe or extensive hardware failure.

{{site.data.keyword.cloud}} Databases provides automatic in-region data redundancy and failover by default. The services are offered in Multi-Zone regions (Dallas, Frankfurt, and Sydney), each with three availability zones for redundancy.

To prepare for the disaster scenario where the entire region fails (broken network, for example) and the service in that region becomes unavailable, you need to define your own cross-region backup policy to restore your data in another available region. 


## Automatic in-region data redundancy and failover

You can create {{site.data.keyword.cloud}} Database service instances in one of the supported IBM Cloud regions, which represent the geographic area where your service requests are handled and processed. By default, your {{site.data.keyword.cloud}} Database service instance consists of three nodes, one primary and two secondary nodes in three different availability zones in the IBM Cloud region.

The data in your primary node is automatically replicated to secondary nodes (replicas) with low latency. You don't need to do anything to enable the replication. When your primary node fails, a secondary node in the cluster will be elected as the primary to prevent your applications from being affected. In this way, you have automatic high availability within one region for your data.

## Manual cross-region backups

To protect your data across more than one region against the disaster scenario where the entire region fails, you need to define your own cross-region backup policy. To create cross-region data redundancy, you need to have regular backups of your complete databases from your service instance in a region. When the region is unavailable, you can provision a new service instance in another available region to restore your database manually. 

Time of restoration varies, depending on the size of your data and network condition. For your reference, it takes about 45 minutes to restore data of 10G from Poughkeepsie to a service instance deployed in Dallas. Therefore, to minimize the impact of region-wide failures, you need to plan ahead, for example, by having a service instance in a second region as a cold standby.

----------
----------

<!-- 

_Document the list of regions or data centers that your offering is available in. For other details, work with your offering management and development teams to define what HA and DR documentation is required for your offering. At a minimum, use the following sections to document the following details:_

_* The automatic HA and DR capabilities that your offering provides, for example, global load balancing, multi-availability zones, data replication or data mirroring, active-active or active-passive clusters_

_* If applicable, the supported tools that your offering provides to help users create their own HA and DR capabilities_

_* Application deployment considerations_

_Do not include any details that would give malicious persons an advantage to compromising your offering environment._
-->