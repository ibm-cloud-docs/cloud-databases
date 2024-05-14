---
copyright:
  years: 2023, 2024
lastupdated: "2024-05-14"

subcollection: cloud-databases, database member, CPU seconds, platform metrics

keywords: sysdig, cpu seconds, cpu cores, common metrics

---

{{site.data.keyword.attribute-definition-list}}

# {{site.data.keyword.mon_full}} with Sysdig
{: #sysdig-monitor}

## Enabling {{site.data.keyword.mon_full}} with Sysdig
{: #sysdig-monitor-enabling}

To enable Sysdig Monitor on {{site.data.keyword.mon_full}}, follow these steps:

1. Log in to the {{site.data.keyword.cloud_notm}} console.
1. Click the **Catalog** tab.
1. In the **Category** list, select **Logging and Monitoring**.
1. Click the {{site.data.keyword.mon_full}} tile.
1. In the **Create** dialog box, do the following:
   - Select a location.
   - Select a pricing plan. For {{site.data.keyword.mon_full}} with Sysdig Monitoring, choose **Graduated Tier - Sysdig Secure + Monitor**. For more information, see [Graduated Tier - Sysdig Secure + Monitor Pricing](/docs/monitoring?topic=monitoring-pricing_plans#graduated_secure){: external}.
   - In the **Service name** field, enter a name for your monitoring instance.
1. Click Create.
1. Then, follow the process found at [Working with platform metrics](/docs/monitoring?topic=monitoring-platform_metrics_working){: external} to configure your platform metrics.

## Sysdig dashboards
{: #sysdig-monitor-dashboards}

Use dashboards to monitor your environments and applications. Sysdig dashboards are designed around time. Select your dashboard based on specific data gathered over a
set time range.

## Common metrics
{: #sysdig-monitor-dashboards-common-metrics}

Here is a detailed description about two of the common metrics across all {{site.data.keyword.databases-for}} offerings.


### CPU cores used per member
{: #sysdig-monitor-dashboards-cpu-cores-used-per-member}

The usage that is presented in this dashboard is the number of CPU cores used per member, which is measured in core seconds. This metric is available for all hosting models; you can monitor this metric for both, databases that are hosted either as a single-tenant on underlying hardware and databases running on multi-tenant hosts.
We recommend that you use this metric to track historical CPU allocation over time, which can help you to decide how many CPU cores to allocate for your database to match desired performance. 

### CPU used per member (data only available with dedicated cores)
{: #sysdig-monitor-dashboards-cpu-used-per-member}

The usage that is presented in this dashboard is a percentage of total CPU being used, based on the number of cores in your {{site.data.keyword.databases-for}} instance. For example, if you have eight cores and your usage is 12.5%, then that percentage reflects that your database member is using 1 core's worth of CPU seconds. However, this does not guarantee that your member's workload is pinned to one core – the workload might be distributed unevenly among your eight cores. In the same example, 25% usage reflects that your database member is using 2 core's worth of CPU seconds out of your available 8 cores.

## Service-specific {{site.data.keyword.databases-for}} metrics
{: #sysdig-monitor-dashboards-specific-metrics}

For metrics relevant to a particular {{site.data.keyword.databases-for}} service, see the appropriate Monitoring documentation:

- [{{site.data.keyword.databases-for-mongodb}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-mongodb){: external}.

- [{{site.data.keyword.databases-for-elasticsearch}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-elasticsearch){: external}.

- [{{site.data.keyword.databases-for-cassandra}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-datastax){: external}.

- [{{site.data.keyword.databases-for-redis}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-redis){: external}.

- [{{site.data.keyword.databases-for-postgresql}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-postgresql){: external}.

- [{{site.data.keyword.databases-for-enterprisedb}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-enterprisedb){: external}.

- [{{site.data.keyword.databases-for-mysql}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-mysql){: external}.

- [{{site.data.keyword.messages-for-rabbitmq}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-rabbitmq){: external}.

- [{{site.data.keyword.databases-for-etcd}}](/docs/cloud-databases?topic=cloud-databases-monitoring#metrics-by-plan-etcd){: external}.
