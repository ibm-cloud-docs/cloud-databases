---

copyright:
  years: 2024
lastupdated: "2024-04-30"

subcollection: cloud-databases

keywords: hosting models, pricing, cost, charges

---

{{site.data.keyword.attribute-definition-list}}

# Hosting model pricing
{: #hosting-pricing}

The following pricing information is for the purpose of understanding the estimated monthly charges for a range of {{site.data.keyword.databases-for}} instance types. 

The estimated charges are for information purposes only and are subject to change without notice. Actual charges may vary.
{: note}

The following table shows the approximate **monthly** charges for {{site.data.keyword.databases-for}} instances with the lowest charge configurations available:

| PostgreSQL | MongoDB Standard Edition | Elasticsearch Enterprise Edition| Redis | etcd | MySQL | RabbitMQ | EnterpriseDB [^tabletext1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $82 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 5 GB disk <br> 2 members | $202 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 10 GB disk <br> 3 members | $252 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 5 GB disk <br> 3 members | $77 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 1 GB disk <br> 2 members | $151 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 20 GB disk <br> 3 members | $181 <br><br> 0.5 vCPU <br> 4 GB RAM <br> 10 GB disk <br> 3 members | $229 <br><br>  1 vCPU <br> 8 GB RAM <br> 1 GB disk <br> 3 members | $1,929 <br><br> 4 vCPU <br> 16 GB RAM <br> 20 GB disk <br> 3 members |
{: caption="Table 1. {{site.data.keyword.databases-for}} approximate monthly charges" caption-side="bottom"}

[^tabletext1]: EnterpriseDB is only available via Isolated Compute, which requires more resources than the Shared Compute configurations used for all other databases in this table.

<br>

The charge for an {{site.data.keyword.databases-for}} instance is determined by the following five factors:

- Database type: PostgreSQL, MongoDB, Elasticsearch, Redis, etcd, MySQL, EnterpriseDB, and RabbitMQ
- Database edition when applicable: MongoDB Standard versus Enterprise and Elasticsearch Enterprise versus Platinum
- Quantity of vCPU allocated per database instance member
- GB of RAM allocated per database instance member
- GB of disk storage allocated per database instance member

Each database instance consists of two or three members, depending on the database type, with each member holding a copy of the data to provide resiliency and high availability. The estimated monthly charges in this example are for one instance, including all of its members.

When deploying a database instance, you can select between Shared Compute hosting and Isolated Compute hosting. Shared Compute offers the lowest minimum resource allocations resulting in lower charges, and extensive flexibility in specifying vCPU, RAM, and storage resources. Isolated compute offers a choice of six standard vCPU x RAM resource profiles that are hosted on single-tenant compute instances for maximum workload isolation and security. Disk storage capacity per member is specified independently of the vCPU x RAM profile selected.

MongoDB Enterprise Edition, Elasticsearch Platinum Edition, and EnterpriseDB require Isolated Compute hosting.
{: note}

The following tables provide estimated monthly charges for a range of configurations. Actual billing for usage is done on an hourly basis, so database instances that exist for less than a full month will be charged based on the number of hours they existed.

## Estimated monthly charges - Shared Compute
{: #hosting-pricing}

| vCPUs | GB RAM | GB disk | PostgreSQL | MongoDB <br> Standard Edition | Elasticsearch <br> Enterprise Edition |
| --- | --- | --- | --- | --- | --- |
| 0.5 | 4 | 40 | $126 | $258 | $318 |
| 1 | 8 | 80 | $252 | $516 | $636 |
| 2 | 8 | 80 | $317 | $661 | $733 |
| 2 | 16 | 160 | $503 | $1,032 | $1,272 |
| 4 | 16 | 160 | $633 | $1,322 | $1,466 |
{: caption="Table 2. Estimated monthly charges - Shared Compute" caption-side="bottom"}

<br>

| vCPUs | GB RAM | GB disk | Redis |etcd | MySQL | RabbitMQ |
| --- | --- | --- | --- | --- | --- | --- |
| 0.5 | 4 | 40 | $126 | $189 | $237 | N/A |
| 1 | 8 | 80 | $252 | $378 | $474 | $378 |
| 2 | 8 | 80 | $317 | $475 | $603 | $475 |
| 2 | 16 | 160 | $503 | $755 | $948 |$755 |
| 4 | 16 | 160 | $633 | $949 | $1,206 | $949 |
{: caption="Table 3. Estimated monthly charges - Shared Compute" caption-side="bottom"}

## Estimated monthly charges - Isolated Compute
{: #hosting-pricing}

| vCPUs | GB RAM | GB disk | PostgreSQL | MongoDB Standard Edition | MongoDB Enterprise Edition | Elasticsearch Enterprise Edition | Elasticsearch Platinum Edition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 16 | 530 | $1,098 | $2,019 | N/A | $2,164 | $2,600 |
| 8 | 32 | 320 | $1,265 | $2,644 | $4,734 | $2,932 | $3,845 |
| 8 | 64 | 640 | $2,012 | $4,125 | $7,918 | $5,088 | $6,936 |
| 16 | 64 | 640 | $2,529 | $5,287 | $9,468 | $5,864 | $7,690 |
| 32 | 128 | 1280 | $5,058 | $10,573 | $18,936 | $11,728 | $15,380 |
| 30 | 240 | 2400 | $7,543 | $15,467 | $29,692 | $19,078 | $26,010 |
{: caption="Table 4. Estimated monthly charges - Isolated Compute" caption-side="bottom"}

<br>

| vCPUs | GB RAM | GB disk | Redis | etcd | MySQL | EnterpriseDB | RabbitMQ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 16 | 530 | $1,098 | $1,646 | $1,904 | $2,891 | $1,646 |
| 8 | 32 | 320 | $1,265 | $1,897 | $2,412 | $4,386 | $1,897 |
| 8 | 64 | 640 | $2,012 | $3,017 | $3,791 | $6,176 | $3,017 |
| 16 | 64 | 640 | $2,529 | $3,794 | $4,824 | $8,771 | $3,794 |
| 32 | 128 | 1280 | $5,058 | $7,587 | $9,647 | $17,542 | $7,587 |
| 30 | 240 | 2400 | $7,543 | $11,314 | $14,213 | $23,157 | $11,314 |
{: caption="Table 5. Estimated monthly charges - Isolated Compute" caption-side="bottom"}

## Estimated monthly charges for other configurations
{: #hosting-pricing-other}

Use the iformation in the following tables to estimate the monthly charge for combinations of vCPU, RAM, and disk that is not shown in the previous tables. The estimated monthly charges are for one member, so to estimate the charge per instance, multiply by the number of members/instance shown in the table.

| | PostgreSQL | MongoDB <br> Standard Edition | MongoDB Enterprise Edition | Elasticsearch Enterprise Edition | Elasticsearch Platinum Edition |
| --- | --- | --- | --- | --- | --- |
| Members/instance | 2 | 3 | 3 | 3 | 3 |
| 1 vCPU/month/member | $32.35 | $48.41 | $64.59 | $32.35 | $32.35 |
| 1 GB RAM/month/member | $5.39 | $9.15 | $26.89 | $16.18 | $26.10 |
| 1 GB disk/month/member | $0.63 | $0.63 | $0.63| $0.63 | $0.63 |
{: caption="Table 6. Estimated monthly charges for other configurations" caption-side="bottom"}

<br>

| | Redis | etcd | MySQL | EnterpriseDB | RabbitMQ |
| --- | --- | --- | --- | --- | --- |
| Members/instance | 2 | 3 | 3 | 3 | 3 |
| 1 vCPU/month/member | $32.35 | $32.35 | $43.06 | $107.15 | $32.35 |
| 1 GB RAM/month/member | $5.39 | $5.39 | $8.08 | $12.36 | $5.39 |
| 1 GB disk/month/member | $0.63 | $0.63 | $0.63| $0.63 | $0.63 |
{: caption="Table 7. Estimated monthly charges for other configurations" caption-side="bottom"}
