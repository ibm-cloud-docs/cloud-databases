---

copyright:
  years: 2021
lastupdated: "2021-11-02"

keywords: IBM Cloud, databases, ICD

subcollection: cloud-databases

content-type: tutorial
completion-time: 15m

---

{:codeblock: .codeblock}
{:screen: .screen}
{:download: .download}
{:external: target="_blank" .external}
{:faq: data-hd-content-type='faq'}
{:gif: data-image-type='gif'}
{:important: .important}
{:note: .note}
{:pre: .pre}
{:tip: .tip}
{:preview: .preview}
{:deprecated: .deprecated}
{:beta: .beta}
{:term: .term}
{:shortdesc: .shortdesc}
{:script: data-hd-video='script'}
{:support: data-reuse='support'}
{:table: .aria-labeledby="caption"}
{:troubleshoot: data-hd-content-type='troubleshoot'}
{:help: data-hd-content-type='help'}
{:tsCauses: .tsCauses}
{:tsResolve: .tsResolve}
{:tsSymptoms: .tsSymptoms}
{:curl: .ph data-hd-programlang='curl'}
{:step: data-tutorial-type='step'}
{:tutorial: data-hd-content-type='tutorial'}
{:ui: .ph data-hd-interface='ui'}
{:cli: .ph data-hd-interface='cli'}
{:api: .ph data-hd-interface='api'}

# Setting up On-Premises Location with NetApp ONTAP-SAN storage
{: #satellite-on-prem}
{: toc-content-type="tutorial"}
{: toc-completion-time="15m"}

Before deploying the ICD enabled by IBM Cloud Satellite service, you should prepare your Satellite location. Follow the steps below to set up IBM Cloud™ Databases (ICD) enabled by IBM Cloud Satellite in an on-premises location.

## Prepare an on-premises Satellite location for IBM Cloud Databases
{: #prepare-satellite-onprem}
{: step}

### Attach additional hosts to the Satellite location
{: #attach-hosts}

These additional attached worker nodes are used to create a service cluster into which the database instances will later be deployed.
Attach to your Satellite location:

- three type **8x32** hosts
- three type **32x128** hosts

### Create an on-prem Satellite block storage configuration for NetAPP ONTAP-SAN block storage
{: #block-storage-config}

#### Set up NetApp ONTAP-SAN storage
{: #set-up-netapp}

To set up your NetApp ONTAP-SAN storage (20.07), refer to [Setting up NetApp storage templates](/docs/satellite?topic=satellite-config-storage-netapp).

#### Deploy your NetApp ONTAP-SAN Block driver
{: #deploy-netapp}

To get a list of NetApp-supported templates, use the following command:

```bash
ibmcloud sat storage templates | grep "NetApp Ontap"
```
{: pre}


#### Create a storage configuration based on your NetApp back end
{: #storage-config}

- Operator configuration:
    ```bash
	ibmcloud sat storage config create 
	  --location ${LOCATION_ID} 
	  --name ${OPERATORCONFIGNAME}  
	  --template-name 'netapp-trident' 
	  --template-version '20.07'
    ```
	{: pre}

- SAN configuration:
    ```bash
	ibmcloud sat storage config create 
	  --location ${LOCATION_ID} 
	  --name ${SANCONFIGNAME}  
	  --template-name 'netapp-ontap-san' 
	  --template-version '20.07' 
	  --param "dataLIF=${DATALIF}" 
	  --param "managementLIF=${MGMLIF}"
	  --param "svm=${SVM}" 
	  --param "username=${USERNAME}" 
	  --param "password=${PASSWORD}"
	  --param "limitVolumeSize=1100Gi"
    ```
    {: pre}


### Enable public endpoints on the Satellite Control Plane
{: #public-endpoints}

In order to provide database management, ICD enabled by IBM Cloud Satellite requires you to enable public endpoints on the Satellite control plane.

For more information on accessing clusters, refer to [Accessing clusters from the public network](/docs/openshift?topic=openshift-access_cluster#sat_public_access).

## Grant a service authorization
{: #grant-service-auth}
{: step}

Begin by configuring IAM Authorizations:

- Configure your IAM Authorizations under the **Manage** tab.
- Choose the **Authorizations** tab from the left hand menu.
- Click the **create** button to create an authorization that will allow a service instance access to another service instance.
    - The source service is the service that is granted access to the target service. The roles you select define the level of access for this service. The target service is the service you are granting permission to be accessed by the source service based on the assigned roles.
    - In the **Source Service** field, select **Databases for < DATABASE TYPE >**.
    - In the **Target Service** field, select **Satellite**.
    - Select all options:
        - **Satellite Cluster Creator**
        - **Satellite Link Administrator**
        - **Satellite Link Source Access Controller**
    - Then **Authorize**.

## Provisioning ICD Satellite Deployment
{: #provision-satellite-deployment}
{: step}

Once you have prepared your satellite location and granted service authorization, you can provision your ICD Satellite Deployment by selecting the Satellite location you have created in the **Location** dropdown of the provisioning page. For thorough documentation of the provisioning process, see the relevant [Provisioning documentation](/docs/cloud-databases?topic=cloud-databases-provisioning) for your ICD Satellite deployment. Once you have created a new service instance, this instance will appear in the IBM Cloud `Resource List` as `Provisioned`.

When you deploy the first database service instance, a service cluster will automatically be deployed into your Satellite location. The deployment of the service cluster can take up to one hour.

You can verify in the IBM Cloud UI whether the service cluster is already created:
- From the left hand **Navigation Menu**, select **Satellite**, then **Locations**.
- Select your Satellite location.
- Select **Services**

Once the service cluster is created, you must create a storage assignment manually (see next step) **before** the database instance will be started. Subsequent database service instances will provision more quickly since those will land on the same service cluster.
{: important}

## Create a Storage Assignment
{: #create-storage-assignment}
{: step}

When the service cluster is available in your Satellite location, the next step is to create a Satellite storage assignment. This will allow the service cluster to create volumes on the previously configured storage.

Note that the first database you provision into a location will remain "Provision In Progress" until this step has been completed.
{: .important}

First, obtain your `ROKS-Service-cluster-ID` by entering the following command into the IBM Cloud CLI:
```bash
ic sat service ls  --location <location name/location id>
```
{: pre}

The output of the command will include the Cluster ID of the newly created Satellite service cluster. 

Use the Cluster ID as an input parameter for `--service-cluster-id` in the following AWS Satellite location storage assignment commands:

```bash
ibmcloud sat storage assignment create 
	--name ${OPERATORASSIGNMENTNAME} 
	--service-cluster-id ${SERVICECLUSTERID} 
	--config ${OPERATORCONFIGNAME} 
```
{: pre}

```bash
ibmcloud sat storage assignment create 
	--name ${SANASSIGNMENTNAME} 
	--service-cluster-id ${SERVICECLUSTERID} 
	--config ${SANCONFIGNAME}
```
{: pre}

After the storage assignment has been created, allow up to 30 minutes for the database instance to be ready for usage.
