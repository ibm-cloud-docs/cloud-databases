---

copyright:
  years: 2023, 2025
lastupdated: "2025-10-07"

subcollection: cloud-databases

keywords: isolated compute, hosting models, shared compute, transition

---

{{site.data.keyword.attribute-definition-list}}

# Hosting models transition timeline and transition placement
{: #hosting-model-transition}


## Transition timeline from existing hosting models to Isolated and Shared Compute
{: #hosting-model-transition-timeline}

Multi-tenant users that are automatically transitioned to Shared Compute will be *grandfathered*, meaning that they get RAM and CPU increased to the Shared Compute minimum resource allocations, if required. These increases will not be charged until May 2025.
{: important}

### August 2024 - RAM minimum allocation applied for multi-tenant instances
{: #hosting-model-transition-timeline-aug24}

- Existing multi-tenant instances will begin the transition to Shared Compute; this means that first, RAM minimum allocation on multi-tenant instances will be applied (8 GB RAM for RabbitMQ, 4 GB RAM for all other databases), lifting the RAM of existing instances that fall below these minimums.
- All new provisioning requests will also have to abide to the minimum resource requirements (1 CPU and 8 GB RAM for RabbitMQ, 0.5 CPU and 4 GB RAM for all other databases).
- Existing dedicated core users will not be impacted by minimum resource requirements unless a scale or provision action is invoked on an instance that is currently below these minimums.
- Following this, multi-tenant databases will be gradually transitioned from non-determinstic CPU allocation to the deterministic Shared Compute CPU allocation. Ahead of this transition, monitor your database's CPU usage to determine what allocation is required to maintain your current performance level.
- Existing multi-tenant users will be grandfathered through to May 2025 for both CPU and minimum RAM resource allocations that are automatically added.

### September 2024 - Transition of multi-tenant instances to Shared Compute
{: #hosting-model-transition-timeline-sept24}

- All new multi-tenant provisions will use Shared Compute.
- Existing multi-tenant instances will begin the transition to Shared Compute. First, RAM minimum allocation on multi-tenant instances will be applied (8 GB RAM for RabbitMQ, 4 GB RAM for all other databases), lifting the RAM of existing instances that fall below these minimums.
- All new provisioning requests will also have to abide to the minimum resource requirements (1 CPU and 8 GB RAM for RabbitMQ, 0.5 CPU and 4 GB RAM for all other databases).
- Existing dedicated core users will not be impacted by minimum resource requirements unless a scale or provision action is invoked on an instance that is currently below these minimums.
- Following this, multi-tenant databases will be gradually transitioned from non-determinstic CPU allocation to the deterministic Shared Compute CPU allocation.
- **Action:** Ahead of this transition, [monitor your database's CPU usage](/docs/cloud-databases?topic=cloud-databases-monitoring#sysdig-monitor-dashboards-cpu-cores-used-per-member) to determine what allocation is required to maintain your current performance level.
- Existing multi-tenant users will be grandfathered through to May 2025 for both CPU and minimum RAM resource allocations that are automatically added.
- Dedicated cores provisioning remains available.

### May 2025 - End of grandfathering for multi-tenant users, transitioning dedicated cores to Isolated Compute
{: #hosting-model-transition-timeline-may25}

- All existing multi-tenant users will be grandfathered for CPU and minimum RAM allocations until this time.
- At this date, multi-tenant instances will need to comply with the Shared Compute resource allocations.

Between May 18 and 26, 2025, dedicated core users will be transitioned to Isolated Compute. Grandfathering will be removed for Shared Compute instances between June 2 and 9, 2025. All Dedicated Cores instances will be transitioned to the nearest larger Isolated Compute size. Dedicated Core instances can follow the simple switchover steps to transition to Isolated Compute at any time by using the [{{site.data.keyword.databases-for}} CLI plug-in](/docs/cloud-databases?topic=cloud-databases-cdb-reference){: external}, the [{{site.data.keyword.databases-for}} API](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5#introduction){: external}, or through [Terraform](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database){: external}.

Notifications will be sent ahead of changes, including at the following times:

- Before the transition of multi-tenant to Shared Compute, to notify you of expected changes.
- After all multi-tenant instances are transitioned to Shared Compute resource allocations, to recommend that you review your database performance and adjust resources as necessary.
- Before final shutdown of dedicated cores and the transition to Isolated Compute. Additionally, before the end of grandfathering of Shared Compute instances.
You can also find all notifications at [{{site.data.keyword.Bluemix_notm}} announcements](https://cloud.ibm.com/status/announcement).

Ahead of the May 2025 date, if you have a multi-tenant instance, there are a few exceptions where grandfathering would no longer apply:

- If you have an existing database and change your RAM allocation only, you will be charged corresponding to the RAM changes.
- If you have an existing database and change your CPU allocation, you will be charged for all CPU and RAM allocated to your database.
- If you create a new Shared Compute instance, you will be charged for all CPU and RAM allocated to your database.
- If you transition your multi-tenant instance yourself to Shared Compute, you will be charged for all CPU and RAM allocated to your database.

## Shared and Isolated Compute transition placement
{: #shared-isolated-placement}

To determine how existing hosting models will switch over to Shared and Isolated Compute, review the tables below. In the switchover, the assumption is that the starting points are old style multitenant (CPU unallocated, or 0) and dedicated cores.

| **If your current resource allocation is N CPU x M RAM <br> (Non-RabbitMQ Databases):** | **You will be automatically placed on <br> (Non-RabbitMQ Databases):** |
|-------------------------|---------------------|
| N = 0 CPU, M < 4 GB RAM | 0.5 CPU x 4 GB RAM, Shared Compute |
| N = 0 CPU, 4 GB RAM < M ≤ 16 GB RAM | M/8 CPU x M GB RAM, Shared Compute|
| N = 0 CPU, M > 16 GB RAM | 2 CPU x M GB RAM, Shared Compute |
| 0 CPU < N ≤ 4 CPU, M ≤ 16 GB RAM | 4 CPU x 16 GB RAM, Isolated Compute |
| 4 CPU < N ≤ 8 CPU OR 16 GB RAM < M ≤ 32 GB RAM | 8 CPU x 32 GB RAM, Isolated Compute |
| 4 CPU < N ≤ 8 CPU OR 32 GB RAM < M ≤ 64 GB RAM | 8 CPU x 64 GB RAM, Isolated Compute |
| 8 CPU < N ≤ 16 CPU OR 32 GB RAM < M ≤ 64 GB RAM | 16 CPU x 64 GB RAM, Isolated Compute |
| 16 CPU < N ≤ 32 CPU OR 64 GB RAM < M ≤ 128 GB RAM | 32 CPU x 128 RAM, Isolated Compute |
| 16 CPU < N ≤ 30 CPU OR 64 GB RAM < M ≤ 240 GB RAM | 30 CPU x 240 RAM, Isolated Compute |
{: caption="Automatic transition placement" caption-side="bottom"}

<br>

<br>

| **If your current resource allocation is N CPU x M RAM <br> (RabbitMQ):** | **You will be automatically placed on <br> (RabbitMQ):** |
|-------------------------|---------------------|
| N = 0 CPU, M < 8 GB RAM | 1 CPU x 8 GB RAM, Shared Compute |
| N = 0 CPU, 8 GB RAM < M ≤ 16 GB RAM | M/8 CPU x M GB RAM, Shared Compute |
| N = 0 CPU, M > 16 GB RAM | 2 CPU x M GB RAM, Shared Compute |
| 0 CPU < N ≤ 4 CPU, M ≤ 16 GB RAM | 4 CPU x 16 GB RAM, Isolated Compute |
| 4 CPU < N ≤ 8 CPU OR 16 GB RAM < M ≤ 32 GB RAM | 8 CPU x 32 GB RAM, Isolated Compute |
| 4 CPU < N ≤ 8 CPU OR 32 GB RAM < M ≤ 64 GB RAM | 8 CPU x 64 GB RAM, Isolated Compute |
| 8 CPU < N ≤ 16 CPU OR 32 GB RAM < M ≤ 64 GB RAM | 16 CPU x 64 GB RAM, Isolated Compute |
| 16 CPU < N ≤ 32 CPU OR 64 GB RAM < M ≤ 128 GB RAM | 32 CPU x 128 RAM, Isolated Compute |
| 16 CPU < N ≤ 30 CPU OR 64 GB RAM < M ≤ 240 GB RAM | 30 CPU x 240 RAM, Isolated Compute |
{: caption="Automatic transition placement RabbitMQ" caption-side="bottom"}
