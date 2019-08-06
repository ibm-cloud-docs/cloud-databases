---
copyright:
  years: 2019
lastupdated: "2019-07-09"

subcollection: cloud-databases

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:tip: .tip}

# Activity Tracker Integration
{: #activity-tracker}

{{site.data.keyword.cloud_notm}} Databases deployments are integrated with Activity Tracker events in [IBM Cloud Activity Tracker with LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about), so you can view service-level events.

Currently, Activity Tracker with LogDNA integration is available for {{site.data.keyword.databases-for}} deployments according to the following table. 

Deployment Region | Activity Tracker Region 
----------|-----------
`us-south` | `us-south`
`jp-tok` | `jp-tok`
`eu-gb` | `eu-gb`
`osl01` | `eu-gb`
`seo01` | `jp-tok`
`che01` | `jp-tok`
`eu-de` | `eu-de`
`us-east` | Not Available
`au-syd` | Not Available
{: caption="Table 1. Activity Tracker regions" caption-side="top"}

Events from your deployments appear in an Activity Tracker instance in the same region, with the exception of `osl01`, `seo01`, and `che01`. Deployments in `osl01` have their events forwarded to `eu-gb`. Deployments in `seo01` and `che01` have their events forwarded to `jp-tok`. If you have deployments in multiple regions you have to set up the Activity Tracker in multiple regions. 

## Activity Tracker through LogDNA

Once you provision the service, events will automatically be forwarded from all your {{site.data.keyword.databases-for}} deployments in the same region.

The service can be provisioned from [its catalog page](https://{DomainName}/catalog/services/ibm-cloud-activity-tracker-with-logdna) or from an existing [Observability Dashboard](https://cloud.ibm.com/observe/activitytracker).

The Activity Tracker with LogDNA service has a lite plan that is free to use, but it only offers streaming events. To take advantage of the tagging, export, retention, and other features, you need to use one of the [paid plans](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

### Using the LogDNA Activity Tracker

Once event activity is being forwarded to the service, each event can be expanded to a detailed view by clicking the arrow to the left of the timestamp.

The LogDNA service offers [searching](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6), [filtering](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5), and [export](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-export#export) of events so you can customize retention for your use-case. 

For more information on features offered by LogDNA, including integrating it with your other {{site.data.keyword.cloud_notm}} services, see [its full documentation](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

## Event Fields

A description of the common fields for an Activity Tracker event is on the [event fields](/docs/services/Activity-Tracker-with-LogDNA?topic=logdnaat-event) page.

## List of Events

The table lists the events that get sent to Activity Tracker from {{site.data.keyword.databases-for}} deployments.

Action|Description
-------|-------
`<service_id>.backup.create`|A backup of your deployment was created. If the backup failed, a "-failure" flag is included in the message.
`<service_id>.user-password.update`|A user's password was updated. A "-failure" flag is included in the message if the attempt to update a user's password failed.
`<service_id>.user.create`|A user was created. A "-failure" flag is included in the message if the attempt to create a user failed.
`<service_id>.user.delete`|A user was deleted. A "-failure" flag is included in the message if the attempt to delete a user failed.
`<service_id>.backup.restore`|A restore from backup was created. If the attempted restore failed, a "-failure" flag is included in the message.
`<service_id>.resources.scale`|A scaling operation was performed. If the scaling operation failed, a "-failure" flag is included in the message.
`<service_id>.whitelisted-ips-list.update`|The whitelist was modified. A "-failure" flag is included in the message if the attempt to modify the whitelist failed.
{: caption="Table 2. List of Events and Event Descriptions" caption-side="top"}

The `service_id` field indicates the type of {{site.data.keyword.databases-for}} deployment. For example, `databases-for-postgresql` or `messages-for-rabbitmq`.

## Legacy Activity Tracker

{{site.data.keyword.cloud_notm}} Databases deployments are still integrated with  [Activity Tracker](/docs/services/cloud-activity-tracker?topic=cloud-activity-tracker-activity_tracker_ov), although this service is in the process of being deprecated.

If have already provisioned the Activity Tracker service, that service might still be running. New provisions of the service are no longer available.

Some {{site.data.keyword.cloud_notm}} regions did not have the Activity Tracker service available. If you have a {{site.data.keyword.databases-for}} deployment in a region that is not supported, your Activity Tracker uses region on the table.

Deployment Region|Monitoring Region|UI Link
----------|-----------|-----------
Dallas | Dallas | https://logging.ng.bluemix.net
Frankfurt | Frankfurt | https://logging.eu-fra.bluemix.net
Oslo | Frankfurt | https://logging.eu-fra.bluemix.net
Tokyo | not supported | not supported
Sydney | Sydney | https://logging.au-syd.bluemix.net
US East | US South | https://logging.ng.bluemix.net
London | Frankfurt | https://logging.eu-fra.bluemix.net
{: caption="Table 3. Activity Tracker service regions" caption-side="top"}

{{site.data.keyword.databases-for}} deployment events appear under _Account Logs_ from the _View Logs_ dropdown menu. 

A description of the common fields for an Activity Tracker event is on the [Activity Tracker event fields](/docs/services/cloud-activity-tracker?topic=cloud-activity-tracker-at_event) page.
