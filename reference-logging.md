---
copyright:
  years: 2019, 2023
lastupdated: "2023-10-31"

subcollection: cloud-databases

keywords: database logs, platform logs, platform logging, hipaa

---

{{site.data.keyword.attribute-definition-list}}

# Log Analysis Integration
{: #logging}

{{site.data.keyword.databases-for}} are integrated with [{{site.data.keyword.loganalysisfull}}](/docs/log-analysis), so you can view database platform logs.

Currently, {{site.data.keyword.loganalysisfull}} integration is available for {{site.data.keyword.databases-for}} instances according to the following table.

| Instance Region | Log Analysis Region |
| ----------|----------- |
| `us-south` | `us-south` |
| `jp-tok` | `jp-tok` |
| `eu-gb` | `eu-gb` |
| `che01` | `che01` |
| `eu-de` | `eu-de` |
| `au-syd` | `au-syd` |
| `us-east` | `us-east` |
| `ca-tor` | `ca-tor` |
| `jp-osa` | `jp-tok`  |
| `br-sao` | `br-sao` |
| `par01` | `eu-de` |
| `eu-es` | `eu-de` |
{: caption="Table 1. Log Analysis regions" caption-side="top"}

Platform logs from your instances appear in a Log Analysis instance in the same region, except for `jp-osa` and `eu-es`. Instances in `jp-osa` have their logs forwarded to `jp-tok`. Instances in `eu-es` have their logs forwarded to `eu-de` If you have instances in multiple regions, you must set up Log Analysis in multiple regions.  

## Provisioning {{site.data.keyword.loganalysisfull}}
{: #provisioning-logging}

Platform log information from your databases is automatically forwarded to {{site.data.keyword.la_full_notm}}, but to access it you must enable platform logging by [provisioning a {{site.data.keyword.loganalysisshort}} service](/docs/log-analysis?topic=log-analysis-provision) in your {{site.data.keyword.cloud_notm}} account and [configuring the service to receive {{site.data.keyword.cloud_notm}} platform logs](/docs/log-analysis?topic=log-analysis-config_svc_logs).

This setting enables platform logs from **ALL** {{site.data.keyword.cloud_notm}} services on your account that have {{site.data.keyword.la_full_notm}} integration to send logs to your {{site.data.keyword.la_full_notm}} service. [A list of the integrated services is available](/docs/log-analysis?topic=log-analysis-cloud_services#cloud_services).
{: .tip}

{{site.data.keyword.la_full_notm}} has a lite plan that is free to use, but it offers only streaming events. To take advantage of the tagging, export, retention, and other features, you need to use one of the [paid plans](/docs/log-analysis?topic=log-analysis-service_plans).

### HIPAA 
{: #hipaa}

{{site.data.keyword.la_full_notm}} offers a HIPAA-compliant plan for the service. For more information, see [Provisioning a HIPAA Compliance instance](/docs/log-analysis?topic=log-analysis-provision_hipaa).

Use caution when configuring the platform service logs, since this setting can impact other services that require HIPAA compliance.

## Using {{site.data.keyword.loganalysisfull}}
{: #using}

You can access {{site.data.keyword.loganalysisshort}} through the _Observability_ tab of your deployment's _Manage_ page. The **Manage Log Analysis** button links to the main list of all {{site.data.keyword.loganalysisshort}} instances in your IBM Cloud account. Select the instance where you set your database platform logs to be forwarded. Click **View Log Analysis** to view the logs.

Each log line can be expanded to a detailed view by clicking the arrow to the left of the timestamp. The expanded view has some handy, color-coded fields to help you parse your logs. 

- _Line Identifiers_
    - `Source` - the region the logs are being sent from
    - `App` - the ID of the application that sent the log. It is the last part of your deployment ID and CRN.

- _Tags_
    - `#` - all of the logs that come from a {{site.data.keyword.databases-for}} deployment are tagged with `ibm-cloud-databases`

- _Labels_
    - `database` - the database type that this log is from
    - `member` - the member ID for which node in the cluster generated the log
    - `CRN` - the full deployment ID of your deployment.

{{site.data.keyword.loganalysisshort}} offers [searching](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step6), [filtering](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step5) to help you navigate your logs.

[Export](/docs/log-analysis?topic=log-analysis-export#export) and [archiving](/docs/log-analysis?topic=log-analysis-archiving#archiving) are available so you can customize retention (and cost) for your use-case.

To set up logging alerts, see [Working with Alerts](/docs/log-analysis?topic=log-analysis-alerts#alerts)

For more information,see [{{site.data.keyword.la_full_notm}}](/docs/log-analysis).

## Internal Log Retention
{: #internal-logging}

Database platform logs for all {{site.data.keyword.databases-for}} instances are kept internally for 30 days and then purged. If your {{site.data.keyword.loganalysisshort}} plan is for a shorter period, logs are only accessible by you for the length of your plan. Regardless of the plan that you choose, all database logs are deleted after 30 days.
