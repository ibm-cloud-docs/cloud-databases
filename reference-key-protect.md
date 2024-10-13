---
copyright:
  years: 2019, 2024
lastupdated: "2024-07-26"

subcollection: cloud-databases

keywords: bring your own key, byok, cryptoshredding, key rotation, key rotation frequency, bring your own key

---

{{site.data.keyword.attribute-definition-list}}

# Key Protect integration
{: #key-protect}

The data that you store in {{site.data.keyword.cloud}} Databases is encrypted by default by using randomly generated keys. To control the encryption keys, you can Bring Your Own Key (BYOK) through [{{site.data.keyword.keymanagementservicelong_notm}}](/docs/key-protect?topic=key-protect-integrate-services) and use one of your own keys to encrypt your databases and backups.

This document covers the integration of Key Protect with Cloud Databases, which includes {{site.data.keyword.databases-for-postgresql}}, {{site.data.keyword.databases-for-mongodb}}, {{site.data.keyword.databases-for-redis}}, {{site.data.keyword.databases-for-elasticsearch}}, {{site.data.keyword.databases-for-mysql_full}}, {{site.data.keyword.messages-for-rabbitmq}}, {{site.data.keyword.databases-for-enterprisedb}} and {{site.data.keyword.databases-for-etcd}}.
{: .note}

To get started, you need [{{site.data.keyword.keymanagementserviceshort}}](https://{DomainName}/catalog/key-protect) provisioned on your {{site.data.keyword.cloud_notm}} account.

## Creating or adding a key in {{site.data.keyword.keymanagementserviceshort}}
{: #key-create}

Go to your instance of {{site.data.keyword.keymanagementserviceshort}} and [generate or enter a key](/docs/key-protect?topic=key-protect-getting-started-tutorial).

## Granting service authorization in the UI
{: #granting-service-auth}
{: ui}

Authorize {{site.data.keyword.keymanagementserviceshort}} for use with {{site.data.keyword.databases-for}} deployments:

1. Open your {{site.data.keyword.cloud_notm}} dashboard.
2. From the menu bar, click **Manage** -> **Access (IAM)**.
3. In the side navigation, click **Authorizations**.
4. Click **Create**.
5. In the **Source service** menu, select the service of the deployment. For example, **Databases for PostgreSQL** or **Messages for RabbitMQ**
6. In the **Source service resources** menu, select **All resources**.
7. In the **Target service** menu, select **Key Protect**.
8. Select or retain the default value **Account** as the resource group for the **Target Service**
9. In the Target service **Instance ID** menu, select the service instances to authorize.
10. Enable the **Reader** role.
11. To use "Bring your own key" (BYOK) for backups, Select the **Enable authorizations to be delegated** box in the **Authorize dependent services** section.  
12. Click **Authorize**.

If the service authorization is not present before provisioning your deployment with a key, the provision fails.

## Using the Key Protect key
{: #key-using}

After you grant your {{site.data.keyword.databases-for}} deployments permission to use your keys, you supply the [key name or CRN](/docs/key-protect?topic=key-protect-view-keys) when you provision a deployment. The deployment uses your encryption key to encrypt your data.

## Using the Key Protect key in the UI
{: #key-using-ui}
{: ui}

If provisioning from the catalog page, select the Key Protect instance and key from the dropdown menus.

## Using the Key Protect key in the CLI
{: #key-using-cli}
{: cli}

In the CLI, use the `disk_encryption_key_crn` parameter in the parameters JSON object.
```sh
ibmcloud resource service-instance-create <INSTANCE_NAME> <SERVICE-NAME> standard us-south \
-p \ '{
  "disk_encryption_key_crn": "crn:v1:<...>:key:<id>"
}'
```

The Key Protect key needs to be identified by its full CRN, not just its ID. A key protect CRN is in the format `crn:v1:<...>:key:<id>`.
{: .tip}

## Using the Key Protect key in the API
{: #key-using-api}
{: api}

In the API, use the `disk_encryption_key` parameter in the body of the request.
```sh
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

The Key Protect key needs to be identified by its full CRN, not just its ID. A key protect CRN is in the format `crn:v1:<...>:key:<id>`.
{: .tip}

## Key rotation
{: #keyrotation}

Key Protect offers manual and automatic [key rotation](/docs/key-protect?topic=key-protect-rotate-keys) and key rotation is supported by Cloud Databases deployments. When you rotate a key, the process initiates a _syncing KMS state_ task, and your deployment is reencrypted with the new key. The task is displayed on the _Tasks_ page on your deployment's _Overview_ and the associated Key Protect and Cloud Databases events are sent to Activity Tracker.

For more information, see [Rotating manually or automatically](/docs/key-protect?topic=key-protect-key-rotation#compare-key-rotation-options).

## Deleting the deployment
{: #key-protect-deleting-deployment}

If you delete a deployment that is protected with a Key Protect key, the deployment remains registered against the key during the soft-deletion period (up to 9 days). To delete the key in the soft-deletion period, [force delete](/docs/key-protect?topic=key-protect-delete-keys) the key. After the soft-deletion period, the key can be deleted without the force. To determine when you can delete the key, check the [association between the key and your deployment](/docs/key-protect?topic=key-protect-view-protected-resources).

## Cryptoshredding
{: #crypto-shredding}

Cryptoshredding is a destructive action. When the key is deleted, your data is unrecoverable.
{: .important}

{{site.data.keyword.keymanagementserviceshort}} allows you to [initiate a force delete](/docs/key-protect?topic=key-protect-delete-keys) of a key that is in use by {{site.data.keyword.cloud}} services, including your {{site.data.keyword.databases-for}} deployments. This action is called cryptoshredding. Deleting a key that is in use on your deployment locks the disks that contain your data and disables your deployment. You are still able to access the UI and some metadata such as security settings in the UI, CLI, and API but you are not able to access any of the databases or data that is contained within them. Key deletion is [sent to the {{site.data.keyword.at_short}}](/docs/key-protect?topic=key-protect-at-events) as `kms.secrets.delete`.

## Bring your own key for backups
{: #key-byok}

If you use Key Protect, when you provision a database you can also designate a key to encrypt the Cloud Object Storage disk that holds your deployment's backups. 

BYOK for backups is available only in US regions `us-south` and `us-east`, and `eu-de`.
{: .note}

Only keys in the `us-south` and `eu-de` are durable to region failures. To ensure that your backups are available even if a region failure occurs, you must use a key from `us-south` or `eu-de`, regardless of your deployment's location.
{: .important}

### Granting the delegation authorization
{: #grant-auth}

To enable your deployment to use the Key Protect key, you need to [Enable authorization to be delegated](/docs/account?topic=account-serviceauth) when granting the service authorizations. If the delegation authorization is not present before provisioning your deployment with a key, the provision fails.

### Using the key at provision in the CLI
{: #key-provision-cli}
{: cli}

After the appropriate authorization and delegation is granted, you supply the [key name or CRN](/docs/key-protect?topic=key-protect-view-keys) when you provision a deployment.

In the CLI, use the `backup_encryption_key_crn` parameter in the parameters JSON object.
```sh
ibmcloud resource service-instance-create <INSTANCE_NAME> <SERVICE-NAME> standard us-south \
-p \ '{
  "backup_encryption_key_crn": "crn:v1:<...>:key:<id>"
}'
```

### Using the key at provision in the API
{: #key-provision-api}
{: api}

In the API, use the `backup_encryption_key_crn` parameter in the body of the request.
```sh
curl -X POST \
  https://resource-controller.cloud.ibm.com/v2/resource_instances \
  -H 'Authorization: Bearer <>' \
  -H 'Content-Type: application/json' \
    -d '{
    "name": "my-instance",
    "target": "blue-us-south",
    "resource_group": "5g9f447903254bb58972a2f3f5a4c711",
    "resource_plan_id": "databases-for-x-standard",
    "backup_encryption_key_crn": "crn:v1:<...>:key:<id>"
  }'
```

After you enable delegation and provisioned your deployment, two entries appear in your _Authorizations_ in IAM. One is the entry for the deployment that lists its status as delegator. It is "User Created".

| Role | Source | Target | Type |
| -----|-----|-----|----- |
| AuthorizationDelegator, Reader | `<cloud-databases>` Service | Key Protect Service | User defined |
{: caption="Example delegator Key Protect Authorization " caption-side="bottom"}

And one for the Cloud Object Storage bucket for its backups, where the deployment is the initiator.

| Role | Source | Target | Type |
| -----|-----|-----|----- |
| Reader | Cloud Object Storage service | Key Protect Service | Created by `<cloud-databases-crn>` |
{: caption="Example Key Protect Authorization for Cloud Object Storage from Cloud Databases " caption-side="bottom"}

### Removing keys
{: #key-remove}

IAM/Key Protect does not stop you from removing the policy between the key and Cloud Object Storage (the second example), but doing so can make your backups unrestorable. To prevent this, if you delete the Cloud Object Storage policy that governs the ability of Cloud Databases to use the key for Cloud Object Storage, the policy is re-created to continue backing up your deployment.

Be careful when removing keys and authorizations. If you have multiple deployments that use the same keys, it is possible to inadvertently destroy backups to **all** of those deployments by revoking the delegation authorization. If possible, do not use the same key for multiple deployment's backups.

If you want to shred the backups, you can delete the key. Cloud Object Storage ensures that the storage is unreadable and unwriteable. However, any other deployments that use that same key for backups encounter subsequent backup failures.

If you do require that the same key to be used for multiple deployment's backups, removing keys and authorizations can have the following side effects.
- If you delete just the Cloud Object Storage authorization (as seen in Table 2), then not only is the deployment that is shown as the creator affected, but any deployments that also use the same key are also affected. Those deployments can encounter temporary backup failures until the policy is automatically re-created. There should be no lasting effects, except for missing backups.
- If you delete just Cloud Databases delegator authorization, which is created by you (as seen in Table 1), nothing immediately breaks because the second authorization is still in place. However, if the Cloud Object Storage authorization is ever removed, it cannot be re-created, and can lead to multiple deployments that use the same key losing the ability to back up.
- If you delete both the Cloud Object Storage authorization **AND** the Cloud Databases delegator authorization, all deployments that use the same key will immediately not have the ability to back up and the correct authorizations will not be able to be re-created, effectively destroying the backups for all deployments that use that key.

Use caution if you reuse keys.
{: .important}
