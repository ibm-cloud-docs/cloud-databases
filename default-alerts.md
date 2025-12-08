---

copyright:
  years: 2025
lastupdated: "2025-12-08"

keywords: alerts, critical alerts, configure alerts

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Default alerts reference
{: #default-alerts}

{{site.data.keyword.databases-for}} integrates with {{site.data.keyword.monitoringfull}} to provide visibility into the health and performance of your database instances. Monitoring and alerting helps administrators to detect issues early, respond to resource constraints, and maintain service reliability. Starting in December 2025, {{site.data.keyword.monitoringfull_notm}} will automatically enable a default set of up to five critical alerts for each new and existing {{site.data.keyword.databases-for}} instance when [platform metrics are enabled](https://cloud.ibm.com/docs/monitoring?topic=monitoring-platform_metrics_enabling). These alerts will monitor key resource metrics such as memory usage, disk I/O, and CPU load, and will be preconfigured to send notifications to the email of the account owner. 

This guide explains the critical alerts installed for your managed database. For each alert, we outline what the metric monitors, why it matters for performance and availability, and the recommended actions to take when the alert triggers. Use this reference to proactively manage capacity, prevent capacity or settings related outages, and maintain resiliency. 

## Setting up monitoring 
{: #default-alerts-set-up}

Default alerts are only installed if you integrate with {{site.data.keyword.monitoringfull_notm}} to gain operational visibility into the performance and health of their applications, services, and platforms. 

To begin collecting metrics for your database instance: 

1. Provision an instance of [{{site.data.keyword.monitoringfull_notm}}](https://cloud.ibm.com/observability/catalog/ibm-cloud-monitoring).
1. Enable **Platform metrics** in the same region as your database instance.
1. Access your monitoring dashboards from the [{{site.data.keyword.monitoringfull_notm}}](https://cloud.ibm.com/observability/catalog/ibm-cloud-monitoring) section in the Cloud console under Observability.

Metrics for instances in multi-zone regions (MZRs) are available in-region. For single-zone regions (SZRs), metrics are forwarded to a designated MZR, for example *che01*.
{: note}

For more information, see [{{site.data.keyword.databases-for}}{{site.data.keyword.monitoringfull_notm}} integration](/docs/cloud-databases?topic=cloud-databases-monitoring).

## Critical alerts: Benefits and response guidance
{: #default-alerts-critical}

{{site.data.keyword.databases-for}} provide a set of common and service-specific metrics to help you monitor performance and resource usage. Every metric supported by each database is listed in the Observability section of the documentation. For a few of critical metrics, at least one alert is set up to notify you when thresholds are exceeded. These alerts are explained below. To see the full list of metrics for each database, see the [ICD monitoring integration](/docs/cloud-databases?topic=cloud-databases-monitoring). 

### PostgreSQL alerts
{: #default-alerts-postgresql}

| Alert   | Condition   | Explanation   |
| ------- | ----------- | ------------- |
| PostgreSQL CPU usage is greater than 90%  \n `avg by (ibm_service_instance_name,  \n ibm_service_instance, ibm_scope, ibm_resource)  \n (avg_over_time  \n (ibm_databases_for_postgresql_cpu_used_percent[10m])) > 0.9` | &amp;gt; 0.95 | This metric tracks CPU usage for {{site.data.keyword.databases-for-postgresql}}. When usage stays above 90%, the database may slow down, stall transactions, or cause application timeouts. Sustained CPU pressure is often due to inefficient queries, large workloads, or insufficient resources. Review and optimize expensive queries or scale compute resources to restore headroom. |
| PostgreSQL disk usage is greater than 80%  \n `max by (ibm_service_instance_name,  \n ibm_service_instance, ibm_scope)  \n (avg_over_time  \n (ibm_databases_for_postgresql_disk_used_percent[10m])) > 0.8` | &amp;gt; 0.80 | Tracks the maximum disk usage across {{site.data.keyword.databases-for-postgresql}} instances. Above 80%, at least one instance is critically close to running out of space, risking blocked transactions and degraded performance. Expand storage, archive or purge unused data immediately. |
{: caption="PostgreSQL alerts" caption-side="top"}

---

### MongoDB alerts
{: #default-alerts-mongodb}

| Alert | Condition | Explanation |
|-------|-----------|-------------|
| MongoDB CPU usage is greater than 90%  \n `avg by (ibm_service_instance_name, ibm_service_instance,  \n ibm_scope, ibm_resource) (avg_over_time  \n (ibm_databases_for_mongodb_cpu_used_percent[10m])) > 0.9` | &amp;gt; 0.90 | CPU usage above 90% in {{site.data.keyword.databases-for-mongodb}} signals heavy query load or insufficient capacity. Sustained pressure impacts replication lag, write throughput, and query latency. Review slow queries with profiling tools, shard or index data where needed, or scale the instance’s CPU resources. |
| MongoDB disk usage is greater than 90%  \n `max by (ibm_service_instance_name,  \n ibm_service_instance, ibm_scope)  \n (avg_over_time  \n (ibm_databases_for_mongodb_disk_used_percent[10m])) > 0.9` | &amp;gt; 0.90 | This metric tracks the maximum {{site.data.keyword.databases-for-mongodb}} disk usage across instances. At greater than 90%, journaling, replication, and storage engine operations may fail. {{site.data.keyword.databases-for-mongodb}} requires free space for internal writes and recovery operations. Expand storage, archive or purge unused collections to prevent write failures. |
| MongoDB connection count is greater than 1000  \n `sum by (ibm_service_instance_name,  \n ibm_service_instance, ibm_scope) (avg_over_time  \n (ibm_databases_for_mongodb_connections[10m])) > 1000` | &amp;gt; 1000 | This metric shows active client connections to {{site.data.keyword.databases-for-mongodb}}. Surpassing 1,000 connections may overwhelm available resources, leading to errors or degraded performance. Connection surges often come from unpooled apps or misbehaving clients. Implement connection pooling and, if needed, scale the instance to handle demand. |
{: caption="MongoDB alerts" caption-side="top"}

---

### MySQL alerts
{: #default-alerts-mysql}

| Alert | Condition | Explanation |
|-------|-----------|-------------|
| MySQL CPU Usage is greater than 95%  \n `avg by (ibm_service_instance_name,  \n ibm_service_instance, ibm_scope,  \n ibm_resource) (avg_over_time  \n  (ibm_databases_for_mysql_cpu_used_percent[10m])) > 0.95`| &amp;gt; 0.95 | {{site.data.keyword.databases-for-mysql}} CPU above 95% indicates that the system is overloaded with queries or background processes. This can delay transactions and degrade application performance. Tune inefficient queries (for example, via EXPLAIN plans) or scale compute capacity to handle demand. |
| MySQL disk usage is greater than 90%  \n `max by(ibm_service_instance_name,  \n ibm_service_instance, ibm_scope)  \n (avg_over_time  \n (ibm_databases_for_mysql_disk_used_percent[10m])) > 0.9` | &amp;gt; 0.90 | Maximum disk usage exceeding 90% indicates at least one {{site.data.keyword.databases-for-mysql}} instance is critically close to running out of space. This can halt transactions and degrade stability. Add storage immediately, purge or archive unused tables to reduce pressure. |
| MySQL connection count is above 95% of total available  \n `avg by (ibm_service_instance_name, ibm_service_instance,  \n ibm_scope) (avg_over_time  \n (ibm_databases_for_mysql_connection_used_percent[10m])) > 0.95` | &amp;gt; 0.95 | This metric tracks percentage of used {{site.data.keyword.databases-for-mysql}} connections. When it reaches 100%, new clients will be blocked, leading to connection errors. When connection usage exceeds 95%, increase max_connections cautiously or adopt connection pooling to avoid overload. |
{: caption="MySQL alerts" caption-side="top"}

---

### Elasticsearch alerts
{: #default-alerts-elasticsearch}

| Alert | Condition | Explanation |
|-------|-----------|-------------|
| Elasticsearch CPU Usage is greater than 95%  \n `avg by (ibm_service_instance_name, ibm_service_instance,  \n ibm_scope, ibm_resource) (avg_over_time  \n (ibm_databases_for_elasticsearch_cpu_used_percent[10m])) > 0.95` | &amp;gt; 0.95 | {{site.data.keyword.databases-for-elasticsearch}} CPU usage above 95% affects indexing, queries, and cluster responsiveness. Sustained overload risks node instability. Optimize queries, reduce shard counts, or scale compute resources. |
| Elasticsearch cluster status is red  \n `avg by (ibm_service_instance_name,  \n ibm_service_instance, ibm_scope) \n (avg_over_time  \n ibm_databases_for_elasticsearch_cluster_status[10m])) == 0` | = 0 | Cluster status = 0 indicates that {{site.data.keyword.databases-for-elasticsearch}} is red, meaning primary shards are missing or unassigned. This poses a risk of data loss. Check node health, ensure sufficient disk space, and reallocate shards. |
| Elasticsearch disk usage is greater than 80%  \n `max by (ibm_service_instance_name,  \n ibm_service_instance, ibm_scope) (avg_over_time  \n (ibm_databases_for_elasticsearch_disk_used_percent[10m])) > 0.8` | &amp;gt; 0.80 | {{site.data.keyword.databases-for-elasticsearch}} disk above 80% prevents new indices or replicas and risks cluster instability. Free space is vital for shard balancing and merging. Expand storage, delete or archive old indices. |
| Elasticsearch JVM heap usage is greater than 95%  \n `avg by (ibm_service_instance_name,  \n ibm_service_instance, ibm_scope, ibm_resource)  \n (avg_over_time  \n (ibm_databases_for_elasticsearch_jvm_heap_percent[10m])) > 95` | &amp;gt; 95 | JVM heap above 95% in {{site.data.keyword.databases-for-elasticsearch}} indicates garbage collection pressure and risk of node crashes. Increase heap size cautiously, optimize queries, or scale the cluster to distribute load. |
{: caption="Elasticsearch alerts" caption-side="top"}

---

### Redis alerts
{: #default-alerts-alerts}

| Alert | Condition | Explanation |
|-------|-----------|-------------|
| Redis memory usage is greater than 85%  \n `max by (ibm_service_instance_name,  \n ibm_service_instance, ibm_scope)  \n (avg_over_time  \n (ibm_databases_for_redis_memory_used_percent[10m])) > 0.85` | &amp;gt; 0.85 | {{site.data.keyword.databases-for-redis}} is memory-driven, and usage above 85% risks forced key evictions or OOM errors. High memory pressure can cause unpredictable data loss if eviction policies are triggered. Scale the memory allocation or enforce TTL/eviction policies aligned with application needs. |
| Redis disk usage is greater than 80%  \n `max by (ibm_service_instance_name,  \n ibm_service_instance, ibm_scope)  \n (avg_over_time  \n (ibm_databases_for_redis_disk_used_percent[10m])) > 0.80` | &amp;gt; 0.80 | {{site.data.keyword.databases-for-redis}} persistence relies on disk space for snapshots and AOF logs. At greater than 80% usage, data persistence may fail, risking durability. Expand storage capacity or clean up unnecessary keys and backups. |
| Redis connection count is greater than 9500  \n `avg by (ibm_service_instance_name,  \n ibm_service_instance, ibm_scope, ibm_resource) \n (avg_over_time  \n (ibm_databases_for_redis_connected_clients[10m])) > 9500` | &amp;gt; 9500 | This metric measures the number of connected {{site.data.keyword.databases-for-redis}} clients. Surpassing 9,500 can overwhelm networking resources, slow responses, or cause dropped connections. Ensure efficient client pooling and scale {{site.data.keyword.databases-for-redis}} instances if the workload requires more connections. |
{: caption="Redis alerts" caption-side="top"}

---

### RabbitMQ alerts
{: #default-alerts-rabbitmq}

| Alert | Condition | Explanation |
|-------|-----------|-------------|
| RabbitMQ CPU usage is greater than 95%  \n `avg by (ibm_service_instance_name, ibm_service_instance,  \n ibm_scope, ibm_resource)  \n (avg_over_time(ibm_messages_for_rabbitmq_cpu_used_percent[10m])) > 0.95` | &amp;gt; 0.95 | {{site.data.keyword.messages-for-rabbitmq}} CPU above 95% suggests the broker is overloaded by message throughput or routing. Sustained CPU saturation risks slowdowns or dropped messages. Scale compute or optimize routing/queues. |
| `avg(avg \n (ibm_messages_for_rabbitmq_disk_used_percent))` | &amp;gt; 0.85 | {{site.data.keyword.messages-for-rabbitmq}} relies on disk for message durability. Above 85% usage, queues may block publishers or lose messages. Expand disk capacity or clear unused queues. |
| RabbitMQ disk usage is greater than 85%  \n `max by (ibm_service_instance_name, ibm_service_instance,  \n ibm_scope)  (avg_over_time  \n (ibm_messages_for_rabbitmq_disk_used_percent[10m])) > 0.85` | &amp;gt; 0.85 | Maximum {{site.data.keyword.messages-for-rabbitmq}} disk usage over 85% indicates some nodes are nearly full, risking message persistence failures. Add disk capacity or purge old/unconsumed queues immediately. |
{: caption="RabbitMQ alerts" caption-side="top"}

## Configure alerts 
{: #default-alerts-configure}

You can modify, test, silence or delete individual alerts. In addition, {{site.data.keyword.databases-for}} default alerts can be disabled per database or as a whole in your {{site.data.keyword.monitoringfull_notm}} dashboard under **Alerts** on the left navigation panel. You can customize alert thresholds for your workloads and explore the full [Alerts library](/docs/monitoring?topic=monitoring-alert-library) for deeper insights and proactive monitoring with pre-configured alerts and best practices.

## Next steps
{: #default-alerts-next-steps}

Default alerts for {{site.data.keyword.databases-for}} only cover critical alerts, chosen based on proven patterns observed across enterprise scale deployments. For most customers using their databases effectively, no additional notifications will be routed to their inbox. To ensure you are receiving these critical notifications, verify that your notification channels are correctly conigured by adding and managing multiple notification channels. For instructions on how to do this, see [Working with notification channels](/docs/monitoring?topic=monitoring-notifications){: external}. 
