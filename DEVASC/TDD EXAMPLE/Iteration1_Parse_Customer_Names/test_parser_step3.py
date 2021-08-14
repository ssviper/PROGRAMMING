import unittest

class TestParse(unittest.TestCase):
    def test_parse_cust_name(self):
        cp = ConfigurationParser()
        expected_names = ['CUSTOMER_A', 'CUSTOMER_B']
        parsed_names = cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)

import re

class ConfigurationParser:
    deviceConfig = open("config.txt", "r").read()
    def parseCustomerNames(self):
        deviceConfig = open("config.txt", "r").read()
        customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, deviceConfig)
        return customerNames