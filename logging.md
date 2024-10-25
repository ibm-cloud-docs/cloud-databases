---

copyright:
  years: 2018, 2024
lastupdated: "2024-10-25"

keywords:

subcollection: repo-name

---

{{site.data.keyword.attribute-definition-list}}

_Include your logging topic in an Observability topic group in the How to nav group in your toc.yaml file._



# Logging for _service-name_
{: #logging}

{{site.data.keyword.cloud_notm}} services, such as _service-name_, generate platform logs that you can use to investigate abnormal activity and critical actions in your account, and troubleshoot problems.
{: shortdesc}

You can use {{site.data.keyword.logs_routing_full_notm}}, a platform service, to route platform logs in your account to a destination of your choice by configuring a tenant that defines where platform logs are sent. For more information, see [About Logs Routing](/docs/logs-router?topic=logs-router-about).

You can use {{site.data.keyword.logs_full_notm}} to visualize and alert on platform logs that are generated in your account and routed by {{site.data.keyword.logs_routing_full_notm}} to an {{site.data.keyword.logs_full_notm}} instance.



As of 28 March 2024, the {{site.data.keyword.la_full_notm}} service is deprecated and will no longer be supported as of 30 March 2025. Customers will need to migrate to {{site.data.keyword.logs_full_notm}} before 30 March 2025. During the migration period, customers can use {{site.data.keyword.la_full_notm}} along with {{site.data.keyword.logs_full_notm}}. Logging is the same for both services. For information about migrating from {{site.data.keyword.la_full_notm}} to {{site.data.keyword.logs_full_notm}} and running the services in parallel, see [migration planning](/docs/cloud-logs?topic=cloud-logs-migration-intro).
{: important}

## Locations where platform logs are generated
{: #log-locations}



### Locations where logs are sent to {{site.data.keyword.la_full_notm}}
{: #la-legacy-locations}



_service-name_ sends platform logs to {{site.data.keyword.la_full_notm}} in the regions indicated in the following table.

| Dallas (`us-south`) | Washington (`us-east`)  | Toronto (`ca-tor`) | Sao Paulo (`br-sao`) |
|---------------------|-------------------------|-------------------|----------------------|
| [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where platform logs are sent in Americas locations" caption-side="top"}
{: #la-table-1}
{: tab-title="Americas"}
{: tab-group="la"}
{: class="simple-tab-table"}
{: row-headers}

| Tokyo (`jp-tok`)    | Sydney (`au-syd`) |  Osaka (`jp-osa`) | Chennai (`in-che`) |
|---------------------|------------------|------------------|--------------------|
| [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where platform logs are sent in Asia Pacific locations" caption-side="top"}
{: #la-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="la"}
{: class="simple-tab-table"}
{: row-headers}

| Frankfurt (`eu-de`)  | London (`eu-gb`) | Madrid (`eu-es`) |
|---------------------------------------------------------------|---------------------|------------------|
| [Yes]{: tag-green} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where platform logs are sent in Europe locations" caption-side="top"}
{: #la-table-3}
{: tab-title="Europe"}
{: tab-group="la"}
{: class="simple-tab-table"}
{: row-headers}

## Locations where logs are sent by {{site.data.keyword.logs_routing_full_notm}}
{: #lr-locations}



_service-name_ sends logs by {{site.data.keyword.logs_routing_full_notm}} in the regions that are indicated in the following table.

| Dallas (`us-south`) | Washington (`us-east`)  | Toronto (`ca-tor`) | Sao Paulo (`br-sao`) |
|---------------------|-------------------------|-------------------|----------------------|
| [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where platform logs are sent in Americas locations" caption-side="top"}
{: #lr-table-1}
{: tab-title="Americas"}
{: tab-group="lr"}
{: class="simple-tab-table"}
{: row-headers}

| Tokyo (`jp-tok`)    | Sydney (`au-syd`) |  Osaka (`jp-osa`) | Chennai (`in-che`) |
|---------------------|------------------|------------------|--------------------|
| [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where platform logs are sent in Asia Pacific locations" caption-side="top"}
{: #lr-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="lr"}
{: class="simple-tab-table"}
{: row-headers}

| Frankfurt (`eu-de`)  | London (`eu-gb`) | Madrid (`eu-es`) |
|---------------------------------------------------------------|---------------------|------------------|
| [Yes]{: tag-green} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where platform logs are sent in Europe locations" caption-side="top"}
{: #lr-table-3}
{: tab-title="Europe"}
{: tab-group="lr"}
{: class="simple-tab-table"}
{: row-headers}

## Platform logs that are generated
{: #log-platform}






## Enabling logging
{: #log-enable}









## Viewing logs
{: #log-viewing}



### Launching {{site.data.keyword.logs_full_notm}} from the _service-name_ dashboard
{: #log-launch-integrated}



### Launching {{site.data.keyword.logs_full_notm}} from the Observability page
{: #log-launch-standalone}



For more information about launching the {{site.data.keyword.logs_full_notm}} UI, see [Launching the UI in the {{site.data.keyword.logs_full_notm}} documentation.](/docs/cloud-logs?topic=cloud-logs-instance-launch)

## Fields by log type
{: #log-fields}



For information about fields included in every platform log, see [Fields for platform logs](/docs/logs-router?topic=logs-router-about-platform-logs#platform_reqd)










## Log messages
{: #log_messages}



The following tables list the message IDs that are generated and additional information available about these messages.

| Message ID | Type | Learn More |
|------------|------|------------|
| `is.flow-log-collector.00001E` | error | Failed to write a Flow log file for the past 24 hours. Dropping flow log for Virtual Server _ServerName_ |
{: caption="Additional information about message IDs" caption-side="top"}


## Analyzing _service-name_ logs
{: #cloud-logs}


