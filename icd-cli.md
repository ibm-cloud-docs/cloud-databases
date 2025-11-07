---

copyright:
  years: 2023, 2025
lastupdated: "2025-11-07"

subcollection: cloud-databases

keywords: cli

---

{{site.data.keyword.attribute-definition-list}}

# {{site.data.keyword.databases-for}} through the CLI
{: #icd-cli}

The {{site.data.keyword.databases-for}} Command Line Interface (CLI) plug-in offers extra methods of accessing the capabilities of the Cloud Databases services.
{: shortdesc}

## The {{site.data.keyword.cloud_notm}} CLI
{: #icd-cli-ibm-cloud-cli}

The {{site.data.keyword.cloud}} CLI provides commands for managing resources in {{site.data.keyword.cloud_notm}}. When you install the standalone {{site.data.keyword.cloud_notm}} CLI, you get only the CLI itself without any recommended plug-ins or tools. For more information, see [Installing the stand-alone IBM Cloud CLI](https://cloud.ibm.com/docs/cli?topic=cli-install-ibmcloud-cli){: external}.

## Installing the {{site.data.keyword.databases-for}} CLI plug-in
{: #icd-cli-install}

After you install the {{site.data.keyword.cloud_notm}} CLI, [log in](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login) and install the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/cloud-databases?topic=cloud-databases-cdb-reference), using a command like:

```sh
ibmcloud plugin install cloud-databases
```
{: .pre}

For a list of commands and usage information, use a command like:
```sh
ibmcloud cdb help
```
{: .pre}

On its own, the `ibmcloud cdb help` command displays the available top-level commands. When followed by another command, it displays specific help for that command.

```sh
ibmcloud cdb help [<command>]
```
{: .pre}

## {{site.data.keyword.databases-for}} service-specific CLIs
{: #icd-cli-service-cli}

| Service | CLI client |
|---------------------------------------------------| :----------------------------------------------------------------------------: |
| [{{site.data.keyword.databases-for-mongodb}}](/docs/databases-for-mongodb){: external}       | [The mongo Shell](https://www.mongodb.com/docs/v4.4/mongo/){: external}    |
| [{{site.data.keyword.databases-for-elasticsearch}}](/docs/databases-for-elasticsearch){: external} |                                                                            |
| [{{site.data.keyword.databases-for-redis}}](/docs/databases-for-redis){: external}         | [The Redis CLI](https://redis.io/docs/latest/integrate/write-behind/reference/cli/){: external}      |
| [{{site.data.keyword.databases-for-postgresql}}](/docs/databases-for-postgresql){: external}    | [psql](https://www.postgresql.org/docs/14/app-psql.html){: external}        |
| [{{site.data.keyword.databases-for-mysql}}](/docs/databases-for-mysql){: external}         | [mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html){: external}    |
| [{{site.data.keyword.messages-for-rabbitmq}}](/docs/messages-for-rabbitmq){: external}       |                                                                            |
| [{{site.data.keyword.databases-for-etcd}}](/docs/databases-for-etcd){: external}          | [etcdctl](https://etcd.io/docs/v3.4/dev-guide/interacting_v3/){: external} |
{: caption="{{site.data.keyword.databases-for}} service-specific CLI clients" caption-side="bottom"}
