import ipaddress
from pprint import pprint
subnet1 = ipaddress.ip_network('80.0.1.0/28')


int1 = ipaddress.ip_interface('10.0.1.1/24')

london_co = {'r1': {'hostname': 'london_r1', 'location': '21 New Globe Walk', 'vendor': 'Cisco', 'model': '4451', 'IOS': '15.4', 'IP': '10.255.0.1'}, 'r2': {'hostname': 'london_r2', 'location': '21 New Globe Walk', 'vendor': 'Cisco', 'model': '4451', 'IOS': '15.4', 'IP': '10.255.0.2'}, 'sw1': {'hostname': 'london_sw1', 'location': '21 New Globe Walk', 'vendor': 'Cisco', 'model': '3850', 'IOS': '3.6.XE', 'IP': '10.255.0.101'}}
pprint(london_co)
