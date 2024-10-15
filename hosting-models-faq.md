---

copyright:
  years: 2023, 2024

lastupdated: "2024-10-14"

subcollection: cloud-databases

keywords: isolated compute, hosting models, shared compute

---

{{site.data.keyword.attribute-definition-list}}

# Hosting models FAQ
{: #hosting-models-faq}

**My Shared Compute database has 0 CPU. What does this mean?**

Shared Compute automatically allocates CPU for customers that do not specify their CPU amount. On API v5, this automatically allocated setting shows as CPU = 0. We also return an "Allocation as Fraction" result that shows what specific CPU value you have. CPU is allocated at 1/8th of a RAM, starting from each databases' minimum CPU amount up to 2 CPU. This CPU value will continue to scale as the RAM value scales.

**Per the [Shared Compute transition placement](/docs/cloud-databases?topic=cloud-databases-hosting-models&interface=cli#shared-compute-placement), my understanding is that because this instance has 8 GB of RAM, it should have 1 CPU allocated per member, but the cloud-databases CLI show 0 CPUs allocated.**

See the previous answer.

**I want fractional CPU. How do I do that?**

Scale your database to the `multitenant` hosting model, and its CPU to 0. This turns on the Shared Compute automatic CPU allocation, where CPU is 1/8th of the database's RAM allocation, up to 2 CPU.

**What does it mean to have fractional CPU?**

CPU time is divided into units called periods or time slices. In each time slice you get a duration of CPU run time.

In general, the number of cores you specify decides how much CPU time you get. The default kernel run time is 50ms; therefore, with one core of CPU available, there is 20 time slices of 50ms run time.

If an instance A requests 0.5 cores or 500 millicores, assuming for simplicity that there is only one core of CPU on a node or server, instance A will get 10 time slices of 50ms run time each to complete the task. If it cannot complete the task within 10 time slices, the kernel throttles the instance's process after the 10 runs. The remaining 10 time slices for this CPU (since 1 core can have 20 time slices using default run time duration) is then scheduled for other processes while A waits. Once that is done, instance A gets the CPU for another 10 time slices.

**I want to scale my database's resources, but they don't seem to be scaling?**

For Shared Compute instances, make sure to set the host flavor to `multitenant` and separately set your CPU and RAM values. For automatically scaling CPU (capped at 2 CPU), set the CPU to 0. To scale Isolated Compute, set the host flavor to your desired size; do not set CPU and RAM values since the Isolated size already includes allocations for both. For more information, see the [Scaling documentation](/docs/cloud-databases?topic=cloud-databases-scale-instance).

**My database is on a hosting model, even though my Terraform configuration didn't specify it.**

Starting August, we begun to switchover customer instances to the new hosting models. This can lead to Terraform scripts that do not reflect the actualstate of the database, since these scripts do not have the new `host_flavor` parameter. Your database will still function as normal, though we recommend adding the `host_flavor` parameter for future ease of use.

**What does it mean to switch / migrate between hosting models? Will there be downtime?**

Switching between databases is not a large migration, but a standard operation similar to our maintenance work. Therefore, it does not involve downtime, though [we recommend](/docs/cloud-databases?topic=cloud-databases-responsibilities-cloud-databases) your application to have retry and reconnect logic.

**If we switch to a hosting model, or switch between hosting models, will the disk size be retained as per the current configuration?**

Yes. Your disk will not be impacted due to hosting model changes.

**Does autoscaling work?**

Autoscaling continues to work for new hosting models. For Shared Compute, RAM and disk autoscaling remains available. For Isolated Compute, disk autoscaling is available.

Note: Due to the size jumps across Isolated Compute, we have currently disallowed RAM/CPU autoscaling on Isolated Compute. If there is interest in this feature, let our team know.

**I’m getting a CLI failed status error or a 403 forbidden error, but on the UI and CLI it looks like my scale operation completed?**

This is due to CLI token expiry. The CLI expires tokens to quickly to preserve the security of your system, meaning any operations in progress will show a fail state. We recommend refreshing your session, and checking the database for the results of the task.
