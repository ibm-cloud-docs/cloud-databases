---

copyright:
  years: 2021, 2024
lastupdated: "2024-09-13"

keywords: IBM Cloud, databases, ICD

subcollection: cloud-databases

content-type: tutorial
completion-time: 15m

---

{{site.data.keyword.attribute-definition-list}}

# Setting up on-premises location with NetApp ONTAP-SAN storage
{: #satellite-on-prem}
{: toc-content-type="tutorial"}
{: toc-completion-time="15m"}

To deploy the {{site.data.keyword.databases-for}} enabled by {{site.data.keyword.satellitelong}} service, prepare your {{site.data.keyword.satelliteshort}} location. Follow these steps to set up {{site.data.keyword.databases-for}} enabled by {{site.data.keyword.satellitelong_notm}} in an on-premises location.

On-premises {{site.data.keyword.satelliteshort}} location currently supports *only* NetApp ONTAP-SAN storage. 

## Prepare an on-premises {{site.data.keyword.satelliteshort}} location for {{site.data.keyword.cloud}} Databases
{: #prepare-satellite-onprem}
{: step}

### Attach extra hosts to the {{site.data.keyword.satelliteshort}} location
{: #attach-hosts}

These additional-attached worker nodes are used to create a service cluster into which the database instances are deployed later.
Attach to your {{site.data.keyword.satelliteshort}} location:

- Three type **8x32** hosts
- Three type **32x128** hosts

You should also attach an additional three **32x128** hosts to be kept in reserve. While optional, this step is recommended and you will see a notification in the UI until the reserve workers are attached. 
{: note}

To be assigned to a service cluster, your worker nodes must match these specifications *exactly*.
{: .important}

### Create an on-premises {{site.data.keyword.satelliteshort}} block storage configuration for NetAPP ONTAP-SAN block storage
{: #block-storage-config}

#### Set up NetApp ONTAP-SAN storage
{: #set-up-netapp}

To set up your NetApp ONTAP-SAN storage (20.07), refer to [Setting up NetApp storage templates](/docs/satellite?topic=satellite-storage-netapp-ontap-nas).

#### Deploy your NetApp ONTAP-SAN Block driver
{: #deploy-netapp}

To get a list of NetApp-supported templates, use the following command:

```bash
ibmcloud sat storage templates | grep "NetApp Ontap"
```
{: pre}


#### Create a storage configuration based on your NetApp backend
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

## Grant a service authorization
{: #grant-service-auth}
{: step}

Begin by configuring IAM Authorizations:

- Configure your IAM Authorizations under the **Manage** tab.
- Choose the **Authorizations** tab from the left menu.
- Click **Create** to allow a service instance access to another service instance.
    - The source service is the service that is granted access to the target service. The roles that you select define the level of access for this service. The target service is the service that you are granting permission to be accessed by the source service based on the assigned roles.
    - In the **Source service** field, select the **Database** type.
    - In the **Target service** field, select **{{site.data.keyword.satelliteshort}}**.
    - Select all options:
        - **{{site.data.keyword.satelliteshort}} Cluster Creator**
        - **{{site.data.keyword.satelliteshort}} Link Administrator**
        - **{{site.data.keyword.satelliteshort}} Link Source Access Controller**
    - Then, click **Authorize**.

## Ensure location readiness
{: step}
{: #onprem-loc-readiness}

Your location needs to report `normal` before you provision your {{site.data.keyword.databases-for}} {{site.data.keyword.satelliteshort}} deployment. This status can be confirmed in the UI, as shown here:

![UI showing location is normal](images/sat-normal.png){: caption="UI showing location is normal" caption-side="bottom"}

The `normal` status can also be confirmed by using the CLI, with a command like:

```sh
ibmcloud sat location get --location <location name> --output=json -q | jq -r .state
```
{: pre}

If successful, the command output reports `normal`.

### Obtaining `normal` state
{: #onprem-norm-state}

To get to this state, attach a minimum of three 4x16 hosts to your location and assign them to the Control plane. After that step is complete, provisioning of the Control plane will begin. Upon successful completion, the location state is going to report as `normal`.

![Control plane in normal state](images/cp-normal.png){: caption="Control plane in normal state" caption-side="bottom"}

Attempting to provision a database instance into a location without a running Control plane (that is, `normal` state), causes a provisioning to fail.
{: .important}

## Provisioning {{site.data.keyword.databases-for}} {{site.data.keyword.satelliteshort}} deployment
{: #provision-satellite-deployment}
{: step}

You can provision your {{site.data.keyword.databases-for}} {{site.data.keyword.satelliteshort}} deployment by selecting the {{site.data.keyword.satelliteshort}} location that you create from the **Location** dropdown on the provisioning page. For more information, see the relevant [Provisioning documentation](/docs/cloud-databases?topic=cloud-databases-getting-started-cdb-provision-instance). After you create a new service instance, this instance will appear in the {{site.data.keyword.cloud_notm}} `Resource list` as `Provisioned`.

When you deploy the first database service instance, a service cluster deploys automatically into your {{site.data.keyword.satelliteshort}} location. The deployment of the service cluster can take up to 1 hour.

You can verify in the {{site.data.keyword.cloud_notm}} UI whether the service cluster is already created:
- From the left **Navigation menu**, select **{{site.data.keyword.satelliteshort}}**, then **Locations**.
- Select your {{site.data.keyword.satelliteshort}} location.
- Select **Services**.

You must create a storage assignment manually (see next step) **before** the database instance will be started. Subsequent database service instances provision more quickly since instances land on the same service cluster.
{: important}

## Create a storage assignment
{: #create-storage-assignment-onprem}
{: step}

The next step is to create a {{site.data.keyword.satelliteshort}} storage assignment that allows the service cluster to create volumes on the previously configured storage.

The first database you provision into a location remains "Provision in progress" until this step is complete.
{: .important}

First, obtain your `ROKS-Service-cluster-ID` by entering the following command into the {{site.data.keyword.cloud_notm}} CLI:

```bash
ic sat service ls  --location <location name/location id>
```
{: pre}

The output of the command includes the Cluster ID of the newly created {{site.data.keyword.satelliteshort}} service cluster. 

Use the Cluster ID as an input parameter for `--service-cluster-id` in the following AWS {{site.data.keyword.satelliteshort}} location storage assignment commands:

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

After you create the storage assignment, allow up to 30 minutes for the database instance to be ready for usage.
