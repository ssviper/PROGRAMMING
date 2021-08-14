#type python
#copy and paste the three lines below into the Python Interpreter


facts = {'platform': 'nexus', 'model': '9396', 'hostname': 'NX01','vendor': 'cisco', 'vlans': ['1', '5', '10']}

import json

print (json.dumps(facts, indent=4))

