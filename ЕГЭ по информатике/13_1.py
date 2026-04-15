from ipaddress import * 
# сколько адресов 
k = 0 
for ip in ip_network('172.16.96.0/255.255.224.0',0):
    ip_2 = f'{ip:b}'
    if ip_2.count('1') % 2 == 0:
        k += 1
print(k)

# наибольший адрес, который может быть назначен компьютеру

net = ip_network('190.202.83.62/255.255.252.0',0)
print(net[-2])

# net= ip_network('46.29.170.214/255.255.128.0',0)
# for ip in net.hosts():
#     a = [int(x) for x in str(ip).split('.')]
#     x,y,z,w = a
#     if (x == z + y +w ) or (y == x + z + w) or (z == x + y + w) or (w == x + y + z):
#         print(ip)

net = ip_network('172.95.116.174/255.255.192.0',0)
for ip in net:
    ip_3 = f'{ip:b}'
    if ip_3.count('1') % 5 == 0:
        print(ip)
        break


net = ip_network('45.172.106.203/255.255.252.0',0)
print(net[1])

# МАСКИ 

for mask in range(33):
    net = ip_network(f'84.32.84.32/{mask}',0)
    if f'{net[-2]:b}'.count('1') % 19 == 0:
        print(mask)
        break

k = 0 
for ip in ip_network('172.16.80.0/0.0.7.255',0):
    ip2 = f'{ip:b}'
    if ip2.count('1') % 3 != 0:
        k += 1
print(k)

k = 0 
for ip in ip_network('192.168.32.64/255.255.255.192',0):
    ip2 = f'{ip:b}'
    if ip2[-3] == ip2[-1] == '1' and ip2[-2] == '0':
        k += 1
print(k)

