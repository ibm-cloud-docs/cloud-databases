---

copyright:
  years: 2018, 2024
lastupdated: "2024-11-13"

keywords: logging

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Logging for {{site.data.keyword.databases-for}}
{: #logging}

{{site.data.keyword.cloud_notm}} services, such as {{site.data.keyword.databases-for}}, generate platform logs that you can use to investigate abnormal activity and critical actions in your account, and troubleshoot problems.
{: shortdesc}

You can use **{{site.data.keyword.logs_routing_full_notm}}**, a platform service, to route platform logs in your account to a destination of your choice by configuring a tenant that defines where platform logs are sent. For more information, see [About logs routing](/docs/logs-router?topic=logs-router-about).

You can use **{{site.data.keyword.logs_full_notm}}** to visualize and alert on platform logs that are generated in your account and routed by {{site.data.keyword.logs_routing_full_notm}} to an {{site.data.keyword.logs_full_notm}} instance.



As of 28 March 2024, the {{site.data.keyword.la_full_notm}} service is deprecated and will no longer be supported as of 30 March 2025. Customers will need to migrate to {{site.data.keyword.logs_full_notm}} before 30 March 2025. During the migration period, customers can use {{site.data.keyword.la_full_notm}} along with {{site.data.keyword.logs_full_notm}}. Logging is the same for both services. For information about migrating from {{site.data.keyword.la_full_notm}} to {{site.data.keyword.logs_full_notm}} and running the services in parallel, see [migration planning](/docs/cloud-logs?topic=cloud-logs-migration-intro).
{: important}

## Locations where platform logs are generated
{: #log-locations}



### Locations where logs are sent to {{site.data.keyword.la_full_notm}}
{: #la-legacy-locations}



{{site.data.keyword.databases-for}} sends platform logs to {{site.data.keyword.la_full_notm}} in the regions indicated in the following table.

| Dallas (`us-south`) | Washington (`us-east`)  | Toronto (`ca-tor`) | Sao Paulo (`br-sao`) |
|---------------------|-------------------------|-------------------|----------------------|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} |
{: caption="Regions where platform logs are sent in Americas locations" caption-side="top"}
{: #la-table-1}
{: tab-title="Americas"}
{: tab-group="la"}
{: class="simple-tab-table"}
{: row-headers}

| Tokyo (`jp-tok`)    | Sydney (`au-syd`) |  Osaka (`jp-osa`) | Chennai (`in-che`) |
|---------------------|------------------|------------------|--------------------|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [No]{: tag-red} | [Yes]{: tag-green} |
{: caption="Regions where platform logs are sent in Asia Pacific locations" caption-side="top"}
{: #la-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="la"}
{: class="simple-tab-table"}
{: row-headers}

| Frankfurt (`eu-de`)  | London (`eu-gb`) | Madrid (`eu-es`) | Paris (`eu-par01`) |
|---------------------------------------------------------------|---------------------|------------------|-----|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [No]{: tag-red} |  [No]{: tag-red} |
{: caption="Regions where platform logs are sent in Europe locations" caption-side="top"}
{: #la-table-3}
{: tab-title="Europe"}
{: tab-group="la"}
{: class="simple-tab-table"}
{: row-headers}

### Locations where logs are sent by {{site.data.keyword.logs_routing_full_notm}}
{: #lr-locations}



{{site.data.keyword.databases-for}} sends logs by {{site.data.keyword.logs_routing_full_notm}} in the regions that are indicated in the following table.

| Dallas (`us-south`) | Washington (`us-east`)  | Toronto (`ca-tor`) | Sao Paulo (`br-sao`) |
|---------------------|-------------------------|-------------------|----------------------|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} |
{: caption="Regions where platform logs are sent in Americas locations" caption-side="top"}
{: #lr-table-1}
{: tab-title="Americas"}
{: tab-group="lr"}
{: class="simple-tab-table"}
{: row-headers}

| Tokyo (`jp-tok`)    | Sydney (`au-syd`) |  Osaka (`jp-osa`) | Chennai (`in-che`) |
|---------------------|------------------|------------------|--------------------|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} | [No]{: tag-red} |
{: caption="Regions where platform logs are sent in Asia Pacific locations" caption-side="top"}
{: #lr-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="lr"}
{: class="simple-tab-table"}
{: row-headers}

| Frankfurt (`eu-de`)  | London (`eu-gb`) | Madrid (`eu-es`) |  Paris (`eu-par01`) | 
|---------------------------------------------------------------|---------------------|------------------|-------|
| [Yes]{: tag-green} | [Yes]{: tag-green} | [Yes]{: tag-green} |  [No]{: tag-red}  |
{: caption="Regions where platform logs are sent in Europe locations" caption-side="top"}
{: #lr-table-3}
{: tab-title="Europe"}
{: tab-group="lr"}
{: class="simple-tab-table"}
{: row-headers}

## Platform logs that are generated
{: #log-platform}



{{site.data.keyword.databases-for}} generates platform logs for the severity types debug, error, info, warning, and critical.

Platform logs from your database instances can be routed to any region supported as per the table above. Logs from Chennai (`in-che`) is routed to Tokyo (`jp-tok`) and Paris (`eu-par01`) is routed to Frankfurt (`eu-de`).



## Enabling logging
{: #log-enable}









Create {{site.data.keyword.logs_full_notm}} and configure routing by setting the target between source location to target instance.

## Viewing logs
{: #log-viewing}



{{site.data.keyword.databases-for}} logs can be viewed in on the {{site.data.keyword.logs_full_notm}} instance created. Go to the [Logging instance page](https://cloud.ibm.com/observability/logging){:external} and click on _Dashboard._

### Launching {{site.data.keyword.logs_full_notm}} from the {{site.data.keyword.databases-for}} page
{: #log-launch-integrated}



Users can visit the {{site.data.keyword.databases-for}} instance. Click on _Overview_ and scroll to the _Observability_ section. Click on *{{site.data.keyword.logs_full_notm}}* to view your logging instances. Click on _Dashboard_ to access the logs.

### Launching {{site.data.keyword.logs_full_notm}} from the Observability page
{: #log-launch-standalone}



For more information about launching the {{site.data.keyword.logs_full_notm}} UI, see [Launching the UI in the {{site.data.keyword.logs_full_notm}} documentation](/docs/cloud-logs?topic=cloud-logs-instance-launch).

## Fields by log type
{: #log-fields}



For information about fields included in every platform log, see [Fields for platform logs](/docs/logs-router?topic=logs-router-about-platform-logs#platform_reqd).









{{site.data.keyword.databases-for}} logs include the following fields.

| Field             | Type       | Description             |
|-------------------|------------|-------------------------|
| `logSourceCRN`    | Required   | Defines the account and flow log instance where the log is published. |
| `saveServiceCopy` | Required   | Defines whether IBM saves a copy of the record for operational purposes. |
| `message`         | Required   | Description of the log that is generated. |
| `messageID`       | Required   | ID of the log that is generated. |
{: caption="Log record fields" caption-side="bottom"}

{{site.data.keyword.databases-for}} sends audit events as platform logs. For more information, see [Activity tracking for Cloud Databases](/cloud-databases?topic=cloud-databases-at_events).






## Analyzing {{site.data.keyword.databases-for}} logs
{: #cloud-logs}



In the {{site.data.keyword.logs_full_notm}} Dashboard, users can filter based on _Application_, _Subsystem_, _Severity_  to find logs specific to an instance. Users can also create a custom dashboard, view logs or write a query to search for a log data. example label.region:"us-south"

They can also create _alerts_ in the {{site.data.keyword.logs_full_notm}}.
