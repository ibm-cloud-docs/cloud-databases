---

copyright:
  years: 2019, 2022
lastupdated: "2022-05-31"

subcollection: cloud-databases

keywords: allowlist, ip addresses, blocklist, whitelist, cloud databases

---

{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:tip: .tip}
{:note: .note}

# Allowlisting
{: #allowlisting} 

To restrict access to your databases, you can allowlist specific IP addresses or ranges of IP addresses on your deployment.

If you use allowlists in your environment, you can allowlist our services by using the list of subnets for each region.

We updated documentation to reflect changes in terminology from `whitelist` to `allowlist`. You might encounter continued references to this former terminology while we work to implement these deeper changes to code, API, and CLI commands. 
{: .note}

Each deployment is limited 100 allowlist entries. 
{: .note}

## Using IP allowlists on your Deployment
{: #ip-allowlist} 

When you create an allowlist, only IP addresses that match the allowlist or are in the range of IP addresses in the allowlist can connect to your deployment. Allowlists can be enabled for both public endpoints and private endpoints. When no IP addresses are in the allowlist, the allowlist is disabled and the deployment accepts connections from any IP address.

Even if not explicitly allowlisted, {{site.data.keyword.cloud_notm}} management services are still able to connect.
{: .tip}

### Setting an allowlist
{: #set-allowlist} 

The UI for managing allowlists is on the _Settings_ tab of your _Deployment Overview_.

![Allowlist UI](images/settings-allowlist-ip.png){: caption="Figure 1. Deployment Overview tab" caption-side="bottom"}

#### IP addresses 
{: #set-allowlist-ip-addresses} 

The _IP_ field can take a single complete IPv4 address with or without a netmask. Without a netmask, incoming connections must come from exactly that IP address. To allow a connection from a specified range of IP addresses, use a netmask. The IP address must be fully specified. That means entering, for example, 192.168.1.0/24 rather than 192.168.1/24.

IPv6 is not currently supported.
{: tip}

#### Description
{: #set-allowlist-desc} 

The _Description_ can be any user-significant text for identifying the allowlist entry - a customer name, project identifier, or employee number, for example. The description field is required.

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

From the UI, remove an IP address or netmask from the allowlist by clicking _Remove_. You can also use CLI command is `cdb deployment-whitelist-delete` or send a `DELETE` request to the API endpoint. When all entries on the allowlist are removed, the allowlist is disabled and all IP addresses are accepted by your deployment.

## Allowlist {{site.data.keyword.databases-for}} in your Environment
{: #allowlist-ips}

If you use allowlists to control connections in your environment, you can use the following IP lists to allowlist {{site.data.keyword.databases-for}} deployments. We recommend you allowlist all of the subnet ranges for the _entire_ region that your deployments live in.

### `in-che` List
{: #che01-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Channai | in-che | che01 | 169.38.95.127/27  | 169.38.95.97         
Channai | in-che | che01 | 169.38.121.159/28 | 169.38.121.145          
Channai | in-che | che01 | 169.38.132.127/25 | 169.38.132.1          
Channai | in-che | che01 | 169.38.136.255/26 | 169.38.136.193          
Channai | in-che | che01 | 169.38.73.151/29  | 169.38.73.145         
Channai | in-che | che01 | 169.38.105.79/29  | 169.38.105.73 
         

### `ca-tor` List
{: #ca-tor-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Toronto | ca-tor | tor01  | 158.85.91.111/28  |  158.85.91.97    
Toronto | ca-tor | tor01  | 158.85.120.63/26  |  158.85.120.1    
Toronto | ca-tor | tor01  | 169.55.142.191/27 |  169.55.142.161     
Toronto | ca-tor | tor01  | 158.85.95.183/29  |  158.85.95.177    
Toronto | ca-tor | tor01  | 169.55.130.215/29 |  169.55.130.209     
Toronto | ca-tor | tor04  | 163.74.68.95/28   |  163.74.68.81    
Toronto | ca-tor | tor04  | 163.74.69.159/27  |  163.74.69.129    
Toronto | ca-tor | tor04  | 163.74.72.127/26  |  163.74.72.65    
Toronto | ca-tor | tor04  | 163.74.68.55/29   |  163.74.68.49    
Toronto | ca-tor | tor04  | 163.74.68.63/29   |  163.74.68.57    
Toronto | ca-tor | tor05  | 163.75.67.111/28  |  163.75.67.97    
Toronto | ca-tor | tor05  | 163.75.68.95/27   |  163.75.68.65    
Toronto | ca-tor | tor05  | 163.75.75.63/26   |  163.75.75.1    
Toronto | ca-tor | tor05  | 163.75.67.7/29    |  163.75.67.1   
Toronto | ca-tor | tor05  | 163.75.67.119/29  |  163.75.67.113

### `br-sao` List
{: #br-sao-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Sao Paolo | br-sao | sao01 | 169.57.154.239/28 | 169.57.154.225            
Sao Paolo | br-sao | sao01 | 169.57.191.63/26  | 169.57.191.1         
Sao Paolo | br-sao | sao01 | 169.57.225.127/27 | 169.57.225.97          
Sao Paolo | br-sao | sao01 | 169.57.167.95/29  | 169.57.167.89            
Sao Paolo | br-sao | sao01 | 169.57.199.23/29  | 169.57.199.17            
Sao Paolo | br-sao | sao04 | 163.107.67.63/28  | 163.107.67.49            
Sao Paolo | br-sao | sao04 | 163.107.69.63/27  | 163.107.69.33           
Sao Paolo | br-sao | sao04 | 163.107.72.127/26 | 163.107.72.65          
Sao Paolo | br-sao | sao04 | 163.107.68.87/29  | 163.107.68.81            
Sao Paolo | br-sao | sao04 | 163.107.68.95/29  | 163.107.68.89          
Sao Paolo | br-sao | sao05 | 163.109.68.63/26  | 163.109.68.1        
Sao Paolo | br-sao | sao05 | 163.109.68.95/27  | 163.109.68.65      
Sao Paolo | br-sao | sao05 | 163.109.68.175/28 | 163.109.68.161            
Sao Paolo | br-sao | sao05 | 163.109.65.119/29 | 163.109.65.113            
Sao Paolo | br-sao | sao05 | 163.109.65.127/29 | 163.109.65.121   

### `eu-gb` List
{: #eu-gb-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
London | eu-gb | lon04 |   158.175.64.95/28  | 158.175.64.81
London | eu-gb | lon04 |  158.175.139.191/27 | 158.175.139.161
London | eu-gb | lon04 |  158.175.147.63/26  | 158.175.147.1
London | eu-gb | lon04 |  158.175.151.127/25 | 158.175.151.1
London | eu-gb | lon04 |  158.175.156.255/24 | 158.175.156.1
London | eu-gb | lon04 |  158.175.81.111/29  | 158.175.81.105
London | eu-gb | lon04 |  158.175.91.151/29  | 158.175.91.145
London | eu-gb | lon04 |  158.175.92.175/29  | 158.175.92.169
London | eu-gb | lon04 |   158.175.97.7/29   | 158.175.97.1
London | eu-gb | lon04 |  158.175.97.167/29  | 158.175.97.161
London | eu-gb | lon04 |  158.175.125.79/29  | 158.175.125.73
London | eu-gb | lon05 |   141.125.69.63/27  | 141.125.69.33
London | eu-gb | lon05 |   141.125.71.15/28  | 141.125.71.1
London | eu-gb | lon05 |  141.125.83.127/26  | 141.125.83.65
London | eu-gb | lon05 |  141.125.88.127/25  | 141.125.88.1
London | eu-gb | lon05 |  141.125.93.255/24  | 141.125.93.1
London | eu-gb | lon05 |   141.125.69.31/29  | 141.125.69.25
London | eu-gb | lon05 |   141.125.70.7/29   | 141.125.70.1
London | eu-gb | lon05 |  141.125.77.191/29  | 141.125.77.185
London | eu-gb | lon05 |   141.125.85.87/29  | 141.125.85.81
London | eu-gb | lon05 |   141.125.87.55/29  | 141.125.87.49
London | eu-gb | lon05 |  141.125.98.103/29  | 141.125.98.97
London | eu-gb | lon06 |  158.176.109.207/28 | 158.176.109.193
London | eu-gb | lon06 |  158.176.109.255/27 | 158.176.109.225
London | eu-gb | lon06 |  158.176.122.63/26  | 158.176.122.1
London | eu-gb | lon06 |  158.176.139.255/25 | 158.176.139.129
London | eu-gb | lon06 |  158.176.148.255/24 | 158.176.148.1
London | eu-gb | lon06 |  158.176.71.255/29  | 158.176.71.249
London | eu-gb | lon06 |  158.176.87.135/29  | 158.176.87.129
London | eu-gb | lon06 |  158.176.113.143/29 | 158.176.113.137
London | eu-gb | lon06 |  158.176.122.239/29 | 158.176.122.233
London | eu-gb | lon06 |  158.176.124.223/29 | 158.176.124.217
London | eu-gb | lon06 |  158.176.131.15/29  | 158.176.131.9

### `kr-seo` List
{: #Seoul 1-list} 

`SEO01` Data Center is scheduled to close on 28 October 2022. For more information (including recommended data centers to which you can migrate), see [Migrating resources to a different data center](/docs/cloud-databases?topic=cloud-databases-migrate-data-center).
{: .important}

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Seoul | kr-seo | seo01 | 169.56.80.143/28  | 169.56.80.129       
Seoul | kr-seo | seo01 | 169.56.106.63/26  | 169.56.106.1       
Seoul | kr-seo | seo01 | 169.56.120.127/27 | 169.56.120.97        
Seoul | kr-seo | seo01 | 169.56.179.255/25 | 169.56.179.129        
Seoul | kr-seo | seo01 | 169.56.67.239/29  | 169.56.67.233       
Seoul | kr-seo | seo01 | 169.56.164.71/29  | 169.56.164.65

### `au-syd` List
{: #au-syd-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Sydney | au-syd | syd01 |  168.1.13.127/26   | 168.1.13.65         
Sydney | au-syd | syd01 |   168.1.29.63/28   | 168.1.29.49         
Sydney | au-syd | syd01 |  168.1.216.127/27  | 168.1.216.97         
Sydney | au-syd | syd01 |  168.1.220.127/25  | 168.1.220.1         
Sydney | au-syd | syd01 |   168.1.32.79/29   | 168.1.32.73         
Sydney | au-syd | syd01 |   168.1.36.95/29   | 168.1.36.89         
Sydney | au-syd | syd01 |  168.1.62.231/29   | 168.1.62.225         
Sydney | au-syd | syd04 | 130.198.102.63/26  | 130.198.102.1         
Sydney | au-syd | syd04 | 130.198.102.159/28 | 130.198.102.145         
Sydney | au-syd | syd04 | 130.198.102.191/27 | 130.198.102.161         
Sydney | au-syd | syd04 |  168.1.108.127/25  | 168.1.108.1         
Sydney | au-syd | syd04 | 130.198.70.239/29  | 130.198.70.233         
Sydney | au-syd | syd04 | 130.198.93.135/29  | 130.198.93.129         
Sydney | au-syd | syd04 |  130.198.99.71/29  | 130.198.99.65         
Sydney | au-syd | syd05 |  135.90.68.111/28  | 135.90.68.97         
Sydney | au-syd | syd05 |  135.90.69.127/27  | 135.90.69.97         
Sydney | au-syd | syd05 |  135.90.83.63/26   | 135.90.83.1         
Sydney | au-syd | syd05 |  135.90.95.127/25  | 135.90.95.1         
Sydney | au-syd | syd05 |  135.90.67.31/29   | 135.90.67.25         
Sydney | au-syd | syd05 |  135.90.67.135/29  | 135.90.67.129         
Sydney | au-syd | syd05 |  135.90.68.39/29   | 135.90.68.33

### `jp-tok` List
{: #jp-tok-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Tokyo | jp-tok | tok02 | 161.202.140.191/27 | 161.202.140.161        
Tokyo | jp-tok | tok02 |  169.56.7.255/26   | 169.56.7.193        
Tokyo | jp-tok | tok02 |  169.56.30.255/25  | 169.56.30.129        
Tokyo | jp-tok | tok02 |  169.56.45.175/28  | 169.56.45.161        
Tokyo | jp-tok | tok02 | 161.202.102.87/29  | 161.202.102.81        
Tokyo | jp-tok | tok02 | 161.202.145.63/29  | 161.202.145.57        
Tokyo | jp-tok | tok02 | 161.202.234.223/29 | 161.202.234.217        
Tokyo | jp-tok | tok02 | 161.202.239.191/29 | 161.202.239.185        
Tokyo | jp-tok | tok04 |  128.168.72.63/27  | 128.168.72.33        
Tokyo | jp-tok | tok04 | 128.168.72.191/28  | 128.168.72.177        
Tokyo | jp-tok | tok04 | 128.168.93.127/26  | 128.168.93.65        
Tokyo | jp-tok | tok04 | 128.168.105.127/25 | 128.168.105.1        
Tokyo | jp-tok | tok04 |  128.168.69.79/29  | 128.168.69.73        
Tokyo | jp-tok | tok04 |  128.168.71.87/29  | 128.168.71.81        
Tokyo | jp-tok | tok04 |  128.168.71.95/29  | 128.168.71.89        
Tokyo | jp-tok | tok04 | 128.168.111.87/29  | 128.168.111.81        
Tokyo | jp-tok | tok05 |  165.192.71.47/28  | 165.192.71.33        
Tokyo | jp-tok | tok05 | 165.192.71.127/27  | 165.192.71.97        
Tokyo | jp-tok | tok05 | 165.192.89.255/26  | 165.192.89.193        
Tokyo | jp-tok | tok05 | 165.192.102.255/25 | 165.192.102.129        
Tokyo | jp-tok | tok05 |  165.192.66.7/29   | 165.192.66.1        
Tokyo | jp-tok | tok05 | 165.192.70.175/29  | 165.192.70.169        
Tokyo | jp-tok | tok05 | 165.192.71.239/29  | 165.192.71.233        
Tokyo | jp-tok | tok05 | 165.192.148.63/29  | 165.192.148.57

Tokyo | jp-tok | tok02 | 161.202.140.191/27 | 161.202.140.161         
Tokyo | jp-tok | tok02 |  169.56.7.255/26   | 169.56.7.193         
Tokyo | jp-tok | tok02 |  169.56.30.255/25  | 169.56.30.129         
Tokyo | jp-tok | tok02 |  169.56.31.255/24  | 169.56.31.1         
Tokyo | jp-tok | tok02 |  169.56.45.175/28  | 169.56.45.161         
Tokyo | jp-tok | tok02 | 161.202.102.87/29  | 161.202.102.81         
Tokyo | jp-tok | tok02 | 161.202.145.63/29  | 161.202.145.57         
Tokyo | jp-tok | tok02 | 161.202.234.223/29 | 161.202.234.217         
Tokyo | jp-tok | tok02 | 161.202.239.191/29 | 161.202.239.185         
Tokyo | jp-tok | tok04 |  128.168.72.63/27  | 128.168.72.33         
Tokyo | jp-tok | tok04 | 128.168.72.191/28  | 128.168.72.177         
Tokyo | jp-tok | tok04 | 128.168.93.127/26  | 128.168.93.65         
Tokyo | jp-tok | tok04 | 128.168.105.127/25 | 128.168.105.1         
Tokyo | jp-tok | tok04 |  128.168.69.79/29  | 128.168.69.73         
Tokyo | jp-tok | tok04 |  128.168.71.87/29  | 128.168.71.81         
Tokyo | jp-tok | tok04 |  128.168.71.95/29  | 128.168.71.89         
Tokyo | jp-tok | tok04 | 128.168.111.87/29  | 128.168.111.81         
Tokyo | jp-tok | tok05 |  165.192.71.47/28  | 165.192.71.33         
Tokyo | jp-tok | tok05 | 165.192.71.127/27  | 165.192.71.97         
Tokyo | jp-tok | tok05 | 165.192.89.255/26  | 165.192.89.193         
Tokyo | jp-tok | tok05 | 165.192.102.255/25 | 165.192.102.129         
Tokyo | jp-tok | tok05 | 165.192.157.255/24 | 165.192.157.1         
Tokyo | jp-tok | tok05 |  165.192.66.7/29   | 165.192.66.1         
Tokyo | jp-tok | tok05 | 165.192.70.175/29  | 165.192.70.169         
Tokyo | jp-tok | tok05 | 165.192.71.239/29  | 165.192.71.233         
Tokyo | jp-tok | tok05 | 165.192.148.63/29  | 165.192.148.57

### `jp-osa` List
{: #jp-osa-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Osaka | jp-osa | osa21 | 163.68.68.127/28 | 163.68.68.113         
Osaka | jp-osa | osa21 | 163.68.73.127/27 | 163.68.73.97         
Osaka | jp-osa | osa21 | 163.68.96.191/26 | 163.68.96.129         
Osaka | jp-osa | osa21 | 163.68.67.119/29 | 163.68.67.113         
Osaka | jp-osa | osa21 | 163.68.70.63/29  | 163.68.70.57         
Osaka | jp-osa | osa22 | 163.69.65.111/28 | 163.69.65.97         
Osaka | jp-osa | osa22 | 163.69.68.31/27  | 163.69.68.1         
Osaka | jp-osa | osa22 | 163.69.71.255/26 | 163.69.71.193         
Osaka | jp-osa | osa22 | 163.69.65.55/29  | 163.69.65.49         
Osaka | jp-osa | osa22 | 163.69.65.63/29  | 163.69.65.57         
Osaka | jp-osa | osa23 | 163.73.65.175/28 | 163.73.65.161         
Osaka | jp-osa | osa23 | 163.73.68.95/27  | 163.73.68.65         
Osaka | jp-osa | osa23 | 163.73.71.63/26  | 163.73.71.1         
Osaka | jp-osa | osa23 | 163.73.67.191/29 | 163.73.67.185         
Osaka | jp-osa | osa23 | 163.73.67.231/29 | 163.73.67.225

### `us-east` List
{: #us-east-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Washington DC | us-east | wdc04 |  52.116.78.127/25  | 52.116.78.1         
Washington DC | us-east | wdc04 | 52.116.115.255/24  | 52.116.115.1         
Washington DC | us-east | wdc04 | 150.239.70.255/24  | 150.239.70.1         
Washington DC | us-east | wdc04 | 150.239.101.255/24 | 150.239.101.1         
Washington DC | us-east | wdc04 |  169.47.179.63/26  | 169.47.179.1         
Washington DC | us-east | wdc04 |  169.63.72.175/28  | 169.63.72.161         
Washington DC | us-east | wdc04 | 169.63.121.159/27  | 169.63.121.129         
Washington DC | us-east | wdc04 |  52.116.73.231/29  | 52.116.73.225         
Washington DC | us-east | wdc04 | 169.47.179.231/29  | 169.47.179.225         
Washington DC | us-east | wdc04 |  169.63.86.31/29   | 169.63.86.25         
Washington DC | us-east | wdc04 | 169.63.111.119/29  | 169.63.111.113         
Washington DC | us-east | wdc04 |  169.63.121.55/29  | 169.63.121.49         
Washington DC | us-east | wdc04 |  169.63.121.63/29  | 169.63.121.57         
Washington DC | us-east | wdc04 | 169.63.123.167/29  | 169.63.123.161         
Washington DC | us-east | wdc04 | 169.63.125.223/29  | 169.63.125.217         
Washington DC | us-east | wdc06 | 169.59.138.255/24  | 169.59.138.1         
Washington DC | us-east | wdc06 | 169.59.144.255/24  | 169.59.144.1         
Washington DC | us-east | wdc06 | 169.59.158.255/24  | 169.59.158.1         
Washington DC | us-east | wdc06 | 169.63.128.191/27  | 169.63.128.161         
Washington DC | us-east | wdc06 | 169.63.135.191/28  | 169.63.135.177         
Washington DC | us-east | wdc06 | 169.63.139.255/26  | 169.63.139.193         
Washington DC | us-east | wdc06 | 169.63.172.127/25  | 169.63.172.1         
Washington DC | us-east | wdc06 | 169.59.145.239/29  | 169.59.145.233         
Washington DC | us-east | wdc06 |  169.60.65.55/29   | 169.60.65.49         
Washington DC | us-east | wdc06 |   169.60.89.7/29   | 169.60.89.1         
Washington DC | us-east | wdc06 |   169.60.93.7/29   | 169.60.93.1         
Washington DC | us-east | wdc06 |  169.60.95.151/29  | 169.60.95.145         
Washington DC | us-east | wdc06 | 169.63.129.119/29  | 169.63.129.113         
Washington DC | us-east | wdc06 | 169.63.141.239/29  | 169.63.141.233         
Washington DC | us-east | wdc06 | 169.63.149.199/29  | 169.63.149.193         
Washington DC | us-east | wdc07 | 52.117.104.255/24  | 52.117.104.1         
Washington DC | us-east | wdc07 | 150.239.194.255/24 | 150.239.194.1         
Washington DC | us-east | wdc07 |  169.61.123.95/28  | 169.61.123.81         
Washington DC | us-east | wdc07 |  169.62.36.255/24  | 169.62.36.1         
Washington DC | us-east | wdc07 |  169.62.42.63/27   | 169.62.42.33         
Washington DC | us-east | wdc07 |  169.62.54.191/26  | 169.62.54.129         
Washington DC | us-east | wdc07 |  169.62.60.127/25  | 169.62.60.1         
Washington DC | us-east | wdc07 |  52.117.76.47/29   | 52.117.76.41         
Washington DC | us-east | wdc07 |  52.117.85.71/29   | 52.117.85.65         
Washington DC | us-east | wdc07 |  169.61.73.231/29  | 169.61.73.225         
Washington DC | us-east | wdc07 |  169.61.95.15/29   | 169.61.95.9         
Washington DC | us-east | wdc07 |  169.61.113.39/29  | 169.61.113.33         
Washington DC | us-east | wdc07 |  169.61.113.47/29  | 169.61.113.41         
Washington DC | us-east | wdc07 | 169.61.122.159/29  | 169.61.122.153         
Washington DC | us-east | wdc07 |   169.62.6.87/29   | 169.62.6.81

### `eu-de` List
{: #eu-de-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Frankfurt | eu-de | fra02 | 158.177.41.255/24  | 158.177.41.1        
Frankfurt | eu-de | fra02 | 158.177.56.255/24  | 158.177.56.1        
Frankfurt | eu-de | fra02 | 158.177.61.255/24  | 158.177.61.1        
Frankfurt | eu-de | fra02 |  158.177.77.63/27  | 158.177.77.33        
Frankfurt | eu-de | fra02 | 158.177.87.255/25  | 158.177.87.129        
Frankfurt | eu-de | fra02 | 158.177.155.63/26  | 158.177.155.1        
Frankfurt | eu-de | fra02 | 158.177.241.255/24 | 158.177.241.1        
Frankfurt | eu-de | fra02 | 158.177.110.111/29 | 158.177.110.105        
Frankfurt | eu-de | fra02 | 158.177.221.175/29 | 158.177.221.169        
Frankfurt | eu-de | fra02 |  159.122.97.23/29  | 159.122.97.17        
Frankfurt | eu-de | fra02 |  159.122.97.47/29  | 159.122.97.41        
Frankfurt | eu-de | fra02 | 159.122.108.215/29 | 159.122.108.209        
Frankfurt | eu-de | fra02 | 159.122.108.223/29 | 159.122.108.217        
Frankfurt | eu-de | fra02 |  169.50.10.15/29   | 169.50.10.9        
Frankfurt | eu-de | fra02 |  169.50.13.207/29  | 169.50.13.201        
Frankfurt | eu-de | fra02 |  169.50.15.31/29   | 169.50.15.25        
Frankfurt | eu-de | fra02 |  169.50.15.191/29  | 169.50.15.185        
Frankfurt | eu-de | fra02 |  169.50.35.111/29  | 169.50.35.105        
Frankfurt | eu-de | fra02 |  169.50.35.239/29  | 169.50.35.233        
Frankfurt | eu-de | fra02 |  169.50.53.247/29  | 169.50.53.241        
Frankfurt | eu-de | fra02 |  169.50.54.23/29   | 169.50.54.17        
Frankfurt | eu-de | fra04 |  161.156.2.255/24  | 161.156.2.1        
Frankfurt | eu-de | fra04 | 161.156.25.255/24  | 161.156.25.1        
Frankfurt | eu-de | fra04 | 161.156.51.255/24  | 161.156.51.1        
Frankfurt | eu-de | fra04 | 161.156.95.223/27  | 161.156.95.193        
Frankfurt | eu-de | fra04 |  161.156.97.63/26  | 161.156.97.1        
Frankfurt | eu-de | fra04 | 161.156.131.255/25 | 161.156.131.129        
Frankfurt | eu-de | fra04 | 161.156.152.255/24 | 161.156.152.1        
Frankfurt | eu-de | fra04 |  161.156.1.79/29   | 161.156.1.73        
Frankfurt | eu-de | fra04 |  161.156.8.47/29   | 161.156.8.41        
Frankfurt | eu-de | fra04 | 161.156.67.247/29  | 161.156.67.241        
Frankfurt | eu-de | fra04 | 161.156.69.135/29  | 161.156.69.129        
Frankfurt | eu-de | fra04 | 161.156.69.143/29  | 161.156.69.137        
Frankfurt | eu-de | fra04 | 161.156.107.159/29 | 161.156.107.153        
Frankfurt | eu-de | fra04 | 161.156.111.55/29  | 161.156.111.49        
Frankfurt | eu-de | fra04 | 161.156.111.79/29  | 161.156.111.73        
Frankfurt | eu-de | fra04 | 161.156.122.239/29 | 161.156.122.233        
Frankfurt | eu-de | fra04 | 161.156.132.103/29 | 161.156.132.97        
Frankfurt | eu-de | fra04 | 161.156.148.215/29 | 161.156.148.209        
Frankfurt | eu-de | fra04 | 161.156.157.135/29 | 161.156.157.129        
Frankfurt | eu-de | fra04 | 161.156.177.183/29 | 161.156.177.177        
Frankfurt | eu-de | fra04 | 161.156.185.31/29  | 161.156.185.25        
Frankfurt | eu-de | fra05 |  149.81.73.159/28  | 149.81.73.145        
Frankfurt | eu-de | fra05 |  149.81.80.255/27  | 149.81.80.225        
Frankfurt | eu-de | fra05 |  149.81.114.63/26  | 149.81.114.1        
Frankfurt | eu-de | fra05 | 149.81.132.127/25  | 149.81.132.1        
Frankfurt | eu-de | fra05 | 149.81.139.255/24  | 149.81.139.1        
Frankfurt | eu-de | fra05 | 149.81.150.255/24  | 149.81.150.1        
Frankfurt | eu-de | fra05 | 149.81.183.255/24  | 149.81.183.1        
Frankfurt | eu-de | fra05 | 149.81.208.255/24  | 149.81.208.1        
Frankfurt | eu-de | fra05 |  149.81.77.207/29  | 149.81.77.201        
Frankfurt | eu-de | fra05 |  149.81.79.183/29  | 149.81.79.177        
Frankfurt | eu-de | fra05 |  149.81.83.215/29  | 149.81.83.209        
Frankfurt | eu-de | fra05 |  149.81.84.103/29  | 149.81.84.97        
Frankfurt | eu-de | fra05 |  149.81.87.143/29  | 149.81.87.137        
Frankfurt | eu-de | fra05 |  149.81.87.151/29  | 149.81.87.145        
Frankfurt | eu-de | fra05 |  149.81.98.167/29  | 149.81.98.161        
Frankfurt | eu-de | fra05 | 149.81.100.207/29  | 149.81.100.201        
Frankfurt | eu-de | fra05 | 149.81.101.119/29  | 149.81.101.113        
Frankfurt | eu-de | fra05 | 149.81.106.239/29  | 149.81.106.233        
Frankfurt | eu-de | fra05 |  149.81.142.47/29  | 149.81.142.41        
Frankfurt | eu-de | fra05 |  149.81.148.79/29  | 149.81.148.73        
Frankfurt | eu-de | fra05 | 149.81.171.231/29  | 149.81.171.225        
Frankfurt | eu-de | fra05 | 149.81.180.207/29  | 149.81.180.201  
Paris | eu-de | par01 | 159.8.70.111/28  | 159.8.70.97        
Paris | eu-de | par01 | 159.8.90.127/26  | 159.8.90.65        
Paris | eu-de | par01 | 159.8.114.127/27 | 159.8.114.97        
Paris | eu-de | par01 | 159.8.78.239/29  | 159.8.78.233        
Paris | eu-de | par01 |  159.8.94.95/29  | 159.8.94.89 

### `us-south` List
{: #us-south-list} 

Location | Region | Data center | Subnet | First IP
-- | -- | -- | -- | --
Dallas | us-south | dal10  | 52.116.167.255/24  | 52.116.167.1         
Dallas | us-south | dal10  | 52.116.179.175/28  | 52.116.179.161         
Dallas | us-south | dal10  |  52.116.190.63/26  | 52.116.190.1         
Dallas | us-south | dal10  | 52.117.150.127/25  | 52.117.150.1         
Dallas | us-south | dal10  | 52.117.184.255/24  | 52.117.184.1         
Dallas | us-south | dal10  |  52.118.10.255/24  | 52.118.10.1         
Dallas | us-south | dal10  |  52.118.48.255/24  | 52.118.48.1         
Dallas | us-south | dal10  | 52.118.138.255/24  | 52.118.138.1         
Dallas | us-south | dal10  | 150.238.244.255/24 | 150.238.244.1         
Dallas | us-south | dal10  | 150.239.46.255/24  | 150.239.46.1         
Dallas | us-south | dal10  | 150.239.63.255/24  | 150.239.63.1         
Dallas | us-south | dal10  |  169.46.57.31/27   | 169.46.57.1         
Dallas | us-south | dal10  | 169.47.212.191/27  | 169.47.212.161         
Dallas | us-south | dal10  | 169.61.212.255/26  | 169.61.212.193         
Dallas | us-south | dal10  | 169.61.219.239/28  | 169.61.219.225         
Dallas | us-south | dal10  | 169.63.201.255/25  | 169.63.201.129         
Dallas | us-south | dal10  | 169.63.204.255/24  | 169.63.204.1         
Dallas | us-south | dal10  | 52.116.160.151/29  | 52.116.160.145         
Dallas | us-south | dal10  | 52.116.190.135/29  | 52.116.190.129         
Dallas | us-south | dal10  | 52.116.190.239/29  | 52.116.190.233         
Dallas | us-south | dal10  |  52.117.148.31/29  | 52.117.148.25         
Dallas | us-south | dal10  | 52.117.166.239/29  | 52.117.166.233         
Dallas | us-south | dal10  |  52.118.41.103/29  | 52.118.41.97         
Dallas | us-south | dal10  | 52.118.153.159/29  | 52.118.153.153         
Dallas | us-south | dal10  |  150.238.4.151/29  | 150.238.4.145         
Dallas | us-south | dal10  | 150.238.229.39/29  | 150.238.229.33         
Dallas | us-south | dal10  | 150.238.247.167/29 | 150.238.247.161         
Dallas | us-south | dal10  |  169.46.13.239/29  | 169.46.13.233         
Dallas | us-south | dal10  |  169.46.17.87/29   | 169.46.17.81         
Dallas | us-south | dal10  |  169.46.18.23/29   | 169.46.18.17         
Dallas | us-south | dal10  |  169.46.21.175/29  | 169.46.21.169         
Dallas | us-south | dal10  |  169.46.25.103/29  | 169.46.25.97         
Dallas | us-south | dal10  |  169.46.31.175/29  | 169.46.31.169         
Dallas | us-south | dal10  |  169.46.39.199/29  | 169.46.39.193         
Dallas | us-south | dal10  |   169.46.40.7/29   | 169.46.40.1         
Dallas | us-south | dal10  |  169.46.42.215/29  | 169.46.42.209         
Dallas | us-south | dal10  |  169.46.50.239/29  | 169.46.50.233         
Dallas | us-south | dal10  |  169.46.51.63/29   | 169.46.51.57         
Dallas | us-south | dal10  |  169.46.51.111/29  | 169.46.51.105         
Dallas | us-south | dal10  |  169.46.60.23/29   | 169.46.60.17         
Dallas | us-south | dal10  |  169.46.65.191/29  | 169.46.65.185         
Dallas | us-south | dal10  |  169.46.71.143/29  | 169.46.71.137         
Dallas | us-south | dal10  |  169.46.76.71/29   | 169.46.76.65         
Dallas | us-south | dal10  |  169.46.78.15/29   | 169.46.78.9         
Dallas | us-south | dal10  |  169.46.81.175/29  | 169.46.81.169         
Dallas | us-south | dal10  |  169.46.91.55/29   | 169.46.91.49         
Dallas | us-south | dal10  |  169.46.99.103/29  | 169.46.99.97         
Dallas | us-south | dal10  |  169.46.99.175/29  | 169.46.99.169         
Dallas | us-south | dal10  |  169.46.110.7/29   | 169.46.110.1         
Dallas | us-south | dal10  | 169.46.120.183/29  | 169.46.120.177         
Dallas | us-south | dal10  | 169.46.121.215/29  | 169.46.121.209         
Dallas | us-south | dal10  |  169.47.193.79/29  | 169.47.193.73         
Dallas | us-south | dal10  |  169.47.194.95/29  | 169.47.194.89         
Dallas | us-south | dal10  |  169.47.195.47/29  | 169.47.195.41         
Dallas | us-south | dal10  | 169.47.195.111/29  | 169.47.195.105         
Dallas | us-south | dal10  | 169.47.197.207/29  | 169.47.197.201         
Dallas | us-south | dal10  | 169.47.203.167/29  | 169.47.203.161         
Dallas | us-south | dal10  |  169.47.205.31/29  | 169.47.205.25         
Dallas | us-south | dal10  | 169.47.228.255/29  | 169.47.228.249         
Dallas | us-south | dal10  | 169.47.229.119/29  | 169.47.229.113         
Dallas | us-south | dal10  | 169.47.233.167/29  | 169.47.233.161         
Dallas | us-south | dal10  |  169.47.246.39/29  | 169.47.246.33         
Dallas | us-south | dal10  |  169.47.251.87/29  | 169.47.251.81         
Dallas | us-south | dal10  | 169.47.252.135/29  | 169.47.252.129         
Dallas | us-south | dal10  |  169.48.135.79/29  | 169.48.135.73         
Dallas | us-south | dal10  |  169.48.139.79/29  | 169.48.139.73         
Dallas | us-south | dal10  | 169.48.140.143/29  | 169.48.140.137         
Dallas | us-south | dal10  | 169.48.161.199/29  | 169.48.161.193         
Dallas | us-south | dal10  | 169.48.163.135/29  | 169.48.163.129         
Dallas | us-south | dal10  | 169.48.164.151/29  | 169.48.164.145         
Dallas | us-south | dal10  |  169.48.171.87/29  | 169.48.171.81         
Dallas | us-south | dal10  | 169.60.229.175/29  | 169.60.229.169         
Dallas | us-south | dal10  | 169.61.193.127/29  | 169.61.193.121         
Dallas | us-south | dal10  | 169.61.214.175/29  | 169.61.214.169         
Dallas | us-south | dal10  | 169.61.216.143/29  | 169.61.216.137         
Dallas | us-south | dal10  |  169.61.235.63/29  | 169.61.235.57         
Dallas | us-south | dal10  | 169.63.194.159/29  | 169.63.194.153         
Dallas | us-south | dal10  |  169.63.195.39/29  | 169.63.195.33         
Dallas | us-south | dal10  | 169.63.218.119/29  | 169.63.218.113         
Dallas | us-south | dal10  |  169.63.220.39/29  | 169.63.220.33         
Dallas | us-south | dal12  |  50.22.135.255/24  | 50.22.135.1         
Dallas | us-south | dal12  | 52.116.212.255/24  | 52.116.212.1         
Dallas | us-south | dal12  | 52.116.218.191/27  | 52.116.218.161         
Dallas | us-south | dal12  | 52.116.229.255/25  | 52.116.229.129         
Dallas | us-south | dal12  | 52.116.252.255/24  | 52.116.252.1         
Dallas | us-south | dal12  | 52.118.193.255/24  | 52.118.193.1         
Dallas | us-south | dal12  | 52.118.197.255/24  | 52.118.197.1         
Dallas | us-south | dal12  | 150.239.149.255/24 | 150.239.149.1         
Dallas | us-south | dal12  | 150.239.187.255/24 | 150.239.187.1         
Dallas | us-south | dal12  | 169.47.108.255/26  | 169.47.108.193         
Dallas | us-south | dal12  | 169.48.215.191/27  | 169.48.215.161         
Dallas | us-south | dal12  | 169.59.194.255/24  | 169.59.194.1         
Dallas | us-south | dal12  | 169.59.234.255/24  | 169.59.234.1         
Dallas | us-south | dal12  | 169.61.157.255/25  | 169.61.157.129         
Dallas | us-south | dal12  |  169.61.167.31/28  | 169.61.167.17         
Dallas | us-south | dal12  |  169.61.169.63/28  | 169.61.169.49         
Dallas | us-south | dal12  |  169.63.57.127/26  | 169.63.57.65         
Dallas | us-south | dal12  |  50.22.153.191/29  | 50.22.153.185         
Dallas | us-south | dal12  | 52.116.234.199/29  | 52.116.234.193         
Dallas | us-south | dal12  | 52.116.244.119/29  | 52.116.244.113         
Dallas | us-south | dal12  |  169.47.101.7/29   | 169.47.101.1         
Dallas | us-south | dal12  |  169.47.101.15/29  | 169.47.101.9         
Dallas | us-south | dal12  |  169.47.101.63/29  | 169.47.101.57         
Dallas | us-south | dal12  |  169.47.107.95/29  | 169.47.107.89         
Dallas | us-south | dal12  | 169.47.107.151/29  | 169.47.107.145         
Dallas | us-south | dal12  |  169.47.109.87/29  | 169.47.109.81         
Dallas | us-south | dal12  |  169.47.111.79/29  | 169.47.111.73         
Dallas | us-south | dal12  | 169.47.113.223/29  | 169.47.113.217         
Dallas | us-south | dal12  |  169.47.124.95/29  | 169.47.124.89         
Dallas | us-south | dal12  | 169.48.207.175/29  | 169.48.207.169         
Dallas | us-south | dal12  |  169.48.216.47/29  | 169.48.216.41         
Dallas | us-south | dal12  | 169.48.218.143/29  | 169.48.218.137         
Dallas | us-south | dal12  | 169.48.222.135/29  | 169.48.222.129         
Dallas | us-south | dal12  | 169.48.236.183/29  | 169.48.236.177         
Dallas | us-south | dal12  | 169.48.240.199/29  | 169.48.240.193         
Dallas | us-south | dal12  | 169.48.241.167/29  | 169.48.241.161         
Dallas | us-south | dal12  |  169.59.203.47/29  | 169.59.203.41         
Dallas | us-south | dal12  | 169.59.203.247/29  | 169.59.203.241         
Dallas | us-south | dal12  | 169.59.225.191/29  | 169.59.225.185         
Dallas | us-south | dal12  | 169.59.255.119/29  | 169.59.255.113         
Dallas | us-south | dal12  | 169.61.133.223/29  | 169.61.133.217         
Dallas | us-south | dal12  | 169.61.136.175/29  | 169.61.136.169         
Dallas | us-south | dal12  | 169.61.138.231/29  | 169.61.138.225         
Dallas | us-south | dal12  |  169.61.139.79/29  | 169.61.139.73         
Dallas | us-south | dal12  | 169.61.139.103/29  | 169.61.139.97         
Dallas | us-south | dal12  | 169.61.150.223/29  | 169.61.150.217         
Dallas | us-south | dal12  | 169.61.170.151/29  | 169.61.170.145         
Dallas | us-south | dal12  | 169.61.178.111/29  | 169.61.178.105         
Dallas | us-south | dal12  | 169.61.190.103/29  | 169.61.190.97         
Dallas | us-south | dal12  |   169.63.1.79/29   | 169.63.1.73         
Dallas | us-south | dal12  |   169.63.2.79/29   | 169.63.2.73         
Dallas | us-south | dal12  |  169.63.18.71/29   | 169.63.18.65         
Dallas | us-south | dal12  |  169.63.21.175/29  | 169.63.21.169         
Dallas | us-south | dal12  |  169.63.21.191/29  | 169.63.21.185         
Dallas | us-south | dal12  |   169.63.25.7/29   | 169.63.25.1         
Dallas | us-south | dal12  |  169.63.26.15/29   | 169.63.26.9         
Dallas | us-south | dal12  |  169.63.26.255/29  | 169.63.26.249         
Dallas | us-south | dal12  |   169.63.27.7/29   | 169.63.27.1         
Dallas | us-south | dal12  |  169.63.29.47/29   | 169.63.29.41         
Dallas | us-south | dal12  |  169.63.34.207/29  | 169.63.34.201         
Dallas | us-south | dal12  |  169.63.47.87/29   | 169.63.47.81         
Dallas | us-south | dal12  |  169.63.54.175/29  | 169.63.54.169         
Dallas | us-south | dal12  |  169.63.55.143/29  | 169.63.55.137         
Dallas | us-south | dal12  |  169.63.58.71/29   | 169.63.58.65         
Dallas | us-south | dal12  |  169.63.58.79/29   | 169.63.58.73         
Dallas | us-south | dal13  |  52.116.16.127/25  | 52.116.16.1         
Dallas | us-south | dal13  |  52.116.24.63/27   | 52.116.24.33         
Dallas | us-south | dal13  |  52.116.60.255/24  | 52.116.60.1         
Dallas | us-south | dal13  |  52.117.49.255/24  | 52.117.49.1         
Dallas | us-south | dal13  | 52.117.198.191/26  | 52.117.198.129         
Dallas | us-south | dal13  | 52.117.202.255/25  | 52.117.202.129         
Dallas | us-south | dal13  | 52.117.205.255/24  | 52.117.205.1         
Dallas | us-south | dal13  | 52.117.230.255/24  | 52.117.230.1         
Dallas | us-south | dal13  | 52.117.235.255/24  | 52.117.235.1         
Dallas | us-south | dal13  | 52.117.254.255/24  | 52.117.254.1         
Dallas | us-south | dal13  | 67.228.229.255/24  | 67.228.229.1         
Dallas | us-south | dal13  | 67.228.234.255/24  | 67.228.234.1         
Dallas | us-south | dal13  | 150.238.107.255/24 | 150.238.107.1         
Dallas | us-south | dal13  | 150.238.113.255/24 | 150.238.113.1         
Dallas | us-south | dal13  |  169.48.76.63/27   | 169.48.76.33         
Dallas | us-south | dal13  |  169.59.14.255/24  | 169.59.14.1         
Dallas | us-south | dal13  |  169.61.32.159/29  | 169.61.32.153         
Dallas | us-south | dal13  | 169.62.218.223/28  | 169.62.218.209         
Dallas | us-south | dal13  |  169.62.237.63/26  | 169.62.237.1         
Dallas | us-south | dal13  |  52.116.17.159/29  | 52.116.17.153         
Dallas | us-south | dal13  |  52.116.19.183/29  | 52.116.19.177         
Dallas | us-south | dal13  |  52.116.19.191/29  | 52.116.19.185         
Dallas | us-south | dal13  |  52.116.25.247/29  | 52.116.25.241         
Dallas | us-south | dal13  |  52.116.32.39/29   | 52.116.32.33         
Dallas | us-south | dal13  |  52.116.54.239/29  | 52.116.54.233         
Dallas | us-south | dal13  |  52.117.22.247/29  | 52.117.22.241         
Dallas | us-south | dal13  |  52.117.23.143/29  | 52.117.23.137         
Dallas | us-south | dal13  |  52.117.31.119/29  | 52.117.31.113         
Dallas | us-south | dal13  |  52.117.35.231/29  | 52.117.35.225         
Dallas | us-south | dal13  |  52.117.55.95/29   | 52.117.55.89         
Dallas | us-south | dal13  |  52.117.55.119/29  | 52.117.55.113         
Dallas | us-south | dal13  |  52.117.62.127/29  | 52.117.62.121         
Dallas | us-south | dal13  | 52.117.234.183/29  | 52.117.234.177         
Dallas | us-south | dal13  | 150.238.100.247/29 | 150.238.100.241         
Dallas | us-south | dal13  |  169.48.71.167/29  | 169.48.71.161         
Dallas | us-south | dal13  |  169.48.71.175/29  | 169.48.71.169         
Dallas | us-south | dal13  |  169.48.78.95/29   | 169.48.78.89         
Dallas | us-south | dal13  |  169.48.96.71/29   | 169.48.96.65         
Dallas | us-south | dal13  |  169.48.98.199/29  | 169.48.98.193         
Dallas | us-south | dal13  |  169.48.98.231/29  | 169.48.98.225         
Dallas | us-south | dal13  |  169.48.99.119/29  | 169.48.99.113         
Dallas | us-south | dal13  |  169.48.107.79/29  | 169.48.107.73         
Dallas | us-south | dal13  | 169.48.114.247/29  | 169.48.114.241         
Dallas | us-south | dal13  | 169.48.123.151/29  | 169.48.123.145         
Dallas | us-south | dal13  |  169.59.10.199/29  | 169.59.10.193         
Dallas | us-south | dal13  | 169.60.131.167/29  | 169.60.131.161         
Dallas | us-south | dal13  |  169.60.137.87/29  | 169.60.137.81         
Dallas | us-south | dal13  | 169.60.138.223/29  | 169.60.138.217         
Dallas | us-south | dal13  | 169.60.150.239/29  | 169.60.150.233         
Dallas | us-south | dal13  | 169.60.159.183/29  | 169.60.159.177         
Dallas | us-south | dal13  |  169.60.164.31/29  | 169.60.164.25         
Dallas | us-south | dal13  |  169.60.184.63/29  | 169.60.184.57         
Dallas | us-south | dal13  |  169.61.23.199/29  | 169.61.23.193         
Dallas | us-south | dal13  |  169.61.48.207/29  | 169.61.48.201         
Dallas | us-south | dal13  |  169.61.48.239/29  | 169.61.48.233         
Dallas | us-south | dal13  |  169.61.49.143/29  | 169.61.49.137         
Dallas | us-south | dal13  |  169.61.56.223/29  | 169.61.56.217         
Dallas | us-south | dal13  |  169.61.59.103/29  | 169.61.59.97         
Dallas | us-south | dal13  |  169.61.60.39/29   | 169.61.60.33         
Dallas | us-south | dal13  |  169.61.60.47/29   | 169.61.60.41         
Dallas | us-south | dal13  | 169.62.134.103/29  | 169.62.134.97         
Dallas | us-south | dal13  |  169.62.151.47/29  | 169.62.151.41         
Dallas | us-south | dal13  |  169.62.158.95/29  | 169.62.158.89         
Dallas | us-south | dal13  | 169.62.184.207/29  | 169.62.184.201         
Dallas | us-south | dal13  | 169.62.187.159/29  | 169.62.187.153         
Dallas | us-south | dal13  | 169.62.193.183/29  | 169.62.193.177         
Dallas | us-south | dal13  |  169.62.206.31/29  | 169.62.206.25         
Dallas | us-south | dal13  | 169.62.238.151/29  | 169.62.238.145         
Dallas | us-south | dal13  |  169.62.239.47/29  | 169.62.239.41         
Dallas | us-south | dal13  | 169.62.240.223/29  | 169.62.240.217         
Dallas | us-south | dal13  | 169.62.240.231/29  | 169.62.240.225         
Dallas | us-south | dal13  |  174.36.70.143/29  | 174.36.70.137