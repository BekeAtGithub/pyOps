import subprocess

# update package lists
def updatePackages():
    try:
        result = subprocess.run(['sudo', 'apt', 'update'], capture_output=True, text=True, check=True)
        print("Package lists updated successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to update package lists: {e.stderr}")

# upgrade all packages
def upgradePackages():
    try:
        result = subprocess.run(['sudo', 'apt', '-y', 'upgrade'], capture_output=True, text=True, check=True)
        print("Packages upgraded successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade packages: {e.stderr}")

# install a specific package
def installPackage(package_name):
    try:
        result = subprocess.run(['sudo', 'apt', '-y', 'install', package_name], capture_output=True, text=True, check=True)
        print(f"Package '{package_name}' installed successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package '{package_name}': {e.stderr}")

# remove a specific package
def removePackage(package_name):
    try:
        result = subprocess.run(['sudo', 'apt', '-y', 'remove', package_name], capture_output=True, text=True, check=True)
        print(f"Package '{package_name}' removed successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to remove package '{package_name}': {e.stderr}")

# start a service - starts a service, but does not "enable", check next function for further notes on this
def startService(service_name):
    try:
        result = subprocess.run(['sudo', 'systemctl', 'start', service_name], capture_output=True, text=True, check=True)
        print(f"Service '{service_name}' started successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to start service '{service_name}': {e.stderr}")

# enable a service to start at boot - note, start a service only turns it on, enabling turns it on - everytime it boots up
#same with stop/disable - stop is to turn it off, disable is to turn it off - on boot
def enableService(service_name):
    try:
        result = subprocess.run(['sudo', 'systemctl', 'enable', service_name], capture_output=True, text=True, check=True)
        print(f"Service '{service_name}' enabled to start on boot:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to enable service '{service_name}': {e.stderr}")

# Check status of a service
def getServiceStatus(service_name):
    try:
        result = subprocess.run(['systemctl', 'status', service_name], capture_output=True, text=True, check=True)
        print(f"Status of service '{service_name}':")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to get status of service '{service_name}': {e.stderr}")

if __name__ == "__main__":
    #call main function
    updatePackages()
    upgradePackages()
    
    package_name = "nginx"  # Example package name
    installPackage(package_name)

    removePackage(package_name)

    service_name = "nginx"
    startService(service_name)
    enableService(service_name)

    getServiceStatus(service_name)
