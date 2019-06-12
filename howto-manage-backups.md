---

copyright:
  years: 2019
lastupdated: "2019-06-12"

subcollection: cloud-databases

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Managing Backups
{: #dashboard-backups}

{{site.data.keyword.databases-for-postgresql_full}} backups are accessible from the _Backups_ tab of your service dashboard. 

Daily and on-demand backups are available for 30 days. Backups cannot be deleted. If you delete your deployment backups are deleted automatically after their 30-day retention period. 

Each backup is labeled with its type, and when the backup was taken. Click the timestamp to change it's format between elapsed time, local time, and UTC. Click the backup to reveal information for that specific backup, including its full ID. For restore options, there is a  button to restore the backup or a pre-formatted CLI command. 

You can also access the list of backups and individual backup information from the {{site.data.keyword.databases-for}} CLI plugin and the {{site.data.keyword.databases-for}} API.

Use the `cdb deployment-backups-list` command to view the list of all available backups for your deployment. To get the details about a specific backup, use `cdb backup-show` command.

For example, to view the backups for a deployment named "example-deployment", use the following command.

```
ibmcloud cdb deployment-backups-list example-deployment
```

To see the details of one of the backups from the list, take the ID from the `ID` field of the `deployment-backups-list` command's response and use it with the `backup-show` command.

```
ibmcloud cdb backup-show crn:v1:staging:public:databases-for-postgresql:us-south:a/6284014dd5b487c87a716f48aeeaf99f:3b4537bf-a585-4594-8262-2b1e24e2701e:backup:a3364821-d061-413f-a0df-6ba0e2951566
```

In the {{site.data.keyword.databases-for}} API, use the [`/backups`](https://{DomainName}/apidocs/cloud-databases-api#get-information-about-a-backup) endpoint.





## Restoring a Backup

Backups are restored to a new deployment. The new deployment is auto-sized to the same disk and memory allocation as the source deployment at the time of the backup you are restoring from. After the new deployment finishes provisioning, your data in the backup file is restored into the new deployment.

## Restoring a Backup in the UI

To restore a backup to a new service instance,

1. Click in the corresponding row to expand the options for the backup you want to restore.
2. Click the **Restore** button.  A message is displayed that a restore from backup has started. Clicking on **Your new instance is available now.** will take you to your _Resources List_.

The new service instance is automatically named "postgres-restore-[timestamp]", and appears on your {{site.data.keyword.cloud_notm}} dashboard when provisioning starts.

### Restoring a Backup in the CLI

The Resource Controller supports provisioning  of database deployments, and provisioning and restoring are the responsibility of the Resource Controller CLI. Use the [`resource service-instance-create`]() command.

```
ibmcloud resource service-instance-create <SERVICE_INSTANCE_NAME> <service-id> <region> -p '{"backup_id":"BACKUP_ID"}'
```

Change the value of `SERVICE_INSTANCE_NAME` to the name you want for your new deployment, `region` is where you want the service to be located, and `BACKUP_ID` is the backup you want to restore.

A pre-formatted command for a specific backup is available in detailed view of the backup on the _Backups_ tab of the service dashboard.
{: .tip}

### Restoring a Backup through the API



### Major Version Upgrades and Cross-Region Restores


## Backups and Restoration

* {{site.data.keyword.cloud_notm}} Databases is not responsible for restoration, timeliness, or validity of said backups.
* Actions that you take as a user can compromise the integrity of backups, such as under-allocating memory and disk. Users can monitor that backups were performed successfully via the API, and periodically restore a backup to ensure validity and integrity. Users can retrieve the most recent scheduled backup details from the IBM Cloud Databases plug-in: `ibmcloud cdb backups deploymentname -s -f`.
* As a managed service {{site.data.keyword.cloud_notm}} Databases monitors the state of your backups and can attempt to remediate when possible. If you encounter issues you cannot recover from, you can contact support for additional help.
