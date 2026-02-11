---
copyright:
  years: 2023, [{CURRENT_YEAR}]
lastupdated: "[{LAST_UPDATED_DATE}]"

subcollection: cloud-databases

keywords: resource config, resource configuration

---

{{site.data.keyword.attribute-definition-list}}

# Resource configuration FAQ
{: #faq-resource-config}
{: faq}
{: support}

## How do I retrieve the resource configuration for a {{site.data.keyword.databases-for}} instance?
{: #faq-resource-config-retrieve}
{: faq}
{: support}

### Retrieving resource configuration through the UI
{: #faq-resource-config-retrieve-ui}
{: faq}
{: support}
{: ui}

After you have selected the specific IBM Cloud Databases instance from the Resource List, navigate to the **Resources** tab, which displays your current resource configuration.

### Retrieving resource configuration through the CLI
{: #faq-resource-config-retrieve-cli}
{: faq}
{: support}
{: cli}

The [{{site.data.keyword.databases-for}} CLI plug-in](/docs/cloud-databases?topic=cloud-databases-cdb-reference){: external} can retrieve your instance's current resource configuration, by using the `ibmcloud cdb deployment-groups` command. The `ibmcloud cdb deployment-groups` displays the scaling group values for a deployment's members. The scaling groups relate to Memory, CPU, and Disk. The default group is named "member". Use a command like:

```sh
ibmcloud cdb deployment-groups <INSTANCE_NAME_OR_CRN>
```
{: pre}

The command will return a value that looks like:

```text
Group   member
Count   3
|
+   Memory
|   Allocation              3072mb
|   Allocation per member   1024mb
|   Minimum                 3072mb
|   Step Size               384mb
|   Adjustable              true
|
+   CPU
|   Allocation              0
|   Allocation per member   0
|   Minimum                 9
|   Step Size               3
|   Adjustable              true
|
+   Disk
|   Allocation              30720mb
|   Allocation per member   10240mb
|   Minimum                 30720mb
|   Step Size               3072mb
|   Adjustable              true
```
{: pre}

For more information, see [ibmcloud cdb deployment-groups](/docs/cloud-databases?topic=cloud-databases-cdb-reference#deployment-groups){: external}.
