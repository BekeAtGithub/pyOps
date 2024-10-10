# Importing the required modules
import subprocess  # subprocess is used to run shell commands
import json  # json is used to work with JSON data

# Function to run an Ansible playbook
def run_ansible_playbook(playbook_path, inventory_file):  # Function definition with parameters
    """Run an Ansible playbook given its path and inventory file."""  # Function docstring
    try:  # Try block for error handling
        # Running the ansible-playbook command using subprocess
        result = subprocess.run(["ansible-playbook", "-i", inventory_file, playbook_path], capture_output=True, text=True)  # Command to run the playbook
        if result.returncode == 0:  # Checking if the playbook run was successful
            print("Playbook ran successfully.")  # Success message
            print(result.stdout)  # Displaying the standard output from the command
        else:
            print("Playbook execution failed.")  # Failure message
            print(f"Error: {result.stderr}")  # Displaying the error output
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while running the playbook: {e}")  # Display the error message

# Function to ping all hosts in the inventory
def ping_ansible_hosts(inventory_file):  # Function definition with a parameter
    """Ping all hosts in the given Ansible inventory file."""  # Function docstring
    try:  # Try block for error handling
        # Running the ansible command to ping all hosts
        result = subprocess.run(["ansible", "all", "-i", inventory_file, "-m", "ping"], capture_output=True, text=True)  # Command to ping all hosts
        if result.returncode == 0:  # Checking if the ping command was successful
            print("Ping succeeded for the following hosts:")  # Success message
            print(result.stdout)  # Displaying the standard output from the command
        else:
            print("Ping failed.")  # Failure message
            print(f"Error: {result.stderr}")  # Displaying the error output
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while pinging hosts: {e}")  # Display the error message

# Function to list Ansible inventory hosts in JSON format
def list_ansible_inventory(inventory_file):  # Function definition with a parameter
    """List hosts from the given Ansible inventory file in JSON format."""  # Function docstring
    try:  # Try block for error handling
        # Running the ansible-inventory command to list hosts
        result = subprocess.run(["ansible-inventory", "-i", inventory_file, "--list"], capture_output=True, text=True)  # Command to list inventory
        if result.returncode == 0:  # Checking if the command was successful
            inventory = json.loads(result.stdout)  # Parsing the JSON output
            print("Ansible Inventory:")  # Title message for inventory display
            print(json.dumps(inventory, indent=2))  # Pretty-printing the inventory JSON
        else:
            print("Failed to list Ansible inventory.")  # Failure message
            print(f"Error: {result.stderr}")  # Displaying the error output
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while listing the inventory: {e}")  # Display the error message

# Function to run a custom Ansible command
def run_ansible_command(inventory_file, host, module, args):  # Function definition with parameters
    """Run a custom Ansible command on a given host."""  # Function docstring
    try:  # Try block for error handling
        # Running the ansible command using the provided arguments
        result = subprocess.run(["ansible", host, "-i", inventory_file, "-m", module, "-a", args], capture_output=True, text=True)  # Command to run the custom module
        if result.returncode == 0:  # Checking if the command was successful
            print(f"Command ran successfully on {host}.")  # Success message
            print(result.stdout)  # Displaying the standard output from the command
        else:
            print(f"Command execution failed on {host}.")  # Failure message
            print(f"Error: {result.stderr}")  # Displaying the error output
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while running the command: {e}")  # Display the error message

# Main function to execute the Ansible tasks
def main():  # Main function definition
    """Execute Ansible tasks for managing hosts and playbooks."""  # Function docstring
    inventory_file = "/path/to/your/inventory.ini"  # Example path to Ansible inventory file
    playbook_path = "/path/to/your/playbook.yml"  # Example path to Ansible playbook

    print("Running Ansible Playbook:")  # Message indicating playbook execution
    run_ansible_playbook(playbook_path, inventory_file)  # Call to run_ansible_playbook function

    print("\nPinging Ansible Hosts:")  # Message indicating pinging of hosts
    ping_ansible_hosts(inventory_file)  # Call to ping_ansible_hosts function

    print("\nListing Ansible Inventory:")  # Message indicating listing of inventory
    list_ansible_inventory(inventory_file)  # Call to list_ansible_inventory function

    print("\nRunning Custom Ansible Command:")  # Message indicating custom command execution
    run_ansible_command(inventory_file, "localhost", "shell", "uptime")  # Call to run_ansible_command function

# This condition ensures the main function runs only when the script is executed directly
if __name__ == "__main__":  # Conditional statement to check if the script is being run directly
    main()  # Call to the main function
