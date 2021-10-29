---

copyright:
  years: 2021
lastupdated: "2021-10-29"

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

With IBM Cloud™ Databases (ICD) enabled by IBM Cloud Satellite, you can deploy ICD instances into a Satellite location. The ICD service will then install an ICD Satellite service cluster in your Satellite location into which your database instances will be deployed.
ICD enabled by IBM Cloud Satellite supports Satellite locations on [Amazon Web Services (AWS)](/docs/satellite?topic=satellite-aws) and [on-premises](/docs/cloud-databases?topic=cloud-databases-satellite-on-prem). 
{: shortdesc}

ICD enabled by IBM Cloud Satellite supports {{site.data.keyword.databases-for-etcd}}, {{site.data.keyword.databases-for-postgresql}}, {{site.data.keyword.databases-for-redis}}, and {{site.data.keyword.messages-for-rabbitmq}}.
{: .note}

Before proceeding, you should refer to the [Satellite Usage requirements](/docs/satellite?topic=satellite-requirements).
{: .tip}

## Before you begin

- Be sure you have set up the [IBM Cloud command-line interface (CLI)](/docs/satellite?topic=satellite-setup-cli), the plug-in for Satellite commands, and other related CLIs.
- If you have not already created a Satellite location, see [Setting up Satellite locations](/docs/satellite?topic=satellite-locations). We recommend following the steps in the [Manually creating Satellite locations](/docs/satellite?topic=satellite-locations#location-create) documentation.
    - For the management location, choose **Washington DC**. If creating your Satellite location on AWS, adjust the **host zones** to AWS-default zone names, for example: **us-east-1a**, **us-east-1b**, **us-east-1c**.
- Before proceeding with **Step 1**, you should have set up your Satellite location properly and ensured the Satellite control plane is up and running.
