import subprocess

#install packages via yum or dnf
def install_package(package_name):
    try:
        # Try using dnf, if available
        try:
            result = subprocess.run(['sudo', 'dnf', '-y', 'install', package_name], capture_output=True, text=True, check=True)
        except FileNotFoundError:
            # If dnf is not available, use yum
            result = subprocess.run(['sudo', 'yum', '-y', 'install', package_name], capture_output=True, text=True, check=True)
        
        print(f"Successfully installed package '{package_name}':")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package '{package_name}': {e.stderr}")

# start a service using systemctl
def start_service(service_name):
    try:
        result = subprocess.run(['sudo', 'systemctl', 'start', service_name], capture_output=True, text=True, check=True)
        print(f"Successfully started service '{service_name}':")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to start service '{service_name}': {e.stderr}")

# enable a service at boot
def enable_service(service_name):
    try:
        result = subprocess.run(['sudo', 'systemctl', 'enable', service_name], capture_output=True, text=True, check=True)
        print(f"Successfully enabled service '{service_name}' to start on boot:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to enable service '{service_name}': {e.stderr}")

# check the status of a service
def check_service_status(service_name):
    try:
        result = subprocess.run(['systemctl', 'status', service_name], capture_output=True, text=True, check=True)
        print(f"Status of service '{service_name}':")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Service '{service_name}' status check failed: {e.stderr}")

if __name__ == "__main__":
#run __main__ variable - the main program 
    package_name = "httpd"  # Example package name (Apache web server)
    install_package(package_name)
    service_name = "httpd"
    start_service(service_name)
    enable_service(service_name)
    check_service_status(service_name)
