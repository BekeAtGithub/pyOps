'''
This script uses `dns.resolver` module from the `dnspython` package to query the DNS server
- it basically monitors DNS resolution times of a specific domain. 

if you're running this on Linux install dnspython if you haven't already with pip:
pip install dnspython
'''

import dns.resolver
import time

def monitor_dns(domain, interval=60):
    resolver = dns.resolver.Resolver()

    while True:
        start_time = time.time()

        try:
            # Query DNS for the domain
            answers = resolver.resolve(domain)
            end_time = time.time()

            # Calculate the response time
            response_time = end_time - start_time
            print(f"DNS resolution for {domain} took {response_time:.4f} seconds.")

        except dns.resolver.NoAnswer:
            print(f"No answer found for domain: {domain}")
        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain} does not exist.")
        except dns.resolver.Timeout:
            print(f"DNS request timed out for domain: {domain}")
        except dns.exception.DNSException as e:
            print(f"An error occurred: {e}")

        # Wait for the specified interval before checking again
        time.sleep(interval)

if __name__ == "__main__":
    domain_to_monitor = "example.com"
    monitor_dns(domain_to_monitor, interval=60)

'''
### Explanation:

- **`monitor_dns(domain, interval)`**: This function continuously monitors DNS resolution times for the given domain at the specified interval (default is 60 seconds).

- **`resolver.resolve(domain)`**: Resolves the DNS for the specified domain. 

- **`time.time()`**: Used to calculate the time before and after the DNS resolution to determine how long it took.

- **Exception Handling**: The script handles different exceptions like `NoAnswer`, `NXDOMAIN`, `Timeout`, and any other general DNS exceptions.

- **`interval`**: This parameter controls how often the script checks the DNS resolution time. You can adjust it as needed.

This script will print the DNS resolution time every 60 seconds. You can modify it to log the results to a file or send alerts if the resolution time exceeds a certain threshold.
'''
