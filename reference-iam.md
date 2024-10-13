---

copyright:
  years: 2019, 2024
lastupdated: "2024-09-13"

subcollection: cloud-databases

---

{:shortdesc: .shortdesc}
{:external: .external target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:note: .note} 
{:tip: .tip}

# Identity and Access Management integration
{: #iam}

Access to {{site.data.keyword.cloud}} Databases service instances for users in your account is controlled by {{site.data.keyword.cloud_notm}} [Identity and Access Management (IAM)](/docs/account?topic=account-cloudaccess). 

This document covers the integration of IAM with Cloud Databases: {{site.data.keyword.databases-for-postgresql}}, {{site.data.keyword.databases-for-mongodb}}, {{site.data.keyword.databases-for-redis}}, {{site.data.keyword.databases-for-elasticsearch}}, {{site.data.keyword.databases-for-mysql_full}}, {{site.data.keyword.messages-for-rabbitmq}}, {{site.data.keyword.databases-for-enterprisedb}} and {{site.data.keyword.databases-for-etcd}}. 
{: .note}

IAM is only integrated with high-level service access, which governs privileges and operations available in the [Cloud Databases API](/apidocs/cloud-databases-api/cloud-databases-api-v5) and the [Cloud Databases CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference). It does not govern database-level users and privileges. Database access is governed by the standard access controls provided by the database. IAM does not control database users.

For more information about assigning user roles in {{site.data.keyword.cloud_notm}}, see [Managing IAM access](/docs/account?topic=account-assign-access-resources).

The following table provides a general overview of actions that are mapped to service management roles. Service management roles enable users to perform tasks on service resources at the service level. For example, assign user access for the service, create or delete service IDs, create instances, and bind instances to applications.

| Service management role | Description of actions | Example actions |
| ----------------- | ----------------- | ----------------- |
| Viewer | As a viewer, you can view database instances but you can't make configuration changes. | View service overview and view alerts. |
| Operator | As an operator, you can view database instances and make configuration changes that include managing database credentials. | Scale a deployment and change a deployment's password. |
| Editor | As an editor, you can perform all platform actions (including making configuration changes and managing credentials) except for managing the account and assigning access policies. | Scale a deployment and change a deployment's password. |
| Administrator | As an administrator, you can perform all platform actions, including assigning access policies to other users. | Scale a deployment, change a deployment's password, and assign access policies. |
{: caption="IAM user roles and actions" caption-side="top"}

## Actions for {{site.data.keyword.databases-for}} API
{: #actions}

Access to certain API endpoints and requests is governed by role. The following lists the access policy for each role for {{site.data.keyword.cloud}} Databases. 

### Viewer 
{: #viewer}

The allowed actions for the Viewer role.

```sh
GET /v5/ibm/deployables
Read Deployables
---
GET /v5/ibm/regions
Read Discover available regions
---
GET /v5/ibm/tasks/:task_id
Read a Task
---
GET /v5/ibm/backups/:backup_id
Read a Backup
---
GET /v5/ibm/deployments/:deployment_id
Read a Deployment
---
GET /v5/ibm/deployables/:deployable_id/groups
Read deployable group
---
GET /v5/ibm/deployments/:deployment_id/point_in_time_recovery_data
Read all deployment point-in-time-recovery data
---
GET /v5/ibm/deployments/:deployment_id/tasks
Read all deployment tasks
---
GET /v5/ibm/deployments/:deployment_id/backups
Read all deployment backups
---
GET /v5/ibm/deployments/:deployment_id/remotes
Read all deployment remotes
---
GET /v5/ibm/deployables/:deployable_id/groups
Read all deployment groups
---
GET /v5/ibm/deployments/:deployment_id/configuration/schema
Read deployment configuration schema
---
GET /v5/ibm/deployments/:deployment_id/users/:user_type/:user_id/connections/:endpoint_type
Read deployment user connections
---
POST /v5/ibm/deployments/:deployment_id/users/:user_type/:user_id/connections/:endpoint_type
Create deployment user connections
---
GET /v5/ibm/deployments/:deployment_id/allowlists/ip_addresses
Read Allowlisted IP Addresses
```

### Operator and Editor
{: #operator}

The Operator and Editor roles are functionally the same for {{site.data.keyword.databases-for}}. This list contains allowed actions for the Operator and the Editor roles.

```sh
GET /v5/ibm/deployables
Read Deployables
---
GET /v5/ibm/regions
Read Discover available regions
---
GET /v5/ibm/tasks/:task_id
Read a Task
---
GET /v5/ibm/backups/:backup_id
Read a Backup
---
GET /v5/ibm/deployments/:deployment_id
Read a Deployment
---
GET /v5/ibm/deployables/:deployable_id/groups
Read deployable group
---
GET /v5/ibm/deployments/:deployment_id/point_in_time_recovery_data
Read all deployment point-in-time-recovery data
---
GET /v5/ibm/deployments/:deployment_id/tasks
Read all deployment tasks
---
GET /v5/ibm/deployments/:deployment_id/backups
Read all deployment backups
---
POST /v5/ibm/deployments/:deployment_id/backups
Create an on-demand backup
---
GET /v5/ibm/deployments/:deployment_id/remotes
Read all deployment remotes
---
POST /v5/ibm/deployments/:deployment_id/remotes/resync
Resync remote replica
---
GET /v5/ibm/deployables/:deployable_id/groups
Read all deployment groups
---
PATCH /v5/ibm/deployments/:deployment_id/groups/:group_id
Set scaling values on a specified group.
---
DELETE /v5/ibm/deployments/:deployment_id/management/database_connections
Closes all the connections on a deployment. Available for PostgreSQL and EnterpriseDB ONLY.
---
PATCH /v5/ibm/deployments/:deployment_id/configuration
Update deployment configuration
---
GET /v5/ibm/deployments/:deployment_id/configuration/schema
Read deployment configuration schema
---
POST /v5/ibm/deployments/:deployment_id/users/:user_type
Create a user based on user type
---
DELETE /v5/ibm/deployments/:deployment_id/users/:user_type/:user_id
Remove a user based on user type
---
GET /v5/ibm/deployments/:deployment_id/users/:user_type/:user_id/connections/:endpoint_type
Read deployment user connections
---
POST /v5/ibm/deployments/:deployment_id/users/:user_type/:user_id/connections/:endpoint_type
Create deployment user connections
---
GET /v5/ibm/deployments/:deployment_id/allowlists/ip_addresses
Read Allowlisted IP Addresses
---
POST /v5/ibm/deployments/:deployment_id/allowlists/ip_addresses
Create an Allowlisted IP Addresses
---
DELETE /v5/ibm/deployments/:deployment_id/allowlists/ip_addresses/:ip_address_id
Remove an Allowlisted IP Addresses
---
PUT /v5/ibm/deployments/:deployment_id/allowlists/ip_addresses
Bulk allowlist IP addresses
---
POST /v5/ibm/deployments/:deployment_id/elasticsearch/file_syncs
Create elasticsearch file sync
```

### Administrator
{: #admin}

The allowed actions for the Administrator role.

```sh
GET /v5/ibm/deployables
Read Deployables
---
GET /v5/ibm/regions
Read Discover available regions
---
GET /v5/ibm/tasks/:task_id
Read a Task
---
GET /v5/ibm/backups/:backup_id
Read a Backup
---
GET /v5/ibm/deployments/:deployment_id
Read a Deployment
---
GET /v5/ibm/deployables/:deployable_id/groups
Read deployable group
---
GET /v5/ibm/deployments/:deployment_id/point_in_time_recovery_data
Read all deployment point-in-time-recovery data
---
GET /v5/ibm/deployments/:deployment_id/tasks
Read all deployment tasks
---
GET /v5/ibm/backups/:backup_id
Read all deployment backups
---
POST /v5/ibm/deployments/:deployment_id/backups
Create an on-demand backup
---
GET /v5/ibm/deployments/:deployment_id/backups
Read all deployment remotes
---
POST /v5/ibm/deployments/:deployment_id/remotes/resync
Resync remote replica
---
GET /v5/ibm/deployables/:deployable_id/groups
Read all deployment groups
---
PATCH /v5/ibm/deployments/:deployment_id/groups/:group_id
Read deployment group
---
DELETE /v5/ibm/deployments/:deployment_id/management/database_connections
Kill all database connections
---
PATCH /v5/ibm/deployments/:deployment_id/configuration
Update deployment configuration
---
GET /v5/ibm/deployments/:deployment_id/configuration/schema
Read deployment configuration schema
---
POST /v5/ibm/deployments/:deployment_id/users/:user_type
Create a user based on user type
---
PATCH /v5/ibm/deployments/:deployment_id/users/:user_type/:user_id
Update a DeploymentUser
---
DELETE /v5/ibm/deployments/:deployment_id/users/:user_type/:user_id
Remove a user based on user type
---
GET /v5/ibm/deployments/:deployment_id/users/:user_type/:user_id/connections/:endpoint_type
Read deployment user connections
---
POST /v5/ibm/deployments/:deployment_id/users/:user_type/:user_id/connections/:endpoint_type
Create deployment user connections
---
GET /v5/ibm/deployments/:deployment_id/allowlists/ip_addresses
Read Allowlisted IP Addresses
---
POST /v5/ibm/deployments/:deployment_id/allowlists/ip_addresses
Create an Allowlisted IP Addresses
---
DELETE /v5/ibm/deployments/:deployment_id/allowlists/ip_addresses/:ip_address_id
Remove an Allowlisted IP Addresses
---
PUT /v5/ibm/deployments/:deployment_id/allowlists/ip_addresses
Bulk allowlist IP addresses
---
POST /v5/ibm/deployments/:deployment_id/elasticsearch/file_syncs
Create elasticsearch file sync
```
