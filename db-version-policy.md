---

copyright:
  years: 2018, 2026
lastupdated: "2026-01-27"

subcollection: cloud-databases

keywords: version for cloud-databases, database version, end of life, major version, minor version, deprecate, deprecation, version number, deprecated, eol

---

{{site.data.keyword.attribute-definition-list}}

# Versioning policy
{: #versioning-policy}

When you provision a {{site.data.keyword.databases-for}} instance, you can choose from the versions currently available on {{site.data.keyword.cloud}}. Find the latest versions from the [catalog pages](https://cloud.ibm.com/catalog?category=databases){: external}, the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/cloud-databases?topic=cloud-databases-cdb-reference#deployables-show){: external}, or the [{{site.data.keyword.databases-for}} API](/apidocs/cloud-databases-api/cloud-databases-api-v5#listdeployables){: external}.

## Major versions defined
{: #version-definitions}





| Service | {{site.data.keyword.databases-for}} versioning schema| Next known end of life version and date | Preferred major version | End of life procedure [^tabletext4] |
|----|----|----|----|----|
| {{site.data.keyword.databases-for-mongodb}} | {{site.data.keyword.databases-for}} major versions are the first two numbers in a `major.x.patch` version number. In cases where `x` is even, it is a stable release suitable for production. Even `x` versions are the only ones available on {{site.data.keyword.databases-for}}. |  v7, 25 Aug 2027 |   v8.0   | Automatically upgraded in place to next Major version |
| {{site.data.keyword.databases-for-elasticsearch}} | {{site.data.keyword.databases-for}} major versions are the first two numbers in a `release.version`.maintenance version number. |  v8.7, v8.10, v8.12, v8.15, 30 June 2026|   v8.19   | Automatically upgraded in-place to next major version. |
| {{site.data.keyword.databases-for-redis}} | {{site.data.keyword.databases-for}} major versions are the first number in a `major.minor.patch` version number. | v7.2, 30 September 2026 |   v7.2   | Automatically upgraded in place to next Major version |
| {{site.data.keyword.databases-for-postgresql}} | {{site.data.keyword.databases-for}} major version is defined by the first number in the version number. |  v14, 21 October 2026 |   v18 | Automatically upgraded in place to next major version, [Customer-initiated in-place upgrade from v14 to v15 supported](/docs/databases-for-postgresql?topic=databases-for-postgresql-upgrading&interface=ui) |
| {{site.data.keyword.databases-for-mysql}} | {{site.data.keyword.databases-for}} major versions are the first two numbers in a `major.x.patch` version number. | v8.0, July 2026 |  v8.0, v8.4 (Preview) | Backup taken and access removed |
| {{site.data.keyword.messages-for-rabbitmq}} | {{site.data.keyword.databases-for}} Major versions are the first two numbers in a `major.x.patch` version number. | v3.13, 20 May 2026, <br> v4.0(preview), 20 May 2026 <br> v4.1, (tentative 31 March 2026) |   v4.1   | Backup taken and access removed until v3.13, <br> Automatically upgraded in place to next Major version starting v4.x |
{: caption="Major versions for {{site.data.keyword.databases-for}}" caption-side="top"}

[^tabletext4]: This column describes the actions that will be taken by the {{site.data.keyword.cloud}} team on database instances that have not been upgraded to a new version prior to the version EoL date. This approach is not recommended. For more information, see [End of life procedure](#version-EOL).

### End of life procedure
{: #version-EOL}

This approach is not recommended for the following reasons:

* We provide no SLAs for this type of forced upgrade.
* Data loss may occur.
* Applications may experience downtime.
* Applications may stop working if they have any incompatibilities with the new database version.
* You cannot control the timing of the forced upgrade of your instances.
* There is no rollback process for forced upgrades.
* We strongly recommend upgrading {{site.data.keyword.databases-for}} instances to the latest version available as soon as possible after that version is made available.

Additional information on upgrade methods for each database type:

- [Upgrading {{site.data.keyword.databases-for-mongodb}} major versions](/docs/databases-for-mongodb?topic=databases-for-mongodb-upgrading&interface=ui)
- [Upgrading {{site.data.keyword.databases-for-elasticsearch}} major versions](/docs/databases-for-elasticsearch?topic=databases-for-elasticsearch-upgrading&interface=ui)
- [Upgrading {{site.data.keyword.databases-for-redis}} major versions](/docs/databases-for-redis?topic=databases-for-redis-upgrading&interface=ui)
- [Upgrading {{site.data.keyword.databases-for-postgresql}} major versions](/docs/databases-for-postgresql?topic=databases-for-postgresql-upgrading&interface=ui)
- [Upgrading {{site.data.keyword.databases-for-mysql}} major versions](/docs/databases-for-mysql?topic=databases-for-mysql-mysql-upgrading&interface=cli) 
- [Upgrading {{site.data.keyword.messages-for-rabbitmq}} major versions](/docs/messages-for-rabbitmq?topic=messages-for-rabbitmq-upgrading&interface=ui))

## Subscribe for version updates
{: #version-updates-subscribe}

Availability of a new major database version in {{site.data.keyword.cloud_notm}} is communicated via the release notes and [{{site.data.keyword.cloud_notm}} status page](https://cloud.ibm.com/status){: external}. Set up {{site.data.keyword.cloud_notm}} status notifications, as described in the [documentation](/docs/cloud-databases?topic=cloud-databases-getting-started-cdb-setup-notifs), in order to receive a notification when new release notes are published. 

## Major version end of life procedures
{: #version-deprecation}

End of life dates for major database versions in {{site.data.keyword.databases-for}} are determined after considering two primary factors. 

1. The date when the open-source community or vendor that provides the database stops maintaining that version.
2. Industry best practices for security that generally prohibit the use of software that is no longer maintained because bugs and security vulnerabilities are unlikely to be addressed in such a version.

Because the frequency of major releases and the maintenance lifecycle policies associated with each database offered in the {{site.data.keyword.cloud_notm}} portfolio is different, the time between general availability of a major release in {{site.data.keyword.cloud_notm}} and the end of life for that version in {{site.data.keyword.cloud_notm}} varies across different databases and over time.  

When the {{site.data.keyword.cloud_notm}} end of life date for a major version is defined, a notification is provided via the {{site.data.keyword.cloud_notm}} status announcements page. During the time between notification and the end of life date for a major version, you are strongly advised to initiate an upgrade to the most recent major version. 

At the end of life date, any database instances that remain on the deprecated major version are handled as described in the end of life procedure column in Table 1. If the end of life procedure includes taking a backup of the instance, the backup is available to be restored into a new supported version for 30 days, after which the backup is deleted.

Requests to re-enable disabled formations of end-of-life versions are not accommodated. 

End of life procedures and related actions happen over several days following the end of life date. We try, but cannot guarantee, to complete these actions outside of business hours in the local region. If you want more control over the upgrade process of your instance, we recommend that you upgrade before the EOL date of your version.
{: note}


## Version tags
{: #version-tags}

| Version tag | Description|
|-------------|-------------|
| **Preferred** | The recommended and default version for all new instances. It's the most stable, up-to-date version from both an instance-level and service-level perspective.|
| **Preview** | A preview version is released for a limited time to try available functions. Often it is the newest available version available from the project maintainers in preparation for making it the "Preferred" version. While deployable, preview versions are not suitable for production, as they are excluded from service-level agreements and support. Also, a preview version isn't guaranteed to become a production-level release. IBM reserves the right to ask a customer to delete an instance that uses a preview version. |
| **Deprecated** | Old versions and versions near their end of life dates are marked as "Deprecated". Provisions and restores of instances that run a deprecated version are still available and instances that run a deprecated version continue to be supported. However, you are encouraged to upgrade to the new "Preferred" version as deprecated versions are eventually removed from {{site.data.keyword.cloud_notm}} and are no longer provisionable, restorable, or supported.  |
| **Untagged** | Untagged versions are fully supported and deployable versions. They are usually slightly older than the current preferred version, but they are still supported by the project maintainers. They continue to be supported on {{site.data.keyword.databases-for}} instances until their deprecation is announced.|
| **Hidden** | A hidden version cannot be provisioned. Existing instances that are using a version marked as hidden are still able to be restored to the hidden version. |
{: caption="{{site.data.keyword.databases-for}} version tags" caption-side="bottom"}

## Minor versions
{: #minor-versions}

{{site.data.keyword.cloud_notm}} is committed to providing secure, up-to-date versions of services. As updates are released by project maintainers, they are tested, evaluated, and released to {{site.data.keyword.databases-for}} instances. Your instance's minor version and patch updates are handled automatically and are not user configurable.

## Major versioning end of life notification
{: #-major-version-eol}

The ability to provide advance notification of the end of lifedate for major database versions to IBM Cloud Database users is limited by the advance notice provided by the associated open-source community or vendor with respect to the date that maintenance of a version will end. 

For those databases where the open-source community or vendor provides advance notice of the end of maintenance date for major versions, multiple notifications will be sent to inform users of upcoming end of life dates. You can typically expect:

1. A Cloud status page announcement, for example: [End of support notices](https://cloud.ibm.com/status/announcement?query=End+of+Support+Notices){: external}.
2. An announcement in your service's Release Notes, for example: [IBM Cloud® Databases for PostgreSQL version 12 end of life on January 22, 2025](https://cloud.ibm.com/docs/databases-for-postgresql?topic=databases-for-postgresql-postgresql-relnotes#databases-for-postgresql-18jan2023){: external}.
3. A notification by email if account notification have been correctly configured to include email addresses. This email contains a *Notifications* link that takes you to a Notifications Management page. **Make sure that these announcements are not being caught by your email service's spam filter.** For more information, see [Setting up distribution lists for IBM Cloud notifications](https://cloud.ibm.com/docs/account?topic=account-add-users-distribution-list)){:external} and [Setting email preferences for notifications](https://cloud.ibm.com/user/notifications).

Ensure that your account is enabled to receive notifications and announcements. You must enable receipt of both platform and resource updates.  

* Turn on major and minor toggle under the **Platform tab > Announcements > Major and minor**.
* Turn on service updates under the **Resource tab > Resource activity > Service updates**.  

Customers are also encouraged to proactively check the database version status of all IBM Cloud Database instances programmatically via either the CLI or API. For more information, see [Programmatic methods for checking version status](https://cloud.ibm.com/docs/cloud-databases?topic=cloud-databases-versioning-policy#-major-version-eol-check-version-status). 

### Database pecific information
{: #-database-specific-information}

**[IBM Cloud Databases for Elasticsearch]**

Elastic publishes the maintenance policy for Elasticsearch versions [here](https://www.elastic.co/support/eol). According to this policy, three versions are maintained by Elastic at any point in time, the most recent release (X.Y), the previous release (X.Y-1), and the last release for the previous major version (X-1.last, 8.19 for example). When a new release is made (X.Y+1), maintenance for release X.Y-1 ends immediately.  
Customers can choose between two approaches to upgrading the Elasticsearch versions they use. The first approach is to always upgrade to the latest Elasticsearch version soon after it is released, making the frequency of upgrades equal to the frequency of releases by Elastic. The second approach is to stay on the last release of the previous major version as long as it continues to be maintained by Elastic in order to reduce the frequency of required version upgrades during that period. 
An IBM Cloud notification will be sent shortly after each Elasticsearch major version release communicating that Elastic maintenance has ended for an additional major version and that this major version will reach end of life in IBM Cloud Databases in 5 weeks. 

**[IBM Cloud Messages for RabbitMQ]**

Only the latest major version of RabbitMQ is maintained by the community. When a new release happens, maintenance of the previous release ends. When maintenance of a RabbitMQ version ends, a single notification will be sent soon after communicating that that version will reach end of life in IBM Cloud Messages for RabbitMQ in 2 months. 


### Programmatic methods for checking version status
{: #-major-version-eol-check-version-status}

**On the CLI** the following [{{site.data.keyword.databases-for}} `deployables-show` command](/docs/cloud-databases?topic=cloud-databases-cdb-reference#deployables-show) shows deployable service types, specifically the available versions and their `preferred` or `stable` status.

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
