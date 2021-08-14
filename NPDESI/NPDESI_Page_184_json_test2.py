facts = '{"hostname": "nxosv", "os": "7.3", "location": "San_Jose"}'
print (facts)
print (type(facts))
import json
#print facts['os']
#TypeError: string indices must be intergers, not str
factsd = json.loads(facts)
print (json.dumps(factsd, indent=4))