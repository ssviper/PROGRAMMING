
import json
if __name__ == "__main__":
	facts = {
		'hostname': 'nxosv',
		'os': '7.3',
		'location': 'San_Jose'
}
#print facts dictionary
print (facts)
#print json.dumps(facts, indent=4)
print (json.dumps(facts, indent=4))
#print facts['os']
print (facts['os'])
    