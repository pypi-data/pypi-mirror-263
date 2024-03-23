# ShodanX

ShodanX ⚡ is a versatile information gathering tool that harnesses the power of Shodan's extensive database. it offers multiple modes and flexible queries to extract valuable insights for security assessments, reconnaissance, and threat intelligence. With colorful output and intuitive commands, ShodanX empowers users to efficiently gather and analyze data from Shodan's facets, enhancing their cybersecurity efforts. Do you Love this project ShodanX⚡ then support the Shodanx by sharing to others
and give a ⭐ for it.

### Why ShodanX

ShodanX is more useful for everyone compared to Shodan because it doesn't require paid API keys. This means anyone can access Shodan's database of internet-connected devices without having to pay for it. It's like getting the benefits of Shodan for free, making it accessible to a wider range of users. Plus, ShodanX provides real-time query results, so you can get the latest information quickly and easily. Overall, it's a more convenient and cost-effective option for anyone interested in network reconnaissance and security analysis.


### Features in V1.0.1

- **New Modes**: Introducing two new modes `subdomain` & `cidr` 
  
- **Query Performance**: Improved the query performance to get accurate results for user queries
  
- **Mode enchancement**: Remastered the update mode to update the shodanx for upcoming versions

- **New Command**: Introduced the new flag `--show-update` in update to know the updates in latest versions

### About ShodanX:

Shodanx ⚡ is a great tool and its uses the shodan facet data then extracts results for given targets by user and ShodanX is fully upto users queries. By making a 
super queries and use good facets queries to get more results about your targets, users can use different modes with proper shodan facets for queries to get lot 
of information about your target.

### ShodanX queries:

ShodanX ⚡ potential depends on how user using it with their queries and these queries can be improved by building more queries with your results
and to know more about queries , Please refere [here](https://www.shodan.io/search/filters) and also refer the analytics queries which you can find [here](https://www.shodan.io/search/facet?query=&facet=asn)
by understanding these queries and references you can use the shodanx with its full potentials.

## Installation

To install ShodanX, simply use pip:

```bash
pip install git+https://github.com/sanjai-AK47/ShodanX
```

### Usage

ShodanX provides a command-line interface (CLI) with intuitive commands for seamless interaction. Here are some of the available commands:

- `shodanx org`: Search for information related to an organization.
- `shodanx domain`: Perform a domain search to gather relevant data.
- `shodanx ssl`: Search for SSL certificates using custom queries.
- `shodanx subdomain`: Search for subdomain from shodan database
- `shodanx cidr`: Search for information related to cidr/subnet from shodan database
- `shodanx custom`: Execute custom queries tailored to your needs.
- `shodanx update`: Check for updates and install the latest version from GitHub and PYPI.

For detailed usage instructions and command options, refer to the help menu:

```yaml
 shodanx -h
        __           __               _  __
  ___  / /  ___  ___/ / ___ _  ___   | |/_/
 (_-< / _ \/ _ \/ _  / / _ `/ / _ \ _>  <  
/___//_//_/\___/\_,_/  \_,_/ /_//_//_/|_|  
                                           

    
                     Author : D.SanjaiKumar @CyberRevoltSecurities


[DESCRIPTION]: ShodanX is a tool to gather information of targets using shodan dorks⚡.
          
[MODES]: 
                                  

    - org         : Org mode to search the data of an organization with different types of facet in shodan
    - domain      : Domain mode to search the data of a domain with different types of facet in shodan
    - subdomain   : Subdomain mode to search the subdomain of the domain from shodan database
    - cidr        : CIDR mode to search data using the CIDR search query with different types of facet in shodan
    - ssl         : SSL modoe to search data using the ssl search query with different types of facet in shodan
    - custom      : Custom search mode to search with custom search with different types of facet shodan
    - update      : Update the ShodanX to latest version 
    
[FLAGS]: 

    -h,  --help   : Shows this help message and exits.
              
[Usage]: 
          
        shodanx [commands]
        
        Available Commands:
    
            - org         : Executes the shodanX org mode for information gathering
            - domain      : Executes the shodanX domain mode for information gathering
            - subdomain   : Executes the shodanX subdomain enumeration query mode for information gathering
            - cidr        : Executes the cidr query mode forinformation gathering
            - ssl         : Executes the shodanX ssl query mode for information gathering
            - custom      : Executes the shodanX Custom search query mode for information gathering
            - update      : Update the ShodanX to latest version 
            
        Help Commands:
        
            - org         : shodanx org -h
            - domain      : shodanx domain -h
            - subdomain   : shodanx subdomain -h
            - cidr        : shodanx cidr -h
            - ssl         : shodanx ssl -h
            - custom      : shodanx custom -h
            - update      : shodanx update -h
```

### Contribution and Support

ShodanX is an open-source project hosted on GitHub. Contributions, bug reports, and feature requests are welcome. Feel free to explore the repository, submit issues, or contribute code to enhance ShodanX's capabilities.

For support or inquiries, please visit the [ShodanX GitHub page](https://github.com/sanjai-AK47/ShodanX).

### Abou the Author

ShodanX is developed by [D.Sanjai Kumar](https://www.linkedin.com/in/d-sanjai-kumar-109a7227b) Yeah its Me!, Hey Guys Im a developer of these tools which helps you in Security assessments, Information gathering and etc., ShodanX ⚡ is a tool that make your information gathering on shodan very easy and its help every people who are in CyberSecurity Field

ShodanX is an open-source project hosted on GitHub. Contributions, bug reports, and feature requests are welcome. Feel free to explore the repository, submit issues, or contribute code to enhance ShodanX's capabilities.

For support or inquiries, please visit the ShodanX GitHub page.

## License

ShodanX is licensed under the MIT License. See the [LICENSE](https://github.com/sanjai-AK47/ShodanX/blob/main/LICENSE) file for details.

