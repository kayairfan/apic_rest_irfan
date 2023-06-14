import requests
import json
from login import get_token
requests.packages.urllib3.disable_warnings()


def list_devices():
    token = get_token()
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
    #url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/ip-address/10.10.20.176"
    headers= {'x-auth-token': f'{token}','content-type': 'application/json'}
    response = requests.get(url=url,headers=headers,verify=False)
    response_json = json.dumps(response.json(),indent=4)
    return response_json

if __name__ == '__main__':
    data = list_devices()
    data = json.loads(data)
    #print(data)
    for i in data['response']:
        for key,value in i.items():
            if i['managementIpAddress'] == "10.10.20.176":
                print(i['upTime'])
                break