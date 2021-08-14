def print_facts(facts):
    
    #Print two facts from from facts dictionary
    

    platform = facts.get('platform', 'unknown platform')
    print ('platform', platform)

    print ('os', facts['os'])

if __name__ == "__main__":

        facts = {'os': '7.2', 'fqdn': 'cisco.com', 'location': 'sjc', 'vlans_list':[1, 5, 10], 'neighbors': ['s2', 's3']}

        # Call print facts function
        print_facts(facts)

        #Extract neightbors from facts dict and assign to new variable
        neighbors = facts['neighbors']

        #Print each neighbor
        for item in neighbors:
            print (item)
