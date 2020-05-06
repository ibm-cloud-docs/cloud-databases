---
copyright:
  years: 2019, 2020
lastupdated: "2020-03-26"

subcollection: cloud-databases, bring you own key, byok, cryptoshredding

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:important: .important}

# Key Protect Integration
{: #key-protect}

The data that you store in {{site.data.keyword.cloud}} Databases is encrypted by default by using randomly generated keys. If you need to control the encryption keys, you can use [{{site.data.keyword.keymanagementservicelong_notm}}](/docs/key-protect?topic=key-protect-integrate-services) to create, add, and manage encryption keys. Then, you can associate those keys with your {{site.data.keyword.databases-for}} deployment to encrypt your databases.

To get started, you need [{{site.data.keyword.keymanagementserviceshort}}](https://{DomainName}/catalog/key-protect) provisioned on your {{site.data.keyword.cloud_notm}} account.

## Creating or adding a key in {{site.data.keyword.keymanagementserviceshort}}

Navigate to your instance of {{site.data.keyword.keymanagementserviceshort}} and [generate or enter a key](/docs/key-protect?topic=key-protect-getting-started-tutorial).

## Granting service authorization

Authorize {{site.data.keyword.keymanagementserviceshort}} for use with {{site.data.keyword.databases-for}} deployments:

1. Open your {{site.data.keyword.cloud_notm}} dashboard.
2. From the menu bar, click **Manage** &gt; **Access (IAM)**.
3. In the side navigation, click **Authorizations**.
4. Click **Create**.
5. In the **Source service** menu, select the service of the deployment. For example, **Databases for PostgreSQL** or **Messages for RabbitMQ**
6. In the **Source service instance** menu, select **All service instances**.
7. In the **Target service** menu, select **Key Protect**.
8. In the **Target service instance** menu, select the service instance to authorize.
9. Enable the **Reader** role.
10. Click **Authorize**.

## Using the Key Protect Key

Once you grant your {{site.data.keyword.databases-for}} deployments permission to use your keys, you supply the [key name or CRN](/docs/key-protect?topic=key-protect-view-keys) when you provision a deployment. The deployment uses your encryption key to encrypt your data.

If you provision a deployment through the CLI or API, the key protect key needs to be identified by its full CRN, not just its ID. A key protect CRN is in the format `crn:v1:<...>:key:<id>`.
{: .tip}

## Deleting the Deployment

If you delete a deployment that is protected with a Key Protect key, the deployment remains registered against the key for the duration of the soft-deletion period (up to 9 days). If you need to delete the key in the soft-deletion period, you have to [force delete](/docs/key-protect?topic=key-protect-delete-keys) the key. After the soft-deletion period the key can be deleted without the force. You can check the [association between the key and your deployment](/docs/key-protect?topic=key-protect-view-protected-resources) to determine when you can delete the key.

## Cryptoshredding

Cryptoshredding is a destructive action. Once the key is deleted your data is unrecoverable.
{: .important}

{{site.data.keyword.keymanagementserviceshort}} allows you to [initiate a force delete](/docs/key-protect?topic=key-protect-delete-keys) of a key that is in use by {{site.data.keyword.cloud}} services, including your {{site.data.keyword.databases-for}} deployments. This action is called cryptoshredding. Deleting a key that is in use on your deployment locks the disks containing your data and disables your deployment. You are still able to access the UI and some metadata such as security settings in the UI, CLI, and API but you are not able to access any of the databases or data contained within them. Key deletion is [sent to the LogDNA Activity Tracker](/docs/key-protect?topic=key-protect-at-events) as `kms.secrets.delete`.

## BYOK for backups

If you use Key Protect, you can also designate a key to encrypt the Cloud-Object Storage disk that holds your deployment's backups.

Things to Note - 
- BYOK for backups is only available in US regions `us-south` and `us-east`.
- Keys for Backups keys are not region-locked. You can use a key from any region, to encrypt the backups of your deployment in `us-south` or `us-east`.
- While backups are normally cross-region and thus resilient to regional failures, Key Protect keys are not. If the region that hosts your key for backups goes down, then you lose access to your backups. Choose a deployment and a key that are in different regions so that a single region failure does not take out both your deployment and your backups.

In order to enable your deployment to use the Key Protect key, you need to [Enable authorization to be delegated](/docs/iam?topic=iam-serviceauth) when granting the service authorizations. Then, when you provision your deployment through the CLI with the `backup_encryption_key_crn` parameter,
```
ibmcloud resource service-instance-create example-database <service-name> standard us-south \
-p \ '{
  "backup_encryption_key_crn": "crn:v1:<...>:key:<id>"
}'
```

Or through API with the `backup_encryption_key_crn` parameter.
```
curl -X POST \
  https://resource-controller.cloud.ibm.com/v2/resource_instances \
  -H 'Authorization: Bearer <>' \
  -H 'Content-Type: application/json' \
    -d '{
    "name": "my-instance",
    "target": "bluemix-us-south",
    "resource_group": "5g9f447903254bb58972a2f3f5a4c711",
    "resource_plan_id": "databases-for-x-standard",
    "backup_encryption_key_crn": "crn:v1:<...>:key:<id>"
  }'

After you have enabled delegation and provisioned your deployment, two entries appear in your _Authorizations_ in IAM. One is the entry for the deployment which lists its status as delegator. It is "User Created".

Role | Source | Target | Type
-----|-----|-----|-----
AuthorizationDelegator, Reader | `<cloud-databases>` service | Key Protect Service | User defined
{: caption="Table 1. Example delegator Key Protect Authorization " caption-side="top"}

And one for the COS bucket for its backups, where the deployment is the initiator.

Role | Source | Target | Type
-----|-----|-----|-----
Reader | Cloud Object Storage service | Key Protect Service | created by `<cloud-databases-crn>`
{: caption="Table 2. Example Key Protect Authorization for COS from Cloud Databases " caption-side="top"}

IAM/Key Protect does not stop you from removing the policy between the key and Cloud Object Storage (the second example), but doing so can make your backups unrestorable. To prevent this, if you delete the COS policy that governs the ability of Cloud Databases to use the key for COS, the policy will be recreated to continue backing up your deployment.

If you want to remove the policy (and effectively cryptoshred your backups), you should remove the Cloud Databases delegator authorization (the first example), which revokes Cloud Databases ability to use the key for COS.


