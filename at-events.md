---

copyright:
  years: 2018, 2024
lastupdated: "2024-10-25"

keywords:

subcollection: repo-name

---

{{site.data.keyword.attribute-definition-list}}

_Include your activity tracking events file in an Observability topic group in the How to nav group in your toc.yaml file._



# Activity tracking events for _service-name_
{: #at_events}



{{site.data.keyword.cloud_notm}} services, such as _service-name_, generate activity tracking events.
{: shortdesc}

Activity tracking events report on activities that change the state of a service in {{site.data.keyword.cloud_notm}}. You can use the events to investigate abnormal activity and critical actions and to comply with regulatory audit requirements.

You can use {{site.data.keyword.atracker_full_notm}}, a platform service, to route auditing events in your account to destinations of your choice by configuring targets and routes that define where activity tracking events are sent. For more information, see [About {{site.data.keyword.atracker_full_notm}}](/docs/atracker?topic=atracker-about).

You can use {{site.data.keyword.logs_full_notm}} to visualize and alert on events that are generated in your account and routed by {{site.data.keyword.atracker_full_notm}} to an {{site.data.keyword.logs_full_notm}} instance.



As of 28 March 2024, the {{site.data.keyword.at_full_notm}} service is deprecated and will no longer be supported as of 30 March 2025. Customers will need to migrate to {{site.data.keyword.logs_full_notm}} before 30 March 2025. During the migration period, customers can use {{site.data.keyword.at_full_notm}} along with {{site.data.keyword.logs_full_notm}}. Activity tracking events are the same for both services. For information about migrating from {{site.data.keyword.at_full_notm}} to {{site.data.keyword.logs_full_notm}} and running the services in parallel, see [migration planning](/docs/cloud-logs?topic=cloud-logs-migration-intro).
{: important}

## Locations where activity tracking events are generated
{: #at-locations}



### Locations where activity tracking events are sent to {{site.data.keyword.at_full_notm}} hosted event search
{: #at-legacy-locations}



_Service-name_ sends activity tracking events to {{site.data.keyword.at_full_notm}} hosted event search in the regions that are indicated in the following table.

| Dallas (`us-south`) | Washington (`us-east`)  | Toronto (`ca-tor`) | Sao Paulo (`br-sao`) |
|---------------------|-------------------------|-------------------|----------------------|
| [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where activity tracking events are sent in Americas locations" caption-side="top"}
{: #at-table-1}
{: tab-title="Americas"}
{: tab-group="at"}
{: class="simple-tab-table"}
{: row-headers}

| Tokyo (`jp-tok`)    | Sydney (`au-syd`) |  Osaka (`jp-osa`) | Chennai (`in-che`) |
|---------------------|------------------|------------------|--------------------|
| [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where activity tracking events are sent in Asia Pacific locations" caption-side="top"}
{: #at-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="at"}
{: class="simple-tab-table"}
{: row-headers}

| Frankfurt (`eu-de`)  | London (`eu-gb`) | Madrid (`eu-es`) |
|---------------------------------------------------------------|---------------------|------------------|
| [Yes]{: tag-green} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where activity tracking events are sent in Europe locations" caption-side="top"}
{: #at-table-3}
{: tab-title="Europe"}
{: tab-group="at"}
{: class="simple-tab-table"}
{: row-headers}

### Locations where activity tracking events are sent by {{site.data.keyword.atracker_full_notm}}
{: #atracker-locations}



_service-name_ sends activity tracking events by {{site.data.keyword.atracker_full_notm}} in the regions that are indicated in the following table.

| Dallas (`us-south`) | Washington (`us-east`)  | Toronto (`ca-tor`) | Sao Paulo (`br-sao`) |
|---------------------|-------------------------|-------------------|----------------------|
| [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where activity tracking events are sent in Americas locations" caption-side="top"}
{: #atracker-table-1}
{: tab-title="Americas"}
{: tab-group="atracker"}
{: class="simple-tab-table"}
{: row-headers}

| Tokyo (`jp-tok`)    | Sydney (`au-syd`) |  Osaka (`jp-osa`) | Chennai (`in-che`) |
|---------------------|------------------|------------------|--------------------|
| [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where activity tracking events are sent in Asia Pacific locations" caption-side="top"}
{: #atracker-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="atracker"}
{: class="simple-tab-table"}
{: row-headers}

| Frankfurt (`eu-de`)  | London (`eu-gb`) | Madrid (`eu-es`) |
|---------------------------------------------------------------|---------------------|------------------|
| [Yes]{: tag-green} | [No]{: tag-red} | [No]{: tag-red} |
{: caption="Regions where activity tracking events are sent in Europe locations" caption-side="top"}
{: #atracker-table-3}
{: tab-title="Europe"}
{: tab-group="atracker"}
{: class="simple-tab-table"}
{: row-headers}

## Enabling activity tracking events for _service-name_
{: #at-enable}







## Viewing activity tracking events for _service-name_
{: #at-viewing}



You can use {{site.data.keyword.logs_full_notm}} to visualize and alert on events that are generated in your account and routed by {{site.data.keyword.atracker_full_notm}} to an {{site.data.keyword.logs_full_notm}} instance.

### Launching {{site.data.keyword.logs_full_notm}} from the _service-name_ dashboard
{: #log-launch-integrated}



### Launching {{site.data.keyword.logs_full_notm}} from the Observability page
{: #log-launch-standalone}



For information on launching the {{site.data.keyword.logs_full_notm}} UI, see [Launching the UI in the {{site.data.keyword.logs_full_notm}} documentation.](/docs/cloud-logs?topic=cloud-logs-instance-launch)


## List of platform events
{: #at_actions_platform}



The following table lists the activity tracking event actions that the {{site.data.keyword.cloud_notm}} platform generates _service-name_ instances are processed.

| Action                                   | Description |
|------------------------------------------|---------|
| `<service-name>.instance.create`           | An event is generated when you provision a service instance. |
| `<service-name>.instance.update`           | An event is generated when you rename a service instance or when you change the service plan. |
| `<service-name>.instance.delete`           | An event is generated when a service instance is deleted. |
| `<service-name>.instance.schedule_reclaim` | An event is generated when a service instance is pending_reclamation. |
| `<service-name>.instance.restore`          | An event is generated when a service instance is restored. |
{: caption="Actions that generate platform events" caption-side="bottom"}

The following table lists the actions that generate an event for managing service credentials that are associated with a service instance.

| Action                         | Description |
|--------------------------------|---------|
| `<service_name>.key.create` | An event is generated when an API key is created for a service instance through the *Service credentials* section of the service instance UI. |
| `<service_name>.key.delete` | An event is generated when an API key that is associated with a service instance is deleted from the *Service credentials* section of the service instance UI. |
{: caption="Actions that generate service credentials events" caption-side="bottom"}


## List of management events
{: #at_actions}



| Action             | Description      |
|--------------------|------------------|
|                    |                  |
{: caption="Actions that generate management events" caption-side="bottom"}

## List of data events
{: #at_actions_data}



| Action                           | Description                        |
|----------------------------------|------------------------------------|
|                                  |                                    |
{: caption="Actions that generate data events" caption-side="bottom"}






## Events for component X
{: #at_actions_x}



| Action                           | Description                        |
|----------------------------------|------------------------------------|
|                                  |                                    |
{: caption="Lists of management events" caption-side="bottom"}
{: #componentX-table-1}
{: tab-title="Management events"}
{: tab-group="componentX"}
{: class="simple-tab-table"}
{: row-headers}

| Action                           | Description                        |
|----------------------------------|------------------------------------|
|                                  |                                    |
{: caption="Lists of data events" caption-side="bottom"}
{: #componentX-table-2}
{: tab-title="Data events"}
{: tab-group="componentX"}
{: class="simple-tab-table"}
{: row-headers}

## Events for component Y
{: #at_actions_x}



| Action                           | Description                        |
|----------------------------------|------------------------------------|
|                                  |                                    |
{: caption="Lists of management events" caption-side="bottom"}
{: #componentY-table-1}
{: tab-title="Management events"}
{: tab-group="componentY"}
{: class="simple-tab-table"}
{: row-headers}

| Action                           | Description                        |
|----------------------------------|------------------------------------|
|                                  |                                    |
{: caption="Lists of data events" caption-side="bottom"}
{: #componentY-table-2}
{: tab-title="Data events"}
{: tab-group="componentY"}
{: class="simple-tab-table"}
{: row-headers}


## Analyzing _service-name_ activity tracking events
{: #at_events_iam_analyze}


