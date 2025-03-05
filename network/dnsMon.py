'''
The script has dns.resolver module from the dnspython library to query the DNS server - might need to install with "pip3 install dnspython" from command line 
- it basically monitors DNS resolution times of a specific domain. 
'''

import dns.resolver
import time

# monitor_dns(domain, interval)` This function continuously monitors DNS resolution times for the given domain at the specified interval (default is 60 seconds)
def monitor_dns(domain, interval=60):
    resolver = dns.resolver.Resolver() # resolver.resolve(domain) Resolves the DNS for the specified domain.  

    while True:
        start_time = time.time() #time.time() Used to calculate the time before and after the DNS resolution to determine how long it took.

        try:
            # Query DNS for the domain
            answers = resolver.resolve(domain)
            end_time = time.time()

            # Calculate the response time
            response_time = end_time - start_time
            print(f"DNS resolution for {domain} took {response_time:.4f} seconds.")

        except dns.resolver.NoAnswer: #The script handles different exceptions like `NoAnswer`, `NXDOMAIN`, `Timeout`, and any other general DNS exceptions.
            print(f"No answer found for domain: {domain}")
        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain} does not exist.")
        except dns.resolver.Timeout:
            print(f"DNS request timed out for domain: {domain}")
        except dns.exception.DNSException as e:
            print(f"An error occurred: {e}")

        # Wait for the specified interval before checking again
        time.sleep(interval) #interval This parameter controls how often the script checks the DNS resolution time. You can adjust it as needed.

if __name__ == "__main__":#call function as main
    domain_to_monitor = "example.com"
    monitor_dns(domain_to_monitor, interval=60) # print the DNS resolution time every 60 seconds. You can modify it to log the results to a file or send alerts if the resolution time exceeds a certain threshold.

