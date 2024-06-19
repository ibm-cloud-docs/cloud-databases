---

copyright:
  years: 2023, 2024
lastupdated: "2024-06-19"

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

## {{site.data.keyword.databases-for}} Shared Compute
{: #hosting-models-shared-compute-cli}
{: cli}

Shared Compute is a flexible multi-tenant offering for dynamic, fine-tuned, and decoupled capacity selections.

Each database instance receives a deterministic CPU allocation. If an instance is provisioned without selecting a CPU amount, Shared Compute automatically allocates a small amount of CPU to your database up to a 2 core max. Automatic CPU is provided at a 1:8 ratio of CPU:RAM; therefore, a user with 4 GB RAM receives 4/8th of a CPU; a user with 8 GB RAM receives 1 CPU; and an user with 20 GB RAM receives 2 CPU due to the 2 CPU limit.

If you have higher performance requirements than 2 CPU, you can easily leverage the flexibility of the Shared model. With the ability to select the amount of CPU and RAM resources you receive, performance can be scaled to fit your workload. Additionally, if you know that your instance will experience variable demand, use RAM autoscaling to set not only the expected load and duration that would initiate resource scaling, but also the resource and cost limit your database will scale to.

Because of each service's individual requirements, {{site.data.keyword.databases-for}} has minimum resource requirements in place for all Shared Compute instances. When all existing multi-tenant instances are transitioned to Shared Compute, these minimum resource requirements will be applied. Current multi-tenant instances will not be charged (that is, they will be _grandfathered_) for any increase to up to these minimum resource requirements actioned by IBM until May 2025. For more information, see [Hosting model grandfathering](/docs/cloud-databases?topic=cloud-databases-hosting-models&interface=ui#hosting-models-grandfathering).
{: note}

## {{site.data.keyword.databases-for}} Isolated Compute
{: #hosting-models-iso-compute-cli}
{: cli}

Isolated Compute is a secure single-tenant offering for complex, highly-performant enterprise workloads. By placing your deployment and all associated user-data management agents on an isolated machine, {{site.data.keyword.databases-for}} Isolated Compute provides dedicated computing resources, dedicated storage bandwidth, and hypervisor-level isolation.

When provisioning, choose the CPU x RAM size for the machine to set up your database. This machine will be exclusively assigned to running your database instance. Storage is still selected separately, allowing you to determine the size of disk and number of [IOPS](#x3858854){: term} your database receives. Scale your database and change your machine size using your preferred method: the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or using [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

## {{site.data.keyword.databases-for}} Shared Compute
{: #hosting-models-shared-compute-api}
{: api}

Shared Compute is a flexible multi-tenant offering for dynamic, fine-tuned, and decoupled capacity selections.

Each database instance receives a deterministic CPU allocation. If an instance is provisioned without selecting a CPU amount, Shared Compute automatically allocates a small amount of CPU to your database up to a 2 core max. Automatic CPU is provided at a 1:8 ratio of CPU:RAM; therefore, a user with 4 GB RAM receives 4/8th of a CPU; a user with 8 GB RAM receives 1 CPU; and an user with 20 GB RAM receives 2 CPU due to the 2 CPU limit.

If you have higher performance requirements than 2 CPU, you can easily leverage the flexibility of the Shared model. With the ability to select the amount of CPU and RAM resources you receive, performance can be scaled to fit your workload. Additionally, if you know that your instance will experience variable demand, use RAM autoscaling to set not only the expected load and duration that would initiate resource scaling, but also the resource and cost limit your database will scale to.

Because of each service's individual requirements, {{site.data.keyword.databases-for}} has minimum resource requirements in place for all Shared Compute instances. When all existing multi-tenant instances are transitioned to Shared Compute, these minimum resource requirements will be applied. Current multi-tenant instances will not be charged (that is, they will be _grandfathered_) for any increase to up to these minimum resource requirements actioned by IBM until May 2025. For more information, see [Hosting model grandfathering](/docs/cloud-databases?topic=cloud-databases-hosting-models&interface=ui#hosting-models-grandfathering).
{: note}

## {{site.data.keyword.databases-for}} Isolated Compute
{: #hosting-models-iso-compute-api}
{: api}

Isolated Compute is a secure single-tenant offering for complex, highly-performant enterprise workloads. By placing your deployment and all associated user-data management agents on an isolated machine, {{site.data.keyword.databases-for}} Isolated Compute provides dedicated computing resources, dedicated storage bandwidth, and hypervisor-level isolation.

When provisioning, choose the CPU x RAM size for the machine to set up your database. This machine will be exclusively assigned to running your database instance. Storage is still selected separately, allowing you to determine the size of disk and number of [IOPS](#x3858854){: term} your database receives. Scale your database and change your machine size using your preferred method: the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or using [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

## {{site.data.keyword.databases-for}} Shared Compute
{: #hosting-models-shared-compute-terraform}
{: terraform}

Shared Compute is a flexible multi-tenant offering for dynamic, fine-tuned, and decoupled capacity selections.

Each database instance receives a deterministic CPU allocation. If an instance is provisioned without selecting a CPU amount, Shared Compute automatically allocates a small amount of CPU to your database up to a 2 core max. Automatic CPU is provided at a 1:8 ratio of CPU:RAM; therefore, a user with 4 GB RAM receives 4/8th of a CPU; a user with 8 GB RAM receives 1 CPU; and an user with 20 GB RAM receives 2 CPU due to the 2 CPU limit.

If you have higher performance requirements than 2 CPU, you can easily leverage the flexibility of the Shared model. With the ability to select the amount of CPU and RAM resources you receive, performance can be scaled to fit your workload. Additionally, if you know that your instance will experience variable demand, use RAM autoscaling to set not only the expected load and duration that would initiate resource scaling, but also the resource and cost limit your database will scale to.

Because of each service's individual requirements, {{site.data.keyword.databases-for}} has minimum resource requirements in place for all Shared Compute instances. When all existing multi-tenant instances are transitioned to Shared Compute, these minimum resource requirements will be applied. Current multi-tenant instances will not be charged (that is, they will be _grandfathered_) for any increase to up to these minimum resource requirements actioned by IBM until May 2025. For more information, see [Hosting model grandfathering](/docs/cloud-databases?topic=cloud-databases-hosting-models&interface=ui#hosting-models-grandfathering).
{: note}

## {{site.data.keyword.databases-for}} Isolated Compute
{: #hosting-models-iso-compute-terraform}
{: terraform}

Isolated Compute is a secure single-tenant offering for complex, highly-performant enterprise workloads. By placing your deployment and all associated user-data management agents on an isolated machine, {{site.data.keyword.databases-for}} Isolated Compute provides dedicated computing resources, dedicated IO and network bandwidth, and hypervisor-level isolation.

When provisioning, choose the CPU x RAM size for the machine to set up your database. This machine will be exclusively assigned to running your database instance. Storage is still selected separately, allowing you to determine the size of disk and number of [IOPS](#x3858854){: term} your database receives. Scale your database and change your machine size using your preferred method: the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or using [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

CPU and RAM autoscaling is not supported on {{site.data.keyword.databases-for}} Isolated Compute. Disk autoscaling is available. If you provisioned an isolated instance or switched over from a deployment with autoscaling, monitor your resources using [{{site.data.keyword.monitoringfull}} integration](/docs/databases-for-mongodb?topic=databases-for-mongodb-monitoring), which provides metrics for memory, disk space, and disk I/O utilization. To add resources to your instance, manually scale your deployment.
{: note}

### Isolated Compute sizing
{: #hosting-models-iso-compute-sizing}

Isolated Compute features 6 size selections:

- 4 CPU x 16 RAM
- 8 CPU x 32 RAM
- 8 CPU x 64 RAM
- 16 CPU x 64 RAM
- 32 CPU x 128 RAM
- 30 CPU x 240 RAM

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

For more detailed instructions, see your [database specific page](https://cloud.ibm.com/docs/cloud-databases?topic=cloud-databases-getting-started-cdb-provision-instance&interface=ui). 

## Switching hosting models
{: #hosting-models-switching}

To switch to or between Shared and Isolated Compute, select your **hosting type** from either Shared Compute or Isolated Compute. On the CLI, API, or Terraform, add a new `host_flavor` parameter.

Then, moving to the hosting type is as simple as running a scale command with the hosting type selected. For more detailed instructions, commands, and parameters, see your database specific page.

Switching hosting models does not cause downtime, as this is not a backup and restore migration. Instead, the same process is applied as for updates or database instance scaling. The database processes will perform a rolling restart, causing existing connections to be dropped. Thus, the recommendation is as always to ensure that your application has retry and reconnect logic to immediately re-establish a connection.

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
| EnterpriseDB |  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| Mongo Community | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| Mongo Enterprise |  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| Elastic Enterprise | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| Elastic Platinum |  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| etcd | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| MySQL | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| Redis | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
| RabbitMQ | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
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

| **If your current resource allocation is N CPU x M RAM <br> (Non-RabbitMQ Version):** | **You will be automatically placed on <br> (Non-RabbitMQ Version):** |
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

| **If your current resource allocation is N CPU x M RAM <br> (RabbitMQ Version):** | **You will be automatically placed on <br> (RabbitMQ Version):** |
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
