---

copyright:
  years: 2023, 2025
lastupdated: "2025-04-25"

keywords: cos bucket, data deletion, data security, password

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Data security FAQ
{: #faq-data-security}
{: faq}
{: support}

## What happens during data deletion?
{: #faq-data-security-deletion}
{: faq}
{: support}

When an instance is deleted, {{site.data.keyword.databases-for}} holds the block storage volume and Cloud Object Storage (COS) bucket in a “soft delete” state up to 3 days before deletion. After that 3-day period, we issue a `delete` to the COS and block storage services for those data volumes.

For more information on volume deletions, see [What happens to the data when Block Storage for Classic volumes are deleted?](/docs/BlockStorage?topic=BlockStorage-block-storage-faqs#deleted){: external}.

For more information on bucket deletions, see [Object Storage data deletion](/docs/cloud-object-storage?topic=cloud-object-storage-security#security-deletion){: external}.

In accordance with GDPR and other regulations, {{site.data.keyword.databases-for}} retains instance logs for 30 days. After 30 days, it is deleted through the same process as a COS bucket.

Instances that are configured with the optional bring your own key (BYOK) capability have their data shredded. The data is inaccessible when the customer-owned encryption key is deleted from the Key Protect or Hyperprotect Crypto Services instance. For more information, see [Deleting your deployment and removing your data](/docs/cloud-databases?topic=cloud-databases-deprovisioning).

## What are user password requirements?
{: #faq-data-security-password}
{: faq}
{: support}

Database user passwords are required to be a minimum of 15 characters, contain at least one letter and number, and a mix of uppercase and lowercase letters. Password complexity validation occurs for database users created using the {{site.data.keyword.cloud_notm}} console, CLI, API, and Terraform.

These password complexity requirements for {{site.data.keyword.databases-for}} users became effective on 24 February 2025. When updating a database user's password for databases created prior to 24 February 2025, you receive an error if the password does not meet these requirements. If you have Terraform configurations created prior to 24 Feb 2025 that are used to manage IBM Cloud Database users, check whether updates are needed to meet the proper complexity requirements.
