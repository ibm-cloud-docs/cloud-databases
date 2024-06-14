---
copyright:
  years: 2018, 2024
lastupdated: "2024-04-22"

subcollection: cloud-databases

keywords: version for cloud-databases, database version, end of life, major version, minor version, deprecate, deprecation, version number, deprecated, eol

---

{{site.data.keyword.attribute-definition-list}}

# Versioning policy
{: #versioning-policy}

When you provision a {{site.data.keyword.databases-for}} instance, you can choose from the versions currently available on {{site.data.keyword.cloud_notm}}. Find the latest versions from the [catalog pages](https://cloud.ibm.com/catalog?category=databases){: external}, the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference#deployables-show){: external}, or the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api#get-all-deployable-databases){: external}.

## Major versions defined
{: #version-definitions}

| Service | Versioning schema| Next known end of life version and date | Preferred major version | End of life procedure |
|----|----|----|----|----|
| {{site.data.keyword.databases-for-mongodb}} | Major versions are the first two numbers in a `major.x.patch` version number. In cases where `x` is even, it is a stable release suitable for production. Even `x` versions are the only ones available on {{site.data.keyword.databases-for}}. | v4.4, 26 April 2024; v5, 25 September 2024 |   v6.0   | Automatically upgraded in place to next Major version |
| {{site.data.keyword.databases-for-mongodb}} | Major versions are the first two numbers in a `major.x.patch` version number. In cases where `x` is even, it is a stable release suitable for production. Even `x` versions are the only ones available on {{site.data.keyword.databases-for}}. | v4.4, 26 April 2024; v5, 25 September 2024 |   v6.0   | Automatically upgraded in place to next Major version |
| {{site.data.keyword.databases-for-elasticsearch}} | Major versions are the first two numbers in a `release.version.maintenance` version number. |  v7.17, 29 August 2024 |   v8.10   | Automatically upgraded in place to next Major version |
| {{site.data.keyword.databases-for-redis}} | Major versions are the first number in a `major.minor.patch` version number. | v5.0, 26 April 2024; v6.0 25 October 2024 |   v6.2   | Automatically upgraded in place to next Major version 6.2 |
| {{site.data.keyword.databases-for-postgresql}} | The major version is defined by the first number in the version number. | v12, 22 January 2025 |   v15   | Backup taken and access removed |
| {{site.data.keyword.databases-for-enterprisedb}}  | The major version is defined by the first number in the version number. | v12, TBD |   v12   | Backup is taken and access is removed |
| {{site.data.keyword.databases-for-mysql}} | Major versions are the first two numbers in a `major.x.patch` version number. | v5.7, 26 April 2024 |  v8.0 For more information, see [MySQL 8 GA](/docs/databases-for-mysql?topic=databases-for-mysql-mysql8-ga).  | Backup taken and access removed |
| {{site.data.keyword.messages-for-rabbitmq}} | Major versions are the first two numbers in a `major.x.patch` version number. | v3.11, 24 July 2024 |   v3.12   | Backup taken and access removed |
| {{site.data.keyword.databases-for-etcd}} | Major versions are the first number in a `major.minor.patch` version number. | v3.3, 26 April 2024 |   v3.5   | Backup taken and access is removed. |
| {{site.data.keyword.databases-for-cassandra}} | Major versions are the first number in a `major.minor.patch` version number. | v6.8x |  | *Full deprecation announced with an end of service date of 30 June 2024* |
{: caption="Table 1. Major versions for {{site.data.keyword.databases-for}}" caption-side="top"}

{{site.data.keyword.databases-for-cassandra_full}} is deprecated and no longer supported as of 30 June 2024. For more information, see the [deprecation details](/docs/databases-for-cassandra?topic=databases-for-cassandra-deprecation#dep_details).
{: deprecated}

## Subscribe for version updates
{: #version-updates-subscribe}

{{site.data.keyword.databases-for}} major version updates are posted in each service's Release Notes. To stay up to date with major version announcements, go to the [{{site.data.keyword.cloud_notm}} status page](https://cloud.ibm.com/status){: external} and sign up for notifications. Service release notes are included in these status notifications.

## Deprecation of Major Versions
{: #version-deprecation}

{{site.data.keyword.databases-for}} tries to support a major version for 3 years from its release. If a version is deprecated or marked end of life by the open source project owners, {{site.data.keyword.databases-for}} takes steps to deprecate that version.

When a major version is deprecated, a six-month transition window is opened for current users of the deprecated version. At the beginning of the period, we seek to contact users affected by the deprecation. During the six-month transition window, users are able to initiate an upgrade to a supported major version. Existing instances continue to run as normal.

Restoration of existing instances into new instances of the deprecated major version is available during the six-month deprecation, although we recommend upgrading to a nondeprecated major version as soon as possible.

At the end of the transition window, deprecated major versions cannot be deployed on {{site.data.keyword.databases-for}}. A backup of the instance is taken and access to instances that are running a deprecated version is removed or instances are automatically upgraded to the next major version. The backup is available to be restored into a new supported version.

Failure to act can result in compatibility issues with your apps when IBM upgrades in-place. On rare occasions, failure can result, impacting your availability. If a failure occurs, the instance is disabled, and you need to restore from backup. We recommend self-migrating before the end of support date.
{: .important}

## Version Tags
{: #version-tags}

| Version Tag | Description|
|-------------|-------------|
| **Preferred** | The recommended and default version for all new instances. It's the most stable, up-to-date version from both an instance-level and service-level perspective.|
| **Preview** | A preview version is released for a limited time to try available functions. Often it is the newest available version available from the project maintainers in preparation for making it the "Preferred" version. While deployable, preview versions are not suitable for production, as they are excluded from service-level agreements and support. Also, a preview version isn't guaranteed to become a production-level release. IBM reserves the right to ask a customer to delete an instance that uses a preview version. |
| **Deprecated** | Old versions and versions near their end of life dates are marked as "Deprecated". Provisions and restores of instances that run a deprecated version are still available and instances that run a deprecated version continue to be supported. However, you are encouraged to upgrade to the new "Preferred" version as deprecated versions are eventually removed from {{site.data.keyword.cloud_notm}} and are no longer provisionable, restorable, or supported.                                                              |
| **Untagged** | Untagged versions are fully supported and deployable versions. They are usually slightly older than the current preferred version, but they are still supported by the project maintainers. They continue to be supported on {{site.data.keyword.databases-for}} instances until their deprecation is announced.|
| **Hidden** | A hidden version cannot be provisioned. Existing instances that are using a version marked as hidden are still able to be restored to the hidden version. |
{: caption="Table 1. {{site.data.keyword.databases-for}} Version Tags" caption-side="bottom"}

## Minor versions
{: #minor-versions}

{{site.data.keyword.cloud_notm}} is committed to providing secure, up-to-date versions of services. As updates are released by project maintainers, they are tested, evaluated, and released to {{site.data.keyword.databases-for}} instances. Your instance's minor version and patch updates are handled automatically and are not user configurable.

### Minor version upgrades and Terraform
{: #minor-versions-tf}

In the event of a minor version update, Terraform

Terraform destroys the resource and re-create it (to match the expected configuration). To prevent Terraform from deleting your instance,

## Major versioning End of Life
{: #-major-version-eol}

You receive multiple notifications when a major version reaches its End of life. You can typically expect:
* A blog post, for example: [Messages for RabbitMQ 3.8 End of Life in July 2022](https://www.ibm.com/cloud/blog/announcements/messages-for-rabbitmq-38-end-of-life-in-july-2022){: external}
* An announcement in your service's Release Notes, for example: [IBM Cloud® Messages for RabbitMQ 3.8 End of Life in July 2022](https://cloud.ibm.com/docs/messages-for-rabbitmq?topic=messages-for-rabbitmq-rabbitmq-relnotes#messages-for-rabbitmq-25jan2022){: external}
* A notification by email through the {{site.data.keyword.IBM_notm}} API. This email contains a *Notifications* link that takes you to a Notifications Management page. **Make sure that these announcements are not being caught by your email service's spam filter.** For more information, see [Setting up Distribution Lists for IBM Cloud Notifications](https://www.ibm.com/cloud/blog/announcements/setting-up-distribution-lists-for-ibm-cloud-notifications){: external}.

For more information, see [Programmatic Methods for Checking Version Status](#-major-version-eol-check-version-status).

Any actions taken after an EOL date happen over several days after the EOL date. We try, but cannot guarantee, to make these upgrades outside of business hours in the local regions. If you want more control over the upgrade process of your instance, we recommend that you upgrade following our [backup and restore process](/docs/cloud-databases?topic=cloud-databases-dashboard-backups) before the EOL date of your version.
{: .note}

### Programmatic Methods for Checking Version Status
{: #-major-version-eol-check-version-status}

The following [{{site.data.keyword.databases-for}} `deployables` command](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference#deployables-show) shows deployable service types, specifically the available versions and their `preferred` or `stable` status.

```sh
ibmcloud cdb deployables-show [--stable] [--preferred] [--json]
```
{: pre}

Check the status of a major version by reviewing the output of the `deployable` command, specifically *Status* and *Preferred*. The following output example shows that version 4.4 is the `Preferred` version and version 4.2's *Status* is `deprecated`.

```text
Service Type:  mongodb
Version   Status       Preferred
4.4       stable       true
4.2       deprecated   false
```

The {{site.data.keyword.databases-for}} API `deployables` endpoint returns all deployable services. Use the `version` parameter to return the version number.
```sh
GET /v5/ibm/deployables
```
{: pre}
