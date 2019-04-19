# This sample code for educational purposes only.
# It is intentionally written to be as simple as possible.
# For a better example of how to structure your code, take a look at 01_network_device


# import the libraries that we need to use
import requests
from requests.auth import HTTPBasicAuth
import json

# Specify the url to get a token
url='https://sandboxdnac2.cisco.com/api/system/v1/auth/token'

# Performs a POST on the specified url.
result = requests.post(url=url, auth=HTTPBasicAuth("devnetuser", "Cisco123!"), verify=False)

# get the token for use in future calls
token = result.json()["Token"]

# prepare to use token in the header
headers = {
    "x-auth-token": token
}

# Specify the url to get the list of devices
devicelisturl='https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'


# Performs a GET on the specified url.
# Pass token in the header
response = requests.get(url=devicelisturl, headers=headers, verify=False)

# print the list of devices
print(response.text)
