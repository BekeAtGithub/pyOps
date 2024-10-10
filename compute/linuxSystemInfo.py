# Importing the required modules
import psutil  # psutil is a module that provides system and hardware information
import subprocess  # subprocess is used to run shell commands
import platform  # platform is used to get the system's platform information
import shutil  # shutil provides file operations, including disk usage

# Function to check disk space
def check_disk_space():  # Function definition
    """Check disk space usage."""  # Function docstring (comment describing the function)
    total, used, free = shutil.disk_usage("/")  # Tuple unpacking from the result of disk_usage
    print(f"Disk Space - Total: {total // (2**30)} GB, Used: {used // (2**30)} GB, Free: {free // (2**30)} GB")  # Formatted string to display disk space in GB

# Function to check CPU usage
def check_cpu_usage():  # Function definition
    """Check CPU usage."""  # Function docstring
    cpu_percent = psutil.cpu_percent(interval=1)  # Variable storing the CPU usage percentage, retrieved using psutil
    print(f"CPU Usage: {cpu_percent}%")  # Formatted string to display CPU usage percentage

# Function to check memory usage
def check_memory_usage():  # Function definition
    """Check memory usage."""  # Function docstring
    memory_info = psutil.virtual_memory()  # Calling the virtual_memory() function from psutil, which returns a namedtuple
    print(f"Memory - Total: {memory_info.total // (2**30)} GB, Used: {memory_info.used // (2**30)} GB, Free: {memory_info.available // (2**30)} GB")  # Formatted string to display memory usage in GB

# Function to check the status of a specific service
def check_service_status(service_name):  # Function definition with a parameter
    """Check the status of a given service."""  # Function docstring
    try:  # Try block to handle potential errors
        # Running a shell command to check the service status
        result = subprocess.run(["systemctl", "is-active", service_name], capture_output=True, text=True)  # Running systemctl to check service status
        # Check if the service is active
        if result.stdout.strip() == "active":  # Conditional statement to check service status
            print(f"The service '{service_name}' is running.")  # Output if the service is running
        else:
            print(f"The service '{service_name}' is not running.")  # Output if the service is not running
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred: {e}")  # Display the error message

# Function to gather system information
def get_system_info():  # Function definition
    """Get basic system information."""  # Function docstring
    info = {  # Dictionary to store system information
        "System": platform.system(),  # OS name
        "Node Name": platform.node(),  # Hostname
        "Release": platform.release(),  # OS version
        "Version": platform.version(),  # Detailed OS version
        "Machine": platform.machine(),  # Machine type
        "Processor": platform.processor()  # Processor information
    }
    # Looping through the dictionary items
    for key, value in info.items():  # Dictionary unpacking to iterate over key-value pairs
        print(f"{key}: {value}")  # Display each key-value pair

# Main function to run all checks
def main():  # Main function definition
    """Run all system administration checks."""  # Function docstring
    print("System Information:")  # Display a title for system information
    get_system_info()  # Call to get_system_info function
    print("\nDisk Space:")  # Display a title for disk space check
    check_disk_space()  # Call to check_disk_space function
    print("\nCPU Usage:")  # Display a title for CPU usage check
    check_cpu_usage()  # Call to check_cpu_usage function
    print("\nMemory Usage:")  # Display a title for memory usage check
    check_memory_usage()  # Call to check_memory_usage function
    print("\nService Check:")  # Display a title for service status check
    check_service_status("ssh")  # Call to check_service_status function with 'ssh' service as an example

# This condition ensures the main function runs only when the script is executed directly
if __name__ == "__main__":  # Conditional statement to check if the script is being run directly
    main()  # Call to the main function
