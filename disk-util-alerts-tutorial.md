---

copyright:
  years: 2021, 2023
lastupdated: "2023-05-16"

keywords: resource utilization, disk utilization, disk alert

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

Getting timely alerts about resource utilization is key to managing your database, avoiding problems, and mitigating downtime. If you know in advance that your database is running out of disk, take steps to scale those resources. Scaling your resources keeps your services running smoothly.

In this tutorial, you use the {{site.data.keyword.cloud_notm}} API and the [{{site.data.keyword.cloud_notm}} CLI](https://cloud.ibm.com/docs/cli?topic=cli-getting-started){: external} to set up an alert that emails you whenever the disk utilization of your database exceeds 90%. This specific example creates an alert on a {{site.data.keyword.databases-for-elasticsearch}} deployment, but it is applicable to all the databases in the IBM {{site.data.keyword.databases-for}} catalog.

## Getting productive 
{: #disk-util-alert-tutorial-getting-started}

To get started, you need access to {{site.data.keyword.mon_full}} in your database region, and you need to have a monitoring instance available. This monitoring instance must be in the same region as the database target. You also must have [Platform Metrics](/docs/monitoring?topic=monitoring-platform_metrics_enabling) enabled.

### Install the necessary CLI plug-ins:
{: #install-plug-ins}

Install the [{{site.data.keyword.cloud_notm}} Monitoring CLI]((https://cloud.ibm.com/docs/cli?topic=cli-monitor-cli)) by running the following command:

```sh
ibmcloud plugin install monitoring
```
{: pre}

Install the [{{site.data.keyword.databases-for}} CLI plug-in](https://cloud.ibm.com/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference#installing-cli-plugin) by running the following command: 

```sh
ibmcloud plugin install cloud-databases
```
{: pre}

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

Now create an authorization token for the API, using a command like:

The following steps only work on bash.
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

To set up the notification channel, use the following command: 

```sh
curl -X POST https://<region>.monitoring.cloud.ibm.com/api/notificationChannels -H "Authorization: Bearer $AUTH_TOKEN" -H "IBMInstanceID: $GUID" -H "content-type: application/json"  --data-raw '{"notificationChannel":{"id":null,"version":null,"teamId":"","name":"<notification_channel>","type":"EMAIL","enabled":true,"sendTestNotification":true,"options":{"notifyOnOk":true,"notifyOnResolve":true,"emailRecipients":["email@email.com"]}}}'
```
{: pre}

You will see the following output:

```screen
{"notificationChannel":{"id":39209,"version":1,"customerId":34292,"enabled":true,"sendTestNotification":true,"createdOn":1678967870764,"modifiedOn":1678967870764,"name":"thursTest","options":{"notifyOnOk":true,"emailRecipients":["email@email.com"],"notifyOnResolve":true},"type":"EMAIL"}}% 
```

You have now created a Notification Channel for your alerts. 

Make a note of the `id` field that is returned by the API call.
{: important}

## Create the alert
{: #create-alert}
{: step}

Now that you have the notification channel, create your alert.

To retrieve the name of the database instance you want to set up the alert for, list all your database instances, using a command like:

```sh
ibmcloud cdb ls
```
{: pre}

Make sure to select a database in the same region as the monitoring instance.
{: important}

You will see output like the following:

```screen
Retrieving instances for all database types in all resource groups in all locations under IBM as …
OK
Name                          Location   State
Databases for PostgreSQL-76   us-south   inactive
testelastic                   eu-gb      active
Databases for MySQL-9j        us-south   active
```

Now, use the name of your database to create the alert, using the the following command:

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

## Check that your alert is created
{: #check-alert-creation}
{: step}

Check that your alert is now created with the following command:

```sh
ibmcloud monitoring alert list --name <monitoring instance name>
```
{: pre}

## {{site.data.keyword.databases-for}} service metrics
{: #icd-service-metrics}

This tutorial uses {{site.data.keyword.databases-for-elasticsearch_full}}. To apply the same method to other {{site.data.keyword.databases-for}} services, find the metrics below:

- [{{site.data.keyword.databases-for-cassandra_full}}](/docs/databases-for-cassandra?topic=databases-for-cassandra-monitoring#metrics-by-plan)
- [{{site.data.keyword.databases-for-enterprisedb_full}}](/docs/databases-for-enterprisedb?topic=databases-for-enterprisedb-monitoring#metrics-by-plan)
- [{{site.data.keyword.databases-for-etcd_full}}](/docs/databases-for-etcd?topic=databases-for-etcd-monitoring#metrics-by-plan)
- [{{site.data.keyword.databases-for-mongodb_full}}](/docs/databases-for-mongodb?topic=databases-for-mongodb-monitoring#metrics-by-plan)
- [{{site.data.keyword.databases-for-postgresql_full}}](/docs/databases-for-postgresql?topic=databases-for-postgresql-monitoring#metrics-by-plan)
- [{{site.data.keyword.databases-for-redis_full}}](/docs/databases-for-redis?topic=databases-for-redis-monitoring#metrics-by-plan)
- [{{site.data.keyword.databases-for-mysql_full}}](/docs/databases-for-mysql?topic=databases-for-mysql-monitoring#metrics-by-plan)
- [{{site.data.keyword.messages-for-rabbitmq_full}}](/docs/messages-for-rabbitmq?topic=messages-for-rabbitmq-monitoring#metrics-by-plan)

## Next Steps
{: #disk-alert-next-steps}

You should now receive an alert whenever your {{site.data.keyword.databases-for-elasticsearch}} instance disk utilization exceeds 90%, so you can take action before the disk is too full. If you want to modify your alert or find out more about Monitoring, please visit the [Monitoring documentation](/docs/monitoring?topic=monitoring-getting-started).
