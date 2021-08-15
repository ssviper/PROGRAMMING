import re
class ConfigurationParser:
    deviceConfig = open("config.txt".read())
    def parseCustomerVlan(self, customerName):
        intPattern = (
            r"interface GigabitEthernet0\/0\. ([0-9]+)\n encapsulation"
            r"dot1Q [0-9]+\n ip vrf forwarding %s"
            % (customerName)
        )

        allCustomerSubInterfaces = re.search(intPattern, self.deviceConfig)
        return int(allCustomerSubInterfaces.group(1))

import unittest

class TestParse(unittest.TestCase):
    def test_parse_cust_name(self):...
    def test_parse_cust_vlan(self):...
cp = ConfigurationParser()
        customer_name = "CUSTOMER_A"
        expected_vlan = 100
        parsed_vlan = cp.parseCustomerVlan(customer_name)
        self.assertEqual(expected_vlan, parsed_vlan)