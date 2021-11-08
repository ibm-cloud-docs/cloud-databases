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
52.116.78.127/25 | Washington 4
52.116.115.255/24 | Washington 4
169.47.179.63/26 | Washington 4
169.63.72.175/28 | Washington 4
169.63.121.159/27 | Washington 4
169.63.86.31/29 | Washington 4
169.63.111.119/29 | Washington 4
169.63.121.55/29 | Washington 4
169.63.121.63/29 | Washington 4
169.63.125.223/29 | Washington 4
169.59.138.255/24 | Washington 6
169.63.128.191/27 | Washington 6
169.63.135.191/28 | Washington 6
169.63.139.255/26 | Washington 6
169.63.172.127/25 | Washington 6
169.60.89.7/29 | Washington 6
169.60.95.151/29 | Washington 6
169.63.129.119/29 | Washington 6
169.63.141.239/29 | Washington 6
169.63.149.199/29 | Washington 6
52.117.104.255/24 | Washington 7
169.61.123.95/28 | Washington 7
169.62.42.63/27 | Washington 7
169.62.54.191/26 | Washington 7
169.62.60.127/25 | Washington 7
52.117.76.47/29 | Washington 7
169.61.113.39/29 | Washington 7
169.61.113.47/29 | Washington 7
169.61.122.159/29 | Washington 7
169.62.6.87/29 | Washington 7

### `eu-de` List
{: #eu-de-list} 

Subnet | Location
-- | --
158.177.41.255/24 | Frankfurt 2
158.177.77.63/27 | Frankfurt 2
158.177.87.255/25 | Frankfurt 2
158.177.155.63/26 | Frankfurt 2
158.177.241.255/24 | Frankfurt 2
158.177.110.111/29 | Frankfurt 2
158.177.221.175/29 | Frankfurt 2
159.122.97.23/29 | Frankfurt 2
159.122.97.47/29 | Frankfurt 2
159.122.108.215/29 | Frankfurt 2
159.122.108.223/29 | Frankfurt 2
169.50.10.15/29 | Frankfurt 2
169.50.15.31/29 | Frankfurt 2
169.50.53.247/29 | Frankfurt 2
161.156.95.223/27 | Frankfurt 4
161.156.97.63/26 | Frankfurt 4
161.156.131.255/25 | Frankfurt 4
161.156.152.255/24 | Frankfurt 4
161.156.69.135/29 | Frankfurt 4
161.156.69.143/29 | Frankfurt 4
161.156.107.159/29 | Frankfurt 4
161.156.111.55/29 | Frankfurt 4
161.156.111.79/29 | Frankfurt 4
161.156.122.239/29 | Frankfurt 4
161.156.132.103/29 | Frankfurt 4
161.156.148.215/29 | Frankfurt 4
161.156.157.135/29 | Frankfurt 4
149.81.73.159/28 | Frankfurt 5
149.81.80.255/27 | Frankfurt 5
149.81.114.63/26 | Frankfurt 5
149.81.132.127/25 | Frankfurt 5
149.81.139.255/24 | Frankfurt 5
149.81.77.207/29 | Frankfurt 5
149.81.79.183/29 | Frankfurt 5
149.81.83.215/29 | Frankfurt 5
149.81.84.103/29 | Frankfurt 5
149.81.87.143/29 | Frankfurt 5
149.81.98.167/29 | Frankfurt 5
149.81.100.207/29 | Frankfurt 5
149.81.101.119/29 | Frankfurt 5
149.81.142.47/29 | Frankfurt 5

### `us-south` List
{: #us-south-list} 

Subnet | Location
-- | --
52.116.167.255/24 | Dallas 10
52.116.179.175/28 | Dallas 10
52.116.190.63/26 | Dallas 10
52.117.150.127/25 | Dallas 10
52.117.184.255/24 | Dallas 10
150.238.244.255/24 | Dallas 10
169.46.57.31/27 | Dallas 10
169.47.212.191/27 | Dallas 10
169.48.141.215/29 | Dallas 10
169.61.212.255/26 | Dallas 10
169.61.219.239/28 | Dallas 10
169.63.201.255/25 | Dallas 10
169.63.204.255/24 | Dallas 10
52.116.190.135/29 | Dallas 10
52.116.190.239/29 | Dallas 10
52.117.148.31/29 | Dallas 10
150.238.4.151/29 | Dallas 10
150.238.247.167/29 | Dallas 10
169.46.13.239/29 | Dallas 10
169.46.17.87/29 | Dallas 10
169.46.21.175/29 | Dallas 10
169.46.40.7/29 | Dallas 10
169.46.50.239/29 | Dallas 10
169.46.51.63/29 | Dallas 10
169.46.51.111/29 | Dallas 10
169.46.78.15/29 | Dallas 10
169.46.81.175/29 | Dallas 10
169.46.99.103/29 | Dallas 10
169.46.99.175/29 | Dallas 10
169.46.110.7/29 | Dallas 10
169.46.120.183/29 | Dallas 10
169.47.197.207/29 | Dallas 10
169.47.228.255/29 | Dallas 10
169.47.229.119/29 | Dallas 10
169.47.246.39/29 | Dallas 10
169.47.252.135/29 | Dallas 10
169.48.135.79/29 | Dallas 10
169.48.140.143/29 | Dallas 10
169.48.161.199/29 | Dallas 10
169.48.164.151/29 | Dallas 10
169.60.229.175/29 | Dallas 10
169.61.193.127/29 | Dallas 10
169.61.214.175/29 | Dallas 10
169.63.195.39/29 | Dallas 10
169.63.218.119/29 | Dallas 10
169.63.220.39/29 | Dallas 10
52.116.212.255/24 | Dallas 12
52.116.218.191/27 | Dallas 12
52.116.229.255/25 | Dallas 12
52.116.252.255/24 | Dallas 12
169.47.108.255/26 | Dallas 12
169.48.215.191/27 | Dallas 12
169.59.194.255/24 | Dallas 12
169.59.234.255/24 | Dallas 12
169.61.157.255/25 | Dallas 12
169.61.167.31/28 | Dallas 12
169.61.169.63/28 | Dallas 12
169.63.57.127/26 | Dallas 12
52.116.244.119/29 | Dallas 12
169.47.101.7/29 | Dallas 12
169.47.101.15/29 | Dallas 12
169.47.101.63/29 | Dallas 12
169.47.107.95/29 | Dallas 12
169.47.107.151/29 | Dallas 12
169.47.109.87/29 | Dallas 12
169.48.236.183/29 | Dallas 12
169.48.240.199/29 | Dallas 12
169.61.133.223/29 | Dallas 12
169.61.136.175/29 | Dallas 12
169.61.139.79/29 | Dallas 12
169.61.139.103/29 | Dallas 12
169.61.150.223/29 | Dallas 12
169.61.178.111/29 | Dallas 12
169.63.2.79/29 | Dallas 12
169.63.18.71/29 | Dallas 12
169.63.25.7/29 | Dallas 12
169.63.27.7/29 | Dallas 12
169.63.54.175/29 | Dallas 12
169.63.55.143/29 | Dallas 12
169.63.58.71/29 | Dallas 12
169.63.58.79/29 | Dallas 12
52.116.16.127/25 | Dallas 13
52.116.24.63/27 | Dallas 13
52.117.49.255/24 | Dallas 13
52.117.198.191/26 | Dallas 13
52.117.202.255/25 | Dallas 13
52.117.205.255/24 | Dallas 13
52.117.230.255/24 | Dallas 13
52.117.235.255/24 | Dallas 13
52.117.254.255/24 | Dallas 13
169.48.76.63/27 | Dallas 13
169.61.32.159/29 | Dallas 13
169.62.218.223/28 | Dallas 13
169.62.237.63/26 | Dallas 13
52.116.19.183/29 | Dallas 13
52.116.19.191/29 | Dallas 13
52.116.25.247/29 | Dallas 13
52.116.32.39/29 | Dallas 13
52.116.54.239/29 | Dallas 13
52.117.22.247/29 | Dallas 13
52.117.23.143/29 | Dallas 13
52.117.55.95/29 | Dallas 13
52.117.55.119/29 | Dallas 13
52.117.62.127/29 | Dallas 13
52.117.234.183/29 | Dallas 13
169.48.98.199/29 | Dallas 13
169.48.107.79/29 | Dallas 13
169.48.123.151/29 | Dallas 13
169.59.10.199/29 | Dallas 13
169.60.138.223/29 | Dallas 13
169.60.159.183/29 | Dallas 13
169.60.164.31/29 | Dallas 13
169.60.184.63/29 | Dallas 13
169.61.23.199/29 | Dallas 13
169.61.48.239/29 | Dallas 13
169.61.49.143/29 | Dallas 13
169.61.56.223/29 | Dallas 13
169.61.59.103/29 | Dallas 13
169.61.60.39/29 | Dallas 13
169.62.134.103/29 | Dallas 13
169.62.158.95/29 | Dallas 13
169.62.187.159/29 | Dallas 13
169.62.239.47/29 | Dallas 13
169.62.240.231/29 | Dallas 13
