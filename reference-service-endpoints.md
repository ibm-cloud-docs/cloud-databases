---
copyright:
  years: 2019, 2023
lastupdated: "2023-07-10"

subcollection: cloud-databases

keywords: service endpoints, private endpoints, private networking, vpe, virtual private endpoints, service endpoint, private network

---

{{site.data.keyword.attribute-definition-list}}

# Service Endpoints Integration
{: #service-endpoints}

All {{site.data.keyword.databases-for}} deployments offer integration with [{{site.data.keyword.cloud_notm}} Service Endpoints](/docs/account?topic=account-service-endpoints-overview) to enable connections to your deployments from the public internet and over the {{site.data.keyword.cloud_notm}} Private network.

Service Endpoints are available in all {{site.data.keyword.cloud_notm}} Multi-Zone Regions and some single-campus multizone regions. Deployments in all other regions are able to use Service Endpoints.

## Public Endpoints
{: #public-endpoints}

Public endpoints provide a connection to your deployment on the public network. At provision, a public endpoint is the default option for all deployments. Your environment needs to have internet access to connect to a deployment.

For enhanced security, it is recommended that users connect to their {{site.data.keyword.databases-for}} deployments using private endpoints instead of public endpoints.
{: important}

## Private Endpoints
{: #private-endpoints}

A deployment with a service endpoint on the private network gets an endpoint that is not accessible from the public internet. All traffic is routed to hardware dedicated to {{site.data.keyword.databases-for}} deployments and remains on the {{site.data.keyword.cloud_notm}} Private network. All traffic to and from this endpoint is free and unmetered on the condition that the traffic remains in {{site.data.keyword.cloud_notm}}. After your environment has access to the {{site.data.keyword.cloud_notm}} Private network, an internet connection is not required to connect to your deployment.

For more information, see [Secure access to services using service endpoints](/docs/account?topic=account-service-endpoints-overview).

Deployments with private endpoints are reachable from any account within the private network and access to each instance requires authentication. To restrict this access to specific IP addresses, or ranges of IP addresses, configure [Context-based restrictions](/docs/cloud-databases?topic=cloud-databases-cbr).
{: .important}

## Enabling Service Endpoints
{: #enabling-service-endpoints}

To use connections over the public internet, you do not have to enable Service Endpoints on your {{site.data.keyword.cloud_notm}} account. To enable private networking on your deployments, follow the instructions at [Enabling VRF and service endpoints](/docs/account?topic=account-vrf-service-endpoint).

Currently, enabling virtual routing and forwarding (VRF) on your account in classic is a manual step that is handled by support ticket. VRF is automatically enabled for VPC. After you complete the [request](/docs/account?topic=account-vrf-service-endpoint#service-endpoint), check on the status of the ticket by going to your [Support](https://cloud.ibm.com/unifiedsupport/cases/manage) page on {{site.data.keyword.cloud_notm}}.

## Provisioning with Service Endpoints through the UI
{: #provisioning-service-endpoints-ui}
{: ui}

To configure your deployment's endpoints on provision, use the *Endpoints* field on the catalog page. Select from the available options:
- Public Network
- Private Network
- Both public and private network

A MongoDB deployment cannot support both [public and private endpoints simultaneously](/docs/databases-for-mongodb?topic=databases-for-mongodb-service-endpoints&interface=ui#provisioning-service-endpoints). *This cannot be changed after provisioning*.
{: .important}

## Provisioning with Service Endpoints through the CLI
{: #provisioning-endpoints-cli}
{: cli}

Service Endpoints are enabled through an optional parameter when you provision through the CLI. Provisioning is handled by the Resource Controller. Pass the `service-endpoints` parameter one of the options `public`, `private`, or `public-and-private`.

```sh
ibmcloud resource service-instance-create <service-name> --service-endpoints <endpoint-type>
```
{: pre}

{{site.data.keyword.databases-for}} deployments except {{site.data.keyword.databases-for-mongodb}} allow for both public and private networking to be enabled at the same time.
{: .tip}

## Provisioning with Service Endpoints through the API
{: #provisioning-endpoints-api}
{: api}

Service Endpoints are enabled through an optional parameter when you provision through the API. Provisioning is handled by the Resource Controller. Pass the `service-endpoints` parameter one of the options `public`, `private`, or `public-and-private`.

```sh
ibmcloud resource service-instance-create <service-name> --service-endpoints <endpoint-type>
```
{: pre}

{{site.data.keyword.databases-for}} deployments except {{site.data.keyword.databases-for-mongodb}} allow for both public and private networking to be enabled at the same time.
{: .tip}

## Changing Service Endpoints
{: #changing-service-endpoints}

After you deploy, it is possible to change your public and private service endpoints configuration, except for {{site.data.keyword.databases-for-mongodb}}.

## Changing Service Endpoints through the UI
{: #changing-service-endpoints-ui}
{: ui}

In the *Overview* tab of your deployment's dashboard, go to the *Endpoints* section. Toggle which types of connections are available to your deployment.

Changing the type of endpoints available on your deployment does not cause any downtime from a database perspective. However, if you disable an endpoint that is being used by you or your applications, those connections are dropped.

## Changing Service Endpoints through the CLI
{: #changing-service-endpoints-cli}
{: cli}

Use the [`ibmcloud resource service-instance-update`](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_update) command in the CLI, specifying the endpoint with the `--service-endpoints` flag.

```sh
ibmcloud resource service-instance-update <service-name> --service-endpoints <endpoint-type>
```
{: pre}

Changing the type of endpoints available on your deployment does not cause any downtime from a database perspective. However, if you disable an endpoint that is being used by you or your applications, those connections are dropped.

## Changing Service Endpoints through the API
{: #changing-service-endpoints-api}
{: api}

Use the [Resource Controller API](https://cloud.ibm.com/apidocs/resource-controller), with a `PATCH` request to the [/resource_instances/{id}](https://cloud.ibm.com/apidocs/resource-controller#update-a-resource-instance) endpoint.

Changing the type of endpoints available on your deployment does not cause any downtime from a database perspective. However, if you disable an endpoint that is being used by you or your applications, those connections are dropped.

## Credentials for Private Endpoints
{: #private-endpoints-credentials}

Use either public or private connection strings with any set of credentials that you make on your deployment. By default, the connection strings for a set of credentials are filled with strings for connecting over a public endpoint. If you are using private endpoints, specify connection strings that contain the private endpoint be generated instead.

When you create credentials in the *Service Credentials* UI, use either the `{ "service-endpoints": "public" }` or the `{ "service-endpoints": "private" }` parameter to specify which endpoint gets filled into the connection strings. 

In the API, use the [`/deployments/{id}/users/{userid}/connections/{endpoint_type}`](https://{DomainName}/apidocs/cloud-databases-api#discover-connection-information-for-a-deployment-f-e81026) to retrieve connection strings for both public or private endpoints.

If you have only private endpoints on your deployments, then all new credentials have private endpoints in the connection strings.

## Connecting Through Private Endpoints
{: #private-endpoint-connections}

{{site.data.keyword.databases-for}} offers both private and public cloud service endpoints. To run your application or access the end point from a browser that is not on the private network, take these additional steps:
  
* Ensure your Cloud IaaS or SL account is [enabled for private endpoints](https://cloud.ibm.com/docs/account?topic=account-service-endpoints-overview).
* Create a virtual machine (VSI) that runs Linux.
* Configure a user account with SSH access.
* From your workstation, run `ssh -D 2345 user@vsi-host` to start an SSH session and open a SOCKS proxy on port `2345` that forwards all traffic through the VSI.
* Configure your browser or application to use a SOCKS5 proxy on `localhost:2345`.
* Run your application or open the preferred private-endpoint in your browser (for example, a management UI).


## Using Virtual Private Endpoints 
{: #Virtual-Private-Endpoints}

For more information, see [Virtual Private Endpoints](/docs/cloud-databases?topic=cloud-databases-vpes).

