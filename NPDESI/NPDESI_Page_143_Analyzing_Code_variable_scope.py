
ipaddr = '10.1.10.1'
mask = '24'

def get_ip(ip):
    print ('Function 1: ', ip)
    print ('Function 2: ', mask)
    print ('Function 3: ', ipaddr)
    print ('Function 4: ', mask)
    
if __name__ == "__main__":
    print ('Main 1: ', ipaddr)
    print ('Main 2: ', mask)
    print ('Main 3: ', ip)
    ipaddr = '200.100.1.1'
    get_ip(ipaddr)
      

