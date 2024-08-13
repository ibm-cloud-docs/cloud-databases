---
copyright:
  years: 2023, 2024
lastupdated: "2024-08-13"

keywords: monitoring

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}


# Monitoring integration
{: #monitoring}

Monitoring for {{site.data.keyword.databases-for}} is provided through integration with the {{site.data.keyword.monitoringfull}} service. Your instances forward select information so that you can monitor instance health and resource usage. To start collecting and viewing monitoring data, follow the instructions to enable [Platform Metrics](/docs/monitoring?topic=monitoring-platform_metrics_enabling). Platform Metrics need to be enabled in the same region as your instance. If you have instances in more than one region, provision {{site.data.keyword.monitoringfull_notm}} and enable platform metrics in each region.

You can then access your monitoring dashboard for each region from the {{site.data.keyword.monitoringfull_notm}} area in the Cloud Console (under Observability).

{{site.data.keyword.monitoringfull_notm}} is available for instances in every region. Instances in Multi-zone Regions (MZRs) - `eu-gb`, `eu-de`, `us-east`, `us-south`, `jp-tok`, `au-syd` - have their metrics in the same region.
If you have instances that are in a Single-zone Region (SZR) (e.g. `che01`) then your logs are forwarded to an {{site.data.keyword.monitoringfull_notm}} instance in another region. You need to provision monitoring instances in the region where your metrics are forwarded to. Metrics for instances in `che01` go to `jp-tok`.
{: note}

Use {{site.data.keyword.mon_full_notm}} dashboards to monitor your environments and applications. {{site.data.keyword.mon_full_notm}} dashboards are designed around time. Select your dashboard based on specific data gathered over a set time range.


## Common metrics
{: #sysdig-monitor-dashboards-common-metrics}

Here is a detailed description about two of the common metrics across all {{site.data.keyword.databases-for}} offerings.

### CPU cores used per member
{: #sysdig-monitor-dashboards-cpu-cores-used-per-member}

The usage that is presented in this dashboard is the number of CPU cores used per member, which is measured in core seconds. This metric is available for all hosting models; you can monitor this metric for both, databases that are hosted either as a single-tenant on underlying hardware and databases running on multi-tenant hosts.
We recommend that you use this metric to track historical CPU allocation over time, which can help you to decide how many CPU cores to allocate for your database to match desired performance. 

### CPU used per member (data only available with dedicated cores)
{: #sysdig-monitor-dashboards-cpu-used-per-member}

The usage that is presented in this dashboard is a percentage of total CPU being used, based on the number of cores in your {{site.data.keyword.databases-for}} instance. For example, if you have 8 cores and your usage is 12.5%, then that percentage reflects that your database member is using 1 core's worth of CPU seconds. However, this does not guarantee that your member's workload is pinned to 1 core – the workload might be distributed unevenly among your 8 cores. In the same example, 25% usage reflects that your database member is using 2 core's worth of CPU seconds out of your available 8 cores.


## Metrics available by Service Plan
{: #metrics-by-plan}

## MongoDB Metrics
{: #metrics-by-plan-mongodb}

| Metric Name |
|-----------|
| [MongoDB Average time spent acquiring locks in microseconds](#ibm_databases_for_mongodb_locks_time_acquiring_microseconds_W_average) |
| [MongoDB Average time spent acquiring locks in microseconds](#ibm_databases_for_mongodb_locks_time_acquiring_microseconds_total_average) |
| [MongoDB Connections](#ibm_databases_for_mongodb_connections) |
| [MongoDB Disk read latency mean](#ibm_databases_for_mongodb_disk_read_latency_mean) |
| [MongoDB Disk write latency mean](#ibm_databases_for_mongodb_disk_write_latency_mean) |
| [MongoDB IO utilization in percent 15-minute average](#ibm_databases_for_mongodb_disk_io_utilization_percent_average_15m) |
| [MongoDB IO utilization in percent 30-minute average](#ibm_databases_for_mongodb_disk_io_utilization_percent_average_30m) |
| [MongoDB IO utilization in percent 5-minute average](#ibm_databases_for_mongodb_disk_io_utilization_percent_average_5m) |
| [MongoDB IO utilization in percent 60-minute average](#ibm_databases_for_mongodb_disk_io_utilization_percent_average_60m) |
| [MongoDB IOPS read and write total count for an instance](#ibm_databases_for_mongodb_disk_iops_read_write_total) |
| [MongoDB Maximum allowed memory for an instance](#ibm_databases_for_mongodb_memory_limit_bytes) |
| [MongoDB Oplog gigabyte per hour](#ibm_databases_for_mongodb_oplog_gb_per_hour) |
| [MongoDB Oplog used bytes](#ibm_databases_for_mongodb_oplog_used_bytes) |
| [MongoDB Oplog used bytes percent of total](#ibm_databases_for_mongodb_oplog_used_bytes_percent) |
| [MongoDB Oplog window hours](#ibm_databases_for_mongodb_oplog_window_hours) |
| [MongoDB Page faults](#ibm_databases_for_mongodb_page_faults) |
| [MongoDB Process resident memory in bytes](#ibm_databases_for_mongodb_process_resident_memory_bytes) |
| [MongoDB Process virtual memory in bytes](#ibm_databases_for_mongodb_process_virtual_memory_bytes) |
| [MongoDB Replica set member state](#ibm_databases_for_mongodb_status) |
| [MongoDB Replication lag](#ibm_databases_for_mongodb_replica_lag) |
| [MongoDB Total disk space for an instance](#ibm_databases_for_mongodb_disk_total_bytes) |
| [MongoDB Used CPU for an instance](#ibm_databases_for_mongodb_cpu_used_percent) |
| [MongoDB Used disk space for an instance](#ibm_databases_for_mongodb_disk_used_bytes) |
| [MongoDB Used disk space for an instance](#ibm_databases_for_mongodb_disk_used_percent) |
| [MongoDB Used memory for an instance](#ibm_databases_for_mongodb_memory_used_bytes) |
| [MongoDB Used memory for an instance](#ibm_databases_for_mongodb_memory_used_percent) |
{: caption="Table 1: Metrics Available by Plan Names" caption-side="top"}

### MongoDB Metric Descriptions
{: #metrics-by-plan-mongodb-desc}

#### MongoDB Average time spent acquiring locks in microseconds total W-average
{: #ibm_databases_for_mongodb_locks_time_acquiring_microseconds_W_average}

Average time spent acquiring locks in microseconds

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_locks_time_acquiring_microseconds_W_average`|
| `Metric Type` | `gauge` |
| `Value Type`  | `second` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 2: Average time spent acquiring locks in microseconds metric metadata" caption-side="top"}

#### MongoDB Average time spent acquiring locks in microseconds total_average
{: #ibm_databases_for_mongodb_locks_time_acquiring_microseconds_total_average}

Average time spent acquiring locks in microseconds

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_locks_time_acquiring_microseconds_total_average`|
| `Metric Type` | `gauge` |
| `Value Type`  | `second` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 3: Average time spent acquiring locks in microseconds metric metadata" caption-side="top"}

#### MongoDB Connections
{: #ibm_databases_for_mongodb_connections}

The number of connections to the database

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_connections`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 16: Connections metric metadata" caption-side="top"}

#### MongoDB Disk read latency mean
{: #ibm_databases_for_mongodb_disk_read_latency_mean}

Disk read latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_disk_read_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 25: Disk read latency mean metric metadata" caption-side="top"}

#### MongoDB Disk write latency mean
{: #ibm_databases_for_mongodb_disk_write_latency_mean}

Disk write latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_disk_write_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 32: Disk write latency mean metric metadata" caption-side="top"}

#### MongoDB IO utilization in percent 15-minute average
{: #ibm_databases_for_mongodb_disk_io_utilization_percent_average_15m}

How much disk I/O has been used over 15 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_disk_io_utilization_percent_average_15m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 41: IO utilization in percent 15 minute average metric metadata" caption-side="top"}

#### MongoDB IO utilization in percent 30-minute average
{: #ibm_databases_for_mongodb_disk_io_utilization_percent_average_30m}

How much disk I/O has been used over 30 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_disk_io_utilization_percent_average_30m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 50: IO utilization in percent 30 minute average metric metadata" caption-side="top"}

#### MongoDB IO utilization in percent 5-minute average
{: #ibm_databases_for_mongodb_disk_io_utilization_percent_average_5m}

How much disk I/O has been used over 5 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_disk_io_utilization_percent_average_5m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 59: IO utilization in percent 5 minute average metric metadata" caption-side="top"}

#### MongoDB IO utilization in percent 60-minute average
{: #ibm_databases_for_mongodb_disk_io_utilization_percent_average_60m}

How much disk I/O has been used over 60 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_disk_io_utilization_percent_average_60m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 68: IO utilization in percent 60 minute average metric metadata" caption-side="top"}

#### MongoDB IOPS read & write total count for an instance
{: #ibm_databases_for_mongodb_disk_iops_read_write_total}

How many input-output operations per second your instance is performing

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_disk_iops_read_write_total`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 77: IOPS read & write total count for an instance metric metadata" caption-side="top"}

#### MongoDB Maximum allowed memory for an instance
{: #ibm_databases_for_mongodb_memory_limit_bytes}

The maximum amount of memory available to your instance

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_memory_limit_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 86: Maximum allowed memory for an instance metric metadata" caption-side="top"}

#### MongoDB Oplog gigabyte per hour
{: #ibm_databases_for_mongodb_oplog_gb_per_hour}

The gigabytes of oplog per hour the primary generates

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_oplog_gb_per_hour`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 92: Oplog gigabyte per hour metric metadata" caption-side="top"}

#### MongoDB Oplog used bytes
{: #ibm_databases_for_mongodb_oplog_used_bytes}

The total amount of space used by the oplog in bytes.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_oplog_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 93: Oplog used bytes metric metadata" caption-side="top"}

#### MongoDB Oplog used bytes percent of total
{: #ibm_databases_for_mongodb_oplog_used_bytes_percent}

The total used oplog space in percent

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_oplog_used_bytes_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 94: Oplog used bytes percent of total metric metadata" caption-side="top"}

#### MongoDB Oplog window hours
{: #ibm_databases_for_mongodb_oplog_window_hours}

The approximate number of hours available in the oplog.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_oplog_window_hours`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 95: Oplog window hours metric metadata" caption-side="top"}

#### MongoDB Page faults
{: #ibm_databases_for_mongodb_page_faults}

The number of times per second that MongoDB had to request data from disk. Scale RAM to reduce the number of disk requests

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_page_faults`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 96: Page faults metric metadata" caption-side="top"}

#### MongoDB Process resident memory in bytes
{: #ibm_databases_for_mongodb_process_resident_memory_bytes}

Amount of actual physical memory used by the MongoDB process.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_process_resident_memory_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 99: Process resident memory in bytes metric metadata" caption-side="top"}

#### MongoDB Process virtual memory in bytes
{: #ibm_databases_for_mongodb_process_virtual_memory_bytes}

Amount of virtual memory used by the MongoDB process.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_process_virtual_memory_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 100: Process virtual memory in bytes metric metadata" caption-side="top"}

#### MongoDB Replica set member state
{: #ibm_databases_for_mongodb_status}

An integer between 0 and 10 that represents the replica state of the current member.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_status`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 103: Replica set member state metric metadata" caption-side="top"}

#### MongoDB Replication lag
{: #ibm_databases_for_mongodb_replica_lag}

The replication lag in seconds

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_replica_lag`|
| `Metric Type` | `gauge` |
| `Value Type`  | `second` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 104: Replication lag metric metadata" caption-side="top"}

#### MongoDB Total disk space for an instance
{: #ibm_databases_for_mongodb_disk_total_bytes}

Represents the total amount of disk space available to your deployment

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_disk_total_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 140: Total disk space for an instance metric metadata" caption-side="top"}

#### MongoDB Used CPU for an instance
{: #ibm_databases_for_mongodb_cpu_used_percent}

How much CPU is used as a percentage of total CPU available. Only for deployments that have dedicated CPU

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_cpu_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 175: Used CPU for an instance metric metadata" caption-side="top"}

#### MongoDB Used disk space for an instance bytes
{: #ibm_databases_for_mongodb_disk_used_bytes}

How much disk space your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_disk_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 190: Used disk space for an instance metric metadata" caption-side="top"}

#### MongoDB Used disk space for an instance
{: #ibm_databases_for_mongodb_disk_used_percent}

How much disk space is used as a percentage of total disk available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_disk_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 191: Used disk space for an instance metric metadata" caption-side="top"}

#### MongoDB Used memory for an instance
{: #ibm_databases_for_mongodb_memory_used_bytes}

How much memory your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_memory_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 208: Used memory for an instance metric metadata" caption-side="top"}

#### MongoDB Used memory for an instance percent
{: #ibm_databases_for_mongodb_memory_used_percent}

How much memory is used as a percentage of total memory available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mongodb_memory_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 209: Used memory for an instance metric metadata" caption-side="top"}

## PostgreSQL Metrics
{: #metrics-by-plan-postgresql}

| Metric Name |
|-----------|
| [PostgreSQL Cache hit ratio](#ibm_databases_for_postgresql_cache_hit_ratio) |
| [PostgreSQL Disk read latency mean](#ibm_databases_for_postgresql_disk_read_latency_mean) |
| [PostgreSQL Disk write latency mean](#ibm_databases_for_postgresql_disk_write_latency_mean) |
| [PostgreSQL IO utilization in percent 15-minute average](#ibm_databases_for_postgresql_disk_io_utilization_percent_average_15m) |
| [PostgreSQL IO utilization in percent 30-minute average](#ibm_databases_for_postgresql_disk_io_utilization_percent_average_30m) |
| [PostgreSQL IO utilization in percent 5-minute average](#ibm_databases_for_postgresql_disk_io_utilization_percent_average_5m) |
| [PostgreSQL IO utilization in percent 60-minute average](#ibm_databases_for_postgresql_disk_io_utilization_percent_average_60m) |
| [PostgreSQL IOPS read & write total count for an instance](#ibm_databases_for_postgresql_disk_iops_read_write_total) |
| [PostgreSQL Maximum allowed memory for an instance](#ibm_databases_for_postgresql_memory_limit_bytes) |
| [PostgreSQL Read replica replication lag](#ibm_databases_for_postgresql_read_replica_replication_lag_bytes) |
| [PostgreSQL Successful archive rate](#ibm_databases_for_postgresql_successful_archive_rate) |
| [PostgreSQL Temporary files size in bytes](#ibm_databases_for_postgresql_temp_bytes_count) |
| [PostgreSQL The total number of PostgreSQL connections being used](#ibm_databases_for_postgresql_total_connections) |
| [PostgreSQL Total disk space for an instance](#ibm_databases_for_postgresql_disk_total_bytes) |
| [PostgreSQL Transaction commit count](#ibm_databases_for_postgresql_transaction_commit_count) |
| [PostgreSQL Transaction commit rate](#ibm_databases_for_postgresql_transaction_commit_rate) |
| [PostgreSQL Transaction rollback count](#ibm_databases_for_postgresql_transaction_rollback_count) |
| [PostgreSQL Transaction rollback rate](#ibm_databases_for_postgresql_transaction_rollback_rate) |
| [PostgreSQL Tuples deleted count](#ibm_databases_for_postgresql_tuples_deleted_count) |
| [PostgreSQL Tuples deleted rate](#ibm_databases_for_postgresql_tuples_deleted_rate) |
| [PostgreSQL Tuples fetched count](#ibm_databases_for_postgresql_tuples_fetched_count) |
| [PostgreSQL Tuples fetched rate](#ibm_databases_for_postgresql_tuples_fetched_rate) |
| [PostgreSQL Tuples inserted count](#ibm_databases_for_postgresql_tuples_inserted_count) |
| [PostgreSQL Tuples inserted rate](#ibm_databases_for_postgresql_tuples_inserted_rate) |
| [PostgreSQL Tuples returned rate](#ibm_databases_for_postgresql_tuples_returned_rate) |
| [PostgreSQL Tuples updated count](#ibm_databases_for_postgresql_tuples_updated_count) |
| [PostgreSQL Tuples updated rate](#ibm_databases_for_postgresql_tuples_updated_rate) |
| [PostgreSQL Used CPU for an instance](#ibm_databases_for_postgresql_cpu_used_percent) |
| [PostgreSQL Used disk space for an instance](#ibm_databases_for_postgresql_disk_used_bytes) |
| [PostgreSQL Used disk space for an instance](#ibm_databases_for_postgresql_disk_used_percent) |
| [PostgreSQL Used memory for an instance](#ibm_databases_for_postgresql_memory_used_bytes) |
| [PostgreSQL Used memory for an instance](#ibm_databases_for_postgresql_memory_used_percent) |
| [PostgreSQL WAL logs used bytes](#ibm_databases_for_postgresql_wal_used_bytes) |
| [PostgreSQL Blocks hit rate](#ibm_databases_for_postgresql_blocks_hit_rate) |
| [PostgreSQL Blocks read rate](#ibm_databases_for_postgresql_blocks_read_rate) |
| [PostgreSQL Buffers backend rate](#ibm_databases_for_postgresql_buffers_backend_rate) |
| [PostgreSQL Buffers checkpoint rate](#ibm_databases_for_postgresql_buffers_checkpoint_rate) |
| [PostgreSQL Deadlocks count](#ibm_databases_for_postgresql_deadlocks_count) |
| [PostgreSQL Deadlocks rate](#ibm_databases_for_postgresql_deadlocks_rate) |
{: caption="Table 1: Metrics Available by Plan Names" caption-side="top"}

### PostgreSQL Metric Descriptions
{: #metrics-by-plan-postgres-desc}

#### PostgreSQL Blocks hit rate
{: #ibm_databases_for_postgresql_blocks_hit_rate}

Blocks hit rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_blocks_hit_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 2: Blocks hit rate metric metadata" caption-side="top"}

#### PostgreSQL Blocks read rate
{: #ibm_databases_for_postgresql_blocks_read_rate}

Blocks read rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_blocks_read_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 3: Blocks read rate metric metadata" caption-side="top"}

#### PostgreSQL Buffers backend rate
{: #ibm_databases_for_postgresql_buffers_backend_rate}

Buffers backend rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_buffers_backend_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 4: Buffers backend rate metric metadata" caption-side="top"}

#### PostgreSQL Buffers checkpoint rate
{: #ibm_databases_for_postgresql_buffers_checkpoint_rate}

Buffers checkpoint rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_buffers_checkpoint_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 5: Buffers checkpoint rate metric metadata" caption-side="top"}

#### PostgreSQL Cache hit ratio
{: #ibm_databases_for_postgresql_cache_hit_ratio}

Cache hit ratio

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_cache_hit_ratio`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 6: Cache hit ratio metric metadata" caption-side="top"}

#### PostgreSQL Deadlocks count
{: #ibm_databases_for_postgresql_deadlocks_count}

Deadlocks count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_deadlocks_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 7: Deadlocks count metric metadata" caption-side="top"}

#### PostgreSQL Deadlocks rate
{: #ibm_databases_for_postgresql_deadlocks_rate}

Deadlocks rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_deadlocks_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 8: Deadlocks rate metric metadata" caption-side="top"}

#### PostgreSQL Disk read latency mean
{: #ibm_databases_for_postgresql_disk_read_latency_mean}

Disk read latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_disk_read_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 9: Disk read latency mean metric metadata" caption-side="top"}

#### PostgreSQL Disk write latency mean
{: #ibm_databases_for_postgresql_disk_write_latency_mean}

Disk write latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_disk_write_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 10: Disk write latency mean metric metadata" caption-side="top"}

#### PostgreSQL IO utilization in percent 15-minute average
{: #ibm_databases_for_postgresql_disk_io_utilization_percent_average_15m}

How much disk I/O has been used over 15 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_disk_io_utilization_percent_average_15m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 11: IO utilization in percent 15 minute average metric metadata" caption-side="top"}

#### PostgreSQL IO utilization in percent 30-minute average
{: #ibm_databases_for_postgresql_disk_io_utilization_percent_average_30m}

How much disk I/O has been used over 30 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_disk_io_utilization_percent_average_30m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 12: IO utilization in percent 30 minute average metric metadata" caption-side="top"}

#### PostgreSQL IO utilization in percent 5-minute average
{: #ibm_databases_for_postgresql_disk_io_utilization_percent_average_5m}

How much disk I/O has been used over 5 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_disk_io_utilization_percent_average_5m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 13: IO utilization in percent 5 minute average metric metadata" caption-side="top"}

#### PostgreSQL IO utilization in percent 60-minute average
{: #ibm_databases_for_postgresql_disk_io_utilization_percent_average_60m}

How much disk I/O has been used over 60 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_disk_io_utilization_percent_average_60m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 14: IO utilization in percent 60 minute average metric metadata" caption-side="top"}

#### PostgreSQL IOPS read & write total count for an instance
{: #ibm_databases_for_postgresql_disk_iops_read_write_total}

How many input-output operations per second your instance is performing

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_disk_iops_read_write_total`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 15: IOPS read & write total count for an instance metric metadata" caption-side="top"}

#### PostgreSQL Maximum allowed memory for an instance
{: #ibm_databases_for_postgresql_memory_limit_bytes}

The maximum amount of memory available to your instance

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_memory_limit_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 16: Maximum allowed memory for an instance metric metadata" caption-side="top"}

#### PostgreSQL Read replica replication lag
{: #ibm_databases_for_postgresql_read_replica_replication_lag_bytes}

How far behind a PostgreSQL read-only replica is, in bytes

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_read_replica_replication_lag_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 17: Read replica replication lag metric metadata" caption-side="top"}

#### PostgreSQL Successful archive rate
{: #ibm_databases_for_postgresql_successful_archive_rate}

Successful archive rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_successful_archive_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 18: Successful archive rate metric metadata" caption-side="top"}

#### PostgreSQL Temporary files size in bytes
{: #ibm_databases_for_postgresql_temp_bytes_count}

Temporary files size in bytes

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_temp_bytes_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 19: Temporary files size in bytes metric metadata" caption-side="top"}

#### PostgreSQL The total number of PostgreSQL connections being used
{: #ibm_databases_for_postgresql_total_connections}

The total number of PostgreSQL connections being used

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_total_connections`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 20: The total number of PostgreSQL connections being used metric metadata" caption-side="top"}

#### PostgreSQL Total disk space for an instance
{: #ibm_databases_for_postgresql_disk_total_bytes}

Represents the total amount of disk space available to your deployment

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_disk_total_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 21: Total disk space for an instance metric metadata" caption-side="top"}

#### PostgreSQL Transaction commit count
{: #ibm_databases_for_postgresql_transaction_commit_count}

Transaction commit count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_transaction_commit_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 22: Transaction commit count metric metadata" caption-side="top"}

#### PostgreSQL Transaction commit rate
{: #ibm_databases_for_postgresql_transaction_commit_rate}

Transaction commit rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_transaction_commit_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 23: Transaction commit rate metric metadata" caption-side="top"}

#### PostgreSQL Transaction rollback count
{: #ibm_databases_for_postgresql_transaction_rollback_count}

Transaction rollback count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_transaction_rollback_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 24: Transaction rollback count metric metadata" caption-side="top"}

#### PostgreSQL Transaction rollback rate
{: #ibm_databases_for_postgresql_transaction_rollback_rate}

Transaction rollback rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_transaction_rollback_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 25: Transaction rollback rate metric metadata" caption-side="top"}

#### PostgreSQL Tuples deleted count
{: #ibm_databases_for_postgresql_tuples_deleted_count}

Tuples deleted count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_tuples_deleted_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 26: Tuples deleted count metric metadata" caption-side="top"}

#### PostgreSQL Tuples deleted rate
{: #ibm_databases_for_postgresql_tuples_deleted_rate}

Tuples deleted rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_tuples_deleted_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 27: Tuples deleted rate metric metadata" caption-side="top"}

#### PostgreSQL Tuples fetched count
{: #ibm_databases_for_postgresql_tuples_fetched_count}

Tuples fetched count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_tuples_fetched_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 28: Tuples fetched count metric metadata" caption-side="top"}

#### PostgreSQL Tuples fetched rate
{: #ibm_databases_for_postgresql_tuples_fetched_rate}

Tuples fetched rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_tuples_fetched_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 29: Tuples fetched rate metric metadata" caption-side="top"}

#### PostgreSQL Tuples inserted count
{: #ibm_databases_for_postgresql_tuples_inserted_count}

Tuples inserted count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_tuples_inserted_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 30: Tuples inserted count metric metadata" caption-side="top"}

#### PostgreSQL Tuples inserted rate
{: #ibm_databases_for_postgresql_tuples_inserted_rate}

Tuples inserted rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_tuples_inserted_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 31: Tuples inserted rate metric metadata" caption-side="top"}

#### PostgreSQL Tuples returned rate
{: #ibm_databases_for_postgresql_tuples_returned_rate}

Tuples returned rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_tuples_returned_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 32: Tuples returned rate metric metadata" caption-side="top"}

#### PostgreSQL Tuples updated count
{: #ibm_databases_for_postgresql_tuples_updated_count}

Tuples updated count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_tuples_updated_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 33: Tuples updated count metric metadata" caption-side="top"}

#### PostgreSQL Tuples updated rate
{: #ibm_databases_for_postgresql_tuples_updated_rate}

Tuples updated rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_tuples_updated_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 34: Tuples updated rate metric metadata" caption-side="top"}

#### PostgreSQL Used CPU for an instance
{: #ibm_databases_for_postgresql_cpu_used_percent}

How much CPU is used as a percentage of total CPU available. Only for deployments that have dedicated CPU

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_cpu_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 35: Used CPU for an instance metric metadata" caption-side="top"}

#### PostgreSQL Used disk space for an instance bytes
{: #ibm_databases_for_postgresql_disk_used_bytes}

How much disk space your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_disk_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 36: Used disk space for an instance metric metadata" caption-side="top"}

#### PostgreSQL Used disk space for an instance
{: #ibm_databases_for_postgresql_disk_used_percent}

How much disk space is used as a percentage of total disk available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_disk_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 37: Used disk space for an instance metric metadata" caption-side="top"}

#### PostgreSQL Used memory for an instance bytes
{: #ibm_databases_for_postgresql_memory_used_bytes}

How much memory your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_memory_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 38: Used memory for an instance metric metadata" caption-side="top"}

#### PostgreSQL Used memory for an instance percent
{: #ibm_databases_for_postgresql_memory_used_percent}

How much memory is used as a percentage of total memory available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_memory_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 39: Used memory for an instance metric metadata" caption-side="top"}

#### PostgreSQL WAL logs used bytes
{: #ibm_databases_for_postgresql_wal_used_bytes}

How much WAL log file uses, in bytes

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_postgresql_wal_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 40: WAL logs used bytes metric metadata" caption-side="top"}

## EnterpriseDB Metrics
{: #metrics-by-plan-enterprisedb}

| Metric Name |
|-----------|
| [EnterpriseDB Blocks hit rate](#ibm_databases_for_enterprisedb_blocks_hit_rate) |
| [EnterpriseDB Blocks read rate](#ibm_databases_for_enterprisedb_blocks_read_rate) |
| [EnterpriseDB Buffers backend rate](#ibm_databases_for_enterprisedb_buffers_backend_rate) |
| [EnterpriseDB Buffers checkpoint rate](#ibm_databases_for_enterprisedb_buffers_checkpoint_rate) |
| [EnterpriseDB Cache hit ratio](#ibm_databases_for_enterprisedb_cache_hit_ratio) |
| [EnterpriseDB Deadlocks count](#ibm_databases_for_enterprisedb_deadlocks_count) |
| [EnterpriseDB Deadlocks rate](#ibm_databases_for_enterprisedb_deadlocks_rate) |
| [EnterpriseDB Disk read latency mean](#ibm_databases_for_enterprisedb_disk_read_latency_mean) |
| [EnterpriseDB Disk write latency mean](#ibm_databases_for_enterprisedb_disk_write_latency_mean) |
| [EnterpriseDB IO utilization in percent 15-minute average](#ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_15m) |
| [EnterpriseDB IO utilization in percent 30-minute average](#ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_30m) |
| [EnterpriseDB IO utilization in percent 5-minute average](#ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_5m) |
| [EnterpriseDB IO utilization in percent 60-minute average](#ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_60m) |
| [EnterpriseDB IOPS read & write total count for an instance](#ibm_databases_for_enterprisedb_disk_iops_read_write_total) |
| [EnterpriseDB Maximum allowed memory for an instance](#ibm_databases_for_enterprisedb_memory_limit_bytes) |
| [EnterpriseDB Read replica replication lag](#ibm_databases_for_enterprisedb_read_replica_replication_lag_bytes) |
| [EnterpriseDB Successful archive rate](#ibm_databases_for_enterprisedb_successful_archive_rate) |
| [EnterpriseDB Temporary files size in bytes](#ibm_databases_for_enterprisedb_temp_bytes_count) |
| [EnterpriseDB The total number of EnterpriseDB connections being used](#ibm_databases_for_enterprisedb_total_connections) |
| [EnterpriseDB Total disk space for an instance](#ibm_databases_for_enterprisedb_disk_total_bytes) |
| [EnterpriseDB Transaction commit count](#ibm_databases_for_enterprisedb_transaction_commit_count) |
| [EnterpriseDB Transaction commit rate](#ibm_databases_for_enterprisedb_transaction_commit_rate) |
| [EnterpriseDB Transaction rollback count](#ibm_databases_for_enterprisedb_transaction_rollback_count) |
| [EnterpriseDB Transaction rollback rate](#ibm_databases_for_enterprisedb_transaction_rollback_rate) |
| [EnterpriseDB Tuples deleted count](#ibm_databases_for_enterprisedb_tuples_deleted_count) |
| [EnterpriseDB Tuples deleted rate](#ibm_databases_for_enterprisedb_tuples_deleted_rate) |
| [EnterpriseDB Tuples fetched count](#ibm_databases_for_enterprisedb_tuples_fetched_count) |
| [EnterpriseDB Tuples fetched rate](#ibm_databases_for_enterprisedb_tuples_fetched_rate) |
| [EnterpriseDB Tuples inserted count](#ibm_databases_for_enterprisedb_tuples_inserted_count) |
| [EnterpriseDB Tuples inserted rate](#ibm_databases_for_enterprisedb_tuples_inserted_rate) |
| [EnterpriseDB Tuples returned rate](#ibm_databases_for_enterprisedb_tuples_returned_rate) |
| [EnterpriseDB Tuples updated count](#ibm_databases_for_enterprisedb_tuples_updated_count) |
| [EnterpriseDB Tuples updated rate](#ibm_databases_for_enterprisedb_tuples_updated_rate) |
| [EnterpriseDB Used CPU for an instance](#ibm_databases_for_enterprisedb_cpu_used_percent) |
| [EnterpriseDB Used disk space for an instance](#ibm_databases_for_enterprisedb_disk_used_bytes) |
| [EnterpriseDB Used disk space for an instance](#ibm_databases_for_enterprisedb_disk_used_percent) |
| [EnterpriseDB Used memory for an instance](#ibm_databases_for_enterprisedb_memory_used_bytes) |
| [EnterpriseDB Used memory for an instance](#ibm_databases_for_enterprisedb_memory_used_percent) |
| [EnterpriseDB WAL logs used bytes](#ibm_databases_for_enterprisedb_wal_used_bytes) |
{: caption="Table 1: Metrics Available by Plan Names" caption-side="top"}

### EnterpriseDB Metrics Descriptions
{: #metrics-by-plan-enterprisedb-desc}

#### EnterpriseDB Blocks hit rate
{: #ibm_databases_for_enterprisedb_blocks_hit_rate}

Blocks hit rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_blocks_hit_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 4: Blocks hit rate metric metadata" caption-side="top"}

#### EnterpriseDB Blocks read rate
{: #ibm_databases_for_enterprisedb_blocks_read_rate}

Blocks read rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_blocks_read_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 1: Blocks read rate metric metadata" caption-side="top"}

#### EnterpriseDB Buffers backend rate
{: #ibm_databases_for_enterprisedb_buffers_backend_rate}

Buffers backend rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_buffers_backend_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 2: Buffers backend rate metric metadata" caption-side="top"}

#### EnterpriseDB Buffers checkpoint rate
{: #ibm_databases_for_enterprisedb_buffers_checkpoint_rate}

Buffers checkpoint rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_buffers_checkpoint_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 3: Buffers checkpoint rate metric metadata" caption-side="top"}

#### EnterpriseDB Cache hit ratio
{: #ibm_databases_for_enterprisedb_cache_hit_ratio}

Cache hit ratio

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_cache_hit_ratio`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 4: Cache hit ratio metric metadata" caption-side="top"}

#### EnterpriseDB Deadlocks count
{: #ibm_databases_for_enterprisedb_deadlocks_count}

Deadlocks count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_deadlocks_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 5: Deadlocks count metric metadata" caption-side="top"}

#### EnterpriseDB Deadlocks rate
{: #ibm_databases_for_enterprisedb_deadlocks_rate}

Deadlocks rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_deadlocks_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 6: Deadlocks rate metric metadata" caption-side="top"}

#### EnterpriseDB Disk read latency mean
{: #ibm_databases_for_enterprisedb_disk_read_latency_mean}

Disk read latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_disk_read_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 7: Disk read latency mean metric metadata" caption-side="top"}

#### EnterpriseDB Disk write latency mean
{: #ibm_databases_for_enterprisedb_disk_write_latency_mean}

Disk write latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_disk_write_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 8: Disk write latency mean metric metadata" caption-side="top"}

#### EnterpriseDB IO utilization in percent 15-minute average
{: #ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_15m}

How much disk I/O has been used over 15 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_15m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 9: IO utilization in percent 15 minute average metric metadata" caption-side="top"}

#### EnterpriseDB IO utilization in percent 30-minute average
{: #ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_30m}

How much disk I/O has been used over 30 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_30m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 10: IO utilization in percent 30 minute average metric metadata" caption-side="top"}

#### EnterpriseDB IO utilization in percent 5-minute average
{: #ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_5m}

How much disk I/O has been used over 5 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_5m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 11: IO utilization in percent 5 minute average metric metadata" caption-side="top"}

#### EnterpriseDB IO utilization in percent 60-minute average
{: #ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_60m}

How much disk I/O has been used over 60 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_disk_io_utilization_percent_average_60m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 12: IO utilization in percent 60 minute average metric metadata" caption-side="top"}

#### EnterpriseDB IOPS read & write total count for an instance
{: #ibm_databases_for_enterprisedb_disk_iops_read_write_total}

How many input-output operations per second your instance is performing

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_disk_iops_read_write_total`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 13: IOPS read & write total count for an instance metric metadata" caption-side="top"}

#### EnterpriseDB Maximum allowed memory for an instance
{: #ibm_databases_for_enterprisedb_memory_limit_bytes}

The maximum amount of memory available to your instance

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_memory_limit_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 14: Maximum allowed memory for an instance metric metadata" caption-side="top"}

#### EnterpriseDB Read replica replication lag
{: #ibm_databases_for_enterprisedb_read_replica_replication_lag_bytes}

How far behind an EnterpriseDB read-only replica is, in bytes

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_read_replica_replication_lag_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 15: Read replica replication lag metric metadata" caption-side="top"}

#### EnterpriseDB Successful archive rate
{: #ibm_databases_for_enterprisedb_successful_archive_rate}

Successful archive rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_successful_archive_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 16: Successful archive rate metric metadata" caption-side="top"}

#### EnterpriseDB Temporary files size in bytes
{: #ibm_databases_for_enterprisedb_temp_bytes_count}

Temporary files size in bytes

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_temp_bytes_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 17: Temporary files size in bytes metric metadata" caption-side="top"}

#### The total number of EnterpriseDB connections being used
{: #ibm_databases_for_enterprisedb_total_connections}

The total number of EnterpriseDB connections being used

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_total_connections`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 18: The total number of EnterpriseDB connections being used metric metadata" caption-side="top"}

#### EnterpriseDB Total disk space for an instance
{: #ibm_databases_for_enterprisedb_disk_total_bytes}

Represents the total amount of disk space available to your deployment

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_disk_total_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 19: Total disk space for an instance metric metadata" caption-side="top"}

#### EnterpriseDB Transaction commit count
{: #ibm_databases_for_enterprisedb_transaction_commit_count}

Transaction commit count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_transaction_commit_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 20: Transaction commit count metric metadata" caption-side="top"}

#### EnterpriseDB Transaction commit rate
{: #ibm_databases_for_enterprisedb_transaction_commit_rate}

Transaction commit rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_transaction_commit_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 21: Transaction commit rate metric metadata" caption-side="top"}

#### EnterpriseDB Transaction rollback count
{: #ibm_databases_for_enterprisedb_transaction_rollback_count}

Transaction rollback count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_transaction_rollback_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 22: Transaction rollback count metric metadata" caption-side="top"}

#### EnterpriseDB Transaction rollback rate
{: #ibm_databases_for_enterprisedb_transaction_rollback_rate}

Transaction rollback rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_transaction_rollback_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 23: Transaction rollback rate metric metadata" caption-side="top"}

#### EnterpriseDB Tuples deleted count
{: #ibm_databases_for_enterprisedb_tuples_deleted_count}

Tuples deleted count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_tuples_deleted_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 24: Tuples deleted count metric metadata" caption-side="top"}

#### EnterpriseDB Tuples deleted rate
{: #ibm_databases_for_enterprisedb_tuples_deleted_rate}

Tuples deleted rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_tuples_deleted_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 25: Tuples deleted rate metric metadata" caption-side="top"}

#### EnterpriseDB EnterpriseDB Tuples fetched count
{: #ibm_databases_for_enterprisedb_tuples_fetched_count}

Tuples fetched count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_tuples_fetched_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 26: Tuples fetched count metric metadata" caption-side="top"}

#### EnterpriseDB Tuples fetched rate
{: #ibm_databases_for_enterprisedb_tuples_fetched_rate}

Tuples fetched rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_tuples_fetched_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 27: Tuples fetched rate metric metadata" caption-side="top"}

#### EnterpriseDB Tuples inserted count
{: #ibm_databases_for_enterprisedb_tuples_inserted_count}

Tuples inserted count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_tuples_inserted_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 28: Tuples inserted count metric metadata" caption-side="top"}

#### EnterpriseDB Tuples inserted rate
{: #ibm_databases_for_enterprisedb_tuples_inserted_rate}

Tuples inserted rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_tuples_inserted_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 29: Tuples inserted rate metric metadata" caption-side="top"}

#### EnterpriseDB Tuples returned rate
{: #ibm_databases_for_enterprisedb_tuples_returned_rate}

Tuples returned rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_tuples_returned_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 30: Tuples returned rate metric metadata" caption-side="top"}

#### EnterpriseDB Tuples updated count
{: #ibm_databases_for_enterprisedb_tuples_updated_count}

Tuples updated count

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_tuples_updated_count`|
| `Metric Type` | `gauge` |
| `Value Type`  | `none` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 31: Tuples updated count metric metadata" caption-side="top"}

#### EnterpriseDB Tuples updated rate
{: #ibm_databases_for_enterprisedb_tuples_updated_rate}

Tuples updated rate

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_tuples_updated_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `rate` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 32: Tuples updated rate metric metadata" caption-side="top"}

#### EnterpriseDB Used CPU for an instance
{: #ibm_databases_for_enterprisedb_cpu_used_percent}

How much CPU is used as a percentage of total CPU available. Only for deployments that have dedicated CPU

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_cpu_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 33: Used CPU for an instance metric metadata" caption-side="top"}

#### EnterpriseDB Used disk space for an instance
{: #ibm_databases_for_enterprisedb_disk_used_bytes}

How much disk space your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_disk_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 34: Used disk space for an instance metric metadata" caption-side="top"}

#### EnterpriseDB Used disk space for an instance percent
{: #ibm_databases_for_enterprisedb_disk_used_percent}

How much disk space is used as a percentage of total disk available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_disk_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 35: Used disk space for an instance metric metadata" caption-side="top"}

#### EnterpriseDB Used memory for an instance bytes
{: #ibm_databases_for_enterprisedb_memory_used_bytes}

How much memory your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_memory_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 36: Used memory for an instance metric metadata" caption-side="top"}

#### EnterpriseDB Used memory for an instance percent
{: #ibm_databases_for_enterprisedb_memory_used_percent}

How much memory is used as a percentage of total memory available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_memory_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 37: Used memory for an instance metric metadata" caption-side="top"}

#### EnterpriseDB WAL logs used bytes
{: #ibm_databases_for_enterprisedb_wal_used_bytes}

How much WAL log file uses, in bytes

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_enterprisedb_wal_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 38: WAL logs used bytes metric metadata" caption-side="top"}

## MySQL Metrics
{: #metrics-by-plan-mysql}

| Metric Name |
|-----------|
| [MySQL Cache hit ratio](#ibm_databases_for_mysql_cache_hit_ratio) |
| [MySQL Connection usage for an instance](#ibm_databases_for_mysql_connection_used_percent) | 
| [MySQL Disk read latency mean](#ibm_databases_for_mysql_disk_read_latency_mean) |
| [MySQL Disk write latency mean](#ibm_databases_for_mysql_disk_write_latency_mean) |
| [MySQL IO utilization in percent 15-minute average](#ibm_databases_for_mysql_disk_io_utilization_percent_average_15m) |
| [MySQL IO utilization in percent 30-minute average](#ibm_databases_for_mysql_disk_io_utilization_percent_average_30m) |
| [MySQL IO utilization in percent 5-minute average](#ibm_databases_for_mysql_disk_io_utilization_percent_average_5m) |
| [MySQL IO utilization in percent 60-minute average](#ibm_databases_for_mysql_disk_io_utilization_percent_average_60m) |
| [MySQL IOPS read & write total count for an instance](#ibm_databases_for_mysql_disk_iops_read_write_total) |
| [MySQL Maximum allowed memory for an instance](#ibm_databases_for_mysql_memory_limit_bytes) |
| [MySQL The maximum permitted number of simultaneous client connections.](#ibm_databases_for_mysql_max_connections) | 
| [MySQL Percent of threads connected](#ibm_databases_for_mysql_threads_connected_usage) |
| [MySQL Percent of threads running](#ibm_databases_for_mysql_threads_running_usage) |
| [MySQL The number of connections that were aborted because the client died without closing the connection properly](#ibm_databases_for_mysql_aborted_clients_rate) |
| [MySQL The number of threads created to handle connections](#ibm_databases_for_mysql_threads_created) |
| [MySQL The number of threads in the thread cache](#ibm_databases_for_mysql_thread_cache_size) |
| [MySQL The number of threads in the thread cache](#ibm_databases_for_mysql_threads_cached) |
| [MySQL The open file usage](#ibm_databases_for_mysql_open_file_usage) |
| [MySQL The pool hit rate](#ibm_databases_for_mysql_pool_hit_rate) |
| [MySQL The pool utilization](#ibm_databases_for_mysql_pool_utilization) |
| [MySQL The rate of bytes received from all clients](#ibm_databases_for_mysql_bytes_received_rate) |
| [MySQL The rate of bytes sent to all clients](#ibm_databases_for_mysql_bytes_sent_rate) |
| [MySQL The rate of failed attempts to connect to the MySQL server](#ibm_databases_for_mysql_aborted_connects_rate) |
| [MySQL The rate of joins that did a full scan of the first table](#ibm_databases_for_mysql_select_scan_rate) |
| [MySQL The rate of joins that perform table scans because they do not use indexes](#ibm_databases_for_mysql_select_full_join_rate) |
| [MySQL The rate of joins that used a range search on a reference table](#ibm_databases_for_mysql_select_full_range_join_rate) |
| [MySQL The rate of joins that used ranges on the first table](#ibm_databases_for_mysql_select_range_rate) |
| [MySQL The rate of joins without keys that check for key usage after each row](#ibm_databases_for_mysql_select_range_check_rate) |
| [MySQL The rate of merge passes that the sort algorithm has had to do](#ibm_databases_for_mysql_sort_merge_passes_rate) |
| [MySQL The rate of queries that have taken more than long_query_time seconds](#ibm_databases_for_mysql_slow_queries_rate) |
| [MySQL The rate of sorted rows](#ibm_databases_for_mysql_sort_rows_rate) |
| [MySQL The rate of sorts that were done by scanning the table](#ibm_databases_for_mysql_sort_scan_rate) |
| [MySQL The rate of sorts that were done using ranges](#ibm_databases_for_mysql_sort_range_rate) |
| [MySQL The rate of statements executed by the server](#ibm_databases_for_mysql_questions_rate) |
| [MySQL The rate of times that a request for a table lock could be granted immediately](#ibm_databases_for_mysql_table_locks_immediate_rate) |
| [MySQL The rate of times that a request for a table lock could not be granted immediately and a wait was needed](#ibm_databases_for_mysql_table_locks_waited_rate) |
| [MySQL The rate of times that the log buffer was too small and a wait was required for it to be flushed before continuing](#ibm_databases_for_mysql_innodb_log_waits_rate) |
| [MySQL The rate of total command statements executed](#ibm_databases_for_mysql_commands_total_rate) |
| [MySQL Total disk space for an instance](#ibm_databases_for_mysql_disk_total_bytes) |
| [MySQL Used CPU for an instance](#ibm_databases_for_mysql_cpu_used_percent) |
| [MySQL Used disk space for an instance](#ibm_databases_for_mysql_disk_used_bytes) |
| [MySQL Used disk space for an instance](#ibm_databases_for_mysql_disk_used_percent) |
| [MySQL Used memory for an instance](#ibm_databases_for_mysql_memory_used_bytes) |
| [MySQL Used memory for an instance](#ibm_databases_for_mysql_memory_used_percent) |
| [MySQL Total active connections to the database](#ibm_databases_for_mysql_total_connections) |
{: caption="Table 1: Metrics Available by Plan Names" caption-side="top"}

### MySQL Metrics Descriptions
{: #metrics-by-plan-mysql-desc}

#### MySQLCache hit ratio
{: #ibm_databases_for_mysql_cache_hit_ratio}

Cache hit ratio

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_cache_hit_ratio`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 2: Cache hit ratio metric metadata" caption-side="top"}

#### MySQL Connection usage for an instance
{: #ibm_databases_for_mysql_connection_used_percent}

Represents the connection usage for your deployment.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_connection_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
`Segment By` | `Service instance, Service instance name` |
{: caption="Table 3: Connection usage for an instance metric metadata" caption-side="top"}

#### MySQL Disk read latency mean
{: #ibm_databases_for_mysql_disk_read_latency_mean}

Disk read latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_disk_read_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 4: Disk read latency mean metric metadata" caption-side="top"}

#### MySQL Disk write latency mean
{: #ibm_databases_for_mysql_disk_write_latency_mean}

Disk write latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_disk_write_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 5: Disk write latency mean metric metadata" caption-side="top"}

#### MySQL IO utilization in percent 15-minute average
{: #ibm_databases_for_mysql_disk_io_utilization_percent_average_15m}

How much disk I/O has been used over 15 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_disk_io_utilization_percent_average_15m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 6: IO utilization in percent 15 minute average metric metadata" caption-side="top"}

#### MySQL IO utilization in percent 30-minute average
{: #ibm_databases_for_mysql_disk_io_utilization_percent_average_30m}

How much disk I/O has been used over 30 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_disk_io_utilization_percent_average_30m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 7: IO utilization in percent 30 minute average metric metadata" caption-side="top"}

#### MySQL IO utilization in percent 5-minute average
{: #ibm_databases_for_mysql_disk_io_utilization_percent_average_5m}

How much disk I/O has been used over 5 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_disk_io_utilization_percent_average_5m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 8: IO utilization in percent 5 minute average metric metadata" caption-side="top"}

#### MySQL IO utilization in percent 60-minute average
{: #ibm_databases_for_mysql_disk_io_utilization_percent_average_60m}

How much disk I/O has been used over 60 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_disk_io_utilization_percent_average_60m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 9: IO utilization in percent 60 minute average metric metadata" caption-side="top"}

#### MySQL IOPS read & write total count for an instance
{: #ibm_databases_for_mysql_disk_iops_read_write_total}

How many input-output operations per second your instance is performing

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_disk_iops_read_write_total`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 10: IOPS read & write total count for an instance metric metadata" caption-side="top"}

#### MySQL Maximum allowed memory for an instance
{: #ibm_databases_for_mysql_memory_limit_bytes}

The maximum amount of memory available to your instance

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_memory_limit_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 11: Maximum allowed memory for an instance metric metadata" caption-side="top"}

#### MySQL Maximum permitted number of simultaneous client connections.
{: #ibm_databases_for_mysql_max_connections}

Represents the maximum permitted number of simultaneous client connections.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_max_connections`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
 `Segment By` | `Service instance, Service instance name` |
{: caption="Table 12: The maximum permitted number of simultaneous client connections. metric metadata" caption-side="top"}

#### MySQL Percent of threads connected
{: #ibm_databases_for_mysql_threads_connected_usage}

Percent of threads connected.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_threads_connected_usage`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 13: Percent of threads connected metric metadata" caption-side="top"}

#### MySQL Percent of threads running
{: #ibm_databases_for_mysql_threads_running_usage}

Percent of threads running.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_threads_running_usage`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 14: Percent of threads running metric metadata" caption-side="top"}

#### MySQL The number of connections that were aborted because the client died without closing the connection properly
{: #ibm_databases_for_mysql_aborted_clients_rate}

The number of connections that were aborted because the client died without closing the connection properly.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_aborted_clients_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 15: The number of connections that were aborted because the client died without closing the connection properly metric metadata" caption-side="top"}

#### MySQL The number of threads created to handle connections
{: #ibm_databases_for_mysql_threads_created}

The number of threads created to handle connections.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_threads_created`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 16: The number of threads created to handle connections metric metadata" caption-side="top"}

#### MySQL The number of threads in the thread cache size
{: #ibm_databases_for_mysql_thread_cache_size}

The number of threads in the thread cache.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_thread_cache_size`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 17: The number of threads in the thread cache metric metadata" caption-side="top"}

#### MySQL The number of threads in the thread cache
{: #ibm_databases_for_mysql_threads_cached}

The number of threads in the thread cache.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_threads_cached`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 18: The number of threads in the thread cache metric metadata" caption-side="top"}

#### MySQL The open file usage
{: #ibm_databases_for_mysql_open_file_usage}

The open file usage.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_open_file_usage`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 19: The open file usage metric metadata" caption-side="top"}

#### MySQL The pool hit rate
{: #ibm_databases_for_mysql_pool_hit_rate}

The pool hit rate.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_pool_hit_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 20: The pool hit rate metric metadata" caption-side="top"}

#### MySQL The pool utilization
{: #ibm_databases_for_mysql_pool_utilization}

The pool utilization.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_pool_utilization`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 21: The pool utilization metric metadata" caption-side="top"}

#### MySQL The rate of bytes received from all clients
{: #ibm_databases_for_mysql_bytes_received_rate}

The rate of bytes received from all clients.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_bytes_received_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 22: The rate of bytes received from all clients metric metadata" caption-side="top"}

#### MySQL The rate of bytes sent to all clients
{: #ibm_databases_for_mysql_bytes_sent_rate}

The rate of bytes sent to all clients.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_bytes_sent_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 23: The rate of bytes sent to all clients metric metadata" caption-side="top"}

#### MySQL The rate of failed attempts to connect to the MySQL server
{: #ibm_databases_for_mysql_aborted_connects_rate}

The rate of failed attempts to connect to the MySQL server.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_aborted_connects_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 24: The rate of failed attempts to connect to the MySQL server metric metadata" caption-side="top"}

#### MySQL The rate of joins that did a full scan of the first table
{: #ibm_databases_for_mysql_select_scan_rate}

The rate of joins that did a full scan of the first table.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_select_scan_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 25: The rate of joins that did a full scan of the first table metric metadata" caption-side="top"}

#### MySQL The rate of joins that perform table scans because they do not use indexes
{: #ibm_databases_for_mysql_select_full_join_rate}

The rate of joins that perform table scans because they do not use indexes.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_select_full_join_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 26: The rate of joins that perform table scans because they do not use indexes metric metadata" caption-side="top"}

#### MySQL The rate of joins that used a range search on a reference table
{: #ibm_databases_for_mysql_select_full_range_join_rate}

The rate of joins that used a range search on a reference table.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_select_full_range_join_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 27: The rate of joins that used a range search on a reference table metric metadata" caption-side="top"}

#### MySQL The rate of joins that used ranges on the first table
{: #ibm_databases_for_mysql_select_range_rate}

The rate of joins that used ranges on the first table.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_select_range_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 28: The rate of joins that used ranges on the first table metric metadata" caption-side="top"}

#### MySQL The rate of joins without keys that check for key usage after each row
{: #ibm_databases_for_mysql_select_range_check_rate}

The rate of joins without keys that check for key usage after each row.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_select_range_check_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 29: The rate of joins without keys that check for key usage after each row metric metadata" caption-side="top"}

#### MySQL The rate of merge passes that the sort algorithm has had to do
{: #ibm_databases_for_mysql_sort_merge_passes_rate}

The rate of merge passes that the sort algorithm has had to do.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_sort_merge_passes_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 30: The rate of merge passes that the sort algorithm has had to do metric metadata" caption-side="top"}

#### MySQL The rate of queries that have taken more than long_query_time seconds
{: #ibm_databases_for_mysql_slow_queries_rate}

The rate of queries that have taken more than long_query_time seconds.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_slow_queries_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 31: The rate of queries that have taken more than long_query_time seconds metric metadata" caption-side="top"}

#### MySQL The rate of sorted rows
{: #ibm_databases_for_mysql_sort_rows_rate}

The rate of sorted rows.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_sort_rows_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 32: The rate of sorted rows metric metadata" caption-side="top"}

#### MySQL The rate of sorts that were done by scanning the table
{: #ibm_databases_for_mysql_sort_scan_rate}

The rate of sorts that were done by scanning the table.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_sort_scan_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 33: The rate of sorts that were done by scanning the table metric metadata" caption-side="top"}

#### MySQL The rate of sorts that were done using ranges
{: #ibm_databases_for_mysql_sort_range_rate}

The rate of sorts that were done using ranges.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_sort_range_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 34: The rate of sorts that were done using ranges metric metadata" caption-side="top"}

#### MySQL The rate of statements executed by the server
{: #ibm_databases_for_mysql_questions_rate}

The rate of statements executed by the server.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_questions_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 35: The rate of statements executed by the server metric metadata" caption-side="top"}

#### MySQL The rate of times that a request for a table lock could be granted immediately
{: #ibm_databases_for_mysql_table_locks_immediate_rate}

The rate of times that a request for a table lock could be granted immediately.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_table_locks_immediate_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 36: The rate of times that a request for a table lock could be granted immediately metric metadata" caption-side="top"}

#### MySQL The rate of times that a request for a table lock could not be granted immediately and a wait was needed
{: #ibm_databases_for_mysql_table_locks_waited_rate}

The rate of times that a request for a table lock could not be granted immediately and a wait was needed.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_table_locks_waited_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 37: The rate of times that a request for a table lock could not be granted immediately and a wait was needed metric metadata" caption-side="top"}

#### MySQL The rate of times that the log buffer was too small and a wait was required for it to be flushed before continuing
{: #ibm_databases_for_mysql_innodb_log_waits_rate}

The rate of times that the log buffer was too small and a wait was required for it to be flushed before continuing.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_innodb_log_waits_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 38: The rate of times that the log buffer was too small and a wait was required for it to be flushed before continuing metric metadata" caption-side="top"}

#### MySQL The rate of total command statements executed
{: #ibm_databases_for_mysql_commands_total_rate}

The rate of total command statements executed.

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_commands_total_rate`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 39: The rate of total command statements executed metric metadata" caption-side="top"}

#### MySQL Total disk space for an instance
{: #ibm_databases_for_mysql_disk_total_bytes}

Represents the total amount of disk space available to your deployment

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_disk_total_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 40: Total disk space for an instance metric metadata" caption-side="top"}

#### MySQL Used CPU for an instance
{: #ibm_databases_for_mysql_cpu_used_percent}

How much CPU is used as a percentage of total CPU available. Only for deployments that have dedicated CPU

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_cpu_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 41: Used CPU for an instance metric metadata" caption-side="top"}

#### MySQL Used disk space for an instance
{: #ibm_databases_for_mysql_disk_used_bytes}

How much disk space your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_disk_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 42: Used disk space for an instance metric metadata" caption-side="top"}

#### MySQL Used disk space for an instance percent
{: #ibm_databases_for_mysql_disk_used_percent}

How much disk space is used as a percentage of total disk available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_disk_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 43: Used disk space for an instance metric metadata" caption-side="top"}

#### MySQL Used memory for an instance
{: #ibm_databases_for_mysql_memory_used_bytes}

How much memory your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_memory_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 44: Used memory for an instance metric metadata" caption-side="top"}

#### MySQL Used memory for an instance percent
{: #ibm_databases_for_mysql_memory_used_percent}

How much memory is used as a percentage of total memory available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_memory_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 45: Used memory for an instance metric metadata" caption-side="top"}

#### MySQL Total active connections to the database
{: #ibm_databases_for_mysql_total_connections}

Represents the total number of active connections to the database

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_mysql_total_connections`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 46: Used memory for an instance metric metadata" caption-side="top"}

## Elasticsearch Metrics
{: #metrics-by-plan-elasticsearch}

| Metric Name |
|-----------|
| [Elasticsearch Cluster status](#ibm_databases_for_elasticsearch_cluster_status) |
| [Elasticsearch Disk read latency mean](#ibm_databases_for_elasticsearch_disk_read_latency_mean) |
| [Elasticsearch Disk write latency mean](#ibm_databases_for_elasticsearch_disk_write_latency_mean) |
| [Elasticsearch GC Percentage](#ibm_databases_for_elasticsearch_garbage_collection_percent_average_15m) |
| [Elasticsearch IO utilization in percent 15-minute average](#ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_15m) |
| [Elasticsearch IO utilization in percent 30-minute average](#ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_30m) |
| [Elasticsearch IO utilization in percent 5-minute average](#ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_5m) |
| [Elasticsearch IO utilization in percent 60-minute average](#ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_60m) |
| [Elasticsearch IOPS read & write total count for an instance](#ibm_databases_for_elasticsearch_disk_iops_read_write_total) |
| [Elasticsearch Maximum allowed memory for an instance](#ibm_databases_for_elasticsearch_memory_limit_bytes) |
| [Elasticsearch Number of unassigned shards](#ibm_databases_for_elasticsearch_unassigned_shards_total) |
| [Elasticsearch Total disk space for an instance](#ibm_databases_for_elasticsearch_disk_total_bytes) |
| [Elasticsearch Used CPU for an instance](#ibm_databases_for_elasticsearch_cpu_used_percent) |
| [Elasticsearch Used JVM heap for a database member of the instance in percent](#ibm_databases_for_elasticsearch_jvm_heap_percent) |
| [Elasticsearch Used disk space for an instance](#ibm_databases_for_elasticsearch_disk_used_bytes) |
| [Elasticsearch Used disk space for an instance](#ibm_databases_for_elasticsearch_disk_used_percent) |
| [Elasticsearch Used memory for an instance](#ibm_databases_for_elasticsearch_memory_used_bytes) |
| [Elasticsearch Used memory for an instance](#ibm_databases_for_elasticsearch_memory_used_percent) |
{: caption="Table 1: Metrics Available by Plan Names" caption-side="top"}

### Elasticsearch Metrics Descriptions
{: #metrics-by-plan-elasticsearch-desc}

#### Elasticsearch Cluster status
{: #ibm_databases_for_elasticsearch_cluster_status}

A number derived from the status value of the /_cluster/health endpoint. Possible Values: 'green' = 1.0, 'yellow' = 0.5, 'red' = 0, ERROR = -1

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_cluster_status`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 2: Cluster status metric metadata" caption-side="top"}

#### Elasticsearch Disk read latency mean
{: #ibm_databases_for_elasticsearch_disk_read_latency_mean}

Disk read latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_disk_read_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 3: Disk read latency mean metric metadata" caption-side="top"}

#### Elasticsearch Disk write latency mean
{: #ibm_databases_for_elasticsearch_disk_write_latency_mean}

Disk write latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_disk_write_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 4: Disk write latency mean metric metadata" caption-side="top"}

#### Elasticsearch GC Percentage
{: #ibm_databases_for_elasticsearch_garbage_collection_percent_average_15m}

Percentage of time the Elasticsearch JVM spends on garbage collection

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_garbage_collection_percent_average_15m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 5: GC Percentage metric metadata" caption-side="top"}

#### Elasticsearch IO utilization in percent 15-minute average
{: #ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_15m}

How much disk I/O has been used over 15 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_15m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 6: IO utilization in percent 15 minute average metric metadata" caption-side="top"}

#### Elasticsearch IO utilization in percent 30-minute average
{: #ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_30m}

How much disk I/O has been used over 30 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_30m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 7: IO utilization in percent 30 minute average metric metadata" caption-side="top"}

#### Elasticsearch IO utilization in percent 5-minute average
{: #ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_5m}

How much disk I/O has been used over 5 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_5m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 8: IO utilization in percent 5 minute average metric metadata" caption-side="top"}

#### Elasticsearch IO utilization in percent 60-minute average
{: #ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_60m}

How much disk I/O has been used over 60 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_disk_io_utilization_percent_average_60m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 9: IO utilization in percent 60 minute average metric metadata" caption-side="top"}

#### Elasticsearch IOPS read & write total count for an instance
{: #ibm_databases_for_elasticsearch_disk_iops_read_write_total}

How many input-output operations per second your instance is performing

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_disk_iops_read_write_total`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 10: IOPS read & write total count for an instance metric metadata" caption-side="top"}

#### Elasticsearch Maximum allowed memory for an instance
{: #ibm_databases_for_elasticsearch_memory_limit_bytes}

The maximum amount of memory available to your instance

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_memory_limit_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 11: Maximum allowed memory for an instance metric metadata" caption-side="top"}

#### Elasticsearch Number of unassigned shards
{: #ibm_databases_for_elasticsearch_unassigned_shards_total}

Number of unassigned shards

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_unassigned_shards_total`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 12: Number of unassigned shards metric metadata" caption-side="top"}

#### Elasticsearch Total disk space for an instance
{: #ibm_databases_for_elasticsearch_disk_total_bytes}

Represents the total amount of disk space available to your deployment

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_disk_total_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 13: Total disk space for an instance metric metadata" caption-side="top"}

#### Elasticsearch Used CPU for an instance
{: #ibm_databases_for_elasticsearch_cpu_used_percent}

How much CPU is used as a percentage of total CPU available. Only for deployments that have dedicated CPU

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_cpu_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 14: Used CPU for an instance metric metadata" caption-side="top"}

#### Elasticsearch Used JVM heap for a database member of the instance in percent
{: #ibm_databases_for_elasticsearch_jvm_heap_percent}

How much JVM heap is used as a percentage of total JVM heap is available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_jvm_heap_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 15: Used JVM heap for a database member of the instance in percent metric metadata" caption-side="top"}

#### Elasticsearch Used disk space for an instance bytes
{: #ibm_databases_for_elasticsearch_disk_used_bytes}

How much disk space your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_disk_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 16: Used disk space for an instance metric metadata" caption-side="top"}

#### Elasticsearch Used disk space for an instance percent
{: #ibm_databases_for_elasticsearch_disk_used_percent}

How much disk space is used as a percentage of total disk available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_disk_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 17: Used disk space for an instance metric metadata" caption-side="top"}

#### Elasticsearch Used memory for an instance
{: #ibm_databases_for_elasticsearch_memory_used_bytes}

How much memory your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_memory_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 18: Used memory for an instance metric metadata" caption-side="top"}

#### Elasticsearch Used memory for an instance percent
{: #ibm_databases_for_elasticsearch_memory_used_percent}

How much memory is used as a percentage of total memory available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_elasticsearch_memory_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 19: Used memory for an instance metric metadata" caption-side="top"}

## etcd Metrics
{: #metrics-by-plan-etcd}

| Metric Name |
|-----------|
| [etcd Disk read latency mean](#ibm_databases_for_etcd_disk_read_latency_mean) |
| [etcd Disk write latency mean](#ibm_databases_for_etcd_disk_write_latency_mean) |
| [etcd IO utilization in percent 15-minute average](#ibm_databases_for_etcd_disk_io_utilization_percent_average_15m) |
| [etcd IO utilization in percent 30-minute average](#ibm_databases_for_etcd_disk_io_utilization_percent_average_30m) |
| [etcd IO utilization in percent 5-minute average](#ibm_databases_for_etcd_disk_io_utilization_percent_average_5m) |
| [etcd IO utilization in percent 60-minute average](#ibm_databases_for_etcd_disk_io_utilization_percent_average_60m) |
| [etcd IOPS read & write total count for an instance](#ibm_databases_for_etcd_disk_iops_read_write_total) |
| [etcd Maximum allowed memory for an instance](#ibm_databases_for_etcd_memory_limit_bytes) |
| [etcd Total disk space for an instance](#ibm_databases_for_etcd_disk_total_bytes) |
| [etcd Used CPU for an instance](#ibm_databases_for_etcd_cpu_used_percent) |
| [etcd Used disk space for an instance](#ibm_databases_for_etcd_disk_used_bytes) |
| [etcd Used disk space for an instance](#ibm_databases_for_etcd_disk_used_percent) |
| [etcd Used memory for an instance](#ibm_databases_for_etcd_memory_used_bytes) |
| [etcd Used memory for an instance](#ibm_databases_for_etcd_memory_used_percent) |
{: caption="Table 1: Metrics Available by Plan Names" caption-side="top"}

### etcd Metrics Descriptions
{: #metrics-by-plan-etcd-desc}

#### etcd Disk read latency mean
{: #ibm_databases_for_etcd_disk_read_latency_mean}

Disk read latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_disk_read_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 2: Disk read latency mean metric metadata" caption-side="top"}

#### etcd Disk write latency mean
{: #ibm_databases_for_etcd_disk_write_latency_mean}

Disk write latency mean

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_disk_write_latency_mean`|
| `Metric Type` | `gauge` |
| `Frequency` | `60ms` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 3: Disk write latency mean metric metadata" caption-side="top"}

#### etcd IO utilization in percent 15-minute average
{: #ibm_databases_for_etcd_disk_io_utilization_percent_average_15m}

How much disk I/O has been used over 15 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_disk_io_utilization_percent_average_15m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 4: IO utilization in percent 15 minute average metric metadata" caption-side="top"}

#### etcd IO utilization in percent 30-minute average
{: #ibm_databases_for_etcd_disk_io_utilization_percent_average_30m}

How much disk I/O has been used over 30 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_disk_io_utilization_percent_average_30m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 5: IO utilization in percent 30 minute average metric metadata" caption-side="top"}

#### etcd IO utilization in percent 5-minute average
{: #ibm_databases_for_etcd_disk_io_utilization_percent_average_5m}

How much disk I/O has been used over 5 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_disk_io_utilization_percent_average_5m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 6: IO utilization in percent 5 minute average metric metadata" caption-side="top"}

#### etcd IO utilization in percent 60-minute average
{: #ibm_databases_for_etcd_disk_io_utilization_percent_average_60m}

How much disk I/O has been used over 60 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_disk_io_utilization_percent_average_60m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 7: IO utilization in percent 60 minute average metric metadata" caption-side="top"}

#### etcd IOPS read & write total count for an instance
{: #ibm_databases_for_etcd_disk_iops_read_write_total}

How many input-output operations per second your instance is performing

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_disk_iops_read_write_total`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 8: IOPS read & write total count for an instance metric metadata" caption-side="top"}

#### etcd Maximum allowed memory for an instance
{: #ibm_databases_for_etcd_memory_limit_bytes}

The maximum amount of memory available to your instance

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_memory_limit_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 9: Maximum allowed memory for an instance metric metadata" caption-side="top"}

#### etcd Total disk space for an instance
{: #ibm_databases_for_etcd_disk_total_bytes}

Represents the total amount of disk space available to your deployment

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_disk_total_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 10: Total disk space for an instance metric metadata" caption-side="top"}

#### etcd Used CPU for an instance
{: #ibm_databases_for_etcd_cpu_used_percent}

How much CPU is used as a percentage of total CPU available. Only for deployments that have dedicated CPU

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_cpu_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 11: Used CPU for an instance metric metadata" caption-side="top"}

#### etcd Used disk space for an instance bytes
{: #ibm_databases_for_etcd_disk_used_bytes}

How much disk space your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_disk_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 12: Used disk space for an instance metric metadata" caption-side="top"}

#### etcd Used disk space for an instance percent
{: #ibm_databases_for_etcd_disk_used_percent}

How much disk space is used as a percentage of total disk available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_disk_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 13: Used disk space for an instance metric metadata" caption-side="top"}

#### etcd Used memory for an instance bytes
{: #ibm_databases_for_etcd_memory_used_bytes}

How much memory your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_memory_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 14: Used memory for an instance metric metadata" caption-side="top"}

#### etcd Used memory for an instance
{: #ibm_databases_for_etcd_memory_used_percent}

How much memory is used as a percentage of total memory available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_etcd_memory_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 15: Used memory for an instance metric metadata" caption-side="top"}

## Redis Metrics
{: #metrics-by-plan-redis}

| Metric Name |
|-----------|
| [Redis IO utilization in percent 15-minute average](#ibm_databases_for_redis_disk_io_utilization_percent_average_15m) |
| [Redis IO utilization in percent 30-minute average](#ibm_databases_for_redis_disk_io_utilization_percent_average_30m) |
| [Redis IO utilization in percent 5-minute average](#ibm_databases_for_redis_disk_io_utilization_percent_average_5m) |
| [Redis IO utilization in percent 60-minute average](#ibm_databases_for_redis_disk_io_utilization_percent_average_60m) |
| [Redis IOPS read & write total count for an instance](#ibm_databases_for_redis_disk_iops_read_write_total) |
| [Redis Maximum allowed memory for an instance](#ibm_databases_for_redis_memory_limit_bytes) |
| [Redis Total disk space for an instance](#ibm_databases_for_redis_disk_total_bytes) |
| [Redis Used CPU for an instance](#ibm_databases_for_redis_cpu_used_percent) |
| [Redis Used disk space for an instance](#ibm_databases_for_redis_disk_used_bytes) |
| [Redis Used disk space for an instance](#ibm_databases_for_redis_disk_used_percent) |
| [Redis Used memory for an instance](#ibm_databases_for_redis_memory_used_bytes) |
| [Redis Used memory for an instance](#ibm_databases_for_redis_memory_used_percent) |
{: caption="Table 1: Metrics Available by Plan Names" caption-side="top"}

### Redis Metrics Descriptions
{: #metrics-by-plan-redis-desc}

#### Redis IO utilization in percent 15-minute average
{: #ibm_databases_for_redis_disk_io_utilization_percent_average_15m}

How much disk I/O has been used over 15 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_disk_io_utilization_percent_average_15m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 2: IO utilization in percent 15 minute average metric metadata" caption-side="top"}

#### Redis IO utilization in percent 30-minute average
{: #ibm_databases_for_redis_disk_io_utilization_percent_average_30m}

How much disk I/O has been used over 30 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_disk_io_utilization_percent_average_30m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 3: IO utilization in percent 30 minute average metric metadata" caption-side="top"}

#### Redis IO utilization in percent 5-minute average
{: #ibm_databases_for_redis_disk_io_utilization_percent_average_5m}

How much disk I/O has been used over 5 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_disk_io_utilization_percent_average_5m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 4: IO utilization in percent 5 minute average metric metadata" caption-side="top"}

#### Redis IO utilization in percent 60-minute average
{: #ibm_databases_for_redis_disk_io_utilization_percent_average_60m}

How much disk I/O has been used over 60 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_disk_io_utilization_percent_average_60m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 5: IO utilization in percent 60 minute average metric metadata" caption-side="top"}

#### Redis IOPS read & write total count for an instance
{: #ibm_databases_for_redis_disk_iops_read_write_total}

How many input-output operations per second your instance is performing

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_disk_iops_read_write_total`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 6: IOPS read & write total count for an instance metric metadata" caption-side="top"}

#### Redis Maximum allowed memory for an instance
{: #ibm_databases_for_redis_memory_limit_bytes}

The maximum amount of memory available to your instance

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_memory_limit_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 7: Maximum allowed memory for an instance metric metadata" caption-side="top"}

#### Redis Total disk space for an instance
{: #ibm_databases_for_redis_disk_total_bytes}

Represents the total amount of disk space available to your deployment

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_disk_total_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 8: Total disk space for an instance metric metadata" caption-side="top"}

#### Redis Used CPU for an instance
{: #ibm_databases_for_redis_cpu_used_percent}

How much CPU is used as a percentage of total CPU available. Only for deployments that have dedicated CPU

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_cpu_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 9: Used CPU for an instance metric metadata" caption-side="top"}

#### Redis Used disk space for an instance
{: #ibm_databases_for_redis_disk_used_bytes}

How much disk space your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_disk_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 10: Used disk space for an instance metric metadata" caption-side="top"}

#### Redis Used disk space for an instance percent
{: #ibm_databases_for_redis_disk_used_percent}

How much disk space is used as a percentage of total disk available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_disk_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 11: Used disk space for an instance metric metadata" caption-side="top"}

#### Redis Used memory for an instance bytes
{: #ibm_databases_for_redis_memory_used_bytes}

How much memory your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_memory_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 12: Used memory for an instance metric metadata" caption-side="top"}

#### Redis Used memory for an instance percent
{: #ibm_databases_for_redis_memory_used_percent}

How much memory is used as a percentage of total memory available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_databases_for_redis_memory_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 13: Used memory for an instance metric metadata" caption-side="top"}

## Messages for RabbitMQ Metrics
{: #metrics-by-plan-rabbitmq}

| Metric Name |
|-----------|
| [Messages for RabbitMQ IO utilization in percent 15-minute average](#ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_15m) |
| [Messages for RabbitMQ IO utilization in percent 30-minute average](#ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_30m) |
| [Messages for RabbitMQ IO utilization in percent 5-minute average](#ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_5m) |
| [Messages for RabbitMQ IO utilization in percent 60-minute average](#ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_60m) |
| [Messages for RabbitMQ IOPS read & write total count for an instance](#ibm_messages_for_rabbitmq_disk_iops_read_write_total) |
| [Messages for RabbitMQ Maximum allowed memory for an instance](#ibm_messages_for_rabbitmq_memory_limit_bytes) |
| [Messages for RabbitMQ Total disk space for an instance](#ibm_messages_for_rabbitmq_disk_total_bytes) |
| [Messages for RabbitMQ Used CPU for an instance](#ibm_messages_for_rabbitmq_cpu_used_percent) |
| [Messages for RabbitMQ Used disk space for an instance](#ibm_messages_for_rabbitmq_disk_used_bytes) |
| [Messages for RabbitMQ Used disk space for an instance](#ibm_messages_for_rabbitmq_disk_used_percent) |
| [Messages for RabbitMQ Used memory for an instance](#ibm_messages_for_rabbitmq_memory_used_bytes) |
| [Messages for RabbitMQ Used memory for an instance](#ibm_messages_for_rabbitmq_memory_used_percent) |
{: caption="Table 1: Metrics Available by Plan Names" caption-side="top"}

### Messages for RabbitMQ Metrics Descriptions
{: #metrics-by-plan-rabbitmq-desc}

#### Messages for RabbitMQ IO utilization in percent 15-minute average
{: #ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_15m}

How much disk I/O has been used over 15 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_15m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 2: IO utilization in percent 15 minute average metric metadata" caption-side="top"}

#### Messages for RabbitMQ IO utilization in percent 30-minute average
{: #ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_30m}

How much disk I/O has been used over 30 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_30m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 3: IO utilization in percent 30 minute average metric metadata" caption-side="top"}

#### Messages for RabbitMQ IO utilization in percent 5-minute average
{: #ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_5m}

How much disk I/O has been used over 5 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_5m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 4: IO utilization in percent 5 minute average metric metadata" caption-side="top"}

#### Messages for RabbitMQ IO utilization in percent 60-minute average
{: #ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_60m}

How much disk I/O has been used over 60 minutes as a percentage of total disk I/O available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_disk_io_utilization_percent_average_60m`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 5: IO utilization in percent 60 minute average metric metadata" caption-side="top"}

#### Messages for RabbitMQ IOPS read & write total count for an instance
{: #ibm_messages_for_rabbitmq_disk_iops_read_write_total}

How many input-output operations per second your instance is performing

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_disk_iops_read_write_total`|
| `Metric Type` | `gauge` |
| `Value Type`  | `count` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 6: IOPS read & write total count for an instance metric metadata" caption-side="top"}

#### Messages for RabbitMQ Maximum allowed memory for an instance
{: #ibm_messages_for_rabbitmq_memory_limit_bytes}

The maximum amount of memory available to your instance

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_memory_limit_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 7: Maximum allowed memory for an instance metric metadata" caption-side="top"}

#### Messages for RabbitMQ Total disk space for an instance
{: #ibm_messages_for_rabbitmq_disk_total_bytes}

Represents the total amount of disk space available to your deployment

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_disk_total_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 8: Total disk space for an instance metric metadata" caption-side="top"}

#### Messages for RabbitMQ Used CPU for an instance
{: #ibm_messages_for_rabbitmq_cpu_used_percent}

How much CPU is used as a percentage of total CPU available. Only for deployments that have dedicated CPU

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_cpu_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 9: Used CPU for an instance metric metadata" caption-side="top"}

#### Messages for RabbitMQ Used disk space for an instance bytes
{: #ibm_messages_for_rabbitmq_disk_used_bytes}

How much disk space your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_disk_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 10: Used disk space for an instance metric metadata" caption-side="top"}

#### Messages for RabbitMQ Used disk space for an instance percent
{: #ibm_messages_for_rabbitmq_disk_used_percent}

How much disk space is used as a percentage of total disk available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_disk_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 11: Used disk space for an instance metric metadata" caption-side="top"}

#### Messages for RabbitMQ Used memory for an instance bytes
{: #ibm_messages_for_rabbitmq_memory_used_bytes}

How much memory your instance is using

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_memory_used_bytes`|
| `Metric Type` | `gauge` |
| `Value Type`  | `byte` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 12: Used memory for an instance metric metadata" caption-side="top"}

#### Messages for RabbitMQ Used memory for an instance percent
{: #ibm_messages_for_rabbitmq_memory_used_percent}

How much memory is used as a percentage of total memory available

| Metadata | Description |
|----------|-------------|
| `Metric Name` | `ibm_messages_for_rabbitmq_memory_used_percent`|
| `Metric Type` | `gauge` |
| `Value Type`  | `percent` |
| `Segment By` | `Service instance, Service instance name` |
{: caption="Table 13: Used memory for an instance metric metadata" caption-side="top"}

## Attributes for Segmentation
{: #attributes}

### Global Attributes
{: #global-attributes}

The following attributes are available for segmenting all of the metrics listed above

| Attribute | Attribute Name | Attribute Description |
|-----------|----------------|-----------------------|
| `Cloud Type` | `ibm_ctype` | The cloud type is a value of public, dedicated or local |
| `Location` | `ibm_location` | The location of the monitored resource - this may be a region, data center or global |
| `Resource` | `ibm_resource` | The resource being measured by the service - typically a indentifying name or GUID |
| `Resource Type` | `ibm_resource_type` | The type of the resource being measured by the service |
| `Scope` | `ibm_scope` | The scope is the account, organization or space GUID associated with this metric |
| `Service name` | `ibm_service_name` | Name of the service generating this metric |
{: caption="Table 1: WAL logs used bytes metric metadata" caption-side="top"}

### Additional Attributes
{: #additional-attributes}

The following attributes are available for segmenting one or more attributes as described in the reference above.  Please see the individual metrics for segmentation options.

| Attribute | Attribute Name | Attribute Description |
|-----------|----------------|-----------------------|
| `Service instance` | `ibm_service_instance` | The service instance segment identifies the instance the metric is associated with |
{: caption="Table 1: WAL logs used bytes metric metadata" caption-side="top"}
