---
copyright:
  years: 2023
lastupdated: "2023-09-25"

keywords: cloud databases

subcollection: cloud-databases

content-type: tutorial
account-plan: paid
completion-time: 30m

---

{{site.data.keyword.attribute-definition-list}}

# Getting Started
{: #getting-started-cdb}
{: toc-content-type="tutorial"}
{: toc-completion-time="30m"}

This tutorial is a short introduction to deploying a {{site.data.keyword.databases-for}} instance.

## Before you begin
{: #getting-started-cdb-before-begin}

- You need to have an [{{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/registration){: external}.

## Choose your service
{: #getting-started-cdb-choose-service}
{: step}

Choose your desired {{site.data.keyword.databases-for}} service.

- {{site.data.keyword.databases-for-mongodb}} is a JSON document store with a rich query and aggregation framework. For more information, see [{{site.data.keyword.databases-for-mongodb}}](/docs/databases-for-mongodb){: external}. {{site.data.keyword.databases-for-mongodb}} offers two plans: Standard and Enterprise.
- {{site.data.keyword.databases-for-elasticsearch}} combines the power of a full text search engine with the indexing strengths of a JSON document database. For more information, see [{{site.data.keyword.databases-for-elasticsearch}}](/docs/databases-for-elasticsearch){: external}. {{site.data.keyword.databases-for-elasticsearch}} offers two plans: Standard and Enterprise.
- {{site.data.keyword.databases-for-cassandra}} is a scale-out NoSQL database built on Apache Cassandra, designed for high-availability and workload flexibility. For more information, see [{{site.data.keyword.databases-for-cassandra}}](/docs/databases-for-cassandra){: external}.
- {{site.data.keyword.databases-for-redis}} is a blazingly fast, in-memory data structure store. For more information, see [{{site.data.keyword.databases-for-redis}}](/docs/databases-for-redis){: external}.
- {{site.data.keyword.databases-for-postgresql}} is a powerful, open source object-relational database that is highly customizable. For more information, see [{{site.data.keyword.databases-for-postgresql}}](/docs/databases-for-postgresql){: external}.
- {{site.data.keyword.databases-for-enterprisedb}} is a PostgreSQL-based database engine optimized for performance, developer productivity, and compatibility with Oracle. For more information, see [{{site.data.keyword.databases-for-enterprisedb}}](/docs/databases-for-enterprisedb){: external}.
- {{site.data.keyword.databases-for-mysql}} is fully managed MySQL relational database service. For more information, see [{{site.data.keyword.databases-for-mysql}}](/docs/databases-for-mysql){: external}.
- {{site.data.keyword.messages-for-rabbitmq}} is an open source multi-protocol messaging broker. For more information, see [{{site.data.keyword.messages-for-rabbitmq}}](/docs/messages-for-rabbitmq){: external}.
- {{site.data.keyword.databases-for-etcd}} is a distributed reliable key-value store for the most critical data of a distributed system. For more information, see [{{site.data.keyword.databases-for-etcd}}](/docs/databases-for-etcd){: external}.

## Provision an instance
{: #getting-started-cdb-provision-instance}
{: step}

Follow the outlined procedures for provisioning a {{site.data.keyword.databases-for}} instance of your preferred service. You can provision through the [catalog](https://cloud.ibm.com/catalog/services/databases-for-mongodb){: external}, the [{{site.data.keyword.databases-for}} CLI](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference), the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction), or through [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

- [{{site.data.keyword.databases-for-mongodb}}](/docs/databases-for-mongodb?topic=databases-for-mongodb-provisioning){: external}. 
   {{site.data.keyword.databases-for-mongodb}} offers two plans: Standard and Enterprise.
   {: note}

- [{{site.data.keyword.databases-for-elasticsearch}}](/docs/databases-for-elasticsearch?topic=databases-for-elasticsearch-provisioning-new){: external}. 
   {{site.data.keyword.databases-for-elasticsearch}} offers two plans: Standard and Enterprise.
   {: note}

- [{{site.data.keyword.databases-for-cassandra}}](/docs/databases-for-cassandra?topic=databases-for-cassandra-provisioning){: external}{: deprecated}.

- [{{site.data.keyword.databases-for-redis}}](/docs/databases-for-redis?topic=databases-for-redis-provisioning){: external}.

- [{{site.data.keyword.databases-for-postgresql}}](/docs/databases-for-postgresql?topic=databases-for-postgresql-provisioning){: external}.

- [{{site.data.keyword.databases-for-enterprisedb}}](/docs/databases-for-enterprisedb?topic=databases-for-enterprisedb-provisioning){: external}.

- [{{site.data.keyword.databases-for-mysql}}](/docs/databases-for-mysql?topic=databases-for-mysql-provisioning){: external}.

- [{{site.data.keyword.messages-for-rabbitmq}}](/docs/messages-for-rabbitmq?topic=messages-for-rabbitmq-provisioning){: external}.

- [{{site.data.keyword.databases-for-etcd}}](/docs/databases-for-etcd?topic=databases-for-etcd-provisioning){: external}.

## Set up Logging and Monitoring
{: #getting-started-cdb-logging-monitoring}
{: step}

1. Use the {{site.data.keyword.at_full}} service to capture a record of your {{site.data.keyword.databases-for}} activities and monitor the activity of your {{site.data.keyword.cloud_notm}} account. For more information, see {{site.data.keyword.databases-for}} [{{site.data.keyword.at_full}} Integration](/docs/cloud-databases?topic=cloud-databases-activity-tracker).

1. Use {{site.data.keyword.la_full}} to add log management capabilities to your {{site.data.keyword.databases-for}} architecture. For more information, see {{site.data.keyword.databases-for}} [{{site.data.keyword.la_full}} Integration](/docs/cloud-databases?topic=cloud-databases-logging).

1. Use {{site.data.keyword.mon_full}} to gain operational visibility into the performance and health of your applications, services, and platforms. For more information, see {{site.data.keyword.databases-for}} [{{site.data.keyword.mon_full}} with Sysdig Integration](/docs/cloud-databases?topic=cloud-databases-sysdig-monitor).
