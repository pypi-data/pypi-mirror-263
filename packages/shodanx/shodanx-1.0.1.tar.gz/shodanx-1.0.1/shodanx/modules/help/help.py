from colorama import Fore,Back,Style


red =  Fore.RED

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

bold = Style.BRIGHT

colors = [ green, cyan, blue]


def mode_help():
    
    print(f"""
[{bold}{blue}DESCRIPTION{reset}]: {bold}{white}ShodanX is a tool to gather information of targets using shodan dorks{reset}⚡.
          
[{bold}{blue}MODES{reset}]: {bold}{white}
                                  

    - org         : Org mode to search the data of an organization with different types of facet in shodan
    - domain      : Domain mode to search the data of a domain with different types of facet in shodan
    - subdomain   : Subdomain mode to search the subdomain of the domain from shodan database
    - cidr        : CIDR mode to search data using the CIDR search query with different types of facet in shodan
    - ssl         : SSL modoe to search data using the ssl search query with different types of facet in shodan
    - custom      : Custom search mode to search with custom search with different types of facet shodan
    - update      : Update the ShodanX to latest version 
    
[{bold}{blue}FLAGS{reset}]: {bold}{white}

    -h,  --help   : Shows this help message and exits.
              
[{bold}{blue}Usage{reset}]: {bold}{white}
          
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
            - update      : shodanx update -h{reset}
""")
    
    quit()
    
def org_mode_help():
    
    print(f"""  
[{bold}{blue}MODE{reset}]: {bold}{white}ShodanX Organization Mode!{reset}
            
[{bold}{blue}Usage{reset}]: {bold}{white}
          
            shodanx org [options]
          
        Options for org mode:
        
               -org,  --organization   : Specify a organization name for shodanX query.
               
               -fct,  --facet          : Specify a Facet type for shodanx query and refer the shodan facet types for this queries.  
               
               -o,    --output         : Specify a filename to save the results of your facet queries.
               
               -ra,   --random-agent   : Enable it to use a random user agents when making shodan's facet queries.
               
               -to,   --timeout        : Specify a value for connection timeout
               
               -r,    --redirect       : Enable it to follow the redirect{reset}
    """)
    
    exit()
    
def dom_mode_help():
    
    print(f"""  
[{bold}{blue}MODE{reset}]: {bold}{white}ShodanX Domain Mode!{reset}
            
[{bold}{blue}Usage{reset}]: {bold}{white}
          
            shodanx domain [options]
          
        Options for domain mode:
        
               -d,    --domain         : Specify a domain name for shodanX query.
               
               -fct,  --facet          : Specify a Facet type for shodanx query and refer the shodan facet types for this queries.  
               
               -o,    --output         : Specify a filename to save the results of your facet queries.
               
               -ra,   --random-agent   : Enable it to use a random user agents when making shodan's facet queries.
               
               -to,   --timeout        : Specify a value for connection timeout
               
               -r,    --redirect       : Enable it to follow the redirect{reset}
    """)
    
    exit()
    
def ssl_mode_help():
    
    print(f"""  
[{bold}{blue}MODE{reset}]: {bold}{white}ShodanX SSL Mode!{reset}
            
[{bold}{blue}Usage{reset}]: {bold}{white}
          
            shodanx ssl [options]
          
        Options for SSL mode:
        
               -sq,    --ssl-query     : Specify a ssl query for shodanx (ex: -sq ssl.cert.issuer.cn:tesla.com).
               
               -fct,  --facet          : Specify a Facet type for shodanx query and refer the shodan facet types for this queries.  
               
               -o,    --output         : Specify a filename to save the results of your facet queries.
               
               -ra,   --random-agent   : Enable it to use a random user agents when making shodan's facet queries.
               
               -to,   --timeout        : Specify a value for connection timeout
               
               -r,    --redirect       : Enable it to follow the redirect{reset}
    """)
    
    exit()
    
    
def subs_mode_help():
    
    print(f"""  
[{bold}{blue}MODE{reset}]: {bold}{white}ShodanX Subdomain Enumeration Mode!{reset}
            
[{bold}{blue}Usage{reset}]: {bold}{white}
          
            shodanx subdomain [options]
          
        Options for subdomain mode:
        
               -d,    --domain         : Specify a domain name for shodanX for subdomain enumeration and not enumerate for subs of subdomains. (ex:tesla.com, google.com, facebook.com)
                              
               -o,    --output         : Specify a filename to save the results of your facet queries.
               
               -ra,   --random-agent   : Enable it to use a random user agents when making shodan's facet queries.
               
               -to,   --timeout        : Specify a value for connection timeout
               
               -r,    --redirect       : Enable it to follow the redirect{reset}
    """)
    
    exit()
    
    
def cidr_mode_help():
    
    print(f"""  
[{bold}{blue}MODE{reset}]: {bold}{white}ShodanX CIDR Mode!{reset}
            
[{bold}{blue}Usage{reset}]: {bold}{white}
          
            shodanx cidr [options]
          
        Options for cidr mode:
        
               -c,    --cidr           : Specify a cidr/subnet for shodanX query.
               
               -fct,  --facet          : Specify a Facet type for shodanx query and refer the shodan facet types for this queries.  
                              
               -o,    --output         : Specify a filename to save the results of your facet queries.
               
               -ra,   --random-agent   : Enable it to use a random user agents when making shodan's facet queries.
               
               -to,   --timeout        : Specify a value for connection timeout
               
               -r,    --redirect       : Enable it to follow the redirect{reset}
    """)
    
    exit()
    

    

    
def cus_mode_help():
    
    print(f"""  
[{bold}{blue}MODE{reset}]: {bold}{white}ShodanX Custom Search Mode!{reset}
            
[{bold}{blue}Usage{reset}]: {bold}{white}
          
            shodanx custom [options]
          
        Options for custom mode:
        
               -cq,   --custom-query   : Specify a custom search for shodan queries (ex: -cq hostname:"tesla.com").
               
               -fct,  --facet          : Specify a Facet type for shodanx query and refer the shodan facet types for this queries.  
               
               -o,    --output         : Specify a filename to save the results of your facet queries.
               
               -ra,   --random-agent   : Enable it to use a random user agents when making shodan's facet queries.
               
               -to,   --timeout        : Specify a value for connection timeout
               
               -r,    --redirect       : Enable it to follow the redirect{reset}
    """)
    
    exit()
    
def update_mode_help():

    print(f"""
[{bold}{blue}MODE{reset}]: {bold}{white}ShodanX Update mode{reset}
  
[{bold}{blue}Usage{reset}]: {bold}{white}
          
            shodanx update [options]   
        
        Options for update mode:
        
            -h,   --help        : Shows this help message and exits
            
            -lt,  --latest      : updates the shodax to latest version{reset}
          """)
    
    exit()
    
