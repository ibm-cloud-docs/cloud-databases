---

copyright:
  years: 2021, 2022
lastupdated: "2022-12-09"

keywords: IBM Cloud, databases, ICD

subcollection: cloud-databases

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

# Getting Started
{: #satellite-get-started}

With {{site.data.keyword.cloud_notm}} Databases (ICD) enabled by {{site.data.keyword.cloud_notm}} Satellite, you can deploy ICD instances into a Satellite location. (ICD) enabled by {{site.data.keyword.cloud_notm}} Satellite currently supports the following ICD managed database services:
- [{{site.data.keyword.databases-for-etcd}}](/docs/databases-for-etcd)
- [{{site.data.keyword.databases-for-postgresql}}](/docs/databases-for-postgresql)
- [{{site.data.keyword.databases-for-redis}}](/docs/databases-for-redis)
- [{{site.data.keyword.messages-for-rabbitmq}}](/docs/messages-for-rabbitmq)

 After your Satellite location instance is deployed, ICD will install an ICD Satellite service cluster in your Satellite location into which your database instances will be deployed. 

 Your ICD service cluster can operate multiple database instances, even with different database types. For instance, you might operate a {{site.data.keyword.databases-for-etcd}} and a {{site.data.keyword.databases-for-postgresql}} instance on the same service cluster. 
 {: .important}

The service cluster name is based on the first database instance, even if multiple instances exist. For example, if your service cluster has both a {{site.data.keyword.databases-for-etcd}} and a {{site.data.keyword.databases-for-postgresql}} instance on the same service cluster, the name is based on your {{site.data.keyword.databases-for-etcd}} instance.
{: .note}

ICD enabled by {{site.data.keyword.cloud_notm}} Satellite supports Satellite locations on [Amazon Web Services (AWS)](/docs/satellite?topic=satellite-aws) and [on-premises](/docs/cloud-databases?topic=cloud-databases-satellite-on-prem). 
{: shortdesc}

## An Overview
{: #before-begin}

![An Overview of ICD enabled by {{site.data.keyword.cloud_notm}} Satellite](images/sat_on_icd.svg){: caption="Image 1. An Overview of ICD enabled by {{site.data.keyword.cloud_notm}} Satellite" caption-side="bottom"}

## Before you begin
{: #satellite-before-begin}

ICD enabled by {{site.data.keyword.cloud_notm}} Satellite does not yet provide the Security and Compliance integration, Activity Tracking, or Metrics Monitoring of a standard {{site.data.keyword.cloud}} Databases deployment.
{: .important}

- Refer to the [Satellite Usage requirements](/docs/satellite?topic=satellite-requirements).
- Be sure you set up the [{{site.data.keyword.cloud_notm}} CLI](/docs/satellite?topic=satellite-setup-cli), the plug-in for Satellite commands, and other related CLIs.
- If you did not create a Satellite location, see [Setting up Satellite locations](/docs/satellite?topic=satellite-locations). Follow the steps in the [Manually creating Satellite locations](/docs/satellite?topic=satellite-locations#location-create) documentation.
    - For the management location, choose **Washington DC**. If you are creating your Satellite location on AWS, adjust the **host zones** to AWS-default zone names, for example: **us-east-1a**, **us-east-1b**, **us-east-1c**.

As ICD enabled by {{site.data.keyword.cloud_notm}} Satellite solely supports resource deployment in the `us-east` region, you must choose the **Washington DC** location when provisioning. 
{: .note}

- Before **Step 1**, have your Satellite location set up properly and ensure that the Satellite control plane is up and running.
