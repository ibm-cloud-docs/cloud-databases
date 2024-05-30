---

copyright:
  years: 2023, 2024
lastupdated: "2024-05-30"

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

If you select Shared Compute in the {{site.data.keyword.cloud_notm}} console, you then choose an initial resource allocation preset: **Small** (1 CPU and 8 GB RAM for {{site.data.keyword.rabbitmq}}, 0.5 CPU and 4 GB RAM for all other databases) or **Custom** (2 CPU and 4 GB RAM). Small has a fixed amount of CPU and RAM, but you can change disk. Custom can be completely customized.

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


To provision a {{site.data.keyword.databases-for}} instance on Isolated Compute, use the {{site.data.keyword.databases-for}} Resource Controller [API](https://cloud.ibm.com/apidocs/resource-controller/resource-controller#create-resource-instance){: external}. Specify `multitenant` as the `host_flavor`.

Use a command like:

```sh
curl -X POST https://resource-controller.cloud.ibm.com/v2/resource_instances -H "Authorization: Bearer <IAM token>" -H 'Content-Type: application/json' -d '{
    "type": "postgresql",
    "version": "14",
    "platform": "classic",
    "location": "us-south",
    "parameters": {"members_host_flavor": "multitenant", "members_cpu_allocation_count": 3, "members_memory_allocation_mb": 3072, "members_disk_allocation_mb": 256000}
  }'
```
{: pre}


## {{site.data.keyword.databases-for}} Isolated Compute
{: #hosting-models-iso-compute-api}
{: api}

Isolated Compute is a secure single-tenant offering for complex, highly-performant enterprise workloads. By placing your deployment and all associated user-data management agents on an isolated machine, {{site.data.keyword.databases-for}} Isolated Compute provides dedicated computing resources, dedicated storage bandwidth, and hypervisor-level isolation.

When provisioning, choose the CPU x RAM size for the machine to set up your database. This machine will be exclusively assigned to running your database instance. Storage is still selected separately, allowing you to determine the size of disk and number of [IOPS](#x3858854){: term} your database receives. Scale your database and change your machine size using your preferred method: the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or using [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

Use a command like:

```sh
curl -X POST https://resource-controller.cloud.ibm.com/v2/resource_instances -H "Authorization: Bearer <IAM token>" -H 'Content-Type: application/json' -d '{
    "type": "postgresql",
    "version": "14",
    "platform": "classic",
    "location": "us-south",
    "parameters": {"members_host_flavor": "b3c.4x16.encrypted"}
  }'
```
{: pre}

The `host_flavor value` parameter defines your Isolated Compute sizing. Input the appropriate value for your desired size.


### The `host flavor` parameter
{: #hosting-models-host-flavor-parameter}
{: api}   
   
The `host_flavor` parameter defines your Compute sizing. To provision a Shared Compute instance, specify `multitenant`. To provision an Isolated Compute instance, input the appropriate value for your desired CPU and RAM configuration. 

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


<br>
<br>

With Isolated Compute, you cannot provision or scale instances by submitting a CPU or memory allocation.

Thus, the following command does not work:

```sh
{
  "memory": {
    "allocation_mb": 55296
  },
  "cpu": {
    "allocation_count": 3
  }
}
```
{: pre}

Instead, you must specify a `host_flavor` like this:

```sh
{
  "host_flavor": {
    "id": <value>
  }
}
```
{: pre}

A host flavor represents fixed sizes of guaranteed resource allocations. You can see which host flavors are available by calling the [host flavors capability endpoint](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#capability) like this:

```sh
curl -X POST  https://api.{region}.databases.cloud.ibm.com/v5/ibm/capability/flavors  \
  -H 'Authorization: Bearer <>' \
  -H 'ContentType: application/json' \
  -d '{
    "deployment": {
      "type": "postgresql",
      "location": "us-south"
    },
  }'

{
  "deployment": {
    "type": "postgresql",
    "location": "us-south",
    "platform": "classic"
  },
  "capability": {
    "flavors": [
      {
        "id": "b3c.4x16.encrypted",
        "name": "4x16",
        "cpu": {
          "allocation_count": 4
        },
        "memory": {
          "allocation_mb": 16384
        },
        "hosting_size": "xs"
      },
      {
        "id": "b3c.8x32.encrypted",
        "name": "8x32",
        "cpu": {
          "allocation_count": 8
        },
        "memory": {
          "allocation_mb": 32768
        },
        "hosting_size": "s"
      },
      {
        "id": "m3c.8x64.encrypted",
        "name": "8x64",
        "cpu": {
          "allocation_count": 8
        },
        "memory": {
          "allocation_mb": 65536
        },
        "hosting_size": "s+"
      },
      {
        "id": "b3c.16x64.encrypted",
        "name": "16x64",
        "cpu": {
          "allocation_count": 16
        },
        "memory": {
          "allocation_mb": 65536
        },
        "hosting_size": "m"
      },
      {
        "id": "b3c.32x128.encrypted",
        "name": "32x128",
        "cpu": {
          "allocation_count": 32
        },
        "memory": {
          "allocation_mb": 131072
        },
        "hosting_size": "l"
      },
      {
        "id": "m3c.30x240.encrypted",
        "name": "30x240",
        "cpu": {
          "allocation_count": 30
        },
        "memory": {
          "allocation_mb": 245760
        },
        "hosting_size": "xl"
      },
      {
        "id": "multitenant",
        "name": "multitenant",
        "cpu": {
          "allocation_count": 0
        },
        "memory": {
          "allocation_mb": 0
        },
        "hosting_size": ""
      }
    ]
  }
}

```
{: pre}

As shown, the isolated compute host flavors available to a PostgreSQL instance in the `us-south` region are:

- `b3c.4x16.encrypted`
- `b3c.8x32.encrypted`
- `m3c.8x64.encrypted`
- `b3c.16x64.encrypted`
- `b3c.32x128.encrypted`
- `m3c.30x240.encrypted`

To provision or scale your instance to 4 CPUs and `16384` megabytes or RAM, you would submit:

```sh
{
  "host_flavor": {
    "id": "`b3c.4x16.encrypted`"
  }
}
```
{: pre}

To scale your instance up to 8 CPUs and `32768` megabytes of RAM, you would submit:

```sh
{
  "host_flavor": {
    "id": "b3c.8x32.encrypted"
  }
}
```
{: pre}

### Scale through the CLI (old snippets)
{: #hosting-models-scaling-cli}
{: cli}

To scale a {{site.data.keyword.databases-for}} Isolated Compute instance, modify the `deployment-groups-set` parameter. Use a command like:

```sh
ibmcloud cdb deployment-groups-set <deploymentid> <groupid> [--disk <val>] [--hostflavor <val>]
```
{: pre}

To scale a {{site.data.keyword.databases-for}} Shared Compute instance. Use a command like:

```sh
ibmcloud cdb deployment-groups-set <deploymentid> <groupid> [--memory <val>] [--cpu <val>] [--disk <val>] [--hostflavor multitenant]
```
{: pre}

### Scale through the API (old snippets)
{: #hosting-models-scaling-api}
{: api}

To scale a {{site.data.keyword.databases-for}} Isolated Compute instance, use the {{site.data.keyword.databases-for}} API [Scaling endpoint](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#setdeploymentscalinggroup){: external}.

Use a command like:

```sh
curl -X PATCH https://api.{region}.databases.cloud.ibm.com/v5/ibm/deployments/{id}/groups/{group_id}
-H 'Authorization: Bearer <>'
-H 'Content-Type: application/json'
-d '{"group":
      {"host_flavor":
        {"id": "b3c.4x16.encrypted"}
      }
    }' \
```
{: pre}

To scale a {{site.data.keyword.databases-for}} Isolated Compute instance to a Shared Compute instance

```sh
curl -X PATCH https://api.{region}.databases.cloud.ibm.com/v5/ibm/deployments/{id}/groups/{group_id}
-H 'Authorization: Bearer <>'
-H 'Content-Type: application/json'
-d '{"group":
      {"host_flavor":
        {"id": "multitenant"}
      },
      {"cpu":
        {"allocation_count": 3}
      },
      {"memory":
        {"allocation_mb": 2048}
      }
    }' \
```
{: pre}

CPU and RAM allocation is not allowed when provisioning or scaling through Isolated Compute. You must specify `mulitenant` for the `host_flavor` parameter.
{: note}

CPU and RAM autoscaling is not supported on {{site.data.keyword.databases-for}} Isolated Compute. Disk autoscaling is available. If you have provisioned an Isolated instance or switched over from a deployment with autoscaling, keep an eye on your resources using [{{site.data.keyword.monitoringfull}} integration](/docs/databases-for-mongodb?topic=databases-for-mongodb-monitoring), which provides metrics for memory, disk space, and disk I/O utilization. To add resources to your instance, manually scale your deployment.
{: note}


### Provision an instance through Shared Compute using Terraform (old snippets)
{: #hosting-models-provisioning-terraform}
{: terraform}

To provision an instance through Shared Compute, use Terraform.

```terraform
data "ibm_resource_group" "group" {
  name = "<your_group>"
}
resource "ibm_database" "<your_database>" {
  name              = "<your_database_name>"
  plan              = "standard"
  location          = "eu-gb"
  service           = "databases-for-etcd"
  resource_group_id = data.ibm_resource_group.group.id
  tags              = ["tag1", "tag2"]
  adminpassword                = "password12"
  group {
    group_id = "member"
    host_flavor {
      id = "multitenant"
    },
    cpu {
      allocation_count = 3
    }
    memory {
      allocation_mb = 2048
    }
    disk {
      allocation_mb = 256000
    }
  }
  users {
    name     = "user123"
    password = "password12"
  }
  allowlist {
    address     = "172.168.1.1/32"
    description = "desc"
  }
}
output "ICD Etcd database connection string" {
  value = "http://${ibm_database.test_acc.ibm_database_connection.icd_conn}"
}
```
{: codeblock}

The `host_flavor` parameter defines your Isolated Compute sizing. Input the appropriate value for your desired size. To provision a Shared Compute instance, specify `multitenant`.
| **Host Flavor** | **host_flavor value** |
|:-------------------------:|:---------------------:|
| Shared Compute            | `multitenant`    |
| 4 CPU x 16 RAM            | `b3c.4x16.encrypted`    |
| 8 CPU x 32 RAM            | `b3c.8x32.encrypted`    |
| 8 CPU x 64 RAM            | `m3c.8x64.encrypted`    |
| 16 CPU x 64 RAM           | `b3c.16x64.encrypted`   |
| 32 CPU x 128 RAM          | `b3c.32x128.encrypted`  |
| 30 CPU x 240 RAM          | `m3c.30x240.encrypted`  |
{: caption="Table 1. Host Flavor sizing parameter" caption-side="bottom"}

CPU and RAM allocation is not allowed when provisioning or scaling through Isolated Compute. You must specify `mulitenant` for the `host_flavor` parameter.
{: note}

CPU and RAM autoscaling is not supported on {{site.data.keyword.databases-for}} Isolated Compute. Disk autoscaling is available. If you have provisioned an Isolated instance or switched over from a deployment with autoscaling, keep an eye on your resources using [{{site.data.keyword.monitoringfull}} integration](/docs/databases-for-mongodb?topic=databases-for-mongodb-monitoring), which provides metrics for memory, disk space, and disk I/O utilization. To add resources to your instance, manually scale your deployment.
{: note}

### Provisioning through Terraform (old snippets)
{: #hosting-models-iso-compute-provisioning-tf}
{: terraform}

To provision an instance through Isolated Compute, use Terraform.

```terraform
data "ibm_resource_group" "group" {
  name = "<your_group>"
}
resource "ibm_database" "<your_database>" {
  name              = "<your_database_name>"
  plan              = "standard"
  location          = "eu-gb"
  service           = "databases-for-etcd"
  resource_group_id = data.ibm_resource_group.group.id
  tags              = ["tag1", "tag2"]
  adminpassword                = "password12"
  group {
    group_id = "member"
    host_flavor {
      id = "b3c.8x32.encrypted"
    }
    disk {
      allocation_mb = 256000
    }
  }
  users {
    name     = "user123"
    password = "password12"
  }
  allowlist {
    address     = "172.168.1.1/32"
    description = "desc"
  }
}
output "ICD Etcd database connection string" {
  value = "http://${ibm_database.test_acc.ibm_database_connection.icd_conn}"
}
```
{: codeblock}

To provision an instance through Shared Compute, use Terraform.

```terraform
data "ibm_resource_group" "group" {
  name = "<your_group>"
}
resource "ibm_database" "<your_database>" {
  name              = "<your_database_name>"
  plan              = "standard"
  location          = "eu-gb"
  service           = "databases-for-etcd"
  resource_group_id = data.ibm_resource_group.group.id
  tags              = ["tag1", "tag2"]
  adminpassword                = "password12"
  group {
    group_id = "member"
    host_flavor {
      id = "multitenant"
    },
    cpu {
      allocation_count = 3
    }
    memory {
      allocation_mb = 2048
    }
    disk {
      allocation_mb = 256000
    }
  }
  users {
    name     = "user123"
    password = "password12"
  }
  allowlist {
    address     = "172.168.1.1/32"
    description = "desc"
  }
}
output "ICD Etcd database connection string" {
  value = "http://${ibm_database.test_acc.ibm_database_connection.icd_conn}"
}
```
{: codeblock}

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

## Switching hosting models
{: #hosting-models-switching}

To switch between Shared and Isolated Compute, select the model you want, review your resource selection, and switch. Switching hosting models does not cause downtime, as this is not a backup and restore migration. Instead, the same process is applied as for updates or database instance scaling. The database processes will perform a rolling restart, causing existing connections to be dropped. Thus, the recommendation is as always to ensure that your application has retry and reconnect logic to immediately re-establish a connection.

For example, submit a value of `multitenant` to switch your instance from another hosting model to *Shared Compute*. Instances running on Shared Compute can be scaled by submitting new CPU and memory values:

```sh
{
  "host_flavor": {
    "id": "multitenant"
  },
  "memory": {
    "allocation_mb": 16384
  },
  "cpu": {
    "allocation_count": 4
  }
}
```
{: pre}

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
