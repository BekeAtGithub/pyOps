#uses Helm CLI via python to manage helm charts. 
#helm doesnt have an API so python executes helm commands 
#Python uses subprocess module to run commands like:
#helm list -all-namespaces 
#helm install --namespace 
#helm upgrade --namespace

#guide: replace "release_name", "chart-name" and "namespace" with actual values
#make sure kubectl context is configured to the right k8s cluster

import subprocess

#lists helm releases from all namespaces
def getHelmRelease():
    try:
        result = subprocess.run(['helm', 'list', '--all-namespaces'], capture_output=True, text=True, check=True)
        print("List of Helm releases:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error listing Helm releases: {e.stderr}")

#install/provision a new helm release
def newHelmRelease(release_name, chart_name, namespace, values_file=None):
    try:
        cmd = ['helm', 'install', release_name, chart_name, '--namespace', namespace]
        if values_file:
            cmd.extend(['-f', values_file])
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Successfully installed release '{release_name}':")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error installing Helm release '{release_name}': {e.stderr}")

# upgrade existing helm release
def upgradeHelmRelease(release_name, chart_name, namespace, values_file=None):
    try:
        cmd = ['helm', 'upgrade', release_name, chart_name, '--namespace', namespace]
        if values_file:
            cmd.extend(['-f', values_file])
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Successfully upgraded release '{release_name}':")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error upgrading Helm release '{release_name}': {e.stderr}")

#uninstall Helm release
def uninstallHelmRelease(release_name, namespace): #this only deletes from specified namespace
    try:
        cmd = ['helm', 'uninstall', release_name, '--namespace', namespace]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Successfully uninstalled release '{release_name}':")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error uninstalling Helm release '{release_name}': {e.stderr}")

if __name__ == "__main__":
    # call functions as __main__
    getHelmRelease()
    
    # Install a new Helm release
    release_name = "my-new-release"
    chart_name = "bitnami/nginx"  # Example chart name from Bitnami
    namespace = "default"
    newHelmRelease(release_name, chart_name, namespace)
    
    upgradeHelmRelease(release_name, chart_name, namespace)

    uninstallHelmRelease(release_name, namespace)
