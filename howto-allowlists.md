---

copyright:
  years: 2019, 2021
lastupdated: "2022-01-07"

subcollection: cloud-databases

keywords: allowlist, ip addresses, blocklist, whitelist

---

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

### `in-che` List
{: #che01-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Chennai  |  in-che |  CHE01 | 69.38.95.127/27   |  169.38.95.96	
Chennai  |  in-che |  CHE01 | 69.38.121.159/28  |   169.38.121.144
Chennai  |  in-che |  CHE01 | 69.38.132.127/25  |   169.38.132.0
Chennai  |  in-che |  CHE01 | 69.38.136.255/26  |   169.38.136.192
Chennai  |  in-che |  CHE01 | 69.38.73.151/29   |  169.38.73.144
Chennai  |  in-che |  CHE01 | 69.38.105.79/29   |  169.38.105.72

### `ca-tor` List
{: #ca-tor-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Toronto  |   ca-tor | TOR01 | 158.85.91.111/28	  |  158.85.91.96	
Toronto  |   ca-tor | TOR01 | 169.55.142.191/27	|  169.55.142.160	
Toronto  |   ca-tor | TOR01 | 158.85.95.183/29	  |  158.85.95.176	
Toronto  |   ca-tor | TOR01 | 169.55.130.215/29	|  169.55.130.208	
Toronto  |   ca-tor | TOR04 | 163.74.68.95/28	  |  163.74.68.80
Toronto  |   ca-tor | TOR04 | 163.74.69.159/27	  |  163.74.69.128	
Toronto  |   ca-tor | TOR04 | 163.74.68.55/29	  |  163.74.68.48
Toronto  |   ca-tor | TOR04 | 163.74.68.63/29	  |  163.74.68.56
Toronto  |   ca-tor | TOR05 | 163.75.67.111/28	  |  163.75.67.96	
Toronto  |   ca-tor | TOR05 | 163.75.68.95/27	  |  163.75.68.64
Toronto  |   ca-tor | TOR05 | 163.75.67.7/29	    |  163.75.67.0	
Toronto  |   ca-tor | TOR05 | 163.75.67.119/29	  |  163.75.67.112

### `eu-gb` List
{: #eu-gb-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
London | eu-gb | LON04  |   158.175.64.95/28	  |  158.175.64.80	
London | eu-gb | LON04  |   158.175.139.191/27 |   158.175.139.160	
London | eu-gb | LON04  |   158.175.147.63/26	|    158.175.147.0	
London | eu-gb | LON04  |   158.175.151.127/25 |   158.175.151.0	
London | eu-gb | LON04  |   158.175.156.255/24 |   158.175.156.0	
London | eu-gb | LON04  |   158.175.81.111/29	|    158.175.81.104	
London | eu-gb | LON04  |   158.175.91.151/29	|    158.175.91.144	
London | eu-gb | LON04  |   158.175.92.175/29	|    158.175.92.168	
London | eu-gb | LON04  |   158.175.97.7/29	  |  158.175.97.0	
London | eu-gb | LON04  |   158.175.97.167/29	|    158.175.97.160	
London | eu-gb | LON04  |   158.175.125.79/29	|    158.175.125.72	
London | eu-gb | LON05  |   141.125.69.63/27	  |  141.125.69.32	
London | eu-gb | LON05  |   141.125.71.15/28	  |  141.125.71.0	
London | eu-gb | LON05  |   141.125.83.127/26	|    141.125.83.64	
London | eu-gb | LON05  |   141.125.88.127/25	|    141.125.88.0	
London | eu-gb | LON05  |   141.125.93.255/24	|    141.125.93.0	
London | eu-gb | LON05  |   141.125.69.31/29	  |  141.125.69.24	
London | eu-gb | LON05  |   141.125.70.7/29	  |  141.125.70.0	
London | eu-gb | LON05  |   141.125.77.191/29	|    141.125.77.184	
London | eu-gb | LON05  |   141.125.85.87/29	  |  141.125.85.80	
London | eu-gb | LON05  |   141.125.87.55/29	  |  141.125.87.48	
London | eu-gb | LON05  |   141.125.98.103/29	|    141.125.98.96	
London | eu-gb | LON06   |  158.176.109.207/28  |  158.176.109.192	
London | eu-gb | LON06   |  158.176.109.255/27  |  158.176.109.224	
London | eu-gb | LON06   |  158.176.122.63/26	 |   158.176.122.0	
London | eu-gb | LON06   |  158.176.139.255/25  |  158.176.139.128	
London | eu-gb | LON06   |  158.176.148.255/24  |  158.176.148.0	
London | eu-gb | LON06   |  158.176.71.255/29	 |   158.176.71.248	
London | eu-gb | LON06   |  158.176.87.135/29	 |   158.176.87.128	
London | eu-gb | LON06   |  158.176.113.143/29  |  158.176.113.136	
London | eu-gb | LON06   |  158.176.122.239/29  |  158.176.122.232	
London | eu-gb | LON06   |  158.176.124.223/29  |  158.176.124.216	
London | eu-gb | LON06   |  158.176.131.15/29	 |   158.176.131.8	

### `kr-seo` List
{: #Seoul 1-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Seoul  | kr-seo	 | SEO01 | 169.56.80.143/28	 |   169.56.80.128	
Seoul  | kr-seo	 | SEO01 | 169.56.106.63/26	 |   169.56.106.0	
Seoul  | kr-seo	 | SEO01 | 169.56.120.127/27	 |   169.56.120.96	
Seoul  | kr-seo	 | SEO01 | 169.56.179.255/25	 |   169.56.179.128	
Seoul  | kr-seo	 | SEO01 | 169.56.67.239/29	 |   169.56.67.232	
Seoul  | kr-seo	 | SEO01 | 169.56.164.71/29	 |   169.56.164.64	

### `au-syd` List
{: #au-syd-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Sydney  | au-syd | SYD01 | 168.1.13.127/26	 |   168.1.13.64	
Sydney  | au-syd | SYD01 | 168.1.29.63/28	   | 168.1.29.48	
Sydney  | au-syd | SYD01 | 168.1.216.127/27	 |   168.1.216.96	
Sydney  | au-syd | SYD01 | 168.1.220.127/25	 |   168.1.220.0	
Sydney  | au-syd | SYD01 | 168.1.32.79/29	   | 168.1.32.72	
Sydney  | au-syd | SYD01 | 168.1.36.95/29	   | 168.1.36.88	
Sydney  | au-syd | SYD01 | 168.1.62.231/29	 |   168.1.62.224
Sydney  | au-syd | SYD04 | 130.198.102.63/26	|    130.198.102.0	
Sydney  | au-syd | SYD04 | 130.198.102.159/28 |   130.198.102.
Sydney  | au-syd | SYD04 | 130.198.102.191/27 |   130.198.102.
Sydney  | au-syd | SYD04 | 168.1.108.127/25	  |  168.1.108.0	
Sydney  | au-syd | SYD04 | 130.198.70.239/29	|    130.198.70.232	
Sydney  | au-syd | SYD04 | 130.198.93.135/29	|    130.198.93.128	
Sydney  | au-syd | SYD04 | 130.198.99.71/29	  |  130.198.99.64
Sydney  | au-syd | SYD05 | 135.90.68.111/28	 |   135.90.68.96	
Sydney  | au-syd | SYD05 | 135.90.69.127/27	 |   135.90.69.96	
Sydney  | au-syd | SYD05 | 135.90.83.63/26	 |   135.90.83.0	
Sydney  | au-syd | SYD05 | 135.90.95.127/25	 |   135.90.95.0	
Sydney  | au-syd | SYD05 | 135.90.67.31/29	 |   135.90.67.24
Sydney  | au-syd | SYD05 | 135.90.67.135/29	 |   135.90.67.128	
Sydney  | au-syd | SYD05 | 135.90.68.39/29	 |   135.90.68.32

### `jp-tok` List
{: #jp-tok-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Tokyo | jp-tok	 |  TOK02 |  161.202.140.191/27  |  161.202.140.160
Tokyo | jp-tok	 |  TOK02 |  169.56.7.255/26	   | 169.56.7.192
Tokyo | jp-tok	 |  TOK02 |  169.56.30.255/25	   | 169.56.30.128	
Tokyo | jp-tok	 |  TOK02 |  169.56.45.175/28	   | 169.56.45.160	
Tokyo | jp-tok	 |  TOK02 |  161.202.102.87/29	 |   161.202.102.80	
Tokyo | jp-tok	 |  TOK02 |  161.202.145.63/29	 |   161.202.145.56	
Tokyo | jp-tok	 |  TOK02 |  161.202.234.223/29  |  161.202.234.216
Tokyo | jp-tok	  | TOK04 |  128.168.72.63/27	   | 128.168.72.32	
Tokyo | jp-tok	  | TOK04 |  128.168.72.191/28	 |   128.168.72.176	
Tokyo | jp-tok	  | TOK04 |  128.168.93.127/26	 |   128.168.93.64	
Tokyo | jp-tok	  | TOK04 |  128.168.105.127/25  |  128.168.105.0
Tokyo | jp-tok	  | TOK04 |  128.168.69.79/29	   | 128.168.69.72	
Tokyo | jp-tok	  | TOK04 |  128.168.71.87/29	   | 128.168.71.80	
Tokyo | jp-tok	  | TOK04 |  128.168.71.95/29	   | 128.168.71.88	
Tokyo | jp-tok	  | TOK05 |  165.192.71.47/28	   | 165.192.71.32	
Tokyo | jp-tok	  | TOK05 |  165.192.71.127/27	 |   165.192.71.96	
Tokyo | jp-tok	  | TOK05 |  165.192.89.255/26	 |   165.192.89.192	
Tokyo | jp-tok	  | TOK05 |  165.192.102.255/25  |  165.192.102.128
Tokyo | jp-tok	  | TOK05 |  165.192.66.7/29	   | 165.192.66.0
Tokyo | jp-tok	  | TOK05 |  165.192.70.175/29	 |   165.192.70.168	
Tokyo | jp-tok	  | TOK05 |  165.192.71.239/29	 |   165.192.71.232	

### `jp-osa` List
{: #jp-osa-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Osaka 21  |  jp-osa	 | OSA21 | 163.68.68.127/28	 |   163.68.68.112	
Osaka 21  |  jp-osa	 | OSA21 | 163.68.73.127/27	 |   163.68.73.96	
Osaka 21  |  jp-osa	 | OSA21 | 163.68.67.119/29	 |   163.68.67.112	
Osaka 21  |  jp-osa	 | OSA21 | 163.68.70.63/29	 |   163.68.70.56
Osaka 22   | jp-osa	 | OSA22 | 163.69.65.111/28	 |   163.69.65.96	
Osaka 22   | jp-osa	 | OSA22 | 163.69.68.31/27	 |   163.69.68.0	
Osaka 22   | jp-osa	 | OSA22 | 163.69.65.55/29	 |   163.69.65.48
Osaka 22   | jp-osa	 | OSA22 | 163.69.65.63/29	 |   163.69.65.56
Osaka 23   | jp-osa	 | OSA23 | 163.73.65.175/28	  |  163.73.65.160	
Osaka 23   | jp-osa	 | OSA23 | 163.73.68.95/27	  |  163.73.68.64
Osaka 23   | jp-osa	 | OSA23 | 163.73.67.191/29	  |  163.73.67.184	
Osaka 23   | jp-osa	 | OSA23 | 163.73.67.231/29	  |  163.73.67.224	

### `us-east` List
{: #us-east-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Washington DC 04  |  us-east	| WDC04 | 52.116.78.127/25	  |  52.116.78.0
Washington DC 04  |  us-east	| WDC04 | 52.116.115.255/24	  |  52.116.115.0	
Washington DC 04  |  us-east	| WDC04 | 150.239.70.255/24	  |  150.239.70.0	
Washington DC 04  |  us-east	| WDC04 | 150.239.101.255/24  |  150.239.101.0
Washington DC 04  |  us-east	| WDC04 | 169.47.179.63/26	  |  169.47.179.0	
Washington DC 04  |  us-east	| WDC04 | 169.63.72.175/28	  |  169.63.72.160	
Washington DC 04  |  us-east	| WDC04 | 169.63.121.159/27	  |  169.63.121.128	
Washington DC 04  |  us-east	| WDC04 | 52.116.73.231/29	  |  52.116.73.224	
Washington DC 04  |  us-east	| WDC04 | 169.47.179.231/29	  |  169.47.179.224	
Washington DC 04  |  us-east	| WDC04 | 169.63.86.31/29	    |  169.63.86.24
Washington DC 04  |  us-east	| WDC04 | 169.63.111.119/29	  |  169.63.111.112	
Washington DC 04  |  us-east	| WDC04 | 169.63.121.55/29	  |  169.63.121.48	
Washington DC 04  |  us-east	| WDC04 | 169.63.121.63/29	  |  169.63.121.56	
Washington DC 04  |  us-east	| WDC04 | 169.63.123.167/29	  |  169.63.123.160	
Washington DC 04  |  us-east	| WDC04 | 169.63.125.223/29	  |  169.63.125.216	
Washington DC 06  |  us-east	| WDC06 | 169.59.138.255/24	  |  169.59.138.0	
Washington DC 06  |  us-east	| WDC06 | 169.59.144.255/24	  |  169.59.144.0	
Washington DC 06  |  us-east	| WDC06 | 169.59.158.255/24	  |  169.59.158.0	
Washington DC 06  |  us-east	| WDC06 | 169.63.128.191/27	  |  169.63.128.160	
Washington DC 06  |  us-east	| WDC06 | 169.63.135.191/28	  |  169.63.135.176	
Washington DC 06  |  us-east	| WDC06 | 169.63.139.255/26	  |  169.63.139.192	
Washington DC 06  |  us-east	| WDC06 | 169.63.172.127/25	  |  169.63.172.0	
Washington DC 06  |  us-east	| WDC06 | 169.59.145.239/29	  |  169.59.145.232	
Washington DC 06  |  us-east	| WDC06 | 169.60.65.55/29	    |  169.60.65.48
Washington DC 06  |  us-east	| WDC06 | 169.60.89.7/29	    |  169.60.89.0	
Washington DC 06  |  us-east	| WDC06 | 169.60.93.7/29	    |  169.60.93.0	
Washington DC 06  |  us-east	| WDC06 | 169.60.95.151/29	  |  169.60.95.144	
Washington DC 06  |  us-east	| WDC06 | 169.63.129.119/29	  |  169.63.129.112	
Washington DC 06  |  us-east	| WDC06 | 169.63.141.239/29	  |  169.63.141.232	
Washington DC 06  |  us-east	| WDC06 | 169.63.149.199/29	  |  169.63.149.192	
Washington DC 07  |  us-east	| WDC07 | 52.117.104.255/24	  |  52.117.104.0	
Washington DC 07  |  us-east	| WDC07 | 150.239.194.255/24  |  150.239.194.0
Washington DC 07  |  us-east	| WDC07 | 169.61.123.95/28	  |  169.61.123.80	
Washington DC 07  |  us-east	| WDC07 | 169.62.36.255/24	  |  169.62.36.0
Washington DC 07  |  us-east	| WDC07 | 169.62.42.63/27	    |  169.62.42.32
Washington DC 07  |  us-east	| WDC07 | 169.62.54.191/26	  |  169.62.54.128	
Washington DC 07  |  us-east	| WDC07 | 169.62.60.127/25	  |  169.62.60.0
Washington DC 07  |  us-east	| WDC07 | 52.117.76.47/29	    |  52.117.76.40
Washington DC 07  |  us-east	| WDC07 | 52.117.85.71/29	    |  52.117.85.64
Washington DC 07  |  us-east	| WDC07 | 169.61.73.231/29	  |  169.61.73.224	
Washington DC 07  |  us-east	| WDC07 | 169.61.95.15/29	    |  169.61.95.8	
Washington DC 07  |  us-east	| WDC07 | 169.61.113.39/29	  |  169.61.113.32	
Washington DC 07  |  us-east	| WDC07 | 169.61.113.47/29	  |  169.61.113.40	
Washington DC 07  |  us-east	| WDC07 | 169.61.122.159/29	  |  169.61.122.152	
Washington DC 07  |  us-east	| WDC07 | 169.62.6.87/29	    |  169.62.6.80	

### `eu-de` List
{: #eu-de-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Frankfurt |  eu-de | fra02    |     158.177.41.255/24  |   158.177.41.0       
Frankfurt |  eu-de | fra02    |     158.177.56.255/24  |   158.177.56.0     
Frankfurt |  eu-de | fra02    |     158.177.61.255/24  |   158.177.61.0     
Frankfurt |  eu-de | fra02    |      158.177.77.63/27  |   158.177.77.32     
Frankfurt |  eu-de | fra02    |     158.177.87.255/25  |   158.177.87.128     
Frankfurt |  eu-de | fra02    |     158.177.155.63/26  |   158.177.155.0     
Frankfurt |  eu-de | fra02    |     158.177.241.255/24 |   158.177.241.0     
Frankfurt |  eu-de | fra02    |     158.177.110.111/29 |   158.177.110.104     
Frankfurt |  eu-de | fra02    |     158.177.221.175/29 |   158.177.221.168     
Frankfurt |  eu-de | fra02    |      159.122.97.23/29  |   159.122.97.16     
Frankfurt |  eu-de | fra02    |      159.122.97.47/29  |   159.122.97.40     
Frankfurt |  eu-de | fra02    |     159.122.108.215/29 |   159.122.108.208     
Frankfurt |  eu-de | fra02    |     159.122.108.223/29 |   159.122.108.216     
Frankfurt |  eu-de | fra02    |      169.50.10.15/29   |   169.50.10.8     
Frankfurt |  eu-de | fra02    |      169.50.13.207/29  |   169.50.13.200     
Frankfurt |  eu-de | fra02    |      169.50.15.31/29   |   169.50.15.24     
Frankfurt |  eu-de | fra02    |      169.50.15.191/29  |   169.50.15.184     
Frankfurt |  eu-de | fra02    |      169.50.35.111/29  |   169.50.35.104     
Frankfurt |  eu-de | fra02    |      169.50.35.239/29  |   169.50.35.232     
Frankfurt |  eu-de | fra02    |      169.50.53.247/29  |   169.50.53.240     
Frankfurt |  eu-de | fra02    |      169.50.54.23/29   |   169.50.54.16     
Frankfurt |  eu-de | fra04    |      161.156.2.255/24  |   161.156.2.0     
Frankfurt |  eu-de | fra04    |     161.156.25.255/24  |   161.156.25.0     
Frankfurt |  eu-de | fra04    |     161.156.51.255/24  |   161.156.51.0     
Frankfurt |  eu-de | fra04    |     161.156.95.223/27  |   161.156.95.192     
Frankfurt |  eu-de | fra04    |      161.156.97.63/26  |   161.156.97.0     
Frankfurt |  eu-de | fra04    |     161.156.131.255/25 |   161.156.131.128     
Frankfurt |  eu-de | fra04    |     161.156.152.255/24 |   161.156.152.0     
Frankfurt |  eu-de | fra04    |      161.156.1.79/29   |   161.156.1.72     
Frankfurt |  eu-de | fra04    |      161.156.8.47/29   |   161.156.8.40     
Frankfurt |  eu-de | fra04    |     161.156.67.247/29  |   161.156.67.240     
Frankfurt |  eu-de | fra04    |     161.156.69.135/29  |   161.156.69.128     
Frankfurt |  eu-de | fra04    |     161.156.69.143/29  |   161.156.69.136     
Frankfurt |  eu-de | fra04    |     161.156.107.159/29 |   161.156.107.152     
Frankfurt |  eu-de | fra04    |     161.156.111.55/29  |   161.156.111.48     
Frankfurt |  eu-de | fra04    |     161.156.111.79/29  |   161.156.111.72     
Frankfurt |  eu-de | fra04    |     161.156.122.239/29 |   161.156.122.232     
Frankfurt |  eu-de | fra04    |     161.156.132.103/29 |   161.156.132.96     
Frankfurt |  eu-de | fra04    |     161.156.148.215/29 |   161.156.148.208     
Frankfurt |  eu-de | fra04    |     161.156.157.135/29 |   161.156.157.128     
Frankfurt |  eu-de | fra04    |     161.156.177.183/29 |   161.156.177.176     
Frankfurt |  eu-de | fra04    |     161.156.185.31/29  |   161.156.185.24     
Frankfurt |  eu-de | fra05    |      149.81.73.159/28  |   149.81.73.144     
Frankfurt |  eu-de | fra05    |      149.81.80.255/27  |   149.81.80.224     
Frankfurt |  eu-de | fra05    |      149.81.114.63/26  |   149.81.114.0     
Frankfurt |  eu-de | fra05    |     149.81.132.127/25  |   149.81.132.0     
Frankfurt |  eu-de | fra05    |     149.81.139.255/24  |   149.81.139.0     
Frankfurt |  eu-de | fra05    |     149.81.150.255/24  |   149.81.150.0     
Frankfurt |  eu-de | fra05    |     149.81.183.255/24  |   149.81.183.0     
Frankfurt |  eu-de | fra05    |     149.81.208.255/24  |   149.81.208.0     
Frankfurt |  eu-de | fra05    |      149.81.77.207/29  |   149.81.77.200     
Frankfurt |  eu-de | fra05    |      149.81.79.183/29  |   149.81.79.176     
Frankfurt |  eu-de | fra05    |      149.81.83.215/29  |   149.81.83.208     
Frankfurt |  eu-de | fra05    |      149.81.84.103/29  |   149.81.84.96     
Frankfurt |  eu-de | fra05    |      149.81.87.143/29  |   149.81.87.136     
Frankfurt |  eu-de | fra05    |      149.81.87.151/29  |   149.81.87.144     
Frankfurt |  eu-de | fra05    |      149.81.98.167/29  |   149.81.98.160     
Frankfurt |  eu-de | fra05    |     149.81.100.207/29  |   149.81.100.200     
Frankfurt |  eu-de | fra05    |     149.81.101.119/29  |   149.81.101.112     
Frankfurt |  eu-de | fra05    |     149.81.106.239/29  |   149.81.106.232     
Frankfurt |  eu-de | fra05    |      149.81.142.47/29  |   149.81.142.40     
Frankfurt |  eu-de | fra05    |      149.81.148.79/29  |   149.81.148.72     
Frankfurt |  eu-de | fra05    |     149.81.171.231/29  |   149.81.171.224     
Frankfurt |  eu-de | fra05    |     149.81.180.207/29  |   149.81.180.200

### `us-south` List
{: #us-south-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Dallas 10  | us-south	 | DAL10 |  2.116.167.255/24	  |  52.116.167.0
Dallas 10  | us-south	 | DAL10 |  2.116.179.175/28	  |  52.116.179.160
Dallas 10  | us-south	 | DAL10 |  2.116.190.63/26	  |  52.116.190.0	
Dallas 10  | us-south	 | DAL10 |  52.117.150.127/25	|    52.117.150.0	
Dallas 10  | us-south	 | DAL10 |  52.117.184.255/24	|    52.117.184.0	
Dallas 10  | us-south	 | DAL10 |  52.118.10.255/24	  |  52.118.10.0
Dallas 10  | us-south	 | DAL10 |  52.118.48.255/24	  |  52.118.48.0
Dallas 10  | us-south	 | DAL10 |  52.118.138.255/24	|    52.118.138.0	
Dallas 10  | us-south	 | DAL10 |  150.238.244.255/24	|150.238.244.0	
Dallas 10  | us-south	 | DAL10 |  150.239.46.255/24	|    150.239.46.0	
Dallas 10  | us-south	 | DAL10 |  150.239.63.255/24	|    150.239.63.0	
Dallas 10  | us-south	 | DAL10 |  169.46.57.31/27	  |  169.46.57.0	
Dallas 10  | us-south	 | DAL10 |  169.47.212.191/27	|    169.47.212.160	
Dallas 10  | us-south	 | DAL10 |  169.61.212.255/26	|    169.61.212.192	
Dallas 10  | us-south	 | DAL10 |  169.61.219.239/28	|    169.61.219.224	
Dallas 10  | us-south	 | DAL10 |  169.63.201.255/25	|    169.63.201.128	
Dallas 10  | us-south	 | DAL10 |  169.63.204.255/24	|    169.63.204.0	
Dallas 10  | us-south	 | DAL10 |  52.116.160.151/29	|    52.116.160.144	
Dallas 10  | us-south	 | DAL10 |  52.116.190.135/29	|    52.116.190.128	
Dallas 10  | us-south	 | DAL10 |  52.116.190.239/29	|    52.116.190.232	
Dallas 10  | us-south	 | DAL10 |  52.117.148.31/29	  |  52.117.148.24	
Dallas 10  | us-south	 | DAL10 |  52.117.166.239/29	|    52.117.166.232	
Dallas 10  | us-south	 | DAL10 |  52.118.41.103/29	  |  52.118.41.96	
Dallas 10  | us-south	 | DAL10 |  52.118.153.159/29	|    52.118.153.152	
Dallas 10  | us-south	 | DAL10 |  150.238.4.151/29	  |  150.238.4.144	
Dallas 10  | us-south	 | DAL10 |  150.238.229.39/29	|    150.238.229.32	
Dallas 10  | us-south	 | DAL10 |  150.238.247.167/29	|150.238.247.160	
Dallas 10  | us-south	 | DAL10 |  169.46.13.239/29	  |  169.46.13.232	
Dallas 10  | us-south	 | DAL10 |  169.46.17.87/29	  |  169.46.17.80	
Dallas 10  | us-south	 | DAL10 |  169.46.18.23/29	  |  169.46.18.16	
Dallas 10  | us-south	 | DAL10 |  169.46.21.175/29	  |  169.46.21.168	
Dallas 10  | us-south	 | DAL10 |  169.46.25.103/29	  |  169.46.25.96	
Dallas 10  | us-south	 | DAL10 |  169.46.31.175/29	  |  169.46.31.168	
Dallas 10  | us-south	 | DAL10 |  169.46.39.199/29	  |  169.46.39.192	
Dallas 10  | us-south	 | DAL10 |  169.46.40.7/29	    |169.46.40.0
Dallas 10  | us-south	 | DAL10 |  169.46.50.239/29	  |  169.46.50.232	
Dallas 10  | us-south	 | DAL10 |  169.46.51.63/29	  |  169.46.51.56	
Dallas 10  | us-south	 | DAL10 |  169.46.51.111/29	  |  169.46.51.104	
Dallas 10  | us-south	 | DAL10 |  169.46.65.191/29	  |  169.46.65.184	
Dallas 10  | us-south	 | DAL10 |  169.46.71.143/29	  |  169.46.71.136	
Dallas 10  | us-south	 | DAL10 |  169.46.78.15/29	  |  169.46.78.8	
Dallas 10  | us-south	 | DAL10 |  169.46.81.175/29	  |  169.46.81.168	
Dallas 10  | us-south	 | DAL10 |  169.46.91.55/29	  |  169.46.91.48	
Dallas 10  | us-south	 | DAL10 |  169.46.99.103/29	  |  169.46.99.96	
Dallas 10  | us-south	 | DAL10 |  169.46.99.175/29	  |  169.46.99.168	
Dallas 10  | us-south	 | DAL10 |  169.46.110.7/29	  |  169.46.110.0	
Dallas 10  | us-south	 | DAL10 |  169.46.120.183/29	|    169.46.120.176	
Dallas 10  | us-south	 | DAL10 |  169.46.121.215/29	|    169.46.121.208	
Dallas 10  | us-south	 | DAL10 |  169.47.194.95/29	  |  169.47.194.88	
Dallas 10  | us-south	 | DAL10 |  169.47.195.47/29	  |  169.47.195.40	
Dallas 10  | us-south	 | DAL10 |  169.47.195.111/29	|    169.47.195.104	
Dallas 10  | us-south	 | DAL10 |  169.47.197.207/29	|    169.47.197.200	
Dallas 10  | us-south	 | DAL10 |  169.47.205.31/29	  |  169.47.205.24	
Dallas 10  | us-south	 | DAL10 |  169.47.228.255/29	|    169.47.228.248	
Dallas 10  | us-south	 | DAL10 |  169.47.229.119/29	|    169.47.229.112	
Dallas 10  | us-south	 | DAL10 |  169.47.233.167/29	|    169.47.233.160	
Dallas 10  | us-south	 | DAL10 |  169.47.246.39/29	  |  169.47.246.32	
Dallas 10  | us-south	 | DAL10 |  169.47.252.135/29	|    169.47.252.128	
Dallas 10  | us-south	 | DAL10 |  169.48.135.79/29	  |  169.48.135.72	
Dallas 10  | us-south	 | DAL10 |  169.48.139.79/29	  |  169.48.139.72	
Dallas 10  | us-south	 | DAL10 |  169.48.140.143/29	|    169.48.140.136	
Dallas 10  | us-south	 | DAL10 |  169.48.161.199/29	|    169.48.161.192	
Dallas 10  | us-south	 | DAL10 |  169.48.163.135/29	|    169.48.163.128	
Dallas 10  | us-south	 | DAL10 |  169.48.164.151/29	|    169.48.164.144	
Dallas 10  | us-south	 | DAL10 |  169.48.171.87/29	  |  169.48.171.80	
Dallas 10  | us-south	 | DAL10 |  169.60.229.175/29	|    169.60.229.168	
Dallas 10  | us-south	 | DAL10 |  169.61.193.127/29	|    169.61.193.120	
Dallas 10  | us-south	 | DAL10 |  169.61.214.175/29	|    169.61.214.168	
Dallas 10  | us-south	 | DAL10 |  169.61.216.143/29	|    169.61.216.136	
Dallas 10  | us-south	 | DAL10 |  169.61.235.63/29	  |  169.61.235.56	
Dallas 10  | us-south	 | DAL10 |  169.63.194.159/29	|    169.63.194.152	
Dallas 10  | us-south	 | DAL10 |  169.63.195.39/29	  |  169.63.195.32	
Dallas 10  | us-south	 | DAL10 |  169.63.218.119/29	|    169.63.218.112	
Dallas 10  | us-south	 | DAL10 |  169.63.220.39/29	  |  169.63.220.32	
Dallas 12  | us-south	 | DAL12 |  50.22.135.255/24	  |   50.22.135.0	
Dallas 12  | us-south	 | DAL12 |  52.116.212.255/24	|     52.116.212.0	
Dallas 12  | us-south	 | DAL12 |  52.116.218.191/27	|     52.116.218.160	
Dallas 12  | us-south	 | DAL12 |  52.116.229.255/25	|     52.116.229.128	
Dallas 12  | us-south	 | DAL12 |  52.116.252.255/24	|     52.116.252.0	
Dallas 12  | us-south	 | DAL12 |  52.118.193.255/24	|     52.118.193.0	
Dallas 12  | us-south	 | DAL12 |  150.239.149.255/24	| 150.239.149.0	
Dallas 12  | us-south	 | DAL12 |  150.239.187.255/24	| 150.239.187.0	
Dallas 12  | us-south	 | DAL12 |  169.47.108.255/26	|     169.47.108.192	
Dallas 12  | us-south	 | DAL12 |  169.48.215.191/27	|     169.48.215.160	
Dallas 12  | us-south	 | DAL12 |  169.59.194.255/24	|     169.59.194.0	
Dallas 12  | us-south	 | DAL12 |  169.59.234.255/24	|     169.59.234.0	
Dallas 12  | us-south	 | DAL12 |  169.61.157.255/25	|     169.61.157.128	
Dallas 12  | us-south	 | DAL12 |  169.61.167.31/28	  |   169.61.167.16	
Dallas 12  | us-south	 | DAL12 |  169.61.169.63/28	  |   169.61.169.48	
Dallas 12  | us-south	 | DAL12 |  169.63.57.127/26	  |   169.63.57.64	
Dallas 12  | us-south	 | DAL12 |  52.116.244.119/29	|     52.116.244.112	
Dallas 12  | us-south	 | DAL12 |  169.47.101.7/29	  |   169.47.101.0	
Dallas 12  | us-south	 | DAL12 |  169.47.101.15/29	  |   169.47.101.8	
Dallas 12  | us-south	 | DAL12 |  169.47.101.63/29	  |   169.47.101.56	
Dallas 12  | us-south	 | DAL12 |  169.47.107.95/29	  |   169.47.107.88	
Dallas 12  | us-south	 | DAL12 |  169.47.107.151/29	|     169.47.107.144	
Dallas 12  | us-south	 | DAL12 |  169.47.109.87/29	  |   169.47.109.80	
Dallas 12  | us-south	 | DAL12 |  169.47.111.79/29	  |   169.47.111.72	
Dallas 12  | us-south	 | DAL12 |  169.47.113.223/29	|     169.47.113.216	
Dallas 12  | us-south	 | DAL12 |  169.47.124.95/29	  |   169.47.124.88	
Dallas 12  | us-south	 | DAL12 |  169.48.207.175/29	|     169.48.207.168	
Dallas 12  | us-south	 | DAL12 |  169.48.216.47/29	  |   169.48.216.40	
Dallas 12  | us-south	 | DAL12 |  169.48.218.143/29	|     169.48.218.136	
Dallas 12  | us-south	 | DAL12 |  169.48.222.135/29	|     169.48.222.128	
Dallas 12  | us-south	 | DAL12 |  169.48.236.183/29	|     169.48.236.176	
Dallas 12  | us-south	 | DAL12 |  169.48.240.199/29	|     169.48.240.192	
Dallas 12  | us-south	 | DAL12 |  169.48.241.167/29	|     169.48.241.160	
Dallas 12  | us-south	 | DAL12 |  169.59.255.119/29	|     169.59.255.112	
Dallas 12  | us-south	 | DAL12 |  169.61.133.223/29	|     169.61.133.216	
Dallas 12  | us-south	 | DAL12 |  169.61.136.175/29	|     169.61.136.168	
Dallas 12  | us-south	 | DAL12 |  169.61.139.79/29	  |   169.61.139.72	
Dallas 12  | us-south	 | DAL12 |  169.61.139.103/29	|     169.61.139.96	
Dallas 12  | us-south	 | DAL12 |  169.61.150.223/29	|     169.61.150.216	
Dallas 12  | us-south	 | DAL12 |  169.61.178.111/29	|     169.61.178.104	
Dallas 12  | us-south	 | DAL12 |  169.63.1.79/29	    | 169.63.1.72	
Dallas 12  | us-south	 | DAL12 |  169.63.2.79/29	    | 169.63.2.72	
Dallas 12  | us-south	 | DAL12 |  169.63.18.71/29	  |   169.63.18.64	
Dallas 12  | us-south	 | DAL12 |  169.63.21.175/29	  |   169.63.21.168	
Dallas 12  | us-south	 | DAL12 |  169.63.25.7/29	    | 169.63.25.0	
Dallas 12  | us-south	 | DAL12 |  169.63.26.15/29	  |   169.63.26.8	
Dallas 12  | us-south	 | DAL12 |  169.63.26.255/29	  |   169.63.26.248	
Dallas 12  | us-south	 | DAL12 |  169.63.27.7/29	    | 169.63.27.0	
Dallas 12  | us-south	 | DAL12 |  169.63.29.47/29	  |   169.63.29.40	
Dallas 12  | us-south	 | DAL12 |  169.63.47.87/29	  |   169.63.47.80	
Dallas 12  | us-south	 | DAL12 |  169.63.54.175/29	  |   169.63.54.168	
Dallas 12  | us-south	 | DAL12 |  169.63.55.143/29	  |   169.63.55.136	
Dallas 12  | us-south	 | DAL12 |  169.63.58.71/29	  |   169.63.58.64	
Dallas 12  | us-south	 | DAL12 |  169.63.58.79/29	  |   169.63.58.72	
Dallas 13  | us-south	 | DAL13 |  52.116.16.127/25	  |   52.116.16.0	
Dallas 13  | us-south	 | DAL13 |  52.116.24.63/27	  |   52.116.24.32	
Dallas 13  | us-south	 | DAL13 |  52.117.49.255/24	  |   52.117.49.0	
Dallas 13  | us-south	 | DAL13 |  52.117.198.191/26	|     52.117.198.128	
Dallas 13  | us-south	 | DAL13 |  52.117.202.255/25	|     52.117.202.128	
Dallas 13  | us-south	 | DAL13 |  52.117.205.255/24	|     52.117.205.0	
Dallas 13  | us-south	 | DAL13 |  52.117.230.255/24	|     52.117.230.0	
Dallas 13  | us-south	 | DAL13 |  52.117.235.255/24	|     52.117.235.0	
Dallas 13  | us-south	 | DAL13 |  52.117.254.255/24	|     52.117.254.0	
Dallas 13  | us-south	 | DAL13 |  67.228.229.255/24	|     67.228.229.0	
Dallas 13  | us-south	 | DAL13 |  67.228.234.255/24	|     67.228.234.0	
Dallas 13  | us-south	 | DAL13 |  150.238.107.255/24	| 150.238.107.0	
Dallas 13  | us-south	 | DAL13 |  150.238.113.255/24	| 150.238.113.0	
Dallas 13  | us-south	 | DAL13 |  169.48.76.63/27	  |   169.48.76.32	
Dallas 13  | us-south	 | DAL13 |  169.59.14.255/24	  |   169.59.14.0	
Dallas 13  | us-south	 | DAL13 |  169.61.32.159/29	  |   169.61.32.152	
Dallas 13  | us-south	 | DAL13 |  169.62.218.223/28	|     169.62.218.208	
Dallas 13  | us-south	 | DAL13 |  169.62.237.63/26	  |   169.62.237.0	
Dallas 13  | us-south	 | DAL13 |  52.116.19.183/29	  |   52.116.19.176	
Dallas 13  | us-south	 | DAL13 |  52.116.19.191/29	  |   52.116.19.184	
Dallas 13  | us-south	 | DAL13 |  52.116.25.247/29	  |   52.116.25.240	
Dallas 13  | us-south	 | DAL13 |  52.116.32.39/29	  |   52.116.32.32	
Dallas 13  | us-south	 | DAL13 |  52.116.54.239/29	  |   52.116.54.232	
Dallas 13  | us-south	 | DAL13 |  52.117.22.247/29	  |   52.117.22.240	
Dallas 13  | us-south	 | DAL13 |  52.117.23.143/29	  |   52.117.23.136	
Dallas 13  | us-south	 | DAL13 |  52.117.31.119/29	  |   52.117.31.112	
Dallas 13  | us-south	 | DAL13 |  52.117.35.231/29	  |   52.117.35.224	
Dallas 13  | us-south	 | DAL13 |  52.117.55.95/29	  |   52.117.55.88	
Dallas 13  | us-south	 | DAL13 |  52.117.55.119/29	  |   52.117.55.112	
Dallas 13  | us-south	 | DAL13 |  52.117.62.127/29	  |   52.117.62.120	
Dallas 13  | us-south	 | DAL13 |  52.117.234.183/29	|     52.117.234.176	
Dallas 13  | us-south	 | DAL13 |  150.238.100.247/29 |    150.238.100.240	
Dallas 13  | us-south	 | DAL13 |  169.48.71.167/29	  |   169.48.71.160	
Dallas 13  | us-south	 | DAL13 |  169.48.71.175/29	  |   169.48.71.168	
Dallas 13  | us-south	 | DAL13 |  169.48.78.95/29	  |   169.48.78.88	
Dallas 13  | us-south	 | DAL13 |  169.48.96.71/29	  |   169.48.96.64	
Dallas 13  | us-south	 | DAL13 |  169.48.98.199/29	  |   169.48.98.192	
Dallas 13  | us-south	 | DAL13 |  169.48.98.231/29	  |   169.48.98.224	
Dallas 13  | us-south	 | DAL13 |  169.48.99.119/29	  |   169.48.99.112	
Dallas 13  | us-south	 | DAL13 |  169.48.107.79/29	  |   169.48.107.72	
Dallas 13  | us-south	 | DAL13 |  169.48.114.247/29	|     169.48.114.240	
Dallas 13  | us-south	 | DAL13 |  169.48.123.151/29	|     169.48.123.144	
Dallas 13  | us-south	 | DAL13 |  169.59.10.199/29	  |   169.59.10.192	
Dallas 13  | us-south	 | DAL13 |  169.60.131.167/29	|     169.60.131.160	
Dallas 13  | us-south	 | DAL13 |  169.60.137.87/29	  |   169.60.137.80	
Dallas 13  | us-south	 | DAL13 |  169.60.138.223/29	|     169.60.138.216	
Dallas 13  | us-south	 | DAL13 |  169.60.150.239/29	|     169.60.150.232	
Dallas 13  | us-south	 | DAL13 |  169.60.159.183/29	|     169.60.159.176	
Dallas 13  | us-south	 | DAL13 |  169.60.164.31/29	  |   169.60.164.24	
Dallas 13  | us-south	 | DAL13 |  169.60.184.63/29	  |   169.60.184.56	
Dallas 13  | us-south	 | DAL13 |  169.61.23.199/29	  |   169.61.23.192	
Dallas 13  | us-south	 | DAL13 |  169.61.48.207/29	  |   169.61.48.200	
Dallas 13  | us-south	 | DAL13 |  169.61.48.239/29	  |   169.61.48.232	
Dallas 13  | us-south	 | DAL13 |  169.61.49.143/29	  |   169.61.49.136	
Dallas 13  | us-south	 | DAL13 |  169.61.56.223/29	  |   169.61.56.216	
Dallas 13  | us-south	 | DAL13 |  169.61.59.103/29	  |   169.61.59.96	
Dallas 13  | us-south	 | DAL13 |  169.61.60.39/29	  |   169.61.60.32	
Dallas 13  | us-south	 | DAL13 |  169.61.60.47/29	  |   169.61.60.40	
Dallas 13  | us-south	 | DAL13 |  169.62.134.103/29	|     169.62.134.96	
Dallas 13  | us-south	 | DAL13 |  169.62.151.47/29	  |   169.62.151.40	
Dallas 13  | us-south	 | DAL13 |  169.62.158.95/29	  |   169.62.158.88	
Dallas 13  | us-south	 | DAL13 |  169.62.184.207/29	|     169.62.184.200	
Dallas 13  | us-south	 | DAL13 |  169.62.187.159/29	|     169.62.187.152	
Dallas 13  | us-south	 | DAL13 |  169.62.193.183/29	|     169.62.193.176	
Dallas 13  | us-south	 | DAL13 |  169.62.239.47/29	  |   169.62.239.40	
Dallas 13  | us-south	 | DAL13 |  169.62.240.223/29	|     169.62.240.216	
Dallas 13  | us-south	 | DAL13 |  169.62.240.231/29	|     169.62.240.224	
Dallas 13  | us-south	 | DAL13 |  174.36.70.143/29	  |   174.36.70.136	