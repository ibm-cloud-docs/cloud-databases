---

copyright:
  years: 2021, 2023
lastupdated: "2023-05-18"

keywords: IBM Cloud, databases, ICD

subcollection: cloud-databases

content-type: tutorial
completion-time: 15m

---

{{site.data.keyword.attribute-definition-list}}	

# Setting up Amazon Web Services Location
{: #satellite-aws}
{: toc-content-type="tutorial"}
{: toc-completion-time="15m"}

Follow these steps to set up {{site.data.keyword.databases-for}} enabled by IBM Cloud Satellite in an on-premises location.

## Prepare a Satellite location for {{site.data.keyword.databases-for}}
{: #prepare-satellite-location}
{: step}

Prepare your Satellite location before deploying the {{site.data.keyword.databases-for}} enabled by IBM Cloud Satellite service.

### Attach extra hosts to the Satellite location
{: #attach-additional-hosts}

These additional-attached worker nodes are used to create a service cluster into which the database instances will later be deployed.
Attach to your Satellite location:

- Three type **8x32** hosts
    - On AWS, choose three hosts of type **AWS m5d.2xlarge**
- Three type **32x128** hosts
    - On AWS choose three hosts of type **AWS m5d.8xlarge**

You should also attach an additional three **32x128** hosts to be kept in reserve. While optional, this step is recommended and you will see a notification in the UI until the reserve workers are attached. 
{: note}

To be assigned to a service cluster, your worker nodes must match these specifications *exactly*.
{: .important}

### Create a Satellite block storage configuration
{: #satellite-blockstorage-config}

To set up your Satellite location using AWS, configure your block storage with [Amazon Elastic Block Storage (EBS)](/docs/satellite?topic=satellite-config-storage-ebs).

- To create a block storage configuration for your Satellite location, refer to [Creating an AWS EBS storage configuration](/docs/satellite?topic=satellite-config-storage-ebs).

- An EBS storage configuration code example

```bash
ibmcloud sat storage config create  \\
  --name 'aws-ebs-config-storage-testing-1' \\
  --template-name 'aws-ebs-csi-driver' \\
  --template-version '0.9.14' \\
  --location '${LOCATION_ID}' \\
  -p "aws-access-key=${SAT_EBS_ADMIN_KEY_ID}" \\
  -p "aws-secret-access-key=${SAT_EBS_ADMIN_KEY}"
```
{: pre}

## Grant a service authorization
{: step}
{: #service-authorization}

Begin by configuring IAM Authorizations:

- Configure your IAM Authorizations under the **Manage** tab.
- Choose the **Authorizations** tab from the left menu.
- Click **create** to create an authorization that allows a service instance access to another service instance.
    - The source service is the service that is granted access to the target service. The roles that you select define the level of access for this service. The target service is the service that you are granting permission to be accessed by the source service based on the assigned roles.
    - In the **Source Service** field, select **Databases for < DATABASE TYPE >**.
    - In the **Target Service** field, select **Satellite**.
    - Select all options:
        - **Satellite Cluster Creator**
        - **Satellite Link Administrator**
        - **Satellite Link Source Access Controller**
    - Then, **Authorize**.

## Ensure location readiness
{: step}
{: #aws-loc-readiness}

Before provisioning your {{site.data.keyword.databases-for}} Satellite Deployment, your location needs to report `Normal`. This status can be confirmed in the UI, as shown here:

![UI showing location is Normal](images/sat-normal.png){: caption="Figure 1. UI showing location is Normal" caption-side="bottom"}

`Normal` status can also be confirmed by using the CLI, with a command like:

```sh
ibmcloud sat location get --location <location name> --output=json -q | jq -r .state
```
If successful, the command output reports `normal`.

### Obtaining `Normal` state
{: #aws-norm-state}

To get to this state, attach a minimum of three 4x16 hosts to your location and assign them to the Control plane. After that step is complete, provisioning of the Control plane begins. Upon successful completion, the location state is going to report as `Normal`, as shown: 

![Control plane in normal state](images/cp-normal.png){: caption="Figure 1. Control plane in normal state" caption-side="bottom"}

Attempting to provision a database instance into a location without a running Control plane (that is, `Normal` state), causes provisioning to fail.
{: .important}

## Provisioning {{site.data.keyword.databases-for}} Satellite Deployment
{: step}
{: #provision-deployment}

You can provision your {{site.data.keyword.databases-for}} Satellite Deployment by selecting the Satellite location that you created in the **Location** menu of the provisioning page. For more information, see the relevant [Provisioning documentation](/docs/cloud-databases?topic=cloud-databases-provisioning) for your {{site.data.keyword.databases-for}} Satellite deployment. After you create a new service instance, this instance will appear in the IBM Cloud `Resource List` as `Provisioned`.

When you deploy the first database service instance, a service cluster is automatically deployed into your Satellite location. The deployment of the service cluster can take up to 1 hour.

You can verify in the IBM Cloud UI whether the service cluster is already created:
- From the left **Navigation menu**, select **Satellite**, then **Locations**.
- Select your Satellite location.
- Select **Services**

After the service cluster is created, you must create a storage assignment manually (see next step) **before** the database instance will be started. Subsequent database service instances provision more quickly since instances land on the same service cluster.
{: .important}

## Create a Storage Assignment
{: #create-storage-assignment-aws}

When the service cluster is available in your Satellite location, the next step is to create a Satellite storage assignment. Creating the storage assignment allows the service cluster to create volumes on the previously configured storage.

The first database you provision into a location remains "Provision In Progress" until this step is complete.
{: important}

For more information, see [AWS EBS IBM Cloud Satellite documentation](/docs/satellite?topic=satellite-config-storage-ebs).
{: note}

First, obtain your `ROKS-Service-cluster-ID` by entering the following command into the IBM Cloud CLI:

```bash
ic sat service ls  --location <location name/location id>
```
{: pre}

The output of the command includes the Cluster ID of the newly created Satellite service cluster. 

Use the Cluster ID as an input parameter for `--service-cluster-id` in the following AWS Satellite location storage assignment command:

```bash
ibmcloud sat storage assignment create  \\
    --name "ebs-assignment"  \\
    --service-cluster-id <ROKS-Service-cluster-ID>  \\
    --config 'aws-ebs-config-storage-testing-1'
```
{: pre}

Assigning a storage configuration to a service cluster autogenerates a `--name` and any user-provided name is ignored.
{: note}

After the storage assignment is created, allow up to 30 minutes for the database instance to be ready for usage.
