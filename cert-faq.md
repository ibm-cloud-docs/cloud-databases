---

copyright:
  years: 2023
lastupdated: "2023-09-28"

keywords: certificate, cert, tls, ssl

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Certificate FAQ
{: #faq-cert}
{: faq}
{: support}

{{site.data.keyword.databases-for}} certificates are authenticated by a unique TLS certificates. To verify this, you can inspect the certificate that your service presents when opening a connection. The certificate contains the hostname for a single instance. {{site.data.keyword.databases-for}} dataplane clusters possess their own distinctive root certificate. When you're engaged in certificate validation procedures, exercise caution and select the correct root certificate for each instance. For more information, see the relevant {{site.data.keyword.databases-for}} [Connecting an external application](/docs/databases-for-elasticsearch?topic=databases-for-elasticsearch-external-app){: external} documentation.

## Connecting an external application documentation
{: #faq-cert-external-app}
{: faq}
{: support}

Choose the appropriate service documentation for connecting an external application:

- [{{site.data.keyword.databases-for-mongodb}}](/docs/databases-for-mongodb?topic=databases-for-mongodb-external-app){: external}
- [{{site.data.keyword.databases-for-elasticsearch}}](/docs/databases-for-elasticsearch?topic=databases-for-elasticsearch-external-app){: external}
- [{{site.data.keyword.databases-for-cassandra}}](/docs/databases-for-cassandra?topic=databases-for-cassandra-external-app){: external}
- [{{site.data.keyword.databases-for-redis}}](/docs/databases-for-redis?topic=databases-for-redis-external-app){: external}
- [{{site.data.keyword.databases-for-postgresql}}](/docs/databases-for-postgresql?topic=databases-for-postgresql-external-app){: external}
- [{{site.data.keyword.databases-for-enterprisedb}}](/docs/databases-for-enterprisedb?topic=databases-for-enterprisedb-external-app){: external}
- [{{site.data.keyword.databases-for-mysql}}](/docs/databases-for-mysql?topic=databases-for-mysql-external-app){: external}
- [{{site.data.keyword.messages-for-rabbitmq}}](/docs/messages-for-rabbitmq?topic=messages-for-rabbitmq-external-app){: external}
- [{{site.data.keyword.databases-for-etcd}}](/docs/databases-for-etcd?topic=databases-for-etcd-external-app){: external}
