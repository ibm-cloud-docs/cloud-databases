---
copyright:
  years: 2021, 2023
lastupdated: "2023-05-11"

keywords: security and compliance for cloud databases, security for cloud databases, compliance for cloud databases, enterprisedb, redis, etcd, elasticsearch, postresgql, datastax, mongodb, rabbitmq, mysql

subcollection: cloud-databases

---

{{site.data.keyword.attribute-definition-list}}

# Managing security and compliance with {{site.data.keyword.databases-for}}
{: #manage-security-compliance}

{{site.data.keyword.databases-for}} is integrated with the {{site.data.keyword.compliance_short}} to help you manage security and compliance for your organization.
{: shortdesc}

With the {{site.data.keyword.compliance_short}}, you can monitor for controls and goals that pertain to {{site.data.keyword.databases-for}}.

## Monitoring security and compliance posture with {{site.data.keyword.databases-for}}
{: #monitor-cloud-databases}

As a security or compliance focal, you can use the {{site.data.keyword.databases-for}} [goals](#x2117978){: term} to help ensure that your organization is adhering to the external and internal standards for your industry. By using the {{site.data.keyword.compliance_short}} to validate the resource configurations in your account against a [profile](#x2034950){: term}, you can identify potential issues as they arise.

All of the goals for {{site.data.keyword.databases-for}} are added to the {{site.data.keyword.cloud_notm}} Control Library profile, but can also be mapped to other profiles.{: note}

To start monitoring your resources, check out [Getting started with {{site.data.keyword.compliance_short}}](/docs/security-compliance?topic-security-compliance-getting-started)

### Available goals for {{site.data.keyword.databases-for}}
{: #cloud-databases-available-goals}

* **Check whether {{site.data.keyword.databases-for}} is enabled with IBM-managed or customer-managed encryption.** All {{site.data.keyword.databases-for}} instances are automatically encrypted at rest with IBM-managed keys. For more information, see [Key Protect Integration](/docs/cloud-databases?topic=cloud-databases-key-protect).
* **Check whether {{site.data.keyword.databases-for}} is accessible only through TLS.** All {{site.data.keyword.databases-for}} connections use TLS/SSL encryption for data in transit. The current supported version of this encryption is TLS 1.2. 
* **Check whether {{site.data.keyword.databases-for}} is accessible only by using private endpoints.** Customers can disable public endpoints at provision time. For more information, see [Service Endpoints Integration](/docs/cloud-databases?topic=cloud-databases-service-endpoints).
* **Check whether D{{site.data.keyword.databases-for}} network access is restricted to a specific IP range.** For more information, [Allowlisting](/docs/cloud-databases?topic=cloud-databases-allowlisting).
