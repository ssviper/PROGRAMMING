# In this task you are going to use the Python Module "cisco.py"

# Connect to the Python Interpreter and enter the following

import cisco

# Then enter

platforms = cisco.platforms

print (platforms)

#You should see the following output

['nexus', 'catalyst', 'asr', 'asa']

#Then type the following

cisco.vlan_exists(10)

#You should see this below

True