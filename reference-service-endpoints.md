---
copyright:
  years: 2019, 2024
lastupdated: "2024-07-23"

subcollection: cloud-databases

keywords: service endpoints, private endpoints, private networking, vpe, virtual private endpoints, service endpoint, private network

---

{{site.data.keyword.attribute-definition-list}}

# Service endpoints integration
{: #service-endpoints}

All {{site.data.keyword.databases-for}} deployments offer integration with [{{site.data.keyword.cloud_notm}} Service Endpoints](/docs/account?topic=account-service-endpoints-overview) to enable connections to your deployments from the public internet and over the {{site.data.keyword.cloud_notm}} private network.

Service endpoints are available in all {{site.data.keyword.cloud_notm}} Multi-Zone Regions and some single-campus multizone regions. Deployments in all other regions are able to use Service Endpoints.

## Public endpoints
{: #public-endpoints}

Public endpoints provide a connection to your deployment on the public network. At provision, a public endpoint is the default option for all deployments. Your environment needs to have internet access to connect to a deployment.

For enhanced security, it is recommended that users connect to their {{site.data.keyword.databases-for}} deployments using private endpoints instead of public endpoints.
{: important}

## Private endpoints
{: #private-endpoints}

A deployment with a service endpoint on the private network gets an endpoint that is not accessible from the public internet. All traffic is routed to hardware dedicated to {{site.data.keyword.databases-for}} deployments and remains on the {{site.data.keyword.cloud_notm}} Private network. All traffic to and from this endpoint is free and unmetered on the condition that the traffic remains in {{site.data.keyword.cloud_notm}}. After your environment has access to the {{site.data.keyword.cloud_notm}} Private network, an internet connection is not required to connect to your deployment.

For more information, see [Secure access to services using service endpoints](/docs/account?topic=account-service-endpoints-overview).

Deployments with private endpoints are reachable from any account within the private network and access to each instance requires authentication. To restrict this access to specific IP addresses, or ranges of IP addresses, configure [Context-based restrictions](/docs/cloud-databases?topic=cloud-databases-cbr).
{: .important}

## Enabling service endpoints
{: #enabling-service-endpoints}

To use connections over the public internet, you do not have to enable service endpoints on your {{site.data.keyword.cloud_notm}} account. To enable private networking on your deployments, follow the instructions at [Enabling VRF and service endpoints](/docs/account?topic=account-vrf-service-endpoint).

Currently, enabling virtual routing and forwarding (VRF) on your account in classic is a manual step that is handled by support ticket. VRF is automatically enabled for VPC. After you complete the [request](/docs/account?topic=account-vrf-service-endpoint#service-endpoint), check on the status of the ticket by going to your [Support](https://cloud.ibm.com/unifiedsupport/cases/manage) page on {{site.data.keyword.cloud_notm}}.

## Provisioning with Service Endpoints through the UI
{: #provisioning-service-endpoints-ui}
{: ui}

To configure your deployment's endpoints on provision, use the *Endpoints* field on the catalog page. Select from the available options:

- Public network
- Private network
- Both public and private network

A MongoDB deployment cannot support both [public and private endpoints simultaneously](/docs/databases-for-mongodb?topic=databases-for-mongodb-service-endpoints&interface=ui#provisioning-service-endpoints). *This cannot be changed after provisioning*.
{: .important}

## Provisioning with service endpoints through the CLI
{: #provisioning-endpoints-cli}
{: cli}

Service endpoints are enabled through an optional parameter when you provision through the CLI. Provisioning is handled by the Resource Controller. Pass the `service-endpoints` parameter one of the options `public`, `private`, or `public-and-private`.

```sh
ibmcloud resource service-instance-create <service-name> --service-endpoints <endpoint-type>
```
{: pre}

{{site.data.keyword.databases-for}} deployments except {{site.data.keyword.databases-for-mongodb}} allow for both public and private networking to be enabled at the same time.
{: .tip}

## Provisioning with service endpoints through the API
{: #provisioning-endpoints-api}
{: api}

Service endpoints are enabled through an optional parameter when you provision through the API. Provisioning is handled by the Resource Controller. Pass the `service-endpoints` parameter one of the options `public`, `private`, or `public-and-private`.

```sh
ibmcloud resource service-instance-create <service-name> --service-endpoints <endpoint-type>
```
{: pre}

{{site.data.keyword.databases-for}} deployments except {{site.data.keyword.databases-for-mongodb}} allow for both public and private networking to be enabled at the same time.
{: .tip}

## Changing service endpoints
{: #changing-service-endpoints}

After you deploy, it is possible to change your public and private service endpoints configuration, except for {{site.data.keyword.databases-for-mongodb}}.

## Changing service endpoints through the UI
{: #changing-service-endpoints-ui}
{: ui}

In the *Overview* tab of your deployment's dashboard, go to the *Endpoints* section. Toggle which types of connections are available to your deployment.

Changing the type of endpoints available on your deployment does not cause any downtime from a database perspective. However, if you disable an endpoint that is being used by you or your applications, those connections are dropped.

## Changing service endpoints through the CLI
{: #changing-service-endpoints-cli}
{: cli}

Use the [`ibmcloud resource service-instance-update`](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_update) command in the CLI, specifying the endpoint with the `--service-endpoints` flag.

```sh
ibmcloud resource service-instance-update <service-name> --service-endpoints <endpoint-type>
```
{: pre}

Changing the type of endpoints available on your deployment does not cause any downtime from a database perspective. However, if you disable an endpoint that is being used by you or your applications, those connections are dropped.

## Changing service endpoints through the API
{: #changing-service-endpoints-api}
{: api}

Use the [Resource Controller API](https://cloud.ibm.com/apidocs/resource-controller), with a `PATCH` request to the [/resource_instances/{id}](https://cloud.ibm.com/apidocs/resource-controller#update-a-resource-instance) endpoint.

Changing the type of endpoints available on your deployment does not cause any downtime from a database perspective. However, if you disable an endpoint that is being used by you or your applications, those connections are dropped.

## Credentials for private endpoints
{: #private-endpoints-credentials}

Use either public or private connection strings with any set of credentials that you make on your deployment. By default, the connection strings for a set of credentials are filled with strings for connecting over a public endpoint. If you are using private endpoints, specify connection strings that contain the private endpoint be generated instead.

When you create credentials in the *Service Credentials* UI, use either the `{ "service-endpoints": "public" }` or the `{ "service-endpoints": "private" }` parameter to specify which endpoint gets filled into the connection strings. 

In the API, use the [`/deployments/{id}/users/{userid}/connections/{endpoint_type}`](https://{DomainName}/apidocs/cloud-databases-api#discover-connection-information-for-a-deployment-f-e81026) to retrieve connection strings for both public or private endpoints.

If you have only private endpoints on your deployments, then all new credentials have private endpoints in the connection strings.

## Connecting through private endpoints
{: #private-endpoint-connections}

{{site.data.keyword.databases-for}} offers both private and public cloud service endpoints. To run your application or access the end point from a browser that is not on the private network, take these additional steps:
  
* Ensure your Cloud IaaS or SL account is [enabled for private endpoints](https://cloud.ibm.com/docs/account?topic=account-service-endpoints-overview).
* Create a virtual machine (VSI) that runs Linux.
* Configure a user account with SSH access.
* From your workstation, run `ssh -D 2345 user@vsi-host` to start an SSH session and open a SOCKS proxy on port `2345` that forwards all traffic through the VSI.
* Configure your browser or application to use a SOCKS5 proxy on `localhost:2345`.
* Run your application or open the preferred private-endpoint in your browser (for example, a management UI).

## Using virtual private endpoints 
{: #Virtual-Private-Endpoints}

For more information, see [Virtual private endpoints](/docs/cloud-databases?topic=cloud-databases-vpes).

## Action required - Upcoming changes to the configuration of endpoint parameters effective Oct 1, 2024
{: #service-endpoints-action}
 
Review the updates to endpoint settings for newly created instances of {{site.data.keyword.cloud_notm}} services, to enable a secure by default approach, effective October 1, 2024. This change impacts how you provision new {{site.data.keyword.databases-for}} services via the UI, CLI, API, and Terraform.
 
### What's changing
{: #service-endpoints-whats-changing}

- Endpoints for newly deployed databases via UI and CLI: New database instances deployed via UI and CLI will have private endpoints enabled by default.
- Endpoints for newly deployed databases via API (SDK and Terraform): To provision database instances via API and Terraform, a mandatory endpoint parameter (private, public, or both) will be required. For more information, see the [Terraform documentation](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database#argument-reference).
 
### Recommendation: Choose private endpoints
{: #service-endpoints-choose-private}

- Enhanced security: Choosing the correct endpoint type is crucial for maintaining the security of your data and applications. Private endpoints improve security by restricting access to your internal network, while public endpoints expose your services to potential security vulnerabilities. For more information, see [Managing security and compliance](/cloud-databases?topic=cloud-databases-manage-security-compliance).

- Increased control and visibility: Private endpoints provide greater control over network traffic to your database. {{site.data.keyword.databases-for}} now support [context-based restrictions](/docs/cloud-databases?topic=cloud-databases-cbr&interface=ui), which allow account owners and administrators to define and enforce access restrictions for {{site.data.keyword.cloud}} resources based on the context of access requests.

- Compliance and regulatory requirements: Private endpoints can be crucial for meeting compliance and regulatory requirements that mandate stringent data security measures. By keeping your database endpoint private, you can demonstrate adherence to industry standards and regulations.
 
### Action required
{: #service-endpoints-action-required}

Perform the following steps to ensure the successful creation of new instances and the alignment of your existing automation with these updates.

1. Evaluate your needs: Determine whether you require private or public endpoints for your applications and make appropriate changes.

2. Update your automation: Modify your scripts (for API and Terraform) to include the new mandatory argument (service_endpoints) that specifies the endpoint type. This parameter is required to create a new database instance via API and Terraform. For detailed instructions, see the [Terraform documentation](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database#argument-reference) or contact our support team for assistance.

3. For existing connections: This change does not impact existing deployments. However, we recommend re-evaluating your endpoint requirements and choosing the option that meets your needs.
 
### Timeline
{: #service-endpoints-timeline}

- These endpoint changes will take effect on October 1, 2024.
- Existing database instances will not be affected by this change unless you modify them.
 
These updates are designed to enhance our services' security and compliance posture. Our support team is ready to assist you with any questions or concerns during this transition.


