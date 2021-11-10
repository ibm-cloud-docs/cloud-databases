---

copyright:
  years: 2019, 2021
lastupdated: "2021-11-04"

subcollection: cloud-databases

keywords: allowlist, ip addresses, blocklist, whitelist

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:tip: .tip}
{:note: .note}

# Allowlisting
{: #allowlisting} 

If you want to restrict access to your databases, you can allowlist specific IP addresses or ranges of IP addresses on your deployment.

If you use allowlists in your environment, you can allowlist our services by using the list of subnets for each region.

We updated documentation to reflect changes in terminology from `whitelist` to `allowlist`. You might encounter continued references to this former terminology while we work to implement these deeper changes to code, API, and CLI commands. 
{: .note}

## Using IP allowlists on your Deployment
{: #ip-allowlist} 

When you create an allowlist, only IP addresses that match the allowlist or are in the range of IP addresses in the allowlist can connect to your deployment. Allowlists can be enabled for both public endpoints and private endpoints. When no IP addresses are in the allowlist, the allowlist is unavailable and the deployment accepts connections from any IP address.

Even if not explicitly allowlisted, {{site.data.keyword.cloud_notm}} management services are still able to connect.
{: .tip}

### Setting an allowlist
{: #set-allowlist} 

The UI for managing allowlists is on the _Settings_ tab of your _Deployment Overview_.

![Allowlist UI](images/settings-allowlist-ip.png){: caption="Figure 1. Deployment Overview tab" caption-side="bottom"}

**IP addresses** - The *IP* field can take a single complete IPv4 address with or without a netmask. Without a netmask, incoming connections must come from exactly that IP address. To allow a connection from a specified range of IP addresses, use a netmask. The IP address must be fully specified. That means entering, for example, 192.168.1.0/24 rather than 192.168.1/24.

IPv6 is not currently supported.
{: tip}

**Description** - The *Description* can be any user-significant text for identifying the allowlist entry - a customer name, project identifier, or employee number, for example. The description field is required.

### Setting an allowlist through the CLI
{: #set-allowlist-cli} 

The {{site.data.keyword.databases-for}} CLI plug-in offers a set of commands for managing allowlists. Use [`cdb deployment-whitelist-add`](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference#deployment-allowlist-add) to add an allowlist. For example,
```bash
ibmcloud cdb deployment-whitelist-add example-deployment 198.51.100.1 "Allowlisted for testing"
```
{: .pre}

for a single IP address and 
```bash
ibmcloud cdb deployment-whitelist-add example-deployment 198.51.100.0/24 "Testing range is now open" 
```
{: .pre}

for an IP range.

Use [`cdb deployment-whitelist-list`](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference#deployment-allowlist-list) to view the current allowlist. For example,
```bash
ibmcloud cdb deployment-whitelist-list <deployment name or CRN>
```
{: .pre}

More information is on the {{site.data.keyword.databases-for}} CLI plug-in [reference page](/docs/databases-cli-plugin?topic=databases-cli-plugin-cdb-reference).

### Setting an allowlist through the API
{: #set-allowlist-api} 

To use the {{site.data.keyword.databases-for}} API to manage your allowlist with the [`/deployments/{id}/whitelists/`](https://cloud.ibm.com/apidocs/cloud-databases-api#retrieve-the-allowlisted-addresses-and-ranges-for-) endpoint. You can retrieve the current allowlist, add entries to the allowlist, and also bulk upload IP addresses to the allowlist from the API. 

More information is in the [API Reference](https://cloud.ibm.com/apidocs/cloud-databases-api)

### Removing an allowlist
{: #remove-allowlist} 

From the UI, remove an IP address or netmask from the allowlist by clicking *Remove*. You can also use CLI command is `cdb deployment-whitelist-delete` or send a `DELETE` request to the API endpoint. When all entries on the allowlist are removed, the allowlist is unavailable and all IP addresses are accepted by your deployment.

## Allowlist {{site.data.keyword.databases-for}} in your Environment
{: #allowlist-ips}

If you use allowlists to control connections in your environment, you can use the following IP lists to allowlist {{site.data.keyword.databases-for}} deployments. You should allowlist all of the subnet ranges for the _entire_ region that your deployments live in.

### `che01` List
{: #che01-list} 

Subnet | Location
-- | --
169.38.95.96/27 | Chennai 1
169.38.121.144/28 | Chennai 1
169.38.136.192/26 | Chennai 1
169.38.73.144/29 | Chennai 1
169.38.105.72/29 | Chennai 1

### `eu-gb` List
{: #eu-gb-list} 

Subnet | Location
-- | --
158.175.64.80/28 | London 4
158.175.139.160/27 | London 4
158.175.147.0/26 | London 4
158.175.151.0/25 | London 4
158.175.156.0/24 | London 4
158.175.81.104/29 | London 4
158.175.92.168/29 | London 4
158.175.97.0/29 | London 4
158.175.97.160/29 | London 4
158.175.125.72/29 | London 4
141.125.69.32/27 | London 5
141.125.71.0/28 | London 5
141.125.83.64/26 | London 5
141.125.88.0/25 | London 5
141.125.93.0/24 | London 5
141.125.69.24/29 | London 5
141.125.70.0/29 | London 5
141.125.77.184/29 | London 5
141.125.85.80/29 | London 5
141.125.87.48/29 | London 5
158.176.109.192/28 | London 6
158.176.109.224/27 | London 6
158.176.122.0/26 | London 6
158.176.139.128/25 | London 6
158.176.148.0/24 | London 6
158.176.71.248/29 | London 6
158.176.87.128/29 | London 6
158.176.113.136/29 | London 6
158.176.122.232/29 | London 6
158.176.124.216/29 | London 6

### `seo01` List
{: #seo01-list} 

Subnet | Location
-- | --
169.56.80.128/28 | Seoul 1
169.56.106.0/26 | Seoul 1
169.56.120.96/27 | Seoul 1
169.56.67.232/29 | Seoul 1
169.56.164.64/29 | Seoul 1

### `au-syd` List
{: #au-syd-list} 

Subnet | Location
-- | --
168.1.13.64/26 | Sydney 1
168.1.29.48/28 | Sydney 1
168.1.216.96/27 | Sydney 1
168.1.32.72/29 | Sydney 1
168.1.36.88/29 | Sydney 1
168.1.62.224/29 | Sydney 1
130.198.102.0/26 | Sydney 4
130.198.102.144/28 | Sydney 4
130.198.102.160/27 | Sydney 4
130.198.70.232/29 | Sydney 4
130.198.93.128/29 | Sydney 4
130.198.99.64/29 | Sydney 4
135.90.68.96/28 | Sydney 5
135.90.69.96/27 | Sydney 5
135.90.83.0/26 | Sydney 5
135.90.67.24/29 | Sydney 5
135.90.67.128/29 | Sydney 5
135.90.67.128/29 | Sydney 5

### `jp-tok` List
{: #jp-tok-list} 

Subnet | Location
-- | --
161.202.140.160/27 | Tokyo 2
169.56.7.192/26 | Tokyo 2
169.56.45.160/28 | Tokyo 2
161.202.102.80/29 | Tokyo 2
161.202.145.56/29 | Tokyo 2
161.202.234.216/29 | Tokyo 2
128.168.72.32/27 | Tokyo 4
128.168.72.176/28 | Tokyo 4
128.168.93.64/26 | Tokyo 4
128.168.69.72/29 | Tokyo 4
128.168.71.80/29 | Tokyo 4
128.168.71.88/29 | Tokyo 4
165.192.71.32/28 | Tokyo 5
165.192.71.96/27 | Tokyo 5
165.192.89.192/26 | Tokyo 5
165.192.66.0/29 | Tokyo 5
165.192.70.168/29 | Tokyo 5
165.192.71.232/29 | Tokyo 5

### `jp-osa` List
{: #jp-osa-list} 

Subnet | Location
-- | --
163.68.68.112/28 | Osaka 21
163.68.73.96/27 | Osaka 21 
163.68.67.112/29 | Osaka 21 
163.68.70.56/29  | Osaka 21 
163.69.65.96/28 | Osaka 22 
163.69.68.0/27  | Osaka 22 
163.69.65.48/29  | Osaka 22 
163.69.65.56/29  | Osaka 22 
163.73.65.160/28 | Osaka 23 
163.73.68.64/27  | Osaka 23 
163.73.67.184/29 | Osaka 23 
163.73.67.224/29 | Osaka 23 

### `us-east` List
{: #us-east-list} 

Subnet | Location
-- | --
52.116.78.0/25 | Washington 4
52.116.115.0/24 | Washington 4
169.47.179.0/26 | Washington 4
169.63.72.160/28 | Washington 4
169.63.121.128/27 | Washington 4
169.63.86.24/29 | Washington 4
169.63.111.112/29 | Washington 4
169.63.121.55/29 | Washington 4
169.63.121.48/29 | Washington 4
169.63.125.216/29 | Washington 4
169.59.138.0/24 | Washington 6
169.63.128.160/27 | Washington 6
169.63.135.176/28 | Washington 6
169.63.139.192/26 | Washington 6
169.63.172.0/25 | Washington 6
169.60.89.0/29 | Washington 6
169.60.95.144/29 | Washington 6
169.63.129.112/29 | Washington 6
169.63.141.232/29 | Washington 6
169.63.149.192/29 | Washington 6
52.117.104.0/24 | Washington 7
169.61.123.80/28 | Washington 7
169.62.42.32/27 | Washington 7
169.62.54.128/26 | Washington 7
169.62.60.0/25 | Washington 7
52.117.76.40/29 | Washington 7
169.61.113.32/29 | Washington 7
169.61.113.40/29 | Washington 7
169.61.122.152/29 | Washington 7
169.62.6.80/29 | Washington 7

### `eu-de` List
{: #eu-de-list} 

Subnet | Location
-- | --
158.177.41.0/24 | Frankfurt 2
158.177.77.32/27 | Frankfurt 2
158.177.87.128/25 | Frankfurt 2
158.177.155.0/26 | Frankfurt 2
158.177.241.0/24 | Frankfurt 2
158.177.110.104/29 | Frankfurt 2
158.177.221.168/29 | Frankfurt 2
159.122.97.16/29 | Frankfurt 2
159.122.97.40/29 | Frankfurt 2
159.122.108.208/29 | Frankfurt 2
159.122.108.216/29 | Frankfurt 2
169.50.10.8/29 | Frankfurt 2
169.50.15.24/29 | Frankfurt 2
169.50.53.240/29 | Frankfurt 2
161.156.95.192/27 | Frankfurt 4
161.156.97.0/26 | Frankfurt 4
161.156.131.128/25 | Frankfurt 4
161.156.152.0/24 | Frankfurt 4
161.156.69.128/29 | Frankfurt 4
161.156.69.136/29 | Frankfurt 4
161.156.107.152/29 | Frankfurt 4
161.156.111.48/29 | Frankfurt 4
161.156.111.72/29 | Frankfurt 4
161.156.122.232/29 | Frankfurt 4
161.156.132.96/29 | Frankfurt 4
161.156.148.208/29 | Frankfurt 4
161.156.157.128/29 | Frankfurt 4
149.81.73.144/28 | Frankfurt 5
149.81.80.224/27 | Frankfurt 5
149.81.114.0/26 | Frankfurt 5
149.81.132.0/25 | Frankfurt 5
149.81.139.0/24 | Frankfurt 5
149.81.77.200/29 | Frankfurt 5
149.81.79.176/29 | Frankfurt 5
149.81.83.208/29 | Frankfurt 5
149.81.84.96/29 | Frankfurt 5
149.81.87.136/29 | Frankfurt 5
149.81.98.160/29 | Frankfurt 5
149.81.100.200/29 | Frankfurt 5
149.81.101.112/29 | Frankfurt 5
149.81.142.40/29 | Frankfurt 5

### `us-south` List
{: #us-south-list} 

Subnet | Location
-- | --
52.116.167.0/24 | Dallas 10
52.116.179.160/28 | Dallas 10
52.116.190.0/26 | Dallas 10
52.117.150.0/25 | Dallas 10
52.117.184.0/24 | Dallas 10
150.238.244.0/24 | Dallas 10
169.46.57.0/27 | Dallas 10
169.47.212.160/27 | Dallas 10
169.48.141.208/29 | Dallas 10
169.61.212.192/26 | Dallas 10
169.61.219.224/28 | Dallas 10
169.63.201.128/25 | Dallas 10
169.63.204.0/24 | Dallas 10
52.116.190.128/29 | Dallas 10
52.116.190.232/29 | Dallas 10
52.117.148.24/29 | Dallas 10
150.238.4.144/29 | Dallas 10
150.238.247.160/29 | Dallas 10
169.46.13.232/29 | Dallas 10
169.46.17.80/29 | Dallas 10
169.46.21.168/29 | Dallas 10
169.46.40.0/29 | Dallas 10
169.46.50.232/29 | Dallas 10
169.46.51.56/29 | Dallas 10
169.46.51.104/29 | Dallas 10
169.46.78.8/29 | Dallas 10
169.46.81.168/29 | Dallas 10
169.46.99.96/29 | Dallas 10
169.46.99.168/29 | Dallas 10
169.46.110.0/29 | Dallas 10
169.46.120.176/29 | Dallas 10
169.47.197.200/29 | Dallas 10
169.47.228.248/29 | Dallas 10
169.47.229.112/29 | Dallas 10
169.47.246.32/29 | Dallas 10
169.47.252.128/29 | Dallas 10
169.48.135.72/29 | Dallas 10
169.48.140.136/29 | Dallas 10
169.48.161.192/29 | Dallas 10
169.48.164.144/29 | Dallas 10
169.60.229.168/29 | Dallas 10
169.61.193.120/29 | Dallas 10
169.61.214.168/29 | Dallas 10
169.63.195.32/29 | Dallas 10
169.63.218.112/29 | Dallas 10
169.63.220.32/29 | Dallas 10
52.116.212.0/24 | Dallas 12
52.116.218.160/27 | Dallas 12
52.116.229.128/25 | Dallas 12
52.116.252.0/24 | Dallas 12
169.47.108.192/26 | Dallas 12
169.48.215.160/27 | Dallas 12
169.59.194.0/24 | Dallas 12
169.59.234.0/24 | Dallas 12
169.61.157.128/25 | Dallas 12
169.61.167.16/28 | Dallas 12
169.61.169.48/28 | Dallas 12
169.63.57.64/26 | Dallas 12
52.116.244.112/29 | Dallas 12
169.47.101.0/29 | Dallas 12
169.47.101.8/29 | Dallas 12
169.47.101.56/29 | Dallas 12
169.47.107.88/29 | Dallas 12
169.47.107.144/29 | Dallas 12
169.47.109.80/29 | Dallas 12
169.48.236.176/29 | Dallas 12
169.48.240.192/29 | Dallas 12
169.61.133.216/29 | Dallas 12
169.61.136.168/29 | Dallas 12
169.61.139.72/29 | Dallas 12
169.61.139.96/29 | Dallas 12
169.61.150.216/29 | Dallas 12
169.61.178.104/29 | Dallas 12
169.63.2.72/29 | Dallas 12
169.63.18.64/29 | Dallas 12
169.63.25.0/29 | Dallas 12
169.63.27.0/29 | Dallas 12
169.63.54.168/29 | Dallas 12
169.63.55.136/29 | Dallas 12
169.63.58.64/29 | Dallas 12
169.63.58.72/29 | Dallas 12
52.116.16.0/25 | Dallas 13
52.116.24.32/27 | Dallas 13
52.117.49.0/24 | Dallas 13
52.117.198.128/26 | Dallas 13
52.117.202.128/25 | Dallas 13
52.117.205.0/24 | Dallas 13
52.117.230.0/24 | Dallas 13
52.117.235.0/24 | Dallas 13
52.117.254.0/24 | Dallas 13
169.48.76.32/27 | Dallas 13
169.61.32.152/29 | Dallas 13
169.62.218.208/28 | Dallas 13
169.62.237.0/26 | Dallas 13
52.116.19.176/29 | Dallas 13
52.116.19.184/29 | Dallas 13
52.116.25.240/29 | Dallas 13
52.116.32.32/29 | Dallas 13
52.116.54.232/29 | Dallas 13
52.117.22.240/29 | Dallas 13
52.117.23.136/29 | Dallas 13
52.117.55.88/29 | Dallas 13
52.117.55.112/29 | Dallas 13
52.117.62.120/29 | Dallas 13
52.117.234.176/29 | Dallas 13
169.48.98.192/29 | Dallas 13
169.48.107.72/29 | Dallas 13
169.48.123.144/29 | Dallas 13
169.59.10.192/29 | Dallas 13
169.60.138.216/29 | Dallas 13
169.60.159.176/29 | Dallas 13
169.60.164.24/29 | Dallas 13
169.60.184.56/29 | Dallas 13
169.61.23.192/29 | Dallas 13
169.61.48.232/29 | Dallas 13
169.61.49.136/29 | Dallas 13
169.61.56.216/29 | Dallas 13
169.61.59.96/29 | Dallas 13
169.61.60.32/29 | Dallas 13
169.62.134.96/29 | Dallas 13
169.62.158.88/29 | Dallas 13
169.62.187.152/29 | Dallas 13
169.62.239.40/29 | Dallas 13
169.62.240.224/29 | Dallas 13
