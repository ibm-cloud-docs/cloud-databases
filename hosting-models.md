---

copyright:
  years: 2023, 2024

lastupdated: "2024-09-25"

subcollection: cloud-databases

keywords: isolated compute, hosting models, shared compute

---

{{site.data.keyword.attribute-definition-list}}

# Hosting models overview
{: #hosting-models}

To allow for reliable resource allocation, {{site.data.keyword.databases-for}} offers two hosting models; Shared Compute and Isolated Compute. {{site.data.keyword.databases-for}} Shared Compute is a flexible option for your database deployment that preserves performance predictability. {{site.data.keyword.databases-for}} Isolated Compute is our recommendation for production enterprise applications, providing more precise control and enterprise features.
{: shortdesc}

Scaling your Shared Compute or Isolated Compute databases is currently available via the CLI, API, or Terraform only. 
{: note}
{: ui}

## {{site.data.keyword.databases-for}} Shared Compute
{: #hosting-models-shared-compute-ui}
{: ui}

Shared Compute is a flexible multi-tenant offering for dynamic, fine-tuned, and decoupled capacity selections.

When provisioning Shared Compute through the {{site.data.keyword.cloud_notm}} console, you have the option to select between the following initial resource allocation presets: **Small** (1 CPU and 8 GB RAM for {{site.data.keyword.rabbitmq}}, 0.5 CPU and 4 GB RAM for all other databases) or **Custom** (≥ 2 CPU and ≥ 4 GB RAM). Small has a fixed amount of CPU and RAM, but you can change disk. Custom can be completely customized. 

With Small allocation preset, you can test out the database with the smallest resource allocation. If you have higher performance requirements, you can easily leverage the flexibility of the Shared model with the Custom allocation preset. With the ability to select the amount of CPU and RAM resources you receive, performance can be scaled to fit your workload.

## {{site.data.keyword.databases-for}} Isolated Compute
{: #hosting-models-iso-compute-ui}
{: ui}

Isolated Compute is a secure single-tenant offering for complex, highly performant enterprise workloads. By placing your deployment and all associated user-data management agents on an isolated machine, {{site.data.keyword.databases-for}} Isolated Compute provides dedicated computing resources, dedicated storage bandwidth, and hypervisor-level isolation.

When provisioning, choose an initial host size for your instance. Storage is still selected separately, allowing you to determine the size of disk and number of [IOPS](#x3858854){: term} your database receives.

CPU and RAM autoscaling is not supported on Isolated Compute. Disk autoscaling is available. If you provisioned an isolated instance or switched over from a deployment with autoscaling, monitor your resources using [{{site.data.keyword.monitoringfull}} integration](/docs/cloud-databases?topic=cloud-databases-monitoring), which provides metrics for memory, disk space, and disk I/O utilization. To add resources to your instance, manually scale your deployment.
{: note}

### Isolated Compute sizing
{: #hosting-models-iso-compute-sizing-ui}
{: ui}

Isolated Compute features 6 size selections:

- 4 CPU x 16 RAM
- 8 CPU x 32 RAM
- 8 CPU x 64 RAM
- 16 CPU x 64 RAM
- 32 CPU x 128 RAM
- 30 CPU x 240 RAM

## {{site.data.keyword.databases-for}} Shared Compute
{: #hosting-models-shared-compute-cli}
{: cli}

Shared Compute is a flexible multi-tenant offering for dynamic, fine-tuned, and decoupled capacity selections.

Each database instance receives a deterministic CPU allocation. If an instance is provisioned without selecting a CPU amount, Shared Compute automatically allocates a small amount of CPU to your database up to a 2 core max. Automatic CPU is provided at a 1:8 ratio of CPU:RAM; therefore, a user with 4 GB RAM receives 4/8th of a CPU; a user with 8 GB RAM receives 1 CPU; and an user with 20 GB RAM receives 2 CPU due to the 2 CPU limit.

For this fractional, automatic vCPU allocation, simply input your RAM and disk allocation needs. Selecting `multitenant` means that our system will handle vCPU allocation at a 1/8 ratio to your RAM allocation. We recommend integer allocations when specifying vCPU allocations.

If you have higher performance requirements than 2 CPU, you can easily leverage the flexibility of the Shared model. With the ability to select the amount of CPU and RAM resources you receive, performance can be scaled to fit your workload. Additionally, if you know that your instance will experience variable demand, use RAM autoscaling to set not only the expected load and duration that would initiate resource scaling, but also the resource and cost limit your database will scale to.

Because of each service's individual requirements, {{site.data.keyword.databases-for}} has minimum resource requirements in place for all Shared Compute instances. When all existing multi-tenant instances are transitioned to Shared Compute, these minimum resource requirements will be applied. Current multi-tenant instances will not be charged (that is, they will be _grandfathered_) for any increase to up to these minimum resource requirements actioned by IBM until May 2025. For more information, see [Hosting model grandfathering](/docs/cloud-databases?topic=cloud-databases-hosting-models&interface=ui#hosting-model-transition-timeline).
{: note}

## {{site.data.keyword.databases-for}} Isolated Compute
{: #hosting-models-iso-compute-cli}
{: cli}

Isolated Compute is a secure single-tenant offering for complex, highly-performant enterprise workloads. By placing your deployment and all associated user-data management agents on an isolated machine, {{site.data.keyword.databases-for}} Isolated Compute provides dedicated computing resources, dedicated storage bandwidth, and hypervisor-level isolation.

When provisioning, choose the CPU x RAM size for the machine to set up your database. This machine will be exclusively assigned to running your database instance. Storage is still selected separately, allowing you to determine the size of disk and number of [IOPS](#x3858854){: term} your database receives. Scale your database and change your machine size using your preferred method: the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or using [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

### Isolated Compute sizing
{: #hosting-models-iso-compute-sizing-cli}
{: cli}

Isolated Compute features 6 size selections:

- 4 CPU x 16 RAM
- 8 CPU x 32 RAM
- 8 CPU x 64 RAM
- 16 CPU x 64 RAM
- 32 CPU x 128 RAM
- 30 CPU x 240 RAM

The `host_flavor` parameter defines your Compute sizing. Input the appropriate value for your desired size. To provision a Shared Compute instance, specify `multitenant`. All other options place you on different Isolated Compute sizes. 

| **Host flavor** | **host_flavor value** |
|:-------------------------:|:---------------------:|
| Shared Compute            | `multitenant`    |
| 4 CPU x 16 RAM            | `b3c.4x16.encrypted`    |
| 8 CPU x 32 RAM            | `b3c.8x32.encrypted`    |
| 8 CPU x 64 RAM            | `m3c.8x64.encrypted`    |
| 16 CPU x 64 RAM           | `b3c.16x64.encrypted`   |
| 32 CPU x 128 RAM          | `b3c.32x128.encrypted`  |
| 30 CPU x 240 RAM          | `m3c.30x240.encrypted`  |
{: caption="Table 1. Host flavor sizing parameter" caption-side="bottom"}

## {{site.data.keyword.databases-for}} Shared Compute
{: #hosting-models-shared-compute-api}
{: api}

Shared Compute is a flexible multi-tenant offering for dynamic, fine-tuned, and decoupled capacity selections.

Each database instance receives a deterministic CPU allocation. If an instance is provisioned without selecting a CPU amount, Shared Compute automatically allocates a small amount of CPU to your database up to a 2 core max. Automatic CPU is provided at a 1:8 ratio of CPU:RAM; therefore, a user with 4 GB RAM receives 4/8th of a CPU; a user with 8 GB RAM receives 1 CPU; and an user with 20 GB RAM receives 2 CPU due to the 2 CPU limit.

For this fractional, automatic vCPU allocation, simply input your RAM and disk allocation needs. Selecting `multitenant` means that our system will handle vCPU allocation at a 1/8 ratio to your RAM allocation. We recommend integer allocations when specifying vCPU allocations.

If you have higher performance requirements than 2 CPU, you can easily leverage the flexibility of the Shared model. With the ability to select the amount of CPU and RAM resources you receive, performance can be scaled to fit your workload. Additionally, if you know that your instance will experience variable demand, use RAM autoscaling to set not only the expected load and duration that would initiate resource scaling, but also the resource and cost limit your database will scale to.

Because of each service's individual requirements, {{site.data.keyword.databases-for}} has minimum resource requirements in place for all Shared Compute instances. When all existing multi-tenant instances are transitioned to Shared Compute, these minimum resource requirements will be applied. Current multi-tenant instances will not be charged (that is, they will be _grandfathered_) for any increase to up to these minimum resource requirements actioned by IBM until May 2025. For more information, see [Hosting model grandfathering](/docs/cloud-databases?topic=cloud-databases-hosting-models&interface=ui#hosting-model-transition-timeline).
{: note}

## {{site.data.keyword.databases-for}} Isolated Compute
{: #hosting-models-iso-compute-api}
{: api}

Isolated Compute is a secure single-tenant offering for complex, highly-performant enterprise workloads. By placing your deployment and all associated user-data management agents on an isolated machine, {{site.data.keyword.databases-for}} Isolated Compute provides dedicated computing resources, dedicated storage bandwidth, and hypervisor-level isolation.

When provisioning, choose the CPU x RAM size for the machine to set up your database. This machine will be exclusively assigned to running your database instance. Storage is still selected separately, allowing you to determine the size of disk and number of [IOPS](#x3858854){: term} your database receives. Scale your database and change your machine size using your preferred method: the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or using [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

### Isolated Compute sizing
{: #hosting-models-iso-compute-sizing-api}
{: api}

Isolated Compute features 6 size selections:

- 4 CPU x 16 RAM
- 8 CPU x 32 RAM
- 8 CPU x 64 RAM
- 16 CPU x 64 RAM
- 32 CPU x 128 RAM
- 30 CPU x 240 RAM

The `host_flavor` parameter defines your Compute sizing. Input the appropriate value for your desired size. To provision a Shared Compute instance, specify `multitenant`. All other options place you on different Isolated Compute sizes. 

| **Host flavor** | **host_flavor value** |
|:-------------------------:|:---------------------:|
| Shared Compute            | `multitenant`    |
| 4 CPU x 16 RAM            | `b3c.4x16.encrypted`    |
| 8 CPU x 32 RAM            | `b3c.8x32.encrypted`    |
| 8 CPU x 64 RAM            | `m3c.8x64.encrypted`    |
| 16 CPU x 64 RAM           | `b3c.16x64.encrypted`   |
| 32 CPU x 128 RAM          | `b3c.32x128.encrypted`  |
| 30 CPU x 240 RAM          | `m3c.30x240.encrypted`  |
{: caption="Table 1. Host flavor sizing parameter" caption-side="bottom"}

## {{site.data.keyword.databases-for}} Shared Compute
{: #hosting-models-shared-compute-terraform}
{: terraform}

Shared Compute is a flexible multi-tenant offering for dynamic, fine-tuned, and decoupled capacity selections.

Each database instance receives a deterministic CPU allocation. If an instance is provisioned without selecting a CPU amount, Shared Compute automatically allocates a small amount of CPU to your database up to a 2 core max. Automatic CPU is provided at a 1:8 ratio of CPU:RAM; therefore, a user with 4 GB RAM receives 4/8th of a CPU; a user with 8 GB RAM receives 1 CPU; and an user with 20 GB RAM receives 2 CPU due to the 2 CPU limit.

For this fractional, automatic vCPU allocation, simply input your RAM and disk allocation needs. Selecting `multitenant` means that our system will handle vCPU allocation at a 1/8 ratio to your RAM allocation. We recommend integer allocations when specifying vCPU allocations.

If you have higher performance requirements than 2 CPU, you can easily leverage the flexibility of the Shared model. With the ability to select the amount of CPU and RAM resources you receive, performance can be scaled to fit your workload. Additionally, if you know that your instance will experience variable demand, use RAM autoscaling to set not only the expected load and duration that would initiate resource scaling, but also the resource and cost limit your database will scale to.

Because of each service's individual requirements, {{site.data.keyword.databases-for}} has minimum resource requirements in place for all Shared Compute instances. When all existing multi-tenant instances are transitioned to Shared Compute, these minimum resource requirements will be applied. Current multi-tenant instances will not be charged (that is, they will be _grandfathered_) for any increase to up to these minimum resource requirements actioned by IBM until May 2025. For more information, see [Hosting model grandfathering](/docs/cloud-databases?topic=cloud-databases-hosting-models&interface=ui#hosting-model-transition-timeline).
{: note}

## {{site.data.keyword.databases-for}} Isolated Compute
{: #hosting-models-iso-compute-terraform}
{: terraform}

Isolated Compute is a secure single-tenant offering for complex, highly-performant enterprise workloads. By placing your deployment and all associated user-data management agents on an isolated machine, {{site.data.keyword.databases-for}} Isolated Compute provides dedicated computing resources, dedicated IO and network bandwidth, and hypervisor-level isolation.

When provisioning, choose the CPU x RAM size for the machine to set up your database. This machine will be exclusively assigned to running your database instance. Storage is still selected separately, allowing you to determine the size of disk and number of [IOPS](#x3858854){: term} your database receives. Scale your database and change your machine size using your preferred method: the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or using [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

CPU and RAM autoscaling is not supported on {{site.data.keyword.databases-for}} Isolated Compute. Disk autoscaling is available. If you provisioned an isolated instance or switched over from a deployment with autoscaling, monitor your resources using [{{site.data.keyword.monitoringfull}} integration](/docs/databases-for-mongodb?topic=databases-for-mongodb-monitoring), which provides metrics for memory, disk space, and disk I/O utilization. To add resources to your instance, manually scale your deployment.
{: note}

### Isolated Compute sizing
{: #hosting-models-iso-compute-sizing-terraform}
{: terraform}

Isolated Compute features 6 size selections:

- 4 CPU x 16 RAM
- 8 CPU x 32 RAM
- 8 CPU x 64 RAM
- 16 CPU x 64 RAM
- 32 CPU x 128 RAM
- 30 CPU x 240 RAM

The `host_flavor` parameter defines your Compute sizing. Input the appropriate value for your desired size. To provision a Shared Compute instance, specify `multitenant`. All other options place you on different Isolated Compute sizes. 

| **Host flavor** | **host_flavor value** |
|:-------------------------:|:---------------------:|
| Shared Compute            | `multitenant`    |
| 4 CPU x 16 RAM            | `b3c.4x16.encrypted`    |
| 8 CPU x 32 RAM            | `b3c.8x32.encrypted`    |
| 8 CPU x 64 RAM            | `m3c.8x64.encrypted`    |
| 16 CPU x 64 RAM           | `b3c.16x64.encrypted`   |
| 32 CPU x 128 RAM          | `b3c.32x128.encrypted`  |
| 30 CPU x 240 RAM          | `m3c.30x240.encrypted`  |
{: caption="Table 1. Host flavor sizing parameter" caption-side="bottom"}

## Provisioning
{: #hosting-models-provisioning}

To provision a {{site.data.keyword.databases-for}} service instance, select your **hosting type** from either Shared Compute or Isolated Compute.
{: ui}

To provision a {{site.data.keyword.databases-for}} service instance, add a new `host_flavor` parameter. This parameter allows you to select either Shared Compute (`multitenant`) or Isolated Compute via assigning the parameter value for the requested Isolated instance size. Note that because Isolated Compute sizes implicitly include both CPU and RAM allocations, CPU and RAM sizes should not be provided with an Isolated Compute request.
{: cli}

To provision a {{site.data.keyword.databases-for}} service instance, add a new `host_flavor` parameter. This parameter allows you to select either Shared Compute (`multitenant`) or Isolated Compute via assigning the parameter value for the requested Isolated instance size. Note that because Isolated Compute sizes implicitly include both CPU and RAM allocations, CPU and RAM sizes should not be provided with an Isolated Compute request.
{: api}

To provision a {{site.data.keyword.databases-for}} service instance, add a new `host_flavor` parameter. This parameter allows you to select either Shared Compute (`multitenant`) or Isolated Compute via assigning the parameter value for the requested Isolated instance size. Note that because Isolated Compute sizes implicitly include both CPU and RAM allocations, CPU and RAM sizes should not be provided with an Isolated Compute request.
{: terraform}

For more detailed instructions, see your [database specific page](/docs/cloud-databases?topic=cloud-databases-getting-started-cdb-provision-instance&interface=ui).

## Scaling and switching between hosting models
{: #hosting-models-scaling}

For new hosting models, scaling and switching are similar operations. While scaling your database as you normally would, select a different **hosting type** from what your database instance is currently placed on to switch to and between Shared and Isolated Compute. 
{: ui}

For new hosting models, scaling and switching are similar operations. While scaling your database as you normally would, switch to and between hosting models by adding a new `host_flavor` parameter set to the hosting model you wish to scale to. Then, moving to the hosting type is as simple as running a scale command with this hosting flavor targeted. 
{: cli}

For new hosting models, scaling and switching are similar operations. While scaling your database as you normally would, switch to and between hosting models by adding a new `host_flavor` parameter set to the hosting model you wish to scale to. Then, moving to the hosting type is as simple as running a scale command with this hosting flavor targeted. 
{: api}

For new hosting models, scaling and switching are similar operations. While scaling your database as you normally would, switch to and between hosting models by adding a new `host_flavor` parameter set to the hosting model you wish to scale to. Then, moving to the hosting type is as simple as running a scale command with this hosting flavor targeted. 
{: terraform}

For more detailed instructions, commands, and parameters, see your [database-specific page](/docs/cloud-databases?topic=cloud-databases-scale-instance).

Note that switching hosting models does not cause downtime, as this is not a backup and restore migration. Instead, the same process is applied as for updates or database instance scaling, where database processes will perform a rolling restart. We recommend ensuring that your application has retry and reconnect login in place to immediately re-establish a connection, as existing connections will be dropped during this time.

## Choosing between hosting models
{: #choosing-between-hosting-models}

| **Isolated Compute** | **Shared Compute** |
| --- | --- |
| Single-tenanted databases with dedicated storage bandwidth. Database management agents are placed on isolated machine. | Multi-tenanted, logically separated databases sharing bandwidth. Database management pods are also multi-tenanted. |
| Receive all the available resources in your machine. | Transparent, deterministic CPU allocation. Know exactly what your performance will be and scale up and down as your workload requires. |
| Some of our database offerings, such as MongoDB Enterprise and Elasticsearch Platinum, will be solely provisioned on Isolated Compute. Future enhancements, such as cross-region replication may be supported solely on Isolated Compute. | Excludes some database offerings, such as MongoDB Enterprise and Elasticsearch Platinum. |
| Scalability is based on provided machine sizes. | Scalability is fine-grained and linear from a database-specific minimum configuration up to 28 CPU and 112 GB RAM. |
{: caption="Table 2. Choosing between hosting models" caption-side="bottom"}

## Databases availability by hosting model
{: #hosting-models-availability}

The following table shows which model is available for each database.

|  | **Shared Compute** | **Isolated Compute**  |
| --- | --- | --- |
| PostgreSQL | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| MongoDB Standard | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| MongoDB Enterprise |  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| Redis | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| Elasticsearch Enterprise | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| Elasticsearch Platinum |  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| MySQL | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| RabbitMQ | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| EnterpriseDB |  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| etcd | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
{: caption="Table 3. {{site.data.keyword.databases-for}} hosting model availability" caption-side="bottom"}

## Transition timeline from existing hosting models to Isolated and Shared Compute
{: #hosting-model-transition-timeline}

Multi-tenant users that are automatically transitioned to Shared Compute will be *grandfathered*, meaning that they get RAM and CPU increased to the Shared Compute minimum resource allocations, if required. These increases will not be charged until May 2025.
{: important}

Starting August 2024, existing multi-tenant instances will begin the transition to Shared Compute; this means that first, RAM minimum allocation on multi-tenant instances will be applied (8 GB RAM for RabbitMQ, 4 GB RAM for all other databases), lifting the RAM of existing instances that fall below these minimums. All new provisioning requests will also have to abide to the minimum resource requirements (1 CPU and 8 GB RAM for RabbitMQ, 0.5 CPU and 4 GB RAM for all other databases). Existing dedicated core users will not be impacted by minimum resource requirements unless a scale or provision action is invoked on an instance that is currently below these minimums.

Following this, multi-tenant databases will be gradually transitioned from non-determinstic CPU allocation to the deterministic Shared Compute CPU allocation. Ahead of this transition, [monitor your database's CPU usage](/docs/cloud-databases?topic=cloud-databases-sysdig-monitor#sysdig-monitor-dashboards-cpu-cores-used-per-member) to determine what allocation is required to maintain your current performance level.

Existing multi-tenant users will be grandfathered through to May 2025 for both CPU and minimum RAM resource allocations that are automatically added. 

From September 2024, the transition of multi-tenant instance to shared compute will be complete. All new multi-tenant provisions are placed on Shared Compute. Dedicated cores provisioning remain available at this time.

In May 2025, we will transition dedicated core users to Isolated Compute and remove grandfathering for Shared Compute instances. All Dedicated Cores instances will be transitioned to the nearest larger Isolated Compute size. Dedicated Core instances can follow the simple switchover steps to transition to Isolated Compute at any time by using the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference){: external}, the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction){: external}, or through [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

Notifications will be sent ahead of changes, including at the following times: 
- Before the transition of multi-tenant to Shared Compute, to notify you of expected changes. 
- After all multi-tenant instances are transitioned to Shared Compute resource allocations, to recommend that you review your database performance and adjust resources as necessary. 
- Before final shutdown of dedicated cores and the transition to Isolated Compute. Additionally, before the end of grandfathering of Shared Compute instances.
You can also find all notifications at [{{site.data.keyword.Bluemix_notm}} announcements](https://cloud.ibm.com/status/announcement).

Ahead of the May 2025 date, if you have a multi-tenant instance, there are a few exceptions where grandfathering would no longer apply: 

- If you have an existing database and change your RAM allocation only, you will be charged corresponding to the RAM changes. 
- If you have an existing database and change your CPU allocation, you will be charged for all CPU and RAM allocated to your database.
- If you create a new Shared Compute instance, you will be charged for all CPU and RAM allocated to your database. 
- If you transition your multi-tenant instance yourself to Shared Compute, you will be charged for all CPU and RAM allocated to your database.  

## Shared Compute transition placement
{: #shared-compute-placement}

To determine how existing hosting models will switch over to Shared and Isolated Compute, review the tables below. In the switchover, the assumption is that the starting points are old style multitenant (CPU unallocated, or 0) and dedicated cores. 

| **If your current resource allocation is N CPU x M RAM <br> (Non-RabbitMQ Databases):** | **You will be automatically placed on <br> (Non-RabbitMQ Databases):** |
|-------------------------|---------------------|
| N = 0 CPU, M < 4 GB RAM | 0.5 CPU x 4 GB RAM, Shared Compute |
| N = 0 CPU, 4 GB RAM < M ≤ 16 GB RAM | M/8 CPU x M GB RAM, Shared Compute|
| N = 0 CPU, M > 16 GB RAM | 2 CPU x M GB RAM, Shared Compute |
| 0 CPU < N ≤ 4 CPU, M < 16 GB RAM | 4 CPU x 16 GB RAM, Isolated Compute |
| 4 CPU < N ≤ 8 CPU OR 16 GB RAM, < M < 32 GB RAM | 8 CPU x 32 GB RAM, Isolated Compute |
| 4 CPU < N ≤ 8 CPU OR 32 GB RAM, < M < 64 GB RAM | 8 CPU x 64 GB RAM, Isolated Compute |
| 8 CPU < N ≤ 16 CPU OR 32 GB RAM, < M < 64 GB RAM | 16 CPU x 64 GB RAM, Isolated Compute |
| 16 CPU < N ≤ 32 CPU OR 64 GB RAM, < M < 128 GB RAM | 32 CPU x 128 RAM, Isolated Compute |
| 16 CPU < N ≤ 30 CPU OR 64 GB RAM, < M < 240 GB RAM | 30 CPU x 240 RAM, Isolated Compute |
{: caption="Table 4. Automatic transition placement" caption-side="bottom"}

<br>

<br>

| **If your current resource allocation is N CPU x M RAM <br> (RabbitMQ):** | **You will be automatically placed on <br> (RabbitMQ):** |
|-------------------------|---------------------|
| N = 0 CPU, M < 8 GB RAM | 1 CPU x 8 GB RAM, Shared Compute |
| N = 0 CPU, 8 GB RAM < M ≤ 16 GB RAM | M/8 CPU x M GB RAM, Shared Compute |
| N = 0 CPU, M > 16 GB RAM | 2 CPU x M GB RAM, Shared Compute |
| 0 CPU < N ≤ 4 CPU , M < 16 GB RAM | 4 CPU x 16 GB RAM, Isolated Compute |
| 4 CPU < N ≤ 8 CPU OR 16 GB RAM < M < 32 GB RAM | 8 CPU x 32 GB RAM, Isolated Compute |
| 4 CPU < N ≤ 8 CPU OR 32 GB RAM < M < 64 GB RAM | 8 CPU x 64 GB RAM, Isolated Compute |
| 8 CPU < N ≤ 16 CPU OR 32 GB RAM < M < 64 GB RAM | 16 CPU x 64 GB RAM, Isolated Compute |
| 16 CPU < N ≤ 32 CPU OR 64 GB RAM < M < 128 GB RAM | 32 CPU x 128 RAM, Isolated Compute |
| 16 CPU < N ≤ 30 CPU OR 64 GB RAM < M < 240 GB RAM | 30 CPU x 240 RA, Isolated Compute |
{: caption="Table 5. Automatic transition placement RabbitMQ" caption-side="bottom"}

## Hosting models FAQ
{: #hosting-models-faq}

**My Shared Compute database has 0 CPU. What does this mean?**

Shared Compute automatically allocates CPU for customers that do not specify their CPU amount. On API v5, this automatically allocated setting shows as CPU = 0. We also return an "Allocation as Fraction" result that shows what specific CPU value you have. CPU is allocated at 1/8th of a RAM, starting from each databases' minimum CPU amount up to 2 CPU. This CPU value will continue to scale as the RAM value scales.

**Per the [Shared Compute transition placement](/docs/cloud-databases?topic=cloud-databases-hosting-models&interface=cli#shared-compute-placement), my understanding is that because this instance has 8 GB of RAM, it should have 1 CPU allocated per member, but the cloud-databases CLI show 0 CPUs allocated.**

See the previous answer.

**I want fractional CPU. How do I do that?**

Scale your database to the `multitenant` hosting model, and its CPU to 0. This turns on the Shared Compute automatic CPU allocation, where CPU is 1/8th of the database's RAM allocation, up to 2 CPU.

**What does it mean to have fractional CPU?**

CPU time is divided into units called periods or time slices. In each time slice you get a duration of CPU run time.

In general, the number of cores you specify decides how much CPU time you get. The default kernel run time is 50ms; therefore, with one core of CPU available, there is 20 time slices of 50ms run time.

If an instance A requests 0.5 cores or 500 millicores, assuming for simplicity that there is only one core of CPU on a node or server, instance A will get 10 time slices of 50ms run time each to complete the task. If it cannot complete the task within 10 time slices, the kernel throttles the instance's process after the 10 runs. The remaining 10 time slices for this CPU (since 1 core can have 20 time slices using default run time duration) is then scheduled for other processes while A waits. Once that is done, instance A gets the CPU for another 10 time slices.

**I want to scale my database's resources, but they don't seem to be scaling?**

For Shared Compute instances, make sure to set the host flavor to `multitenant` and separately set your CPU and RAM values. For automatically scaling CPU (capped at 2 CPU), set the CPU to 0. To scale Isolated Compute, set the host flavor to your desired size; do not set CPU and RAM values since the Isolated size already includes allocations for both. For more information, see the [Scaling documentation](/docs/cloud-databases?topic=cloud-databases-scale-instance).

**My database is on a hosting model, even though my Terraform configuration didn't specify it.**

Starting August, we begun to switchover customer instances to the new hosting models. This can lead to Terraform scripts that do not reflect the actualstate of the database, since these scripts do not have the new `host_flavor` parameter. Your database will still function as normal, though we recommend adding the `host_flavor` parameter for future ease of use.

**What does it mean to switch / migrate between hosting models? Will there be downtime?**

Switching between databases is not a large migration, but a standard operation similar to our maintenance work. Therefore, it does not involve downtime, though [we recommend](/docs/cloud-databases?topic=cloud-databases-responsibilities-cloud-databases) your application to have retry and reconnect logic.

**If we switch to a hosting model, or switch between hosting models, will the disk size be retained as per the current configuration?**

Yes. Your disk will not be impacted due to hosting model changes.

**Does autoscaling work?**

Autoscaling continues to work for new hosting models. For Shared Compute, RAM and disk autoscaling remains available. For Isolated Compute, disk autoscaling is available.

Note: Due to the size jumps across Isolated Compute, we have currently disallowed RAM/CPU autoscaling on Isolated Compute. If there is interest in this feature, let our team know.

**I’m getting a CLI failed status error or a 403 forbidden error, but on the UI and CLI it looks like my scale operation completed?**

This is due to CLI token expiry. The CLI expires tokens to quickly to preserve the security of your system, meaning any operations in progress will show a fail state. We recommend refreshing your session, and checking the database for the results of the task.
