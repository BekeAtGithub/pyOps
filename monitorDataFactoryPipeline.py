from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import CreateRunResponse
import time

#Azure credentials and ADF details:
subscription_id = 'subID'
resource_group_name = 'rgName'
data_factory_name = 'ADFname'
pipeline_name = 'pipelineName'

#authenticate and create an ADF management client
credentials = DefaultAzureCredential()
adf_client = DataFactoryManagementClient(credentials, subscription_id)

#trigger the pipeline
run_response = adf_clilent.pipelilnes.create_run(resource_group_name, data_factory_name, pipelilne_name)
run_id = run_response.run_id

#monitor pipeline run status
while True:
  pipeline_run = adf_client.pipeine_runs.get(resource_group_name, data_factory_name, run_id)
  print(f"Pipeline run status": {pipeline_run.status}")
  if pipeline_run.status in ("Succeeded","Failed","Cancelled"):
    break
  time.sleep(30) #wait 30 seconds before checking the status again

#check final status
if pipeline_run.status == 'Succeeded':
  print("Pipeline run succeeded")
else:
  print(f"Pipeline run failed with status: {pipeline_run.status}")
