# Importing the required modules
import subprocess  # subprocess is used to run shell commands
import requests  # requests is a library for making HTTP requests 
import time  # time is used for pausing execution and timing operations 

# Function to check the status of a build
def check_build_status(build_url):  # Function definition with a parameter
    """Check the status of a CI build given its URL."""  # Function docstring 
    try:  # Try block for error handling
        response = requests.get(build_url)  # Sending an HTTP GET request to the build URL
        if response.status_code == 200:  # Checking if the request was successful
            build_info = response.json()  # Parsing the response as JSON
            status = build_info.get("status", "Unknown")  # Getting the build status from the response
            print(f"Build Status: {status}")  # Displaying the build status
            return status  # Returning the build status
        else:
            print(f"Failed to get build status. HTTP Status Code: {response.status_code}")  # Error message for failed request
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while checking build status: {e}")  # Display the error message
    return "Unknown"  # Return a default status if an error occurs

# Function to deploy code to a server
def deploy_code(server_address, deployment_script):  # Function definition with parameters
    """Deploy code to a given server using a deployment script."""  # Function docstring
    try:  # Try block for error handling
        # Running the deployment script using subprocess
        result = subprocess.run(["ssh", server_address, deployment_script], capture_output=True, text=True)  # Executing SSH command to run the deployment script
        if result.returncode == 0:  # Checking if the deployment was successful
            print("Deployment succeeded.")  # Success message
        else:
            print("Deployment failed.")  # Failure message
            print(f"Error: {result.stderr}")  # Displaying the error output
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred during deployment: {e}")  # Display the error message

# Function to monitor the deployment status
def monitor_deployment(deployment_url, timeout=300):  # Function definition with parameters
    """Monitor the status of a deployment until it's completed or the timeout is reached."""  # Function docstring
    start_time = time.time()  # Getting the current time to track the timeout
    while time.time() - start_time < timeout:  # Looping until the timeout is reached
        try:  # Try block for error handling
            response = requests.get(deployment_url)  # Sending an HTTP GET request to the deployment URL
            if response.status_code == 200:  # Checking if the request was successful
                deployment_info = response.json()  # Parsing the response as JSON
                status = deployment_info.get("status", "Unknown")  # Getting the deployment status
                print(f"Deployment Status: {status}")  # Displaying the deployment status
                if status.lower() in ["succeeded", "failed"]:  # Checking if the deployment is complete
                    break  # Exit the loop if deployment is finished
            else:
                print(f"Failed to get deployment status. HTTP Status Code: {response.status_code}")  # Error message for failed request
        except Exception as e:  # Catch any exceptions
            print(f"An error occurred while monitoring deployment: {e}")  # Display the error message
        time.sleep(10)  # Pause for 10 seconds before checking again
    else:
        print("Deployment monitoring timed out.")  # Message if the timeout is reached

# Function to trigger a new build
def trigger_build(build_trigger_url, payload):  # Function definition with parameters
    """Trigger a new build using a POST request."""  # Function docstring
    try:  # Try block for error handling
        response = requests.post(build_trigger_url, json=payload)  # Sending an HTTP POST request with a JSON payload
        if response.status_code == 201:  # Checking if the request was successful
            print("Build triggered successfully.")  # Success message
        else:
            print(f"Failed to trigger build. HTTP Status Code: {response.status_code}")  # Error message for failed request
            print(f"Response: {response.text}")  # Displaying the response text
    except Exception as e:  # Catch any exceptions
        print(f"An error occurred while triggering build: {e}")  # Display the error message

# Main function to run the CI/CD tasks
def main():  # Main function definition
    """Run the CI/CD pipeline tasks."""  # Function docstring
    build_url = "http://example.com/api/builds/123"  # Example URL for build status
    deployment_url = "http://example.com/api/deployments/123"  # Example URL for deployment status
    build_trigger_url = "http://example.com/api/builds/trigger"  # Example URL to trigger a build
    server_address = "user@your-server.com"  # Example server address for deployment
    deployment_script = "/path/to/deployment_script.sh"  # Example deployment script path
    payload = {"branch": "main"}  # Example JSON payload for triggering a build

    print("Triggering a new build:")  # Display a message for build triggering
    trigger_build(build_trigger_url, payload)  # Call to trigger_build function

    print("\nChecking the build status:")  # Display a message for build status check
    build_status = check_build_status(build_url)  # Call to check_build_status function

    if build_status.lower() == "succeeded":  # Checking if the build succeeded
        print("\nDeploying code to the server:")  # Display a message for deployment
        deploy_code(server_address, deployment_script)  # Call to deploy_code function

        print("\nMonitoring the deployment status:")  # Display a message for deployment monitoring
        monitor_deployment(deployment_url)  # Call to monitor_deployment function
    else:
        print("Build did not succeed, skipping deployment.")  # Message if the build failed

# This condition ensures the main function runs only when the script is executed directly
if __name__ == "__main__":  # Conditional statement to check if the script is being run directly
    main()  # Call to the main function
