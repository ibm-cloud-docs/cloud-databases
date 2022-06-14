---
copyright:
  years: 2018, 2022
lastupdated: "2022-06-14"

subcollection: cloud-databases

keywords: version for cloud-databases

---

{:external: .external target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}


# Database Versioning Policy
{: #versioning-policy}

When you provision a {{site.data.keyword.databases-for}} deployment, you can choose from the versions currently available on {{site.data.keyword.cloud_notm}}. You can find the latest versions from the [catalog pages](https://cloud.ibm.com/catalog?category=databases), from the cloud databases cli plug-in command [`ibmcloud cdb deployables-show`](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference#deployables-show), or from the cloud databases API [`/deployables`](https://cloud.ibm.com/apidocs/cloud-databases-api#get-all-deployable-databases) endpoint.

## Version Tags
{: #version-tags}

**Preferred** - The recommended and default database version for all new deployments. It's the most stable, up-to-date version of the database from both a database-level and service-level perspective.

**Preview** - A preview database version is released for a limited time to try available functions. Often it is the newest available version available from the database project maintainers in preparation for making it the "Preferred" version. While deployable, preview versions are not suitable for production, as they are excluded from service-level agreements and support. Also, a preview version isn't guaranteed to become a production-level release. IBM reserves the right to ask a customer to delete a deployment that uses a preview version.

**Deprecated** - Old versions and versions nearing their end of life dates are marked as "Deprecated". Provisions and restores of deployments that run a deprecated version are still available and deployments that are running a deprecated version continue to be supported. However, you are encouraged to upgrade to the new "Preferred" version of the database as deprecated versions are eventually removed from {{site.data.keyword.cloud_notm}} and are no longer provisionable, restorable, or supported. 

**Untagged** - Untagged database versions are fully supported and deployable versions. They are usually slightly older than the current preferred version, but they are still supported by the database project maintainers. They continue to be supported on {{site.data.keyword.databases-for}} deployments until their deprecation is announced.

## Deprecation of Major Versions
{: #version-deprecation}

{{site.data.keyword.IBM_notm}} {{site.data.keyword.databases-for}} tries to support a major version of a database for 3 years from its release. 

If a database version is deprecated or marked end of life by the open source project owners, {{site.data.keyword.IBM_notm}} {{site.data.keyword.databases-for}} takes steps to deprecate that version.

When a major version is deprecated, a six-month transition window is opened for current users of the deprecated version.

At the beginning of the period, we seek to contact users affected by the deprecation. During the six-month transition window, users are able to initiate an upgrade to a supported major version. Existing deployments continue to run as normal.

Restoration of existing databases into new deployments of the deprecated major version is available during the six-month deprecation, although we recommend upgrading to a nondeprecated major version as soon as possible.
{: .tip}

At the end of the transition window, deprecated major versions cannot be deployed on {{site.data.keyword.IBM_notm}} {{site.data.keyword.databases-for}}. A backup of the deployment is taken and access to databases that are running a deprecated version is removed or automatically upgraded to the next major version. See table 1 for which databases are upgraded or removed. Regardless, the backup is available to be restored into a new supported database version.

Failure to act can result in compatibility issues with your apps when IBM upgrades in-place. On rare occasions, failure can result, impacting your availability. If a failure occurs, the database is disabled and you need to restore from backup. We recommend self-migrating before the end of support date.
{: .note}

## Major versions defined
{: #version-definitions}

Database | Versioning Schema | Next Known End of Life Version and Date | End of Life procedure |
--------- | --------- | --------- | --------- |
DataStax | Major versions are the first number in a `major.minor.patch` version number. | v6.7, [24 May 2022](https://www.ibm.com/cloud/blog/announcements/databases-for-datastax-6-7-end-of-life-in-may-2022) | Backup taken and access removed|  
Elasticsearch | Major versions are the first number in a `release.version.maintenance` version number.| Backup taken and access removed|  
EnterpriseDB | Major version is defined by the first number in the version number. | v12, December 2024 | Backup taken and access removed|  
etcd | Major versions are the first number in a `major.minor.patch` version number. | v3.3, unplanned | Backup taken and access removed|  
MongoDB | Major versions are the first two numbers in a `major.x.patch` version number. In cases where `x` is even, it is a stable release suitable for production. Even `x` versions are the only ones available on Cloud Databases. | v4.0, [26 April 2022](https://www.ibm.com/cloud/blog/announcements/databases-for-mongodb-40-end-of-life-in-april-2022) | Automatically upgraded in place to next Major version|
PostgreSQL* | Major version is defined by the first number in the version number. | v9.6, [11 November 2021](https://www.postgresql.org/support/versioning/)| Backup taken and access removed|  
Redis | Major versions are the first number in a `major.minor.patch` version number. | v4.0, [27 May 2022](https://www.ibm.com/cloud/blog/announcements/ibm-cloud-databases-for-redis-4-end-of-life-in-march-2022) | Automatically upgraded in place to next Major version only for Redis 4 to Redis 5|  
RabbitMQ | Major versions are the first two numbers in a `major.x.patch` version number. | v3.8, [12 July 2022](https://www.ibm.com/cloud/blog/announcements/messages-for-rabbitmq-38-end-of-life-in-july-2022) | Backup taken and access removed|  
MySQL | Major versions are the first two numbers in a `major.x.patch` version number. | v5.7, October 2023 | Backup taken and access removed|  
{: caption="Table 1. Major versions for {{site.data.keyword.databases-for}}" caption-side="top"}

**The versioning schema for PostgreSQL changed after version 9.6. Before and including version 9.6, a PostgreSQL major version was defined by the first two numbers in the version.*

Any actions taken after a database EOL date happen over several days after the EOL date. We try, but cannot guarantee, to make these upgrades outside of business hours in the local regions. If you want more control over the upgrade process of your database instance, we recommend that you upgrade following our [backup and restore process](/docs/cloud-databases?topic=cloud-databases-dashboard-backups) before the EOL date of your database version.
{: .note}

## Minor versions
{: #minor-versions}

{{site.data.keyword.cloud_notm}} is committed to providing secure, up-to-date versions of databases. As updates are released by database project maintainers, they are tested, evaluated, and released to {{site.data.keyword.databases-for}} deployments. Your deployment's minor version and patch updates are handled automatically and are not user configurable. 
