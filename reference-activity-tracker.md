---
copyright:
  years: 2019, 2023
lastupdated: "2023-10-31"

subcollection: cloud-databases

keywords: events, auditing, activity tracker, auditing

---

{{site.data.keyword.attribute-definition-list}}

# Activity Tracker Integration
{: #activity-tracker}

{{site.data.keyword.cloud_notm}} Databases instances are integrated with Activity Tracker events in [{{site.data.keyword.at_full}}](/docs/activity-tracker?topic=activity-tracker-getting-started), so you can view service-level events.

Currently, {{site.data.keyword.at_short}} integration is available for {{site.data.keyword.databases-for}} instances according to the following table. 

| Deployment Region | Activity Tracker Region |
| ----------|----------- |
| `us-south` | `us-south` |
| `jp-tok` | `jp-tok` |
| `jp-osa` | `jp-tok` |
| `eu-gb` | `eu-gb` |
| `che01` | `che01` |
| `eu-de` | `eu-de` |
| `au-syd` | `au-syd` |
| `us-east` | `us-east` |
| `ca-tor` | `ca-tor` |
| `par01` | `eu-de` |
| `eu-es` | `eu-de` |
{: caption="Table 1. Activity Tracker regions" caption-side="bottom"}

Events from your instances appear in an Activity Tracker instance in the same region, except for `jp-osa` and `eu-es`. Events for instances in `jp-osa` are forwarded to `jp-tok` and events for `eu-es` are forwarded to `eu-de`. If you have instances in multiple regions, you must set up the {{site.data.keyword.at_short}} in multiple regions. 

## Activity Tracker
{: #activity-tracker-provision}

When you provision the service, events are automatically forwarded from all your {{site.data.keyword.databases-for}} instances in the same region.

The service can be provisioned from [its catalog page](/catalog/ibm-cloud-activity-tracker) or from an existing [Observability Dashboard](https://cloud.ibm.com/observe/activitytracker).

The {{site.data.keyword.at_short}} service has a lite plan that is free to use, but it only offers streaming events. To take advantage of the tagging, export, retention, and other features, you need to use one of the [paid plans](/docs/activity-tracker?topic=activity-tracker-service_plan).

### Using the Activity Tracker
{: #using-activity-tracker}

You can access {{site.data.keyword.at_short}} through the _Observability_ tab of your instance's _Manage_ page. The **Manage Activity Tracker** button links to the main list of all {{site.data.keyword.at_short}} instances in your {{site.data.keyword.cloud_notm}} account. Select the instance where you set your database logs to be forwarded. Click **View Activity Tracker** to view the events.

After event activity is being forwarded to the service, each event can be expanded to a detailed view by clicking the arrow to the left of the timestamp.

When reviewing Activity Tracker logs, you see `denies` that include the `dry_run` tag. These `denies` are marked with a `true` or `false` value. 
- Events with `dry_run: false` indicate an attempt to run an action. 
- Events with `dry_run: true` indicate an attempt to determine support for an action without triggering that action to occur. Such `dry_run` attempts can occur as the service instance management console determines the features to which a logged-in user has access.

The {{site.data.keyword.at_short}} service offers [searching](/docs/activity-tracker?topic=activity-tracker-view_events#view_events_step2), [filtering](/docs/activity-tracker?topic=activity-tracker-view_events#view_events_step3), and [export](/docs/activity-tracker?topic=activity-tracker-export) of events so you can customize retention for your use-case. You can also use it to configure [alerts](/docs/activity-tracker?topic=activity-tracker-alerts).

We recommend alerting on database lifecycle events, such as failed backups. For example, you can create that Activity Tracker alert by filtering audit events to `outcome:failure action:"<service_id>.deployment-backup-scheduled.create"` and then following the alert configuration instructions. 
{: .tip}

## Event Fields
{: #event-fields}

A description of the common fields for an {{site.data.keyword.at_short}} event is on the [event fields](/docs/activity-tracker?topic=activity-tracker-event) page.

## List of Events
{: #list-of-events}

The table lists the events that are sent to {{site.data.keyword.at_short}} from {{site.data.keyword.databases-for}} instances.

A new auditing message format has been released and the legacy format for events that are submitted to your Activity Tracker instances will be deprecated. Deprecated events, and their analogous new events, are listed in the table. You should update any alerting or tools that rely on the text strings of the deprecated events to the new event format.
{: .note}

| Action Name | Legacy Action name | Description |
| ------- | ------- | ------- |
| `<service_id>.deployment-backup.create`|`<service_id>.backup-ondemand.create` | An on-demand backup of your instance was created. If the backup failed, a "-failure" flag is included in the message. |
|`<service_id>.deployment-backup-scheduled.create`| `<service_id>.backup-scheduled.create`| A scheduled backup of your instance was created. If the backup failed, a "-failure" flag is included in the message. |
|`<service_id>.deployment-user.update`|`<service_id>.user-password.update`| A user's password was updated. A "-failure" flag is included in the message if the attempt to update a user's password failed. |
|`<service_id>.deployment-user.create`|`<service_id>.user.create` | A user was created. A "-failure" flag is included in the message if the attempt to create a user failed. |
|`<service_id>.deployment-user.delete`|`<service_id>.user.delete` | A user was deleted. A "-failure" flag is included in the message if the attempt to delete a user failed. |
|No Longer Sent (_see below for more information_) | `<service_id>.backup.restore`|A restore from backup was created. If the attempted restore failed, a "-failure" flag is included in the message. |
|`<service_id>.deployment-group.update`|`<service_id>.resources.scale` | A scaling operation was performed. If the scaling operation failed, a "-failure" flag is included in the message. |
|`<service_id>.deployment-allowlist-ip-addresses.update` | `<service_id>.whitelisted-ips-list.update`|The allowlist was modified. A "-failure" flag is included in the message if the attempt to modify the allowlist failed. |
|`<service_id>.deployment.update`|`<service_id>.serviceendpoints.update` | A change was made to the service endpoints configuration. If the operation failed, a "-failure" flag is included in the message. |
|`<service_id>.deployment-group-autoscaling.update` | `<service_id>.autoscaling.update` | An autoscaling configuration change or an autoscaling operation was performed. If an autoscaling operation was performed the message includes `autoscale resources for instance <deployment-id>`. If the autoscaling operation or the configuration change failed, a "-failure" flag is included in the message. |
|`<service_id>.deployment-volumes.update`|`<service_id>.volumes.update` | An activity was performed on the encryption key that is used by the database, such as rotation or shredding. Details of the action are in the event. |
{: caption="Table 2. List of Events and Event Descriptions" caption-side="bottom"}

The `service_id` field indicates the type of {{site.data.keyword.databases-for}} instance. For example, `databases-for-postgresql` or `messages-for-rabbitmq`.

The `<service_id>.backup.restore` auditing message is no longer sent because this action is already covered by the `<service_name>.instance.create` {{site.data.keyword.cloud_notm}} global event. For more resource-related global events, you can review the [{{site.data.keyword.at_full}} documentation](/docs/activity-tracker?topic=activity-tracker-at_events_rc#rc_ui). {{site.data.keyword.cloud_notm}} global events include generation of events such as provisioning, deprovisioning, service plan changes, and tagging of resources. To view these events, you must [provision an instance](/docs/services/activity-tracker?topic=activity-tracker-provision#provision) of the {{site.data.keyword.at_full}} service in the Frankfurt (`eu-de`) region.
