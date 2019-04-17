---
Copyright:
  years: 2018, 2019
lastupdated: "2019-01-31"
---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}


# Database Versioning Policy
{: #versioning-policy}

{{site.data.keyword.IBM_notm}} {{site.data.keyword.databases-for}} allow users to select the major version for their deployments. We are committed to providing secure, up-to-date versions of databases, and we upgrade database minor versions when appropriate.

## Major Versions

{{site.data.keyword.IBM_notm}} {{site.data.keyword.databases-for}} sets out to support a major version of a database for 3 years from its release. If a database version is deprecated or marked end of life by the open source project owners, we will move to immediately deprecate that version on {{site.data.keyword.IBM_notm}} {{site.data.keyword.databases-for}}.

## Deprecation of Major Versions 

When a major version is deprecated, a six-month transition window is opened for current users of the deprecated version.

At the beginning of the period, we seek to contact users affected by the deprecation. 30 days after the communication, deprecated major versions cannot be deployed as new deployments on {{site.data.keyword.IBM_notm}} {{site.data.keyword.databases-for}}.

During the six-month transition window, users are able to initiate an upgrade to a supported major version. Existing customers instances will continue to run as normal.

Restoration of existing databases into new deployments of the deprecated major version is possible during the 30 day deprecation, although we recommend upgrading to a non-deprecated major version as soon as possible.
{: .tip}

At the end of the six-month window, we will remove access to databases running a deprecated version and take a backup. The backup is available to be restored into a new supported database version.

## Major versions defined

Database|Versioning Schema|Major Versions
----------|---------|----------
Elasticsearch|Major versions are the first number in a `release.version.maintenance` version number.|2, 5, 6
etcd|Major versions are the first number in a `major.minor.patch` version number.|2, 3
MongoDB|Major versions are the first number in a `major.minor.maintenance` version number.|2, 3, 4
PostgreSQL*|Major version is defined by the first number in the version number.| 9.5, 9.6, 10
Redis|Major versions are the first number in a `major.minor.patch` version number.|2, 3, 4
RabbitMQ|Major versions are the first number in a `major.minor.patch` version number.|2, 3
{: caption="Table 1. Major versions for {{site.data.keyword.databases-for}}" caption-side="top"}


* There was a change of versioning scheme for PostgreSQL after version 9.6. Before and including version 9.6, a PostgreSQL major version was defined by the first two numbers in the version.


