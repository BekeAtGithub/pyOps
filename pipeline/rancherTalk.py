#uses Rancher server API to manage k8s clusters 

import requests
#you need to install requests with pip- make sure you know your
#rancher API URL and API key and the cluster ID you want to interact with 

#rancher endpoint/API key (use variables for a key vault) - so basically this script 
RANCHER_API_URL = "https://<your-rancher-server-url>/v3"
API_ACCESS_KEY = "<your-access-key>"
API_SECRET_KEY = "<your-secret-key>"

# this function lists all clusters connected to the Rancher server 
def getClusters():
    url = f"{RANCHER_API_URL}/clusters"
    response = requests.get(url, auth=(API_ACCESS_KEY, API_SECRET_KEY))
    
    if response.status_code == 200:
        clusters = response.json().get("data", [])
        for cluster in clusters:
            print(f"Cluster Name: {cluster['name']}, Cluster ID: {cluster['id']}")
    else:
        print(f"Failed to get clusters. Status Code: {response.status_code}, Error: {response.text}")

# get information on the clusters we pulled from the getClusters function
def getClusterDetails(cluster_id):
    url = f"{RANCHER_API_URL}/clusters/{cluster_id}"
    response = requests.get(url, auth=(API_ACCESS_KEY, API_SECRET_KEY))
    
    if response.status_code == 200:
        cluster = response.json()
        print(f"Cluster Name: {cluster['name']}")
        print(f"State: {cluster['state']}")
        print(f"Cluster Type: {cluster['clusterType']}")
        # Add more fields as needed
    else:
        print(f"Failed to get cluster details. Status Code: {response.status_code}, Error: {response.text}")

# provision a new cluster
def provCluster(cluster_name):
    url = f"{RANCHER_API_URL}/clusters"
    headers = {"Content-Type": "application/json"}
    data = {
        "name": cluster_name,
        "type": "cluster",
        "rancherKubernetesEngineConfig": {
            #can add additional configuration parameters here
            "kubernetesVersion": "v1.22.6-rancher1-1"
        }
    }
    
    response = requests.post(url, json=data, headers=headers, auth=(API_ACCESS_KEY, API_SECRET_KEY))
    
    if response.status_code == 201:
        print(f"Cluster '{cluster_name}' created successfully.")
    else:
        print(f"Failed to create cluster. Status Code: {response.status_code}, Error: {response.text}")

if __name__ == "__main__":
    # calls the functions of our program
    getClusters()
    
    cluster_id = "<your-cluster-id>"
    getClusterDetails(cluster_id)
    
    new_cluster_name = "my-new-cluster"
    provCluster(new_cluster_name)
