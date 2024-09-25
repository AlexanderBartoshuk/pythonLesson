#  tabulate

from tabulate import tabulate

sh_ip_int_br = [('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
('Loopback0', '10.1.1.1', 'up', 'up'),
('Loopback100', '100.0.0.1', 'up', 'up')]

print(tabulate(sh_ip_int_br))

colims = ["Interface","IP","Status","Protocol"]
print(tabulate(sh_ip_int_br, headers=colims))


first_dict = [{'IP': '15.0.15.1',
  'Interface': 'FastEthernet0/0',
  'Protocol': 'up',
  'Status': 'up'},
 {'IP': '10.0.12.1',
  'Interface': 'FastEthernet0/1',
  'Protocol': 'up',
  'Status': 'up'},
 {'IP': '10.0.13.1',
  'Interface': 'FastEthernet0/2',
  'Protocol': 'up',
  'Status': 'up'},
 {'IP': '10.1.1.1',
  'Interface': 'Loopback0',
  'Protocol': 'up',
  'Status': 'up'},
 {'IP': '100.0.0.1',
  'Interface': 'Loopback100',
  'Protocol': 'up',
  'Status': 'up'}]

print(tabulate(first_dict,headers="keys", tablefmt='grid', stralign='center'))
#print(tabulate(first_dict,headers="keys", tablefmt='html'))
#print(tabulate(first_dict,headers="keys", tablefmt=''))