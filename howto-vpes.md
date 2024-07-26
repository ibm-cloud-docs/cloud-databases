---
copyright:
  years: 2021, 2024
lastupdated: "2024-07-26"

subcollection: cloud-databases

keywords: pDNS, private endpoints, private networking, vpe, virtual private endpoints

---

{:external: .external target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:note: .note}
{:tip: .tip}


# Virtual Private Endpoints 
{: #vpes}

This document covers all the IBM Cloud Databases: {{site.data.keyword.databases-for-elasticsearch}}, {{site.data.keyword.databases-for-enterprisedb}}, {{site.data.keyword.databases-for-etcd}}, {{site.data.keyword.databases-for-mongodb}}, {{site.data.keyword.databases-for-postgresql}}, {{site.data.keyword.databases-for-redis}}, {{site.data.keyword.databases-for-mysql_full}}, and {{site.data.keyword.messages-for-rabbitmq}}. 
{: .note}

{{site.data.keyword.cloud}} Virtual Private Endpoint (VPE) for {{site.data.keyword.vpc_full}} provides connection points to IBM services on the IBM private network from your VPC network.


## Using Virtual Private Endpoints
{: #using-vpes}

Virtual Private Endpoints (VPEs) are generally available in all regions. 
{: .note}

### Before you begin
{: #vpes-before-begin}

- You need to have an [{{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/registration){: .external}
- And a {{site.data.keyword.databases-for}} deployment. You can [provision](/docs/cloud-databases?topic=cloud-databases-getting-started-cdb-provision-instance) one from the [{{site.data.keyword.cloud_notm}} catalog](https://cloud.ibm.com/catalog/services/). Give your deployment a memorable name that appears in your account's Resource List.

### Setting up your VPE
{: #vpes-setup}

1. Create an {{site.data.keyword.vpc_full}}. Follow the `Getting started` [instructions here](/docs/vpc?topic=vpc-getting-started). 

2. Make sure that your VPC has at least one VSI (virtual server instance), and can connect to the VSI. You can use the UI, CLI, and API to quickly provision {{site.data.keyword.vpc_full}} from the Virtual server instances page in IBM Cloud console: 
   1. Use this information when you're creating [generation 1 virtual server instances](/docs/vpc-on-classic-vsi?topic=vpc-on-classic-vsi-creating-virtual-servers).
   2. Use this information when you're creating [generation 2 virtual server instances](/docs/vpc?topic=vpc-creating-virtual-servers).

3. Make sure your {{site.data.keyword.databases-for}} deployment's [private endpoint is enabled](/docs/cloud-databases?topic=cloud-databases-service-endpoints).

4. In the {{site.data.keyword.cloud_notm}} console, click the menu icon and select -> VPC Infrastructure -> Network -> Virtual private endpoint gateways. Create a VPE for your {{site.data.keyword.databases-for}} instances with the [following instruction](/docs/vpc?topic=vpc-about-vpe). 

5. After you create your VPE, it might take a few minutes for the new VPE and pDNS to complete the process and begin working for your VPC. Completion is confirmed when you see an IP address set in the [details view](/docs/vpc?topic=vpc-vpe-viewing-details-of-an-endpoint-gateway) of the VPE. 

6. To make sure pDNS is functioning for your VPE, `ssh` into your VSI and run `nslookup <instance_hostname>`. The following example shows the output from running `nslookup` on instance hostnames of `host-0.private.databases.appdomain.cloud`, `host-1.private.databases.appdomain.cloud`, and `host-2.private.databases.appdomain.cloud`:
   ```bash
   root@test-vpc-vsi:~# nslookup host-0.private.databases.appdomain.cloud
   Server:		127.0.0.53
   Address:	127.0.0.53#53
   Non-authoritative answer:
   Name:	host-0.private.databases.appdomain.cloud
   Address: 10.240.64.6
   ```
   ```bash
   root@test-vpc-vsi:~# nslookup host-1.private.databases.appdomain.cloud
   Server:		127.0.0.53
   Address:	127.0.0.53#53
   Non-authoritative answer:
   Name:	host-1.private.databases.appdomain.cloud
   Address: 10.240.64.6
   ```
   ```bash
   root@test-vpc-vsi:~# nslookup host-2.private.databases.appdomain.cloud
   Server:		127.0.0.53
   Address:	127.0.0.53#53
   Non-authoritative answer:
   Name:	host-2.private.databases.appdomain.cloud
   Address: 10.240.64.6    < ---- your VPE IP address
   ```

7. You can now use your instance in the VSI. For example, 

   ```bash
   mongo -u $USERNAME -p $PASSWORD --tls --tlsCAFile /root/   c--authenticationDatabase admin --host replset/host-0.private.databaseappdomain.   cloud:30066,host-1.private.databases.appdomain.cloud:30066,host-private.   databases.appdomain.cloud:30066
   ```

### VPE Discoverability
{: #vpes-discoverability}

Following the previous steps results in a database instance with private endpoints that is reachable with the Virtual Private Endpoints from your VPC network.

Database instances with private endpoints are reachable from any account within the private network and access to each instance requires authentication. To restrict this access to specific IP addresses, or ranges of IP addresses, configure [allowlisting](/docs/cloud-databases?topic=cloud-databases-allowlisting). 
{: .important}

A MongoDB deployment cannot support both [public and private endpoints simultaneously](/docs/cloud-databases?topic=cloud-databases-service-endpoints&interface=ui). *This cannot be changed after provisioning*.
{: .important}


For more information, see [Secure access to services by using service endpoints](/docs/account?topic=account-service-endpoints-overview).
{: .tip}

### More resources
{: #vpes-resources}

- [Planning for virtual private endpoint gateways](/docs/vpc?topic=vpc-planning-considerations)
- [Creating an endpoint gateway](/docs/vpc?topic=vpc-ordering-endpoint-gateway)
- For further assistance, see the [FAQs for virtual private endpoints here](/docs/vpc?topic=vpc-faqs-vpe), and the `Troubleshooting VPE gateways` documentation that includes [how to fix communications issues here](/docs/vpc?topic=vpc-troubleshoot-cannot-communicate). 
