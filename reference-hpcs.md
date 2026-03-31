---
copyright:
  years: 2020, 2026
lastupdated: "2026-03-31"

keywords: bring your own key, byok, cryptoshredding, hpcs, hyper protect crypto services, deprecation of hpcs, key protect dedicated

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# {{site.data.keyword.hscrypto}} integration
{: #hpcs}


{{site.data.keyword.cloud}} is transitioning the dedicated key management services from {{site.data.keyword.hscrypto}} to {{site.data.keyword.keymanagementservicelong}} Dedicated. Migrate existing {{site.data.keyword.hscrypto}} (HPCS) root keys to {{site.data.keyword.keymanagementservicelong}} Dedicated (Single Tenant) before HPCS End of Life (EOL) on March 20, 2027 to ensure continued service availability. After that date any remaining instances will be terminated. To ensure continued service availability and support, you must migrate all existing HPCS root keys to {{site.data.keyword.keymanagementservicelong_notm}} Dedicated (Single Tenant) before the EOL date. [Learn how to migrate your root keys](#migrating_hpcs_to_kp).
{: deprecated}

The data that you store in {{site.data.keyword.databases-for}} is encrypted by default by using randomly generated keys. If you need to control the encryption keys, you can Bring Your Own Key (BYOK) through [{{site.data.keyword.hscrypto}}](/docs/hs-crypto?topic=hs-crypto-get-started), and use one of your own keys to encrypt your databases. Take note that {{site.data.keyword.hscrypto}} for {{site.data.keyword.cloud}} Databases backups is currently not supported for the majority of regions and not recommended to be used without careful considerations of the impact to disaster recovery.

To get started, you need [{{site.data.keyword.hscrypto}}](/catalog/services/hyper-protect-crypto-services) provisioned on your {{site.data.keyword.cloud_notm}} account.

## Creating or adding a key in {{site.data.keyword.hscrypto}}
{: #create-key}

Navigate to your instance of {{site.data.keyword.hscrypto}} and [generate or enter a key](/docs/hs-crypto?topic=hs-crypto-get-started).

## Granting service authorization
{: #grant-auth}

Authorize {{site.data.keyword.hscrypto}} for use with {{site.data.keyword.databases-for}} deployments:

1. Open your {{site.data.keyword.cloud_notm}} dashboard.
2. From the menu bar, click **Manage** > **Access (IAM)**.
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

## Using the HPCS key
{: #use-hpcs}

After you grant your {{site.data.keyword.databases-for}} deployments permission to use your keys, you supply the [key name or CRN](/docs/hs-crypto?topic=hs-crypto-view-keys) when you provision a deployment. The deployment uses your encryption key to encrypt your data.

If provisioning from the catalog page, select the HPCS instance and key from the drop-down menu.

In the CLI, use the `disk_encryption_key_crn` parameter in the parameter's JSON object.

```bash
ibmcloud resource service-instance-create <INSTANCE_NAME> <SERVICE-NAME> standard us-south \
-p \ '{
  "disk_encryption_key_crn": "crn:v1:<...>:key:<id>"
}'
```
{: codeblock}

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
{: codeblock}

If you provision a deployment through the CLI or API, the HPCS key must be identified by its full CRN, not just its ID. An HPCS CRN has the format `crn:v1:<...>:key:<id>`.
{: .tip}

## Using the HPCS key for backup encryption
{: #use-hpcs-backups}

This feature is only supported in the eu-es and br-sao regions. Encrypting backups with HPCS in a single region renders the backups inaccessible, if availability of HPCS is disrupted in this region. Taking a backup and restoring from backups will fail for the period that HPCS is unavailable. Therefore, encrypting backups with HPCS is not recommended. Use {{site.data.keyword.keymanagementservicelong}} to encrypt backups.
{: .note}

If you encrypted the backup with HPCS, encrypt the disk also with HPCS.
{: .tip}

After you grant your {{site.data.keyword.databases-for}} deployments permission to use your keys, you supply the [key name or CRN](/docs/hs-crypto?topic=hs-crypto-view-keys) when you provision a deployment. The deployment uses your encryption key to encrypt your data.

If you provision from the Catalog, select the HPCS instance and key from the drop-down menu.

In the CLI, use the `backup_encryption_key_crn` parameter in the parameter's JSON object.

```bash
ibmcloud resource service-instance-create <INSTANCE_NAME> <SERVICE-NAME> standard eu-es \
-p \ '{
  "backup_encryption_key_crn": "crn:v1:<...>:key:<id>"
}'
```
{: codeblock}

In the API, use the `backup-encryption-key` parameter in the body of the request.

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
    "parameters": {
      "backup_encryption_key_crn": "crn:v1:<...>:key:<id>"
    }
  }'
```
{: codeblock}

If you provision a deployment through the CLI or API, the HPCS key must be identified by its full CRN, not just its ID. An HPCS CRN has the format `crn:v1:<...>:key:<id>`.
{: .tip}

## Key rotation
{: #hpcs-rotation}

HPCS offers manual and automatic [key rotation](/docs/hs-crypto?topic=hs-crypto-set-rotation-policy) and key rotation is supported by Cloud Databases deployments. When you rotate a key, the process initiates a _Syncing KMS state_ task, and your deployment is reencrypted with the new key. The task is displayed on the _Tasks_ panel on your deployment's _Overview_ and the associated HPCS and Cloud Databases events are sent to Activity Tracker.

## Deleting the deployment
{: #deleting-deployment}

If you delete a deployment that is protected with an HPCS key, the deployment remains registered against the key during the soft-deletion period (up to 9 days). If you need to delete the key in the soft-deletion period, you must [force delete](/docs/hs-crypto?topic=hs-crypto-delete-keys) the key. After the soft-deletion period, the key can be deleted without the force. You can check the [association between the key and your deployment](/docs/hs-crypto?topic=hs-crypto-view-key-details) to determine when you can delete the key.

## Cryptoshredding
{: #cryptoshredding}

Cryptoshredding is a destructive action. When the key is deleted, your data is unrecoverable.
{: .important}

{{site.data.keyword.hscrypto}} enables [initiation of a force delete](/docs/hs-crypto?topic=hs-crypto-delete-keys) of a key that is in use by {{site.data.keyword.cloud}} services, including your {{site.data.keyword.databases-for}} deployments. This action is called cryptoshredding. Deleting a key that is in use on your deployment locks the disks that contain your data and disables your deployment. You are still able to access the UI and some metadata such as security settings in the UI, CLI, and API but you are not able to access any of the databases or data that is contained within them. Key deletion is [sent to the {{site.data.keyword.atracker_short}}](/docs/hs-crypto?topic=hs-crypto-at-events) as `hs-crypto.secrets.delete`.

## Migrating from {{site.data.keyword.hscrypto}} (HPCS) to {{site.data.keyword.keymanagementserviceshort}} Dedicated (KP-ST)
{: #migrating_hpcs_to_kp}

During the migration from {{site.data.keyword.hscrypto}} (HPCS) to {{site.data.keyword.keymanagementserviceshort}} Dedicated (KP‑ST), the following occurs:

- Each KMS instance maintains its own unique root keys. Migration involves re‑associating the service with a new {{site.data.keyword.keymanagementserviceshort}} Dedicated root key.
- Existing data encryption keys (DEKs) are securely re‑wrapped.
- During the transition, both {{site.data.keyword.hscrypto}} to Service and {{site.data.keyword.keymanagementserviceshort}} to Service access policies must remain in place.
- Encrypted data is not re‑encrypted or moved.
- Service availability is maintained.

### Pre-requisites
{: #migrating_hpcs_to_kp_prereqs}

Before starting the migration, ensure you have:

- A {{site.data.keyword.keymanagementserviceshort}} Dedicated (Single Tenant) instance.
- A root key created in that {{site.data.keyword.keymanagementserviceshort}} Dedicated (KP‑ST) instance.
- Permissions to manage keys and service access policies.

### Migration steps
{: #migrating_hpcs_to_kp_steps}

1. Identify the existing {{site.data.keyword.hscrypto}} root key in use. The key must exist in an {{site.data.keyword.hscrypto}} instance and the service must already have access to it.
1. Create or select a {{site.data.keyword.keymanagementserviceshort}} Dedicated root key. The key must be in the appropriate {{site.data.keyword.keymanagementserviceshort}} Dedicated (Single Tenant) instance and accessible to the service.
1. Create a migration intent linking the two keys. The migration intent maps the current {{site.data.keyword.hscrypto}} key (source) to the new {{site.data.keyword.keymanagementserviceshort}} Dedicated key (target). For more information about {{site.data.keyword.keymanagementserviceshort}} migration, see [Migrating from {{site.data.keyword.hscrypto}} (HPCS) to {{site.data.keyword.keymanagementserviceshort}} Dedicated](/docs/key-protect?topic=key-protect-migrate-st#migrate-hpcs-usage).
1. Allow 1-2 business days for the migration to be executed. {{site.data.keyword.messagehub}} securely re‑associates and re-wraps DEKs where applicable, without re‑encrypting or moving data.
1. Verify migration completion. The service must now reference the {{site.data.keyword.keymanagementserviceshort}} Single Tenant root key. {{site.data.keyword.keymanagementserviceshort}} Single Tenant root key should be visible and active and the {{site.data.keyword.hscrypto}} association should be removed.
