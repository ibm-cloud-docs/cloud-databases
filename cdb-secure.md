---

copyright:
  years: 2023, 2025
lastupdated: "2025-10-23"

keywords: context-based restrictions, allowlist, disaster recovery

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Securing your service
{: #cdb-secure-service}

1. Context-based restrictions give account owners and administrators the ability to define and enforce access restrictions for {{site.data.keyword.cloud_notm}} resources based on the context of access requests. Access to {{site.data.keyword.databases-for}} resources can be controlled with context-based restrictions and Identity and Access Management (IAM) policies. For more information, see [Protecting your {{site.data.keyword.databases-for}} instance with context-based restrictions](/docs/cloud-databases?topic=cloud-databases-cbr).
1. To restrict access to your databases, allowlist specific IP addresses or ranges of IP addresses on your deployment. Using IBM Cloud's native context-based restrictions is recommended over using the allowlist, which is deprecated. For more information, see [Allowlisting](/docs/cloud-databases?topic=cloud-databases-allowlisting).
1. [Disaster recovery](#x2113280){: term} involves a set of policies, tools, and procedures for returning a system, an application, or an entire data center to full operation after a catastrophic interruption. It includes procedures for copying and storing an installed system's essential data in a secure location, and for recovering that data to restore normalcy of operation. For more information, see [Understanding business continuity and disaster recovery for {{site.data.keyword.databases-for}}](/docs/cloud-databases?topic=cloud-databases-bc-dr).

## Next steps
{: #cdb-secure-service-next-steps}

You've now provisioned a {{site.data.keyword.databases-for}} service instance, set up notifications and monitoring, and secured it. Next, jump into the specific Getting Started documentation for your chosen service.

- [{{site.data.keyword.databases-for-postgresql}}](/docs/databases-for-postgresql?topic=databases-for-postgresql-getting-started){: external}

- [{{site.data.keyword.databases-for-mongodb}}](/docs/databases-for-mongodb?topic=databases-for-mongodb-getting-started-new){: external}

- [{{site.data.keyword.databases-for-redis}}](/docs/databases-for-redis?topic=databases-for-redis-getting-started){: external}

- [{{site.data.keyword.databases-for-elasticsearch}}](/docs/databases-for-elasticsearch?topic=databases-for-elasticsearch-getting-started){: external}

- [{{site.data.keyword.databases-for-mysql}}](/docs/databases-for-mysql?topic=databases-for-mysql-getting-started){: external}

- [{{site.data.keyword.messages-for-rabbitmq}}](/docs/messages-for-rabbitmq?topic=messages-for-rabbitmq-getting-started){: external}

- [{{site.data.keyword.databases-for-etcd}}](/docs/databases-for-etcd?topic=databases-for-etcd-getting-started){: external}
