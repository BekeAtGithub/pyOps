#uses Argo CD - rest API to list apps, retreive details and forces sync

import requests
#install requests with pip
#need Argo CD API server URL and token with right permissions

# Argo CD API URL and token - use a vault for yuour token, dont store it here in plain text
ARGOCD_API_URL = "https://<your-argocd-server-url>/api/v1"
ARGOCD_AUTH_TOKEN = "<your-argocd-auth-token>"

# Header setup for authentication
headers = {
    "Authorization": f"Bearer {ARGOCD_AUTH_TOKEN}",
    "Content-Type": "application/json"
}

# lists all the applications that argocd is connected with
def getApps():
    url = f"{ARGOCD_API_URL}/applications"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        applications = response.json().get("items", [])
        for app in applications:
            print(f"Application Name: {app['metadata']['name']}, Project: {app['spec']['project']}")
    else:
        print(f"Failed to list applications. Status Code: {response.status_code}, Error: {response.text}")

# get details from the applications that are pulled by "getApps"
def getAppDetails(app_name):
    url = f"{ARGOCD_API_URL}/applications/{app_name}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        app = response.json()
        print(f"Application Name: {app['metadata']['name']}")
        print(f"Project: {app['spec']['project']}")
        print(f"Sync Status: {app['status']['sync']['status']}")
        print(f"Health Status: {app['status']['health']['status']}")
        # Add more fields as needed
    else:
        print(f"Failed to get application details. Status Code: {response.status_code}, Error: {response.text}")

# Function to synchronize an application
def syncApp(app_name):
    url = f"{ARGOCD_API_URL}/applications/{app_name}/sync"
    data = {
        "revision": "HEAD",  # Sync to the latest commit, adjust as needed
        "prune": False,        # Set True if you want to remove resources that are no longer defined in Git
        "dryRun": False        # Set True if you want to preview the changes
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print(f"Application '{app_name}' synchronized successfully.")
    else:
        print(f"Failed to synchronize application. Status Code: {response.status_code}, Error: {response.text}")

if __name__ == "__main__":
    # call functions as __main__
    getApps()
  
    application_name = "<your-application-name>"
    getAppDetails(application_name)

    syncApp(application_name)
