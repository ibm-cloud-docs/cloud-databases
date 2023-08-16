---

copyright:
  years: 2023
lastupdated: "2023-08-16"

keywords: cos bucket, data deletion, data security

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Data security FAQ
{: #faq-data-security}
{: faq}
{: support}

## Data deletion
{: #faq-data-security-deletion}
{: faq}
{: support}

When an instance is deleted, {{site.data.keyword.databases-for}} holds the block storage volume and Cloud Object Storage (COS) bucket in a “soft delete” state up to 8 days before deletion. After that 8-day period, we issue a `delete` to the COS and block storage services for those data volumes.

The data is inaccessible when a block storage device is deleted. Pointers are removed and overwritten before given to other customers. For more information, see [What happens to the data when Block Storage for Classic LUNs are deleted?](/docs/BlockStorage?topic=BlockStorage-block-storage-faqs#deleted){: external}.

The same applies when a COS bucket is deleted. Data is overwritten before the space is reallocated to another tenant. For more information, see [Object Storage data deletion](/docs/cloud-object-storage?topic=cloud-object-storage-security#security-deletion){: external}.

In accordance with GDPR and other regulations, {{site.data.keyword.databases-for}} retains instance logs for 30 days. After 30 days, it is deleted through the same process as a COS bucket.

Instances that are configured with the optional bring your own key (BYOK) capability have their data shredded. The data is inaccessible when the customer-owned encryption key is deleted from the Key Protect or Hyperprotect Crypto Services instance: For more information, see the relevant Deleting your Deployment and Removing your Data for your {{site.data.keyword.databases-for}} service.

