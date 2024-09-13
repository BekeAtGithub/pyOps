from urllib import response
import urllib3
import json

urllib3.disable_warnings()

# MODIFY URL IP TO LOCAL IP OF SERVER - DEFAULT 0.0.0.0 
BASE_URL = "https://0.0.0.0:443/"

def sdwan_authenticate(BASE_URL, username, password):
    auth_url = f'{BASE_URL}J_security_check'
    payload = f'j_username={username}&j_password={password}'
    headers = {
        'Content-Type': '<url extension>',  # REPLACE URL EXTENSION WITH WHATEVER PATH COMES AFTER THE BASE_URL
    }

    response = requests.post(auth_url, headers=headers, data=payload, verify=False)
    cookie = response.cookies.get_dict()
    if response.status_code == 200:
        return 'AUTH_DONE', cookie
    else:
        return 'AUTH_ERROR', response.status_code

def sdwan_get_token(BASE_URL, cookies):
    token_url = f'{BASE_URL}dataservice/client/token'
    payload={}
    headers={
        'Cookie': f'JSessionID={cookies}'
    }
    
    response = requests.get(token_url, headers=headers, data=payload, verify=False)
    if response.status_code == 200:
        return str(response.text)
    else:
        return 'TOKEN_RETRIEVAL FAILURE'

def sdwan_get_all_devices(BASE_URL, cookies, TOKEN):
    all_device_url = f'{BASE_URL}datasevice/device'
    payload = {}
    headers = {
        'Cookie': f'JSessionID={cookies}',
        'X-XSRF-TOKEN': TOKEN,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def pretty_print_device_data(data):
    console = Console()
    table = Table(show_header=True, header_style='bold magenta')
    table.add_column('HOSTNAME')
    table.add_column('SYSTEM-IP')
    table.add_column('REACHABILITY')
    table.add_column('STATUS')
    table.add_column('DEVICE-TYPE')
    table.add_column('SITE-ID')
    table.add_column('OS-VERSION')
    table.add_column('OMP-PEERS')
    table.add_column('CONTROL-SESSIONS')
    table.add_column('BFD-SESSIONS-UP')

    for device in data:
        if 'ompPeers' not in device:
            ompPeers = 'None'
        else:
            ompPeers = device['ompPeers']

        if 'controlConnections' not in device:
            controlConnections = 'None'
        else:
            controlConnections = device['controlConnections']
        
        if device['reachability'] == 'Unreachable':
            reach = f'[red]unreachable[/red]'
        else:
            reach = f'[green]{device["reachability"]}[/green]'
        
        if 'bfdSessionsUp' in device:
            bfd_sess = device['bfdSessionsUp']
        else:
            bfd_sess = 'None'

        table.add_row(device['host-name'], device['system-ip'], reach, device['status'], device['device-model'],
                      device['site-id'], device['version'], ompPeers, controlConnections, str(bfd_sess))
    console.print(table)

def main():
    username = 'admin'
    password = 'SecurePass123!'

    # AUTHENTICATE WITH VMANAGE
    print('[AUTHENTICATING]')
    auth_status, cookie_or_code = sdwan_authenticate(BASE_URL, username, password)
    if 'DONE' in auth_status:
        print(f'[AUTHENTICATION STATUS] SUCESS {auth_status.lower()} {cookie_or_code}')
    else:
        print(f'[AUTHENTICATION STATUS] FAILURE {auth_status} {cookie_or_code}')

    # RETRIEVE TOKEN USED IN SUBSEQUENT REQUESTS
    print('[TOKEN RETRIEVAL]')
    token = sdwan_get_token(BASE_URL, cookie_or_code['JSessionID'])
    print(f'[TOKEN RETRIEVAL] TOKEN: {token}')

    print('[DEVICE-DATA RETREIVAL]')

    # RETRIEVE TOKEN USED IN ALL DEVICES
    response_dict1 = sdwan_get_all_devices(BASE_URL, cookie_or_code['JSessionID'], token)
    print(json.dumps(response_dict1['data'], indent=4))
    pretty_print_device_data(response_dict1['data'])


if __name__ == '__main__':
    main()
