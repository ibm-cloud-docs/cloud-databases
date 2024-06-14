---

copyright:
  years: 2021, 2023
lastupdated: "2023-11-23"

keywords: IBM Cloud, databases, ICD

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Your service cluster
{: #icd-service-cluster}

As outlined in your initial {{site.data.keyword.databases-for}} Satellite location deployment, your initial service cluster was established with the following hosts:

- Three type **8x32** hosts (on AWS, three hosts of type **AWS m5d.2xlarge**)
- Three type **32x128** hosts (on AWS, three hosts of type **AWS m5d.8xlarge**)

The three type **8x32** hosts are for {{site.data.keyword.databases-for}} enabled by IBM Cloud Satellite internal use, while the three type **32x128** hosts are for your use.

## Growing your service cluster
{: #icd-service-cluster-grow}

As your service cluster grows, you might be required to add extra hosts. If required, add **32x128** hosts in increments of three (for example, three type **8x32** hosts to six type **8x32** hosts, then nine type **8x32** hosts, and so on).

## Service cluster removal
{: #icd-remove-service-cluster}

Just as extra hosts are added as your data needs grow, as you downsize your service cluster, hosts are automatically deleted when they are no longer needed.

## Verifying Service cluster storage assignment
{: #icd-service-cluster-verify-storage}

To verify a service cluster storage assignment, use the following command to list your service clusters and configurations:

```sh
ic sat storage assignment ls
```
