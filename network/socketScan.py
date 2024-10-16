# Importing the required modules
import socket  # socket is a module that provides low-level networking interface 
import subprocess  # subprocess is used to run shell commands
import platform  # platform is used to get system's platform information 
import dns.resolver  # dnspython library used for DNS resolution 

# Function to check network connectivity
def check_network_connectivity(hostname="8.8.8.8"):  # Function definition with a default parameter
    """Check network connectivity to a given hostname."""  # Function docstring
    try:  # Try block for error handling
        # Running the ping command to check connectivity
        response = subprocess.run(["ping", "-c", "1", hostname], capture_output=True, text=True)  # Using subprocess to ping a host
        if response.returncode == 0:  # Conditional statement to check if ping was successful
            print(f"Network is up. Able to reach {hostname}.")  # Output if network is reachable
        else:
            print(f"Network is down. Unable to reach {hostname}.")  # Output if network is not reachable
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while checking network connectivity: {e}")  # Display the error message

# Function to retrieve IP information
def get_ip_info():  # Function definition
    """Retrieve local IP information."""  # Function docstring
    try:
        # Getting the hostname and IP address
        hostname = socket.gethostname()  # Using socket module to get the local hostname
        local_ip = socket.gethostbyname(hostname)  # Using socket module to get the local IP address
        print(f"Hostname: {hostname}")  # Display the local hostname
        print(f"Local IP Address: {local_ip}")  # Display the local IP address
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while retrieving IP information: {e}")  # Display the error message

# Function to scan open ports on a given host
def scan_open_ports(hostname="localhost", port_range=(1, 1024)):  # Function definition with parameters
    """Scan open ports on the given hostname within the specified port range."""  # Function docstring
    open_ports = []  # List to store open ports
    for port in range(port_range[0], port_range[1]):  # Looping over a range of ports
        # Creating a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET specifies IPv4, SOCK_STREAM specifies TCP
        sock.settimeout(0.5)  # Setting a timeout for the connection attempt
        # Trying to connect to the port
        result = sock.connect_ex((hostname, port))  # connect_ex returns 0 if successful, otherwise an error code
        if result == 0:  # Checking if the port is open
            open_ports.append(port)  # Adding the port to the list of open ports
        sock.close()  # Closing the socket connection
    if open_ports:  # Checking if any open ports were found
        print(f"Open ports on {hostname}: {open_ports}")  # Displaying the open ports
    else:
        print(f"No open ports found on {hostname}.")  # Message if no open ports were found

# Function to resolve DNS for a given domain
def resolve_dns(domain_name):  # Function definition with a parameter
    """Resolve DNS for a given domain name."""  # Function docstring
    try:  # Try block for error handling
        answers = dns.resolver.resolve(domain_name, "A")  # Resolving the domain's A record
        # Looping through the DNS answers
        for ip in answers:  # Iterating over the list of IP addresses
            print(f"{domain_name} resolves to {ip}")  # Displaying the resolved IP addresses
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while resolving DNS: {e}")  # Display the error message

# Function to gather network interface information
def get_network_interfaces():  # Function definition
    """Get information about network interfaces."""  # Function docstring
    interfaces = psutil.net_if_addrs()  # Dictionary containing network interface addresses, retrieved using psutil
    for interface_name, addresses in interfaces.items():  # Iterating over the dictionary items
        print(f"\nInterface: {interface_name}")  # Displaying the interface name
        for address in addresses:  # Iterating over the list of addresses for each interface
            if address.family == socket.AF_INET:  # Checking if the address family is IPv4
                print(f"  IPv4 Address: {address.address}")  # Displaying the IPv4 address
                print(f"  Netmask: {address.netmask}")  # Displaying the netmask
                print(f"  Broadcast IP: {address.broadcast}")  # Displaying the broadcast IP
            elif address.family == socket.AF_INET6:  # Checking if the address family is IPv6
                print(f"  IPv6 Address: {address.address}")  # Displaying the IPv6 address
                print(f"  Netmask: {address.netmask}")  # Displaying the netmask
            elif address.family == socket.AF_LINK:  # Checking if the address family is MAC address
                print(f"  MAC Address: {address.address}")  # Displaying the MAC address

# Main function to run all network checks
def main():  # Main function definition
    """Run all network administration tasks."""  # Function docstring
    print("Network Connectivity Check:")  # Display a title for network connectivity check
    check_network_connectivity()  # Call to check_network_connectivity function
    print("\nIP Information:")  # Display a title for IP information
    get_ip_info()  # Call to get_ip_info function
    print("\nPort Scanning:")  # Display a title for port scanning
    scan_open_ports()  # Call to scan_open_ports function
    print("\nDNS Resolution:")  # Display a title for DNS resolution
    resolve_dns("google.com")  # Call to resolve_dns function with 'google.com' as an example
    print("\nNetwork Interfaces:")  # Display a title for network interface information
    get_network_interfaces()  # Call to get_network_interfaces function

# This condition ensures the main function runs only when the script is executed directly
if __name__ == "__main__":  # Conditional statement to check if the script is being run directly
    main()  # Call to the main function
