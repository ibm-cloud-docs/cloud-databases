---
Copyright:
  years: 2019
lastupdated: "2019-04-08"

subcollection: cloud-databases

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:tip: .tip}

# Service Endpoints Integration
{: #service-endpoints}

All {{site.data.keyword.databases-for}} deployments offer integration with [{{site.data.keyword.cloud_notm}} Service Endpoints](/docs/services/service-endpoint?topic=service-endpoint-about#about). It allows you to enable connections to your deployments from the public internet and over the {{site.data.keyword.cloud_notm}} private network.

## Public Endpoints

By default, all deployments provision with a service endpoint on the {{site.data.keyword.cloud_notm}} public network. Access to deployments is available from the public internet. Your environment needs to have internet access to connect to a deployment.

## Private Endpoints

A deployment with a service endpoint on the private network gets an endpoint that is not accessible from the public internet. All traffic is routed to hardware dedicated to {{site.data.keyword.databases-for}} deployments and remains on the {{site.data.keyword.cloud_notm}} private network. Once your environment has access to the {{site.data.keyword.cloud_notm}} private network, an internet connection is not required to connect to your deployment.

## Enabling Service Endpoints

If you only wish to use connections over the public internet, you do not have to enable Service Endpoints on your {{site.data.keyword.cloud_notm}} account. If you want to enable private networking on your deployments you will need to follow the instructions in the Service Endpoint documentation under [Enabling your account for using Service Endpoints using IBM Cloud CLI](/docs/services/service-endpoint?topic=service-endpoint-getting-started#cs_cli_install_steps).

## Provisioning with Service Endpoints

From the catalog page:

### Provisioning from the CLI and API

Service Endpoints are enabled through an optional parameter when you provision through the CLI and API. Provisioning is handled by the Resource Controller, and you pass the `service-endpoint` parameter one of the options `public`, `private`, or `public-and-private`. 

For more information, see the [Provisioning](/docs/services/cloud-databases?topic=cloud-databases-provisioning) page.

{{site.data.keyword.databases-for}} deployments except {{site.data.keyword.databases-for-mongodb}} allow for both public and private networking to be enabled at the same time.
{: .tip}

## Changing Service Endpoints

Once you have provisioned a deployment, it is possible to change your public/private service endpoints configuration, with the exception of {{site.data.keyword.databases-for-mongodb}}. In the _Settings_ tab of your deployment's dashboard there is a card for _Service Endpoints_. You can toggle which types of connections are available to your deployment.

## Credentials for Private Endpoints