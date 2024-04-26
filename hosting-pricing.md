---

copyright:
  years: 2023, 2024
lastupdated: "2024-04-25"

subcollection: cloud-databases

keywords: hosting models, pricing, cost, charges

---

{{site.data.keyword.attribute-definition-list}}

# {{site.data.keyword.databases-for}} pricing
{: #hosting-pricing}

Information in this section is for the purpose of understanding the estimated monthly charges for a range of {{site.data.keyword.databases-for}} instance types.

The estimated charges provided in this document are for information purposes only and are subject to change without notice. Actual charges may vary.

The following table shows the approximate **monthly** charges for {{site.data.keyword.databases-for}} instances with the lowest charge configurations available:

| PostgreSQL | MongoDB Standard Edition | Elasticsearch Enterprise Edition| Redis | etcd | MySQL | RabbitMQ | EnterpriseDB1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $82 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 5 GB disk <br> 2 members | $202 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 10 GB disk <br> 3 members | $252 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 5 GB disk <br> 3 members | $77 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 1 GB disk <br> 2 members | $151 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 20 GB disk <br> 3 members | $181 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 10 GB disk <br> 3 members | $229 <br><br>  1 vCPU <br> 8 GB RAM <br> 1 GB disk <br> 3 members | $1,929 <br><br> 4 vCPU <br> 16 GB RAM <br> 20 GB disk <br> 3 members |
{: caption="Table 1. {{site.data.keyword.databases-for}} approximate monthly charges " caption-side="bottom"}

1 Enterprise DB is only available via Isolated Compute which requires more resources that the Shared Compute configurations used for all other databases in the Table above.

The charge for an {{site.data.keyword.databases-for}} instance is determined by the following five factors:

- Database type: PostgreSQL, MongoDB, Elasticsearch, Redis, etcd, MySQL, EnterpriseDB, and RabbitMQ
- Database edition when applicable: MongoDB Standard versus Enterprise and Elasticsearch Enterprise versus Platinum
- Quantity of vCPU allocated per database instance member
- GB of RAM allocated per database instance member
- GB of disk storage allocated per database instance member

Each database instance consists of 2 or 3 members, depending on the database type, with each member holding a copy of the data to provide a resiliency and high availability. The estimated monthly charges shown in this example are for one instance, including all of its members.

When deploying a database instance, you can select between Shared Compute hosting and Isolated Compute hosting. Shared Compute offers the lowest minimum resource allocations resulting in lower charges, and extensive flexibility in specifying vCPU, RAM, and storage resources. Isolated compute offers a choice of six standard vCPU x RAM resource profiles that are hosted on single tenant compute instances for maximum workload isolation and security. Disk storage capacity per member is specified independently of the vCPU x RAM profile selected.

MongoDB Enterprise Edition, Elasticsearch Platinum Edition, and EnterpriseDB require Isolated Compute hosting.

The following tables provide the estimated monthly charges for a range of configurations. Actual billing for usage is done on an hourly basis, so database instances that exist for less than a full month will be charged based on the number of hours they existed.

## Estimated Monthly Charges - Shared Compute
{: #hosting-pricing}

| vCPUs | GB RAM | GB disk | PostgreSQL | MongoDB Standard Edition | Elasticsearch Enterprise Edition |
| --- | --- | --- | --- | --- | --- |
| 0.5 | 4 | 40 | $126 | $258 | $318 |
| 1 | 8 | 80 | $252 | $516 | $636 |
| 2 | 8 | 80 | $317 | $661 | $733 |
| 2 | 16 | 160 | $503 | $1,032 | $1,272 |
| 4 | 16 | 160 | $633 | $1,322 | $1,466 |
{: caption="Table 2. Estimated monthly charges - Shared Compute " caption-side="bottom"}

| vCPUs | GB RAM | GB disk | Redis |etcd | MySQL | RabbitMQ |
| --- | --- | --- | --- | --- | --- | --- |
| 0.5 | 4 | 40 | $126 | $189 | $237 | |
| 1 | 8 | 80 | $252 | $378 | $474 | $378 |
| 2 | 8 | 80 | $317 | $475 | $603 | $475 |
| 2 | 16 | 160 | $503 | $755 | $948 |$755 |
| 4 | 16 | 160 | $633 | $949 | $1,206 | $949 |
{: caption="Table 3. Estimated monthly charges - Shared Compute " caption-side="bottom"}

## Estimated Monthly Charges - Isolated Compute
{: #hosting-pricing}

| vCPUs | GB RAM | GB disk | PostgreSQL | MongoDB Standard Edition | MongoDB Enterprise Edition | Elasticsearch Enterprise Edition | Elasticsearch Enterprise Edition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 16 | 530 | $1,098 | $2,019 | | $2,164 | $2,600 |
| 8 | 32 | 320 | $1,265 | $2,644 | $4,734 | $2,932 | $3,845 |
| 8 | 64 | 640 | $2,012 | $4,125 | $7,918 | $5,088 | $6,936 |
| 16 | 64 | 640 | $2,529 | $5,287 | $9,468 | $5,864 | $7,690 |
| 32 | 128 | 1280 | $5,058 | $10,573 | $18,936 | $11,728 | $15,380 |
| 32 | 240 | 2400 | $7,543 | $15,467 | $29,692 | $19,078 | $26,010 |
{: caption="Table 2. Estimated monthly charges - Isolated Compute " caption-side="bottom"}

| vCPUs | GB RAM | GB disk | Redis | etcd | MySQL | EnterpriseDB | RabbitMQ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 16 | 530 | $1,098 | $1,646 | $1,904 | $2,891 | $1,646 |
| 8 | 32 | 320 | $1,265 | $2,644 | $4,734 | $2,932 | $3,845 |
| 8 | 64 | 640 | $2,012 | $4,125 | $7,918 | $5,088 | $6,936 |
| 16 | 64 | 640 | $2,529 | $5,287 | $9,468 | $5,864 | $7,690 |
| 32 | 128 | 1280 | $5,058 | $10,573 | $18,936 | $11,728 | $15,380 |
| 32 | 240 | 2400 | $7,543 | $15,467 | $29,692 | $19,078 | $26,010 |
{: caption="Table 2. Estimated monthly charges - Isolated Compute " caption-side="bottom"}
