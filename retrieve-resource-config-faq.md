---
copyright:
  years: 2023
lastupdated: "2023-08-02"

subcollection: cloud-databases

keywords: resource config, resource configuration

---

{{site.data.keyword.attribute-definition-list}}

# Resource Configuration FAQ
{: #faq-resource-config}
{: faq}
{: support}

## How do I retrieve the resource configuration for a {{site.data.keyword.databases-for}} instance?
{: #faq-resource-config-retrieve}
{: faq}
{: support}

The [{{site.data.keyword.databases-for}} CLI plug-in](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference){: external} can retrieve your instance's current resource configuration, using the `ibmcloud cdb deployment-groups` command. The `ibmcloud cdb deployment-groups` displays the scaling group values for a deployment's members. The scaling groups relate to Memory, CPU, and Disk. The default group is named "member". Use a command like:

```sh
ibmcloud cdb deployment-groups <DEPLOYMENT NAME>
```
{: pre}

For more information, see [ibmcloud cdb deployment-groups](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference){: external}.
