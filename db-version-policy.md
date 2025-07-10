---

copyright:
  years: 2018, 2025
lastupdated: "2025-07-10"

subcollection: cloud-databases

keywords: version for cloud-databases, database version, end of life, major version, minor version, deprecate, deprecation, version number, deprecated, eol

---

{{site.data.keyword.attribute-definition-list}}

# Versioning policy
{: #versioning-policy}

When you provision a {{site.data.keyword.databases-for}} instance, you can choose from the versions currently available on {{site.data.keyword.cloud_notm}}. Find the latest versions from the [catalog pages](https://cloud.ibm.com/catalog?category=databases){: external}, the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference#deployables-show){: external}, or the [{{site.data.keyword.databases-for}} API](/apidocs/cloud-databases-api/cloud-databases-api-v5#listdeployables){: external}.

## Major versions defined
{: #version-definitions}

| Service | Versioning schema| Next known end of life version and date | Preferred major version | End of life procedure |
|----|----|----|----|----|
| {{site.data.keyword.databases-for-mongodb}} | Major versions are the first two numbers in a `major.x.patch` version number. In cases where `x` is even, it is a stable release suitable for production. Even `x` versions are the only ones available on {{site.data.keyword.databases-for}}. | v6, 30 July 2025, <br> v7, 26 Aug 2026 |   v7.0   | Automatically upgraded in place to next Major version |
| {{site.data.keyword.databases-for-elasticsearch}} | Major versions are the first two numbers in a `release.version.maintenance` version number. |  v8.7, 4 March 2026, <br> v8.10, 4 March 2026, <br> v8.12, 4 March 2026, <br> v8.15, 4 March 2026|   v8.15   | Automatically upgraded in-place to next major version. |
| {{site.data.keyword.databases-for-redis}} | Major versions are the first number in a `major.minor.patch` version number. | v6.2, 30 July 2025 |   v7.2   | Automatically upgraded in place to next Major version |
| {{site.data.keyword.databases-for-postgresql}} | The major version is defined by the first number in the version number. | v13, 22 October 2025 |   v17 | Automatically upgraded in place to next major version |
| {{site.data.keyword.databases-for-mysql}} | Major versions are the first two numbers in a `major.x.patch` version number. | v8.0, April 2026 |  v8.0 | Backup taken and access removed |
| {{site.data.keyword.messages-for-rabbitmq}} | Major versions are the first two numbers in a `major.x.patch` version number. | v3.12, 30 April 2025 |   v3.13   | Backup taken and access removed |
| {{site.data.keyword.databases-for-enterprisedb}} | The major version is defined by the first number in the version number. | End of service/full deprecation on 15 October 2025. |  v12  | Permanently disabled and de-provisioned. [Refer to critical timelines](https://cloud.ibm.com/docs/databases-for-enterprisedb?topic=databases-for-enterprisedb-deprecation){: external}. |
| {{site.data.keyword.databases-for-etcd}} | Major versions are the first number in a `major.minor.patch` version number. | End of Service/Full deprecation on 15 October 2025 |   v3.5   | Permanently disabled and de-provisioned. [Refer to critical timelines](https://cloud.ibm.com/docs/databases-for-etcd?topic=databases-for-etcd-deprecation&interface=ui){: external}.
 |
{: caption="Major versions for {{site.data.keyword.databases-for}}" caption-side="top"}

## Subscribe for version updates
{: #version-updates-subscribe}

{{site.data.keyword.databases-for}} major version updates are posted in each service's Release Notes. To stay up to date with major version announcements, go to the [{{site.data.keyword.cloud_notm}} Status page](https://cloud.ibm.com/status){: external} and sign up for notifications. Service release notes are included in these status notifications.

## Deprecation of major versions
{: #version-deprecation}

{{site.data.keyword.databases-for}} tries to support a major version for 3 years from its release. If a version is deprecated or marked end of life by the open source project owners, {{site.data.keyword.databases-for}} takes steps to deprecate that version.

When a major version is deprecated, a six-month transition window is opened for current users of the deprecated version. At the beginning of the period, we seek to contact users affected by the deprecation. During the six-month transition window, users are able to initiate an upgrade to a supported major version. Existing instances continue to run as normal.

Restoration of existing instances into new instances of the deprecated major version is available during the six-month deprecation, although we recommend upgrading to a nondeprecated major version as soon as possible.

At the end of the transition window, deprecated major versions cannot be deployed on {{site.data.keyword.databases-for}}. A backup of the instance is taken and access to instances that are running a deprecated version is removed or instances are automatically upgraded to the next major version. The backup is available to be restored into a new supported version.

Backups are retained for 30 days only. Requests to reenable disabled formations of end-of-life versions are not accommodated.

Failure to act can result in compatibility issues with your apps when IBM upgrades in-place. On rare occasions, failure can result, impacting your availability. If a failure occurs, the instance is disabled, and you need to restore from backup. We recommend self-migrating before the end of support date.
{: important}


## Version tags
{: #version-tags}

| Version tag | Description|
|-------------|-------------|
| **Preferred** | The recommended and default version for all new instances. It's the most stable, up-to-date version from both an instance-level and service-level perspective.|
| **Preview** | A preview version is released for a limited time to try available functions. Often it is the newest available version available from the project maintainers in preparation for making it the "Preferred" version. While deployable, preview versions are not suitable for production, as they are excluded from service-level agreements and support. Also, a preview version isn't guaranteed to become a production-level release. IBM reserves the right to ask a customer to delete an instance that uses a preview version. |
| **Deprecated** | Old versions and versions near their end of life dates are marked as "Deprecated". Provisions and restores of instances that run a deprecated version are still available and instances that run a deprecated version continue to be supported. However, you are encouraged to upgrade to the new "Preferred" version as deprecated versions are eventually removed from {{site.data.keyword.cloud_notm}} and are no longer provisionable, restorable, or supported.                                                              |
| **Untagged** | Untagged versions are fully supported and deployable versions. They are usually slightly older than the current preferred version, but they are still supported by the project maintainers. They continue to be supported on {{site.data.keyword.databases-for}} instances until their deprecation is announced.|
| **Hidden** | A hidden version cannot be provisioned. Existing instances that are using a version marked as hidden are still able to be restored to the hidden version. |
{: caption="{{site.data.keyword.databases-for}} Version Tags" caption-side="bottom"}

## Minor versions
{: #minor-versions}

{{site.data.keyword.cloud_notm}} is committed to providing secure, up-to-date versions of services. As updates are released by project maintainers, they are tested, evaluated, and released to {{site.data.keyword.databases-for}} instances. Your instance's minor version and patch updates are handled automatically and are not user configurable.

## Major versioning end of life notifications
{: #-major-version-eol}

You receive multiple notifications when a major version reaches its end of life. You can typically expect:

* A Cloud status page announcement, for example: [End of support notices](https://cloud.ibm.com/status/announcement?query=End+of+Support+Notices){: external}.
* An announcement in your service's Release Notes, for example: [IBM Cloud® Databases for PostgreSQL version 12 end of life on January 22, 2025](https://cloud.ibm.com/docs/databases-for-postgresql?topic=databases-for-postgresql-postgresql-relnotes#databases-for-postgresql-18jan2023){: external}.
* A notification by email through the {{site.data.keyword.IBM_notm}} API. This email contains a *Notifications* link that takes you to a Notifications Management page. **Make sure that these announcements are not being caught by your email service's spam filter.** For more information, see [Setting up distribution lists for IBM Cloud notifications](https://cloud.ibm.com/docs/account?topic=account-add-users-distribution-list)){:external}.
* Ensure that your account is enabled to receive notifications and announcements. You **must** enable toggle to receive platform and resource updates. Turn on major and minor toggle under the Platform tab > Announcements > Major and Minor, and service updates under the Resource tab > Resource Activity > Service Updates. For more information, see [Setting email preferences for notifications](https://cloud.ibm.com/docs/account?topic=account-email-prefs).

For more information, see [Programmatic methods for checking version status](#-major-version-eol-check-version-status). Customers are encouraged to use **programatic ways**, via CLI or API, to get updated about database version status. For more information, see [Programmatic methods for checking version status](#-major-version-eol-check-version-status).

Any actions taken after an EOL date happen over several days after the EOL date. We try, but cannot guarantee, to make these upgrades outside of business hours in the local regions. If you want more control over the upgrade process of your instance, we recommend that you upgrade following our [backup and restore process](/docs/cloud-databases?topic=cloud-databases-dashboard-backups) before the EOL date of your version.
{: .note}

### Programmatic methods for checking version status
{: #-major-version-eol-check-version-status}

**On the CLI** the following [{{site.data.keyword.databases-for}} `deployables-show` command](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference#deployables-show) shows deployable service types, specifically the available versions and their `preferred` or `stable` status.

```sh
ibmcloud cdb deployables-show [--stable] [--preferred] [--json]
```
{: pre}

Check the status of a major version by reviewing the output of the `deployable` command, specifically *Status* and *Preferred*. The following output example shows that version 7 is the `Preferred` version and version 6 *Status* is `deprecated`.

```text
Service Type:  mongodb
Version   Status       Preferred
7       stable       true
6       deprecated   false
```

**On the {{site.data.keyword.databases-for}} API** the [`deployables` endpoint](/apidocs/cloud-databases-api/cloud-databases-api-v5#listdeployables){: external} returns all deployable services. Use the `version` parameter to return the version number.

```sh
GET /v5/ibm/deployables
```
{: pre}

### Major versions and Terraform
{: #-major-version-eol-terraform}

Note that you cannot currently upgrade to a new major version using Terraform. Changing the version number on a Terraform script could lead to your data being destroyed. The recommended method of version upgrade is restoring a backup into a new deployment with the latest version. For more information, see [Restoring a backup](/docs/cloud-databases?topic=cloud-databases-dashboard-backups&interface=ui#restore-backup).
{: important}
