import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()


def get_token():
    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    response = requests.post(url=url, auth=HTTPBasicAuth(username="devnetuser", password="Cisco123!"), verify=False)
    token = response.json()['Token']
    return token


def main():
    pass


if __name__ == "__main__":
    print(get_token())
