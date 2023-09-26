---

copyright:
  years: 2023
lastupdated: "2023-09-26"

subcollection: cloud-databases

keywords: isolated compute, hosting models

---

{{site.data.keyword.attribute-definition-list}}

# {{site.data.keyword.databases-for}} Hosting Models
{: #hosting-models}

To allow for reliable resource allocation, {{site.data.keyword.databases-for}} offers two hosting models: Shared Compute and Isolated Compute. {{site.data.keyword.databases-for}} Shared Compute is a cost-effective, flexible option for your database deployment. {{site.data.keyword.databases-for}} Isolated Compute is an appealing option for applications that require more precise control, security, or performance.
{: shortdesc}

Switching hosting models does not cause downtime.
{: note}

## {{site.data.keyword.databases-for}} Isolated Compute
{: #hosting-models-iso-compute}

By placing your deployment and all associated user-data operations on its own isolated machine, {{site.data.keyword.databases-for}} Isolated Compute provides dedicated computing resourcees and security. Shared Compute improves our existing multi-tenant offering ({{site.data.keyword.databases-for}} Shared Compute) by delivering predictable performance and stronger security through logically separated tenants.

CPU and RAM autoscaling is not supported on {{site.data.keyword.databases-for}} Isolated Compute. Disk autoscaling is available. If you have provisioned an Isolated instance or migrated from a deployment with autoscaling, keep an eye on your resources using [{{site.data.keyword.monitoringfull}} integration](/docs/databases-for-mongodb?topic=databases-for-mongodb-monitoring), which provides metrics for memory, disk space, and disk I/O utilization. To add resources to your instance, manually scale your deployment.
{: note}

## {{site.data.keyword.databases-for}} Isolated Compute Provisioning
{: #hosting-models-iso-compute-provisioning}

### {{site.data.keyword.databases-for}} Isolated Compute Provisioning through the UI
{: #hosting-models-iso-compute-provisioning}
{: ui}

### {{site.data.keyword.databases-for}} Isolated Compute using the API
{: #hosting-models-iso-compute-api}
{: api}

#### Retrieve Isolated Compute Resources the API
{: #hosting-models-iso-compute-retrieve-api}
{: api}

To retrieve the Isolated Compute resources available for a {{site.data.keyword.databases-for}} Isolated Compute instance, use the {{site.data.keyword.databases-for}} API [Scaling endpoint](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#listdeploymentscalinggroups){: external}.

Use a command like:

```sh
curl -X GET https://api.{region}.databases.cloud.ibm.com/v5/ibm/deployments/{id}/groups -H 'Authorization: Bearer <>' \
```
{: pre}

#### Provisioning using the API
{: #hosting-models-iso-compute-provisioning-api}
{: api}

To provision a {{site.data.keyword.databases-for}} Isolated Compute instance, use the {{site.data.keyword.databases-for}} API [Capability endpoint](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#capability){: external}.

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

#### Scaling using the API
{: #hosting-models-iso-compute-scaling-api}
{: api}

To scale a {{site.data.keyword.databases-for}} Isolated Compute instance, use the {{site.data.keyword.databases-for}} API [Scaling endpoint](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#setdeploymentscalinggroup){: external}.

Use a command like:

```sh
curl -X PATCH https://api.{region}.databases.cloud.ibm.com/v5/ibm/deployments/{id}/groups/{group_id} 
-H 'Authorization: Bearer <>' 
-H 'Content-Type: application/json' 
-d '{"group": 
      {"host_flavor": "b3c.4x16.encrypted"}
    }' \
```
{: pre}

CPU and RAM autoscaling is not supported on {{site.data.keyword.databases-for}} Isolated Compute. Disk autoscaling is available. If you have provisioned an Isolated instance or migrated from a deployment with autoscaling, keep an eye on your resources using [{{site.data.keyword.monitoringfull}} integration](/docs/databases-for-mongodb?topic=databases-for-mongodb-monitoring), which provides metrics for memory, disk space, and disk I/O utilization. To add resources to your instance, manually scale your deployment.
{: note}

### {{site.data.keyword.databases-for}} Isolated Compute Provisioning through the CLI
{: #hosting-models-iso-compute-provisioning}
{: cli}



### {{site.data.keyword.databases-for}} Isolated Compute Provisioning through Terraform
{: #hosting-models-iso-compute-provisioning}
{: terraform}

## {{site.data.keyword.databases-for}} Isolated Compute Pricing
{: #hosting-models-iso-compute-pricing}

Isolated Compute grandfathered pricing structure:
- if version EOL: no change
- if increase RAM: no change
- if increase CPU: charge for all cores, cores ONLY
- if migrate to shared: charge for all cores, cores ONLY

we might still want to raise the RAM price (ie, use ram_new rather than ram parts), so the logic should still be there. we just don’t want to raise ram prices now
Right now, no new/migrated shared instances will have increased ram pricing. Instead, when you provision a new instance, migrate an instance, or scale CPU, you will be charged for all the CPU you have, and no longer be considered grandfathered , but this does not add the RAM $5 increase.

## {{site.data.keyword.databases-for}} Shared Compute
{: #hosting-models-iso-compute}

## Hosting model migration
{: #hosting-models-migration}

Migration between hosting models is an easy, one-click process. There is no downtime during the migration and you can feel free to move back and forth between models.

## Hosting model Grandfathering
{: #hosting-models-grandfathering}


