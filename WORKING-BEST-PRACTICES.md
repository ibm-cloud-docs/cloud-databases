---
copyright:
  years: 2020
lastupdated: "2020-09-30"

keywords: guidance, recommendations, best practice, 

subcollection: cloud-databases

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:note: .note}
{:tip: .tip}


# Best practices for IBM Cloud Databases
{: #best-practices}

## Prework

1. Ensure you complete your data modeling and architectural reviews to ensure cloud-native best practices.
2. Determine the best method for your initial set-up, including [Terraform, API, CLI, or UI methods](/docs/cloud-databases?topic=cloud-databases-provisioning).
3. If you require the ability to manage the key, you must `Bring Your Own encryption Key` (BYOK) when creating your database. This can’t be changed after provisioning your instance.
4. Make sure that IAM access policies and resource groups are set up correctly for your business protocols.
5. Ensure your account is [VRF-enabled](https://cloud.ibm.com/docs/account?topic=account-vrf-service-endpoint#before-service-endpoint-enablement)


## Best Practices

1. Create a database with the required disk, RAM, and virtual CPUs. While these scaling parameters can be changed after the initial provisioning, disks cannot be scaled down. 
2. If you would like Hypervisor level isolation, or if you want to isolate the database from any possible "noisy-neighbor" impact, ensure your [database CPU allocation](/docs/cloud-databases?topic=cloud-databases-provisioning#using-the-catalog) is provisioned to use `dedicated cores`.
3. Add users
4. Change the `Admin` Password
5. _Optional step for {{site.data.keyword.databases-for-postgresql}} only_: set up and validate [read-only replicas](/docs/databases-for-postgresql?topic=databases-for-postgresql-read-only-replicas)
6. Set up Auto-Scaling policies if wanted. 
   * The recommended disk space reflects the minimum amounts that are needed, but note that disk capacity cannot be scaled down without a backup and restore. RAM and virtual CPUs (vCPUs) can scale up and down. Likewise, auto-scaling can scale memory but cannot scale due to memory use, which can approach 100% for databases.
   See the Auto-scaling documentation of your {{site.data.keyword.databases-for}} instance for more information on capabilities.  
   {: .note}
7. Set up monitoring with Sysdig, AT, and LogDNA. At minimum, set alerts on:
   * [Sysdig](/docs/Monitoring-with-Sysdig) - disk utilization is greater than 80% of provisioned capacity
   * [Activity Tracker with LogDNA](/docs/cloud-databases?topic=cloud-databases-activity-tracker) audit events in for control plane actions, such as ip whitelisting, scaling, initiating a backup
   * [Logging with LogDNA](/docs/cloud-databases?topic=cloud-databases-logging) - any particular database-specific logs.
   * If available, turn on granular in-database auditing (only available for {{site.data.keyword.databases-for-postgresql}} and {{site.data.keyword.databases-for-mongodb}} Enterprise Edition).
8. Set up [IP Allowlisting](/docs/cloud-databases?topic=cloud-databases-allowlisting) for your instance
9.  Set [Private Endpoints](/docs/cloud-databases?topic=cloud-databases-service-endpoints#private-endpoints) if the application runs in IBM Cloud. You might also choose to disable public endpoints (highly recommended if no connection is expected from outside IBM Cloud)
10. Connect to application with TLS
11. Thoroughly load test, and then, load test again.
12. Validate the application's reconnect logic; for many high-volume applications, retry is not enough and you must reconnect.
13. Set up development and testing environments as separate instances, then work through this checklist again. You may or may not want to use dedicated cores for these test environments. Not using dedicated cores helps to keep costs lower. 
14. Complete [Disaster Recovery](/docs/cloud-databases?topic=cloud-databases-ha-dr) testing. Test restoring your application to a different IBM Cloud region. Ensure you are able to connect to a "restored" database with new connection details.
    * Ensure you are able to achieve your Recovery Point Objective (RPO) and Recovery Time Objective (RTO) 


