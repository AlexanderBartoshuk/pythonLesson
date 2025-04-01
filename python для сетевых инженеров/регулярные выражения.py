import re

int_line = 'Саша очень любит заниматься программированием и хочет стать data science разработчиком'
match = re.search(r'science', int_line)

print(match)

int_lines = '  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'
match = re.search(r'BW \d+',int_lines)
print(match.group())

log2 = 'Oct  3 12:49:15.941: %SW_MATM-4-MACFLAP_NOTIF: Host f04d.a206.7fd6 in vlan 1 is flapping between port Gi0/5 and port Gi0/16'
print(re.search(r'Host (\S+) in vlan (\d+) is flapping between port (\S+) and port (\S+)', log2).groups())