---

copyright:
  years: 2021, 2024
lastupdated: "2024-08-02"

keywords: resource utilization, disk utilization, disk alert, notification channel, resource management, disk utilization, alert rule

subcollection: cloud-databases

content-type: tutorial
account-plan: paid
completion-time: 30m

---

{{site.data.keyword.attribute-definition-list}}

# Setting up disk alerts for disk utilization
{: #disk-util-alert-tutorial}
{: toc-content-type="tutorial"}
{: toc-completion-time="30m"}

## Objectives
{: #disk-util-alert-tutorial-objectives}

Getting timely alerts about resource utilization is key to managing your database, avoiding problems, and mitigating downtime. If you know in advance that your database is running out of disk, take steps to scale those resources.

In this tutorial, you use the {{site.data.keyword.cloud_notm}} API and the [{{site.data.keyword.cloud_notm}} CLI](https://cloud.ibm.com/docs/cli?topic=cli-getting-started){: external} to set up an alert that emails you whenever the disk utilization of your database exceeds 90%. This specific example creates an alert on a {{site.data.keyword.databases-for-elasticsearch}} deployment, but it is applicable to all the databases in the IBM {{site.data.keyword.databases-for}} catalog.

## Getting productive 
{: #disk-util-alert-tutorial-getting-started}

### Set up monitoring instance and Platform Metrics
{: #disk-util-alert-tutorial-monitor-platform}

To get started, you need access to [{{site.data.keyword.mon_full}}](https://www.ibm.com/products/cloud-monitoring) in your database region, and you need to have a [monitoring instance](/docs/monitoring?topic=monitoring-getting-started) available. This monitoring instance must be in the same region as the database target. 

You also must have [Platform Metrics](/docs/monitoring?topic=monitoring-platform_metrics_enabling) enabled.

### Install Command Line Interface tools
{: #disk-util-alert-tutorial-cli-tools}

Next, you need the [{{site.data.keyword.cloud_notm}} Monitoring CLI]((https://cloud.ibm.com/docs/cli?topic=cli-monitor-cli)) and [{{site.data.keyword.databases-for}} CLI plug-in](https://cloud.ibm.com/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference#installing-cli-plugin).

Install the {{site.data.keyword.cloud_notm}} Monitoring CLI by running the following command:

```sh
ibmcloud plugin install monitoring
```
{: pre}

Install the {{site.data.keyword.databases-for}} CLI plug-in by running the following command:

```sh
ibmcloud plugin install cloud-databases
```
{: pre}

You are now ready to retrieve and monitor your service instance.

## Retrieve your monitoring service instance
{: #retrieve-monitoring-serv-instance}
{: step}

In this step, you retrieve the necessary credentials to gain access to your monitoring instance.

Begin by logging in to the {{site.data.keyword.cloud_notm}} CLI with the following command:

```sh
ibmcloud login -sso
```
{: pre}

Follow the on-screen instructions to log in.

Next, target the appropriate [region](/docs/overview?topic=overview-locations) for your instance:

```sh
ibmcloud target -r <REGION>
```
{: pre}

Then, list the existing monitoring instances in that region with the following command:

```sh
ibmcloud monitoring service-instances
```
{: pre}

Note the service instance name that has “Platform Metrics” enabled.
{: note}

Now create an authorization token for the API, by using a command like:

The following steps work only on Bash.
{: important}

```sh
AUTH_TOKEN=$(ibmcloud iam oauth-tokens | awk '{print $4}')
```
{: pre}

You can now retrieve the ID of your monitoring service instance for the API with the following command:

```sh
GUID=$(ibmcloud resource service-instance <instance_name_from_step_above> --output json | jq -r '.[].guid')
```
{: pre}

## Set up the notification channel
{: #set-up-notif-channel}
{: step}

Configure a [notification channel](/docs/monitoring?topic=monitoring-notifications) to be notified when an alert is triggered. To set up your notification channel, use the following command:

```sh
curl -X POST https://<region>.monitoring.cloud.ibm.com/api/notificationChannels -H "Authorization: Bearer $AUTH_TOKEN" -H "IBMInstanceID: $GUID" -H "content-type: application/json"  --data-raw '{"notificationChannel":{"id":null,"version":null,"teamId":"","name":"<notification_channel>","type":"EMAIL","enabled":true,"sendTestNotification":true,"options":{"notifyOnOk":true,"notifyOnResolve":true,"emailRecipients":["email@email.com"]}}}'
```
{: pre}

You see the following output:

```screen
{"notificationChannel":{"id":39209,"version":1,"customerId":34292,"enabled":true,"sendTestNotification":true,"createdOn":1678967870764,"modifiedOn":1678967870764,"name":"thursTest","options":{"notifyOnOk":true,"emailRecipients":["email@email.com"],"notifyOnResolve":true},"type":"EMAIL"}}% 
```

You have now created a notification channel for your alerts.

Make a note of the `id` field that is returned by the API call.
{: important}

## Create the alert
{: #disk-util-alert-tutorial-create-alert}
{: step}

Now that you have a notification channel, create your [alert rule](https://cloud.ibm.com/docs/monitoring?topic=monitoring-alert_api){: external}. Your alert rule describes the metric query to be monitored, the threshold value, and the action to take when the threshold is crossed. In this case, you're monitoring your `ibm_service_instance_name` to ensure that `max` utilization doesn't exceed 90%. If that happens, an alert is triggered and you're notified.

This alert is triggered at 90% disk utilization. However, 50-70% disk utilization is preferred.
{: note}

To retrieve the name of the database instance you want to set up the alert for, list all your database instances with a command like:

```sh
ibmcloud cdb ls
```
{: pre}

Make sure to select a database in the same region as the monitoring instance.
{: important}

You see output like the following:

```screen
Retrieving instances for all database types in all resource groups in all locations under IBM as …
OK
Name                          Location   State
Databases for PostgreSQL-76   us-south   inactive
testelastic                   eu-gb      active
Databases for MySQL-9j        us-south   active
```

Now, use the name of your database to create the alert by using a command like:

```sh
curl --request POST \
  --url https://<region>.monitoring.cloud.ibm.com/api/alerts \
  --header "Authorization: Bearer  $AUTH_TOKEN" \
  --header 'Content-Type: application/json' \
  --header "IBMInstanceID: $GUID" \
  --data-raw  '{
	"alert":
		{
			"type": "MANUAL",
			"name": "Disk Alert",
			"description": "",
			"enabled": true,
			"severity": 1,
			"timespan": 60000000,
			"notificationChannelIds": [
				<id_from_previous_step>
			],
			"filter": "ibm_service_instance_name in (\"<db_instance_name_from_previous_step>\")",
		  "condition": "max(max(ibm_databases_for_elasticsearch_disk_used_percent)) > 0.9"
		}
}'
```
{: pre}

This command takes the max disk utilization of any member available, regardless of the number of members.
{: note}

## Check that your alert is created
{: #check-alert-creation}
{: step}

An alert is created whenever you reach 90% of disk size. You receive the alert to the same email that you created in the notification channel. You can also use the following command to check current active alerts:

```sh
ibmcloud monitoring alert list --name <monitoring instance name>
```
{: pre}

You now receive an alert whenever your {{site.data.keyword.databases-for-elasticsearch}} instance disk utilization exceeds 90%, so you can act before the disk is too full.

## Next steps
{: #disk-alert-tut-next-steps}

To modify your alert or find out more about Monitoring, see [Getting started with{{site.data.keyword.mon_full_notm}}](/docs/monitoring?topic=monitoring-getting-started).

### Scaling resources
{: #check-alert-scale-resources}

If you receive an alert that your disk utilization exceeds 90%, scale your disk so that you do not exceed 50-70% usage. Manually manage your service's resources or autoscale.

| Service                                          | Managing Resources         | Autoscaling |
|--------------------------------------------------|----------------------------|-------------|
| {{site.data.keyword.databases-for-enterprisedb}} | [Scaling Disk, RAM, and CPU](/docs/databases-for-enterprisedb?topic=databases-for-enterprisedb-resources-scaling&interface=ui) | [Autoscaling](/docs/databases-for-enterprisedb?topic=databases-for-enterprisedb-autoscaling&interface=ui) |
| {{site.data.keyword.databases-for-etcd}} | [Scaling Disk, RAM, and CPU](/docs/databases-for-etcd?topic=databases-for-etcd-resources-scaling&interface=ui) | [Autoscaling](/docs/databases-for-etcd?topic=databases-for-etcd-autoscaling&interface=ui) |
| {{site.data.keyword.databases-for-mongodb}} | [Scaling Disk, RAM, and CPU](/docs/databases-for-mongodb?topic=databases-for-mongodb-resources-scaling&interface=ui) | [Autoscaling](/docs/databases-for-mongodb?topic=databases-for-mongodb-autoscaling&interface=ui) |
| {{site.data.keyword.databases-for-postgresql}} | [Scaling Disk, RAM, and CPU](/docs/databases-for-postgresql?topic=databases-for-postgresql-resources-scaling&interface=ui) | [Autoscaling](/docs/databases-for-postgresql?topic=databases-for-postgresql-autoscaling&interface=ui) |
| {{site.data.keyword.databases-for-redis}} | [Scaling Disk, RAM, and CPU](/docs/databases-for-redis?topic=databases-for-redis-resources-scaling&interface=ui) | [Autoscaling](/docs/databases-for-redis?topic=databases-for-redis-autoscaling&interface=ui) |
| {{site.data.keyword.databases-for-mysql}} | [Scaling Disk, RAM, and CPU](/docs/databases-for-mysql?topic=databases-for-mysql-resources-scaling) | [Autoscaling](/docs/databases-for-redis?topic=databases-for-redis-autoscaling&interface=ui) |
| {{site.data.keyword.messages-for-rabbitmq}} | [Scaling Disk, RAM, and CPU](/docs/messages-for-rabbitmq?topic=messages-for-rabbitmq-resources-scaling&interface=ui) | [Autoscaling](/docs/messages-for-rabbitmq?topic=messages-for-rabbitmq-autoscaling&interface=ui) |
{: caption="Table 1. Scaling Resources" caption-side="bottom"}

## {{site.data.keyword.databases-for}} service metrics
{: #icd-service-metrics}

This tutorial uses {{site.data.keyword.databases-for-elasticsearch_full}}. However, the same process applies to other {{site.data.keyword.databases-for}} services:

- [{{site.data.keyword.databases-for-enterprisedb_full}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-enterprisedb)
- [{{site.data.keyword.databases-for-etcd_full}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-etcd)
- [{{site.data.keyword.databases-for-mongodb_full}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-mongodb)
- [{{site.data.keyword.databases-for-postgresql_full}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-postgresql)
- [{{site.data.keyword.databases-for-redis_full}}](https://cloud.ibm.com/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-redis)
- [{{site.data.keyword.databases-for-mysql_full}}](/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-mysql)
- [{{site.data.keyword.messages-for-rabbitmq_full}}](https://cloud.ibm.com/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-rabbitmq)
