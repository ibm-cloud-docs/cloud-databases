---

copyright:
  years: 2023
lastupdated: "2023-06-07"

subcollection: cloud-databases

keywords: isolated compute

---

{{site.data.keyword.attribute-definition-list}}

# {{site.data.keyword.databases-for}} Isolated Compute
{: #iso-compute}

{{site.data.keyword.databases-for}} Isolated Compute provides dedicated computing resources. 

## {{site.data.keyword.databases-for}} Isolated Compute Advantages
{: #iso-compute-advantages}

Isolated compute offers several advantages:

|                       | Shared Compute                                           | Isolated Compute                                                  |
|-----------------------|---------------------------------------------------------|------------------------------------------------------------------|
| Performance           | Performance may vary due to resource contention.         | Consistent and predictable performance.                           |
| Security              | Shared infrastructure increases the risk of breaches.    | Enhanced security with reduced risk of unauthorized access.       |
| Customization         | Limited control over resource allocation and settings.   | Greater control for customization and performance tuning.         |
| Scalability           | Resource scaling may be constrained or limited.          | Flexible resource scaling to meet changing demands.               |
| Compliance            | Compliance may be challenging due to shared resources.   | Easier compliance adherence with dedicated resources.             |
| Noise Isolation       | May experience performance issues due to noisy neighbors.| Eliminates performance impact that is caused by other tenants' activities.|
{: caption="Table 1. Isolated Compute Differences" caption-side="top"}

- Performance: Isolated compute ensures consistent and predictable performance for your database. By dedicating computing resources to your workload, you can avoid performance fluctuations that are caused by resource contention with other users or applications sharing the same infrastructure.

- Security: Isolated compute provides enhanced security for your deployment. With dedicated resources, the risk of unauthorized access or data breaches due to the actions of other users is significantly reduced. It helps to isolate your sensitive data and prevent unauthorized access from other tenants or applications.

- Customization: Dedicated compute resources allow you to customize the environment according to your specific requirements. You have more control over resource allocation, configuration settings, and performance tuning, enabling you to optimize the database for your workload's unique demands.

- Scalability: Isolated compute provides scalability benefits by allowing you to scale resources up or down as needed. You can easily adjust compute capacity based on your database workload's changing demands, ensuring optimal performance and cost efficiency.

- Compliance: If your application or workload has specific compliance requirements, isolated compute can help meet those requirements more effectively. By isolating your database on dedicated resources, you can ensure compliance with data sovereignty, privacy regulations, or industry-specific compliance standards.

- Noise isolation: Sharing infrastructure with other users or applications may result in "noisy neighbors" that consume excessive resources, impacting your database's performance. Isolated compute mitigates this issue by providing dedicated resources that are not affected by the activities of other tenants, ensuring consistent and reliable performance.

Assess your workload's requirements and consider the tradeoffs between performance, security, and cost before choosing an isolated compute solution for your deployment.

## {{site.data.keyword.databases-for}} Isolated Compute Provisioning
{: #iso-compute-provisioning}

### {{site.data.keyword.databases-for}} Isolated Compute Provisioning through the UI
{: #iso-compute-provisioning}
{: ui}

### {{site.data.keyword.databases-for}} Isolated Compute Provisioning through the API
{: #iso-compute-provisioning}
{: api}

### {{site.data.keyword.databases-for}} Isolated Compute Provisioning through the CLI
{: #iso-compute-provisioning}
{: cli}

### {{site.data.keyword.databases-for}} Isolated Compute Provisioning through Terraform
{: #iso-compute-provisioning}
{: terraform}
