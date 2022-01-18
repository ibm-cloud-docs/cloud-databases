---

copyright:
  years: 2021
lastupdated: "2022-01-18"

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

# Your service cluster
{: #icd-service-cluster}

As outlined in your initial ICD Satellite location deployment, your initial service cluster was established with the following hosts:

- three type **8x32** hosts (on AWS, three hosts of type **AWS m5d.2xlarge**)
- three type **32x128** hosts (on AWS, three hosts of type **AWS m5d.8xlarge**)

The three type **8x32** hosts are for IBM Cloud™ Databases (ICD) enabled by IBM Cloud Satellite internal use, while the three type **32x128** hosts are for your use.

## Growing your service cluster
{: #icd-service-cluster-grow}

As your service cluster grows, you might be required to add additional hosts. If required, add **32x128** hosts in increments of three (e.g., three type **8x32** hosts to six type **8x32** hosts, then nine type **8x32** hosts, and so on).

## Service cluster removal
{: #icd-remove-service-cluster}

Just as additional hosts are added as your data needs grow, as you downsize your service cluster, hosts will be automatically deleted when they are no longer needed.

## Verifying Service cluster storage assignment
{: #icd-service-cluster-verify-storage}

To verify a service cluster storage assignment, use the following command to list your service clusters and configurations:

```shell
ic sat storage assignment ls
```
