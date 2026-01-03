from ipaddress import * 

net = ip_network('226.185.90.162/255.255.252.0',0)
print(int(ip_address('226.185.90.162'))-int(net.network_address))


c = 0
for x in range(2**3):
    if (15+bin(x)[2:].count('1')) % 4 != 0:
        c += 1
print(c)

from ipaddress import ip_network, ip_address
ip_b = ip_address('157.220.184.230')
for mask in range(32, -1, -1):
    net = ip_network(f'157.220.185.237/{mask}',0)
    if ip_b in net:
        print(sum(bin(int(ip)).count('1')==15 for ip in net))
        break

from itertools import product
s=product('01', repeat = 10)
k=0
for i in s:
    if i.count('1')==3:
        k+=1
print(k)


#for m in range(0,255):
#    if 64 == 112 & m:
#        print(bin(m),m)
#
#for x in range(0,255):
#    if 80 == 83 & x:
#        print(bin(x),x)
for x in range(0,255):
    if 192 == 203 & x:
        print(bin(x)[2:].count('1'),x)

