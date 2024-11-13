---

copyright:
  years: 2018, 2024
lastupdated: "2024-11-13"

keywords: activity tracker

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}



# Activity tracking events for {{site.data.keyword.databases-for}}
{: #at_events}



{{site.data.keyword.cloud}} services, such as {{site.data.keyword.databases-for}}, generate activity tracking events.
{: shortdesc}

Activity tracking events report on activities that change the state of a service in {{site.data.keyword.cloud_notm}}. You can use the events to investigate abnormal activity and critical actions and to comply with regulatory audit requirements.

You can use **{{site.data.keyword.atracker_full}}**, a platform service, to route auditing events in your account to destinations of your choice by configuring targets and routes that define where activity tracking events are sent. For more information, see [About {{site.data.keyword.atracker_full_notm}}](/docs/atracker?topic=atracker-about).

You can use **{{site.data.keyword.logs_full}}** to visualize and alert on events that are generated in your account and routed by {{site.data.keyword.atracker_full_notm}} to an {{site.data.keyword.logs_full_notm}} instance.



As of 28 March 2024, the {{site.data.keyword.at_full_notm}} service is deprecated and will no longer be supported as of 30 March 2025. Customers will need to migrate to {{site.data.keyword.logs_full_notm}} before 30 March 2025. During the migration period, customers can use {{site.data.keyword.at_full_notm}} along with {{site.data.keyword.logs_full_notm}}. Activity tracking events are the same for both services. For information about migrating from {{site.data.keyword.at_full_notm}} to {{site.data.keyword.logs_full_notm}} and running the services in parallel, see [migration planning](/docs/cloud-logs?topic=cloud-logs-migration-intro).
{: important}

## Locations where activity tracking events are generated
{: #at-locations}



### Locations where activity tracking events are sent to {{site.data.keyword.at_full_notm}} hosted event search
{: #at-legacy-locations}



{{site.data.keyword.databases-for}} send activity tracking events to {{site.data.keyword.at_full_notm}} hosted event search in the regions that are indicated in the following table.

| Dallas (`us-south`) | Washington (`us-east`)  | Toronto (`ca-tor`) | Sao Paulo (`br-sao`) |
|---------------------|-------------------------|-------------------|----------------------|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} |
{: caption="Regions where activity tracking events are sent in Americas locations" caption-side="top"}
{: #at-table-1}
{: tab-title="Americas"}
{: tab-group="at"}
{: class="simple-tab-table"}
{: row-headers}

| Tokyo (`jp-tok`)    | Sydney (`au-syd`) |  Osaka (`jp-osa`) | Chennai (`in-che`) |
|---------------------|------------------|------------------|--------------------|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [No]{: tag-red} | [Yes]{: tag-green} |
{: caption="Regions where activity tracking events are sent in Asia Pacific locations" caption-side="top"}
{: #at-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="at"}
{: class="simple-tab-table"}
{: row-headers}

| Frankfurt (`eu-de`)  | London (`eu-gb`) | Madrid (`eu-es`) |  Paris (`eu-par01`) |
|---------------------------------------------------------------|---------------------|------------------|------|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [No]{: tag-red} |  [No]{: tag-red} |
{: caption="Regions where activity tracking events are sent in Europe locations" caption-side="top"}
{: #at-table-3}
{: tab-title="Europe"}
{: tab-group="at"}
{: class="simple-tab-table"}
{: row-headers}

### Locations where activity tracking events are sent by {{site.data.keyword.atracker_full_notm}}
{: #atracker-locations}



{{site.data.keyword.databases-for}} sends activity tracking events by {{site.data.keyword.atracker_full_notm}} in the regions that are indicated in the following table.

| Dallas (`us-south`) | Washington (`us-east`)  | Toronto (`ca-tor`) | Sao Paulo (`br-sao`) |
|---------------------|-------------------------|-------------------|----------------------|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} |
{: caption="Regions where activity tracking events are sent in Americas locations" caption-side="top"}
{: #atracker-table-1}
{: tab-title="Americas"}
{: tab-group="atracker"}
{: class="simple-tab-table"}
{: row-headers}

| Tokyo (`jp-tok`)    | Sydney (`au-syd`) |  Osaka (`jp-osa`) | Chennai (`in-che`) |
|---------------------|------------------|------------------|--------------------|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} |
{: caption="Regions where activity tracking events are sent in Asia Pacific locations" caption-side="top"}
{: #atracker-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="atracker"}
{: class="simple-tab-table"}
{: row-headers}

| Frankfurt (`eu-de`)  | London (`eu-gb`) | Madrid (`eu-es`) |  Paris (`eu-par01`) |
|---------------------------------------------------------------|---------------------|------------------|------|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} |  [No]{: tag-red}
{: caption="Regions where activity tracking events are sent in Europe locations" caption-side="top"}
{: #atracker-table-3}
{: tab-title="Europe"}
{: tab-group="atracker"}
{: class="simple-tab-table"}
{: row-headers}

## Enabling activity tracking events for {{site.data.keyword.databases-for}}
{: #at-enable}






Create an {{site.data.keyword.logs_full_notm}} instance and configure {{site.data.keyword.atracker_full_notm}} by setting the routing rule between the {{site.data.keyword.databases-for}} instance and the {{site.data.keyword.logs_full_notm}} target instance. 

## Viewing activity tracking events for {{site.data.keyword.databases-for}}
{: #at-viewing}



You can use {{site.data.keyword.logs_full_notm}} to visualize and alert on events that are generated in your account and routed by {{site.data.keyword.atracker_full_notm}} to an {{site.data.keyword.logs_full_notm}} instance.

### Launching {{site.data.keyword.logs_full_notm}} from the {{site.data.keyword.databases-for}} dashboard
{: #log-launch-integrated}



You can visit the {{site.data.keyword.databases-for}} instance. Click on _Overview_ and scroll to the _Observability_ section. Click on *{{site.data.keyword.logs_full_notm}}* to view your logging instances. Click on _Open Dashboard_ to access the logs.

### Launching {{site.data.keyword.logs_full_notm}} from the Observability page
{: #log-launch-standalone}



For information on launching the {{site.data.keyword.logs_full_notm}} UI, see [Launching the UI in the {{site.data.keyword.logs_full_notm}} documentation.](/docs/cloud-logs?topic=cloud-logs-instance-launch)

## List of platform events
{: #at_actions_platform}



The following table lists the activity tracking event actions that {{site.data.keyword.databases-for}} and {{site.data.keyword.cloud_notm}} generate.

| Action name | Legacy action name | Description |
| ------- | ------- | ------- |
| `<service_name>.deployment-backup.create`|`<service_id>.backup-ondemand.create` | An on-demand backup of your instance was created. If the backup failed, a "-failure" flag is included in the message. |
|`<service_name>.deployment-backup-scheduled.create`| `<service_id>.backup-scheduled.create`| A scheduled backup of your instance was created. If the backup failed, a "-failure" flag is included in the message. |
|`<service_name>.deployment-user.update`|`<service_id>.user-password.update`| A user's password was updated. A "-failure" flag is included in the message if the attempt to update a user's password failed. |
|`<service_name>.deployment-user.create`|`<service_id>.user.create` | A user was created. A "-failure" flag is included in the message if the attempt to create a user failed. |
|`<service_name>.deployment-user.delete`|`<service_id>.user.delete` | A user was deleted. A "-failure" flag is included in the message if the attempt to delete a user failed. |
|`<service_name>.deployment-group.update`|`<service_id>.resources.scale` | A scaling operation was performed. If the scaling operation failed, a "-failure" flag is included in the message. |
|`<service_name>.deployment-allowlist-ip-addresses.update` | `<service_id>.whitelisted-ips-list.update`|The allowlist was modified. A "-failure" flag is included in the message if the attempt to modify the allowlist failed. |
|`<service_name>.deployment.update`|`<service_id>.serviceendpoints.update` | A change was made to the service endpoints configuration. If the operation failed, a "-failure" flag is included in the message. |
|`<service_name>.deployment-group-autoscaling.update` | `<service_id>.autoscaling.update` | An autoscaling configuration change or an autoscaling operation was performed. If an autoscaling operation was performed the message includes `autoscale resources for instance <deployment-id>`. If the autoscaling operation or the configuration change failed, a "-failure" flag is included in the message. |
|`<service_name>.deployment-volumes.update`|`<service_id>.volumes.update` | An activity was performed on the encryption key that is used by the database, such as rotation or shredding. Details of the action are in the event. |
{: caption="List of events and event descriptions by {{site.data.keyword.databases-for}}" caption-side="bottom"}

The `service_name` field indicates the type of {{site.data.keyword.databases-for}} instance. For example, `databases-for-postgresql` or `messages-for-rabbitmq`.

Auditing of global events, such as `<service_name>.instance.create`, is covered by the {{site.data.keyword.cloud_notm}} global event. For more resource-related global events, see [Auditing events for service instances](/docs/atracker?topic=atracker-at_events_rc).
