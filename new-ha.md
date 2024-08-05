---

copyright:
  years: 2023
lastupdated: "2023-08-31"

subcollection: cloud-databases

keywords: HA for cloud-databases, DR for cloud-databases, high availability for cloud-databases, disaster recovery for cloud-databases, failover for cloud-databases

---

{{site.data.keyword.attribute-definition-list}}



# Understanding high availability for {{site.data.keyword.databases-for}}
{: #ha}

[High availability](#x2284708){: term} (HA) is a core discipline in an IT infrastructure to keep your apps up and running, even after a partial or full site failure. The main purpose of high availability is to eliminate potential points of failures in an IT infrastructure.
{: shortdesc}

## Responsibilities
{: #ha-responsibilities}

To find out more about responsibility ownership for using {{site.data.keyword.databases-for}} and the customer, see [Responsibilities for {{site.data.keyword.databases-for}}](/docs/cloud-databases?topic=cloud-databases-responsibilities-cloud-databases){: external}.

To find out more about responsibility ownership for using {{site.data.keyword.cloud}} products between {{site.data.keyword.IBM_notm}} and the customer, see [Shared responsibilities for {{site.data.keyword.cloud_notm}} products](/docs/overview?topic=overview-shared-responsibilities).

## What level of availability do I need?
{: #ha-level}

You can achieve high availability on different levels in your IT infrastructure and within different components of your cluster. The level of availability that is right for you depends on several factors, such as your business requirements, the service level agreements (SLAs) that you have with your customers, and the resources that you want to expend.

## Application-level high availability
{: #ha-app-ha}

Applications that communicate over networks and cloud services are subject to transient connection failures. Design your applications to retry connections when errors are caused by a temporary loss in connectivity to your deployment or to {{site.data.keyword.cloud}}.

Because {{site.data.keyword.databases-for}} is a managed service, regular updates and database maintenance occur as part of normal operations. Such maintenance can occasionally cause short intervals where your database is disabled.

Your applications must be designed to handle temporary interruptions to the database, implement error handling for failed database commands, and implement retry logic to recover from a temporary interruption.

Several minutes of database unavailability or connection interruptions are not expected. Open a support ticket with details if you have time periods longer than a minute with no connectivity so we can investigate.

If you have deployments in more than one region, you must provision {{site.data.keyword.monitoringlong}} and enable platform metrics in each region.

## What level of availability does {{site.data.keyword.cloud_notm}} offer?
{: #ha-service}

The level of availability that you set up for your cluster impacts your coverage under the {{site.data.keyword.cloud_notm}} high availability service level agreement terms.

Service level objectives (SLOs) describe the design points that the {{site.data.keyword.cloud_notm}} services are engineered to meet. {{site.data.keyword.databases-for}} is designed to achieve the following availability target.

| Availability target | Target Value   |
|---|---|
|  Availability % |   |
{: caption="Table 1. SLO for {{site.data.keyword.databases-for}}" caption-side="bottom"}

The SLO is not a warranty and {{site.data.keyword.IBM_notm}} will not issue credits for failure to meet an objective. Refer to the SLAs for commitments and credits that are issued for failure to meet any committed SLAs. For a summary of all SLOs, see [{{site.data.keyword.cloud_notm}} service level objectives](/docs/overview?topic=overview-slo).

## Locations
{: #ha-locations}

For more information about service availability within regions and data centers, see [Service and infrastructure availability by location](/docs/overview?topic=overview-services_region).
