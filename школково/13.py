import ipaddress
from ipaddress import *
#                              Номер компьютера в сети
net= ip_network('188.134.59.77/255.255.255.192',0)
numbe = int(ip_address('188.134.59.77'))-int(net.network_address)
print(numbe)

net = ip_network('145.125.105.101/255.255.248.0',0)
nb = int(ip_address('145.125.105.101')) - int(net.network_address)
print(nb)


ip = ip_address('7.120.112.5')
network = ip_network('7.120.96.0/255.255.224.0')
host = int(ip) - int(network.network_address)
print(host)

ip = ip_address('108.23.252.178')
net = ip_network('108.23.252.176/255.255.255.248')
new = int(ip) - int(net.network_address)
print(new)


ip = ip_address('134.242.26.155')
net = ip_network('134.242.26.128/255.255.255.192')
new = int(ip) - int(net.network_address)
print(new)


ip = ip_address('166.229.54.0')
net = ip_network('166.229.0.0/255.255.128.0')
new = int(ip) - int(net.network_address)
print(new)

#                           IP-Адреса

net = ip_network('186.215.243.5/255.255.192.0',0)
print(str(net[-2]).replace('.',''))

net = ip_network('191.128.68.83/255.192.0.0',0)
print(str(net[-2]).replace('.',''))

net = ip_network('127.204.113.250/255.255.254.0',0)
print(str(net[1]))

#                   Подсчет количества адресов в сети

net = ip_network('10.18.134.17/255.255.255.128',0)
total = net.num_addresses - 2
print(total)

net = ip_network('88.147.254.128/255.255.255.128',0)
tot = net.num_addresses - 2
print(tot)

ip = ip_address('200.14.152.118')
net = ip_address('200.14.152.112')
for mask in range(33):
    network = ip_network(f"{ip}/{mask}",0)
    if net == network.network_address:
        print(network.num_addresses)


# номер с пробника

network = ipaddress.ip_network('0.0.0.0/255.255.224.0',0)
print(network.num_addresses-2)


тге =  ip_network('142.111.21.144/255.255.255.240')
total = тге.num_addresses
print(total)

print(202&192)

net= ip_network('127.98.13.192/255.255.255.192')
totol = net.num_addresses
print(totol)

c = 0
net = ip_network('164.148.22.144/255.255.255.240')
for i in net:
    if bin(int(i))[2:].count('0')>18:
        c += 1
print(c)

cot = 0
net = ip_network('134.127.52.160/255.255.255.224')
for i in net:
    if bin(int(i))[2:].count('1') % 2 == 0:
        cot += 1
print(cot)

count =  0
net = ip_network('164.128.132.192/255.255.255.224')
for i in net:
    if bin(int(i))[2:].count('0') > 22:
        count += 1
print(count)


ip = ip_address("231.25.4.185")
net = ip_address("231.25.4.176")
for mask in range(33):
   network = ip_network(f"{ip}/{mask}", 0)
   if net == network.network_address:
       print(network.num_addresses)


#                   Определение адреса сети

net = ip_network('68.232.57.148/255.255.252.0',0)
print(bin(int(net.network_address))[2:].zfill(32).count('0'))

#                   Определение маски


for mask in range(1,33):
    net = ip_network(f'97.122.41.0/{mask}',0)
    print(net,net.netmask)

for mask in range(1, 33):
    net = ip_network(f'125.170.90.148/{mask}', strict=False)  # Создаем сеть с текущим количеством единиц в маске
    # Извлекаем третий байт маски, преобразуем в двоичное число и дополняем нулями до 8 бит
    third_byte_mask = bin(int(net.netmask))[2:].zfill(32)[16:24]
    print(net, third_byte_mask)












