
def vlan_exists(vlan_id):
    vlans_list = [1, 3, 10, 20]
    return vlan_id in vlans_list

if __name__ == "__main__":
    vlans = [5, 8, 10, 15, 20]
    for vlan in vlans:
        print (vlan, vlan_exists(vlan))
         