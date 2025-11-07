---

copyright:
  years: 2023, 2025
lastupdated: "2025-11-07"

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

When provisioning, choose the CPU x RAM size for the machine to set up your database. This machine will be exclusively assigned to running your database instance. Storage is still selected separately, allowing you to determine the size of disk and number of [IOPS](#x3858854){: term} your database receives. Scale your database and change your machine size using your preferred method: the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/cloud-databases?topic=cloud-databases-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or using [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

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
{: caption="Host flavor sizing parameter" caption-side="bottom"}

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

When provisioning, choose the CPU x RAM size for the machine to set up your database. This machine will be exclusively assigned to running your database instance. Storage is still selected separately, allowing you to determine the size of disk and number of [IOPS](#x3858854){: term} your database receives. Scale your database and change your machine size using your preferred method: the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/cloud-databases?topic=cloud-databases-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or using [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

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
{: caption="Host flavor sizing parameter" caption-side="bottom"}

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

When provisioning, choose the CPU x RAM size for the machine to set up your database. This machine will be exclusively assigned to running your database instance. Storage is still selected separately, allowing you to determine the size of disk and number of [IOPS](#x3858854){: term} your database receives. Scale your database and change your machine size using your preferred method: the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/cloud-databases?topic=cloud-databases-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or using [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

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
{: caption="Host flavor sizing parameter" caption-side="bottom"}

## Isolated Compute capacity
{: isolated-compute-capacity}

Isolated Compute fully isolates your database, including database management pods (which touch user data). These management pods take up some overhead in your isolated compute instance, consuming a portion of the machine's compute. The following table shows the estimated remaining compute for each Isolated Compute size.

| **Host flavor** | **CPU remaining** | **RAM remaining** |
|:-------------------------:|:---------------------:|:---------------------:|
| 4 CPU x 16 RAM            | 2.865    | 12.193    |
| 8 CPU x 32 RAM            | 6.855    | 26.952    |
| 8 CPU x 64 RAM            | 6.855    | 56.519    |
| 16 CPU x 64 RAM           | 14.835   | 56.519    |
| 32 CPU x 128 RAM          | 30.795  | 115.738    |
| 30 CPU x 240 RAM          | 28.8  | 223.596    |
{: caption="Isolated Compute capacity" caption-side="bottom"}

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
{: caption="Choosing between hosting models" caption-side="bottom"}

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
| etcd | ![Checkmark icon](../icons/checkmark-icon.svg)  | ![Checkmark icon](../icons/checkmark-icon.svg)  |
{: caption="{{site.data.keyword.databases-for}} hosting model availability" caption-side="bottom"}
