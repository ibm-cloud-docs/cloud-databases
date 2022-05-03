---
copyright:
  years: 2020, 2022
lastupdated: "2022-04-06"

keywords: bring your own key, byok, cryptoshredding, hpcs, hyper protect crypto services

subcollection: cloud-databases

---

{:shortdesc: .shortdesc}
{:external: .external target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:note: .note}
{:important: .important}

# Hyper Protect Crypto Services Integration
{: #hpcs}

The data that you store in {{site.data.keyword.cloud}} Databases is encrypted by default by using randomly generated keys. If you need to control the encryption keys, you can Bring Your Own Key (BYOK) through [{{site.data.keyword.hscrypto}}](/docs/hs-crypto?topic=hs-crypto-get-started), and use one of your own keys to encrypt your databases. Take note that {{site.data.keyword.hscrypto}} for {{site.data.keyword.cloud}} Databases backups is not currently supported. 

This document covers the integration of {{site.data.keyword.hscrypto}} (HPCS) with Cloud Databases, which includes {{site.data.keyword.databases-for-cassandra}},{{site.data.keyword.databases-for-elasticsearch}}, {{site.data.keyword.databases-for-enterprisedb}}, {{site.data.keyword.databases-for-etcd}}, {{site.data.keyword.databases-for-mongodb}}, {{site.data.keyword.databases-for-postgresql}}, {{site.data.keyword.databases-for-redis}}, {{site.data.keyword.databases-for-mysql_full}}, and {{site.data.keyword.messages-for-rabbitmq}}.
{: .note}

To get started, you need [{{site.data.keyword.hscrypto}}](/catalog/services/hyper-protect-crypto-services) provisioned on your {{site.data.keyword.cloud_notm}} account. 

## {{site.data.keyword.hscrypto}} versus {{site.data.keyword.keymanagementserviceshort}}
{: #hpcs-key-protect}

{{site.data.keyword.hscrypto}} is a dedicated key management service and hardware security module (HSM){: term} based on {{site.data.keyword.cloud_notm}}. With this service, you can take the ownership of the cloud HSM to fully manage your encryption keys and to perform cryptographic operations. {{site.data.keyword.hscrypto}} is also the only service in the cloud industry that is built on FIPS 140-2 Level 4-certified hardware.
For more information, check out {{site.data.keyword.hscrypto}}'s [documentation](/docs/hs-crypto?topic=hs-crypto-get-started).

{{site.data.keyword.keymanagementservicefull}} is a full-service encryption solution that allows data to be secured and stored in {{site.data.keyword.cloud_notm}} using the latest envelope encryption techniques that leverage FIPS 140-2 Level 3 certified cloud-based hardware security modules.
For more information, check out {{site.data.keyword.keymanagementservicefull}}'s [documentation](/key-protect?topic=key-protect-about).

## Creating or adding a key in {{site.data.keyword.hscrypto}}
{: #create-key}

Navigate to your instance of {{site.data.keyword.hscrypto}} and [generate or enter a key](/docs/hs-crypto?topic=hs-crypto-get-started).

## Granting service authorization
{: #grant-auth}

Authorize {{site.data.keyword.hscrypto}} for use with {{site.data.keyword.databases-for}} deployments:

1. Open your {{site.data.keyword.cloud_notm}} dashboard.
2. From the menu bar, click **Manage** &gt; **Access (IAM)**.
3. In the side navigation, click **Authorizations**.
4. Click **Create**.
5. In the **Source service** menu, select the service of the deployment. For example, **Databases for PostgreSQL** or **Messages for RabbitMQ**
6. In the **Source service instance** menu, select **All instances**.
7. In the **Target service** menu, select **HPCS**.
8. Select or retain the default value **`Account`** as the resource group for the **Target Service**
9. In the Target service **Instance ID** menu, select the service instances to authorize.
10. Enable the **Reader** role.
11. Click **Authorize**.

If the service authorization is not present before provisioning your deployment with a key, the provision fails.

## Using the HPCS Key
{: #use-hpcs}

After you grant your {{site.data.keyword.databases-for}} deployments permission to use your keys, you supply the [key name or CRN](/docs/hs-crypto?topic=hs-crypto-view-keys) when you provision a deployment. The deployment uses your encryption key to encrypt your data.

If provisioning from the catalog page, select the HPCS instance and key from the dropdown menus.

In the CLI, use the `disk_encryption_key_crn` parameter in the parameters JSON object.
```bash
ibmcloud resource service-instance-create example-database <service-name> standard us-south \
-p \ '{
  "disk_encryption_key_crn": "crn:v1:<...>:key:<id>"
}'
```

In the API, use the `disk-encryption-key` parameter in the body of the request.
```curl
curl -X POST \
  https://resource-controller.cloud.ibm.com/v2/resource_instances \
  -H 'Authorization: Bearer <>' \
  -H 'Content-Type: application/json' \
    -d '{
    "name": "my-instance",
    "target": "blue-us-south",
    "resource_group": "5g9f447903254bb58972a2f3f5a4c711",
    "resource_plan_id": "databases-for-x-standard",
    "disk_encryption_key_crn": "crn:v1:<...>:key:<id>"
  }'
```

If you provision a deployment through the CLI or API, the HPCS key needs to be identified by its full CRN, not just its ID. An HPCS CRN is in the format `crn:v1:<...>:key:<id>`.
{: .tip}

## Key Rotation
{: #hpcs-rotation}

HPCS offers manual and automatic [key rotation](/docs/hs-crypto?topic=hs-crypto-set-rotation-policy) and key rotation is supported by Cloud Databases deployments. When you rotate a key, the process initiates a _Syncing KMS state_ task, and your deployment is reencrypted with the new key. The task is displayed on the _Tasks_ panel on your deployment's _Overview_ and the associated HPCS and Cloud Databases events are sent to Activity Tracker.

## Deleting the Deployment
{: #deleting-deployment}

If you delete a deployment that is protected with an HPCS key, the deployment remains registered against the key during the soft-deletion period (up to 9 days). If you need to delete the key in the soft-deletion period, you must [force delete](/docs/hs-crypto?topic=hs-crypto-delete-keys) the key. After the soft-deletion period, the key can be deleted without the force. You can check the [association between the key and your deployment](/docs/hs-crypto?topic=hs-crypto-view-key-details) to determine when you can delete the key.

## Cryptoshredding
{: #cryptoshredding}

Cryptoshredding is a destructive action. When the key is deleted, your data is unrecoverable.
{: .important}

{{site.data.keyword.hscrypto}} enables [initiation of a force delete](/docs/hs-crypto?topic=hs-crypto-delete-keys) of a key that is in use by {{site.data.keyword.cloud}} services, including your {{site.data.keyword.databases-for}} deployments. This action is called cryptoshredding. Deleting a key that is in use on your deployment locks the disks that contain your data and disables your deployment. You are still able to access the UI and some metadata such as security settings in the UI, CLI, and API but you are not able to access any of the databases or data that is contained within them. Key deletion is [sent to the {{site.data.keyword.at_short}}](/docs/hs-crypto?topic=hs-crypto-at-events) as `hs-crypto.secrets.delete`.


