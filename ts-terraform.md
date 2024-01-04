---

copyright:
  years: 2024
lastupdated: "2024-01-04"

keywords: question about terraform

subcollection: cloud-databases

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

<!-- Remember that this is the individual topic template for each troubleshooting entry that belongs in a troubleshooting topic group in the Help left nav group. For more information, see the guidance page: https://test.cloud.ibm.com/docs/writing?topic=writing-troubleshooting-topics-->

# Why did my Terraform script delete my instance?
{: #troubleshoot-terraform}
{: troubleshoot}
{: support}

Your Terraform script deleted your {{site.data.keyword.databases-for}} instance. Why did this happen, and what can I do?
{: shortdesc}

You ran your Terraform script and now your instance has been deleted. You may receive an error that looks like:
{: tsSymptoms}

```text
ibm_database.database_instance must be replaced
```

Before executing a Terraform script on an existing instance, use the `terraform plan` command to compare the current infrastructure state with the desired state defined in your Terraform files. If altered, the following attributes recreate the instance: `resource_group_id`, `service plan`, `version`, `key_protect_instance`, `key_protect_key`, `backup_encryption_key_crn`.
{: tsCauses}

Before executing a Terraform script on an existing instance, use the `terraform plan` command to compare the current infrastructure state with the desired state defined in your Terraform files. Altering the following attributes recreates the instance: `resource_group_id`, `service plan`, `version`, `key_protect_instance`, `key_protect_key`, `backup_encryption_key_crn`
{: tsResolve}
