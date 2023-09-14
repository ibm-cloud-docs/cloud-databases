---
copyright:
  years: 2023
lastupdated: "2023-09-14"

subcollection: cloud-databases

keywords: 

---

{{site.data.keyword.attribute-definition-list}}

# High-Availability FAQ
{: #faq-high-availability}
{: faq}
{: support}

You encounter the following error: `READONLY You can't write against a read only replica`.
{: shortdesc}

{{site.data.keyword.databases-for}} instances are deployed as [highly available](/docs/databases-for-redis?topic=databases-for-redis-high-availability){: external}. The `READONLY` error message occurs when an application retains an active connection against a replica and attempts to write to the database, after a switchover has occurred. To resolve this error, the application should recreate their connection so they establish a new connection against the leader.
