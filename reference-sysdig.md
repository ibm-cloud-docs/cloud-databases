---
copyright:
  years: 2023
lastupdated: "2023-07-17"

subcollection: cloud-databases, database member, CPU seconds, platform metrics

keywords: sysdig

---

{{site.data.keyword.attribute-definition-list}}

# IBM Cloud Monitor Sysdig
{: #sysdig-monitor}

## Enabling {{site.data.keyword.mon_full}} with Sysdig
{: #sysdig-monitor-enabling}

To enable Sysdig Monitor on {{site.data.keyword.mon_full}}, follow these steps: 

1. Log in to the {{site.data.keyword.cloud_notm}} console.
1. Click the **Catalog** tab.
1. In the **Category** list, select *Logging and Monitoring*.
1. Click the {{site.data.keyword.mon_full}} tile.
1. In the **Create** dialog box, do the following:
   - Select a location.
   - Select a pricing plan. For {{site.data.keyword.mon_full}} with Sysdig Monitoring, choose **Graduated Tier - Sysdig Secure + Monitor**. For more information, see [Graduated Tier - Sysdig Secure + Monitor Pricing](/docs/monitoring?topic=monitoring-pricing_plans#graduated_secure){: external}.
   - In the **Service name** field, enter a name for your monitoring instance.
1. Click Create.
1. Then, follow the process found at [Working with platform metrics](/docs/monitoring?topic=monitoring-platform_metrics_working){: external} to configure your platform metrics.

## Sysdig Dashboards
{: #sysdig-monitor-dashboards}

### CPU used per member (data only available with dedicated cores)
{: #sysdig-monitor-dashboards-cpu-used-per-member}

The usage that is presented in this dashboard is a percentage of total CPU being used, based on the number of cores in your {{site.data.keyword.databases-for}} instance. For example, if you have eight cores and your usage is 12.5%, then that percentage reflects that your database member is using 1 core's worth of CPU seconds; however, that does not guarantee that your member's workload is pinned to one core – the workload might be distributed unevenly among your eight cores. In the same example, 25% usage reflects that your database member is using 2 core's worth of CPU seconds out of your available 8 cores.
