#!/usr/bin/env python

# Filename:                     restconf-tutorial.py
# Command to run the program:   python restconf-tutorial.py
# Make sure to run in terminal windows and not run code

import requests
import json

# Suppress HTTPS warnings
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Print a stream of bytes as pretty JSON
def printBytesAsJSON(bytes):
	print(json.dumps(json.loads(bytes), indent=2))

 # Retrieve configuration through RESTCONF
response = requests.get(
	url = 'https://192.168.69.86/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=0%2F0%2F1',
	auth = ('jfriedrich', '867GeneSimmon$'),
	headers = {
		'Accept': 'application/yang-data+json'
	},
	verify = False)

# Pretty print our JSON response
printBytesAsJSON(response.content)