---
copyright:
  years: 2020
lastupdated: "2020-10-06"

keywords: guidance, recommendations, best practices, initial steps, setup

subcollection: cloud-databases

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:note: .note}
{:tip: .tip}


# Getting to production for {{site.data.keyword.databases-for}}
{: #best-practices}

## Prework

1. Complete your data modeling and architectural reviews to ensure cloud-native alignment. If you need help with that, contact the [IBM Garage] (https://cloud.ibm.com/catalog/services/consult-with-ibm-garage)
2. Determine the best method for your initial setup, including [Terraform, API, CLI, or UI methods](/docs/cloud-databases?topic=cloud-databases-provisioning).
3. If you require the ability to manage your database's encryption key for data-at-rest, you must `Bring Your Own encryption Key` (BYOK) when creating your database. This setup can’t be changed after your instance is provisioned.
4. Make sure that [IAM access policies and resource groups](/docs/account?topic=account-iamoverview) are set up correctly for your business protocols.
5. Ensure that your account is [VRF-enabled](/docs/account?topic=account-vrf-service-endpoint#before-service-endpoint-enablement)


## Sample "Getting to production" checklist

1. Create a database with the required disk, RAM, and virtual CPUs. While these scaling parameters can be changed after the initial provisioning, disks cannot be scaled down. 
2. If you would like Hypervisor level isolation, or if you want to isolate the database from any possible "noisy-neighbor" impact, ensure that your [database CPU allocation](/docs/cloud-databases?topic=cloud-databases-provisioning#using-the-catalog) is provisioned to use `dedicated cores`.
3. Add users. (See the related documentation for your {{site.data.keyword.databases-for}} instance.)
4. Change the `Admin` Password
5. _Optional step for {{site.data.keyword.databases-for-postgresql}} only_: set up and validate [read-only replicas](/docs/databases-for-postgresql?topic=databases-for-postgresql-read-only-replicas)
6. Set up Auto-Scaling policies if appropriate. 
   * The recommended disk space reflects the minimum amounts that are needed, but note that disk capacity cannot be scaled down without a backup and restore. RAM and virtual CPUs (vCPUs) can scale up and down. Likewise, auto-scaling can scale memory but cannot scale due to memory use, which during normal use can approach 100% for databases.
   For more information on Auto-scaling capabilities, see the related documentation for your {{site.data.keyword.databases-for}} instance.  
   {: .note}
7. Set up monitoring with Sysdig, AT, and LogDNA. At minimum, set alerts on:
   * [Sysdig](/docs/Monitoring-with-Sysdig) - when disk usage is greater than 80% of provisioned capacity
   * [Activity Tracker with LogDNA](/docs/cloud-databases?topic=cloud-databases-activity-tracker) audit events for control plane actions, such as ip allowlist updates, scaling, initiating a backup
   * [Logging with LogDNA](/docs/cloud-databases?topic=cloud-databases-logging) - any particular database-specific logs.
   * If available, turn on granular in-database auditing (only available for {{site.data.keyword.databases-for-postgresql}} and {{site.data.keyword.databases-for-mongodb}} Enterprise Edition).
8. Set up an [IP Allowlist](/docs/cloud-databases?topic=cloud-databases-allowlisting) for your instance
9. Set [Private Endpoints](/docs/cloud-databases?topic=cloud-databases-service-endpoints#private-endpoints) if the application runs in IBM Cloud. You might also choose to disable public endpoints (highly recommended if no connection is expected from outside IBM Cloud)
10. Connect to your application by using TLS.
11. Thoroughly load test, and then load test again.
12. Validate the application's reconnect logic; for many high-volume applications, retry is not enough and you must reconnect.
13. Set up development and testing environments as separate instances, then work through this checklist again. Depending on your requirements, you might not want to use dedicated cores for these test environments. Not using dedicated cores helps to keep costs lower. 
14. Complete [Disaster Recovery](/docs/cloud-databases?topic=cloud-databases-ha-dr) testing. Test restoring your application to a different IBM Cloud region. Ensure you are able to connect to a "restored" database with new connection details.
    * Ensure you are able to achieve your Recovery Point Objective (RPO) and Recovery Time Objective (RTO) 


