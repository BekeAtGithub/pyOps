#executes an ansible playbook - sets ansible runner parameters
#add inventory, add extra variables
#checks the status and prints results

#guide**** rplace "playbook_directory" "playbook_path" "inventory_path"
#with actual values from your ecosystem/infrastructure

import ansible_runner
import os

#have to install ansible with "pip install ansible ansible-runner"


# this does not create a playbook, it runs an existing one
def runPlaybook(playbook_path, inventory_path=None, extra_vars=None):
    try:
        # Set up Ansible Runner parameters
        runner_args = {
            'private_data_dir': '/tmp/ansible_runner',  # Directory for temporary data
            'playbook': playbook_path,
        }
        
        # Add inventory if provided
        if inventory_path:
            runner_args['inventory'] = inventory_path
            
        # Add extra vars if provided
        if extra_vars:
            runner_args['extravars'] = extra_vars
            
        # Run the playbook
        result = ansible_runner.run(**runner_args)
        
        # Check the status and print results
        if result.status == "successful":
            print(f"Playbook '{playbook_path}' executed successfully.")
            print("Playbook Output:")
            print(result.stdout.read())
        else:
            print(f"Playbook '{playbook_path}' failed with status: {result.status}")
    
    except Exception as e:
        print(f"Error running playbook '{playbook_path}': {str(e)}")

# gets and lists the playbooks available in a specific directory
def getPlaybooks(playbook_directory):
    try:
        playbooks = [f for f in os.listdir(playbook_directory) if f.endswith('.yml') or f.endswith('.yaml')]
        if playbooks:
            print("Available Playbooks:")
            for playbook in playbooks:
                print(f"- {playbook}")
        else:
            print("No playbooks found in the specified directory.")
    except Exception as e:
        print(f"Error listing playbooks: {str(e)}")

if __name__ == "__main__":
    # runs functions as main
    playbook_directory = "./playbooks"
    getPlaybooks(playbook_directory)

    playbook_path = "./playbooks/example_playbook.yml"
    inventory_path = "./inventory/hosts.ini"
    extra_vars = {"variable_name": "variable_value"}
    runPlaybook(playbook_path, inventory_path, extra_vars)
