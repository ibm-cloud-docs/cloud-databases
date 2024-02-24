---

copyright:
  years: 2023, 2024
lastupdated: "2024-02-24"

subcollection: cloud-databases

keywords: isolated compute, hosting models

---

{{site.data.keyword.attribute-definition-list}}

# {{site.data.keyword.databases-for}} Hosting Models
{: #hosting-models}

To allow for reliable resource allocation, {{site.data.keyword.databases-for}} offers two hosting models: Shared Compute and Isolated Compute. {{site.data.keyword.databases-for}} Shared Compute is a cost-effective, flexible option for your database deployment. {{site.data.keyword.databases-for}} Isolated Compute is an appealing option for applications that require more precise control, security, or performance.
{: shortdesc}

## {{site.data.keyword.databases-for}} Shared Compute
{: #hosting-models-shared-compute}

Shared compute is a flexible multi-tenant offering for dynamic, fine-tuned, and decoupled capacity selections.

Each database instance receives a deterministic CPU allocation. If an instance is provisioned without selecting a CPU amount, Shared Compute automatically allocates a small amount of CPU to your database up to a 2 core max. Automatic CPU is provided at a 1:8 ratio of CPU:RAM; therefore, a user with 1 GB RAM receives 1/8th of a CPU; an user with 8 GB RAM receives 1 CPU; and an user with 20 GB RAM receives 2 CPU due to the 2 CPU limit.

If you have higher performance requirements than 2 CPU, you can easily leverage the flexibility of the Shared model. With the ability to select the amount of CPU and RAM resources you receive, scale performance to fit your workload. Additionally, if you know that your instance will experience variable demand, use autoscaling to set not only the expected load and duration that would initiate resource scaling, but also the resource and cost limit your database will scale to.

Due to each service's individual requirements, {{site.data.keyword.databases-for}} has minimums in place for all Shared Compute instances. When all instances are transitioned to Shared Compute, we will apply the same minimums to Shared Compute and Isolated Core instances. Current users of multi-tenant will be grandfathered.
{: note}

## {{site.data.keyword.databases-for}} Isolated Compute
{: #hosting-models-iso-compute}

Isolated Compute is a secure single-tenant offering for complex, highly-performant enterprise workloads. By placing your deployment and all associated user-data operations on an isolated machine, {{site.data.keyword.databases-for}} Isolated Compute provides computing resources and security.

At provisioning, choose the CPU x RAM size for the machine to set up your database. This machine will be exclusively assigned to running your database instance, ensuring hypervisor-level isolation from any other databases.
To enhance isolation, specialized database management agents operate alongside the database instance on the same isolated machines. Both IO bandwidth and network bandwidth will be exclusively allocated to the database instance.

Storage is still selected separately, allowing you to determine the number of [IOPS](#x3858854){: term} your database receives. Scale your database and change your machine size through your preferred method: the [dashboard](https://cloud.ibm.com/){: external}, the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or through [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.


CPU and RAM allocation is not allowed when provisioning or scaling through Isolated Compute. You must specify `mulitenant` for the `host_flavor` parameter.
{: note}

CPU and RAM autoscaling is not supported on {{site.data.keyword.databases-for}} Isolated Compute. Disk autoscaling is available. If you have provisioned an Isolated instance or switched over from a deployment with autoscaling, monitor your resources using [{{site.data.keyword.monitoringfull}} integration](/docs/databases-for-mongodb?topic=databases-for-mongodb-monitoring), which provides metrics for memory, disk space, and disk I/O utilization. To add resources to your instance, manually scale your deployment.
{: note}

### Isolated Compute Sizing
{: #hosting-models-iso-compute-sizing}

Isolated Compute features 6 size selections:
- 4 CPU x 16 RAM
- 8 CPU x 32 RAM
- 8 CPU x 64 RAM
- 16 CPU x 64 RAM
- 32 CPU x 128 RAM
- 30 CPU x 240 RAM

The price of CPU and RAM resources remains the same.

## Switching hosting models
{: #hosting-models-switching}

To switch between our Shared and Isolated compute, select the model you want, review your resource selection, and switch. Switching hosting models does not cause downtime.

## Hosting model grandfathering
{: #hosting-models-grandfathering}

Current multi-tenant users that are automatically switched over to Shared Compute will begin to be charged for their CPU use starting March 2025.
{: important}

Starting in May 2024, existing multi-tenant customers will undergo a gradual transition from free-for-all CPU allocation to a deterministic allocation. However, automatic CPU allocation will continue with grandfathered charging until March 2025.

All Dedicated Cores instances will be switched over to the nearest larger Isolated Compute size. To provision a Dedicated Cores instance before it is shut down, use the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference){: external}, the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction){: external}, or through [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

New Shared Compute users, or users who switch over to Shared Compute on their own, will receive Shared Compute charging.

## {{site.data.keyword.databases-for}} Provisioning
{: #hosting-models-provisioning}

### Provision through the UI
{: #hosting-provisioning-ui}
{: ui}

To provision a {{site.data.keyword.databases-for}} service instance through the UI, select your **hosting type**. Choose either Shared Compute or Isolated Compute. Next, select the appropriate **Resource Allocation** for your workload.

### Provision through the CLI
{: #hosting-provisioning-cli}
{: cli}

To provision a {{site.data.keyword.databases-for}} instance, use the `deployment-groups-set`. Use a command like:

```sh
ibmcloud cdb deployment-groups-set <deploymentid> <groupid> [--memory <val>] [--cpu <val>] [--disk <val>] [--hostflavor <val>]
```
{: pre}

### Provision using the API
{: #hosting-models-provisioning-api}
{: api}

To provision a {{site.data.keyword.databases-for}} instance on Isolated Compute, use the {{site.data.keyword.databases-for}} API [Capability endpoint](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#capability){: external}.

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

To provision a Shared Compute instance, specify `multitenant`.

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

### Retrieve Resources through the API
{: #hosting-models-retrieve-api}
{: api}

To retrieve the Isolated Compute resources available for a {{site.data.keyword.databases-for}} Isolated Compute instance, use the {{site.data.keyword.databases-for}} API [Scaling endpoint](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#listdeploymentscalinggroups){: external}.

Use a command like:

```sh
curl -X GET https://api.{region}.databases.cloud.ibm.com/v5/ibm/deployments/{id}/groups -H 'Authorization: Bearer <>' \
```
{: pre}

### Scale through the CLI
{: #hosting-models-scaling-cli}
{: cli}

To scale a {{site.data.keyword.databases-for}} Shared Compute instance. Use a command like:

```sh
ibmcloud cdb deployment-groups-set <deploymentid> <groupid> [--memory <val>] [--cpu <val>] [--disk <val>] [--hostflavor multitenant]
```
{: pre}

### Scale through the API
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

### Scaling through Terraform
{: #hosting-models-scaling-tf}
{: terraform}

To scale a {{site.data.keyword.databases-for}} Isolated Compute instance, use Terraform.

Update `host_flavor` with your desired amount. To implement your change, run `terraform apply`.

### Provisioning through the CLI
{: #hosting-models-provisioning-cli}
{: cli}

To provision a {{site.data.keyword.databases-for}} Isolated Compute instance, use the CLI.

```sh
ibmcloud resource service-instance-create <INSTANCE_NAME> <SERVICE_NAME> <SERVICE_PLAN> <LOCATION> `{"members_host_flavor": "<host_flavor value>"}`
```
{: pre}

The `host_flavor value` parameter defines your Isolated Compute sizing. Input the appropriate value for your desired size. To provision a Shared Compute instance, specify `multitenant`.
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

### Provisioning through Terraform
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
{: caption="Table 2. Host Flavor sizing parameter" caption-side="bottom"}

CPU and RAM allocation is not allowed when provisioning or scaling through Isolated Compute. You must specify `multitenant` for the `host_flavor` parameter.
{: note}

CPU and RAM autoscaling is not supported on {{site.data.keyword.databases-for}} Isolated Compute. Disk autoscaling is available. If you have provisioned an Isolated instance or switched over from a deployment with autoscaling, keep an eye on your resources using [{{site.data.keyword.monitoringfull}} integration](/docs/databases-for-mongodb?topic=databases-for-mongodb-monitoring), which provides metrics for memory, disk space, and disk I/O utilization. To add resources to your instance, manually scale your deployment.
{: note}
