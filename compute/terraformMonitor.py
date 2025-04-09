# Importing the required modules 
import subprocess  # subprocess is used to run shell commands

# Function to initialize a Terraform configuration
def terraform_init(terraform_dir):  # Function definition with a parameter
    """Initialize a Terraform configuration directory."""  # Function docstring
    try:  # Try block for error handling
        # Running the terraform init command
        result = subprocess.run(["terraform", "init"], cwd=terraform_dir, capture_output=True, text=True)  # Command to initialize Terraform
        if result.returncode == 0:  # Checking if the initialization was successful
            print("Terraform initialization succeeded.")  # Success message
            print(result.stdout)  # Displaying the standard output from the command
        else:
            print("Terraform initialization failed.")  # Failure message
            print(f"Error: {result.stderr}")  # Displaying the error output
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while initializing Terraform: {e}")  # Display the error message

# Function to apply Terraform changes
def terraform_apply(terraform_dir, auto_approve=True):  # Function definition with parameters
    """Apply Terraform changes to the infrastructure."""  # Function docstring
    try:  # Try block for error handling
        # Command to apply Terraform changes with or without auto-approval
        command = ["terraform", "apply", "-auto-approve"] if auto_approve else ["terraform", "apply"]
        result = subprocess.run(command, cwd=terraform_dir, capture_output=True, text=True)  # Running the apply command
        if result.returncode == 0:  # Checking if the apply was successful
            print("Terraform apply succeeded.")  # Success message
            print(result.stdout)  # Displaying the standard output from the command
        else:
            print("Terraform apply failed.")  # Failure message
            print(f"Error: {result.stderr}")  # Displaying the error output
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while applying Terraform changes: {e}")  # Display the error message

# Function to destroy Terraform-managed infrastructure
def terraform_destroy(terraform_dir, auto_approve=True):  # Function definition with parameters
    """Destroy Terraform-managed infrastructure."""  # Function docstring
    try:  # Try block for error handling
        # Command to destroy Terraform resources with or without auto-approval
        command = ["terraform", "destroy", "-auto-approve"] if auto_approve else ["terraform", "destroy"]
        result = subprocess.run(command, cwd=terraform_dir, capture_output=True, text=True)  # Running the destroy command
        if result.returncode == 0:  # Checking if the destroy was successful
            print("Terraform destroy succeeded.")  # Success message
            print(result.stdout)  # Displaying the standard output from the command
        else:
            print("Terraform destroy failed.")  # Failure message
            print(f"Error: {result.stderr}")  # Displaying the error output
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while destroying Terraform resources: {e}")  # Display the error message

# Function to plan Terraform changes
def terraform_plan(terraform_dir):  # Function definition with a parameter
    """Generate a Terraform execution plan."""  # Function docstring
    try:  # Try block for error handling
        # Running the terraform plan command
        result = subprocess.run(["terraform", "plan"], cwd=terraform_dir, capture_output=True, text=True)  # Command to generate the plan
        if result.returncode == 0:  # Checking if the plan generation was successful
            print("Terraform plan succeeded.")  # Success message
            print(result.stdout)  # Displaying the standard output from the command
        else:
            print("Terraform plan failed.")  # Failure message
            print(f"Error: {result.stderr}")  # Displaying the error output
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while generating the Terraform plan: {e}")  # Display the error message

# Main function to execute Terraform tasks
def main():  # Main function definition
    """Execute basic Terraform tasks for managing infrastructure."""  # Function docstring
    terraform_dir = "/path/to/your/terraform/configuration"  # Example path to the Terraform configuration directory

    print("Initializing Terraform:")  # Message indicating Terraform initialization
    terraform_init(terraform_dir)  # Call to terraform_init function

    print("\nPlanning Terraform changes:")  # Message indicating Terraform plan
    terraform_plan(terraform_dir)  # Call to terraform_plan function

    print("\nApplying Terraform changes:")  # Message indicating Terraform apply
    terraform_apply(terraform_dir)  # Call to terraform_apply function

    # Optional: Uncomment the following lines if you want to destroy the resources afterward
    # print("\nDestroying Terraform-managed infrastructure:")  # Message indicating Terraform destroy
    # terraform_destroy(terraform_dir)  # Call to terraform_destroy function

# This condition ensures the main function runs only when the script is executed directly
if __name__ == "__main__":  # Conditional statement to check if the script is being run directly
    main()  # Call to the main function
