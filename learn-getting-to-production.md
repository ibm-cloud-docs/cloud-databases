---
copyright:
  years: 2020, 2023
lastupdated: "2023-03-02"

keywords: guidance, recommendations, best practices, initial steps, setup

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Getting to production for {{site.data.keyword.databases-for}}
{: #best-practices}

## Prework
{: #before-starting}

- [ ] To ensure cloud-native alignment, complete your data modeling and architectural reviews. For help with data modeling and architecture, contact the [IBM Garage](https://cloud.ibm.com/catalog/services/consult-with-ibm-garage){: .external}.
- [ ] Determine the best method for your initial setup, including [Terraform, API, CLI, or UI methods](/docs/cloud-databases?topic=cloud-databases-provisioning).
- [ ] To manage your database's encryption key for data-at-rest, you must [Bring Your Own encryption Key (BYOK)](/docs/cloud-databases?topic=cloud-databases-key-protect) when creating your database. This setup cannot be changed after your instance is provisioned.
- [ ] Make sure that [IAM access policies and resource groups](/docs/account?topic=account-iamoverview) are set up correctly for your business protocols.
- [ ] Ensure that your account is [VRF-enabled](/docs/account?topic=account-vrf-service-endpoint#before-service-endpoint-enablement).
- [ ] Understand your database's high availability model. This is covered in the "High-Availability" section of each database's documentation. 
- [ ] To ensure you receive messages, enroll in [IBM Cloud notifications](https://cloud.ibm.com/docs/account?topic=account-email-prefs), specifically the "Resource Activity" notification. We directly notify you when your database version is approaching end of life. In addition, you may bookmark our [Database Version Lifecycle policy](/docs/cloud-databases?topic=cloud-databases-versioning-policy), which is kept up to date with end of life dates and resources for all databases.


## Sample "Getting to production" checklist
{: #sample-checklist}

- [ ] Create a database with the required disk, RAM, and virtual CPUs. While these scaling parameters can be changed after the initial provisioning, disks *cannot be scaled down*. 
- [ ] If you would like hypervisor level isolation, or if you want to guarantee a number of vCPUs, ensure that your [database CPU allocation](/docs/cloud-databases?topic=cloud-databases-provisioning#using-the-catalog) is provisioned to use `dedicated cores`.
- [ ] Add users. See the related documentation for your {{site.data.keyword.databases-for}} instance.
- [ ] Change the `Admin` Password.
- [ ] Set up auto scaling policies, if appropriate. 
   Default auto scaling logic is the suggested baseline. Tune these parameters to your budget and use case. The recommended disk space reflects the minimum amounts that are needed, but note that disk capacity cannot be scaled down without a backup and restore. RAM and virtual CPUs (vCPUs) can scale up and down. Memory auto scaling works based on disk I/O usage to optimize page cache performance. Databases will not auto-scale when in-use memory approaches 100%; this is often the desired state.{: .note}
   
   For more information, see your {{site.data.keyword.databases-for}} instance.  
- [ ] Set up monitoring with {{site.data.keyword.monitoringfull}}, {{site.data.keyword.at_full}}, and {{site.data.keyword.loganalysisfull}}. At minimum, set alerts on:
   * [{{site.data.keyword.monitoringlong_notm}}](/docs/monitoring) - when disk usage is greater than 80% of provisioned capacity (we encourage you to use auto scaling for disk capacity). We also encourage you to use, understand, and alert on all provided metrics like disk I/O or CPU usage. 
   * [{{site.data.keyword.at_full_notm}}](/docs/cloud-databases?topic=cloud-databases-activity-tracker) audit events for control plane actions, such as failed backups, IP allowlist updates, and auto scaling.  
   * [{{site.data.keyword.loganalysisfull_notm}}](/docs/cloud-databases?topic=cloud-databases-logging) - any particular database-specific logs you wish to be notified about, such as slow query logs. 
   * If available, turn on granular in-database auditing (only available for {{site.data.keyword.databases-for-postgresql}} and {{site.data.keyword.databases-for-mongodb}} Enterprise Edition).
- [ ] Set up an [IP allowlist](/docs/cloud-databases?topic=cloud-databases-allowlisting) for your instance.
- [ ] Set [Private Endpoints](/docs/cloud-databases?topic=cloud-databases-service-endpoints#private-endpoints). You might also choose to disable public endpoints (highly recommended if no connection is expected from outside {{site.data.keyword.cloud}}).
- [ ] Make sure that your application uses TLS for connecting to the database. Insecure connections to {{site.data.keyword.databases-for}} are not allowed.
- [ ] Thoroughly load test, and then load test again.
- [ ] Validate the application's reconnect logic. For some applications retry is not enough and you must reconnect. Review the article, ["Unresponsive Redis Service"](https://developer.ibm.com/articles/error-detection-and-handling-with-redis/) for an example of implementation on {{site.data.keyword.databases-for-redis_full}}. 
- [ ] Set up development and testing environments as separate instances, then work through this checklist again. Depending on your requirements, you might not want to use dedicated cores for these test environments. Not using dedicated cores helps to keep costs lower. 
- [ ] Complete [Disaster Recovery](/docs/cloud-databases?topic=cloud-databases-ha-dr) testing. Test restoring your application to a different IBM Cloud region. Ensure you are able to connect to a "restored" database with new connection details.
    * Understand your Recovery Point Objective (RPO) and Recovery Time Objective (RTO) requirements and ensure that you can meet them with your database's configuration.

To resolve a database's UUID, use the command `ibmcloud resource search <UUID>`. Other useful CLI commands are: `ibmcloud cdb about` and `ibmcloud cdb cxn`. For more information, see the [CLI plug-in reference documentation](/docs/cloud-databases?topic=databases-cli-plugin-cdb-reference).
{: .tip}
