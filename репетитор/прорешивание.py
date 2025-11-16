from itertools import * 
from ipaddress import  ip_network, ip_address
from turtle import *
from string import *
#
#a = 'dc de da ea cf eg ag ab gb fb'.split()
#b = '36 4567 17 257 246 125 234'.split()
#print('1 2 3 4 5 6 7')
#for p in permutations('abcdefg'):
#    if all(str(p.index(c2)+1) in b[p.index(c1)] for c1,c2 in a):
#        print(*p)
#        break
#
#
#def fe(x,y,z,w):
#    return (x == (w or y)) or ((w <= z) and (y <= w))
#
#for a,b,c,d,e,f,g in product([0,1],repeat=7):
#    table = ((1,a,b,1,0),
#             (c,d,e,1,0),
#             (1,f,1,g,0))
#    
#    if len(table) == len(set(table)):
#        for p in permutations('xyzw',r=4):
#            if all(fe(**dict(zip(p,line))) == line[-1] for line in table):
#                print(*p)
#                break
#
#for i in range(1000):
#    n = bin(i)[2:]
#    if i % 2 == 0:
#        n = n + '00'
#    else:
#        n = n + '11'
#
#    r = int(n,2)
#    if r > 115:
#        print(i)
#        break
#
#
#a = list(product('АОУ',repeat=5))
#print(*a[209])

#ip = '162.198.0.157'
#mask = '255.255.224.0' 
#net = ip_network(f'{ip}/{mask}',0)
#print(int(ip_address(ip))-int(net.network_address))

#
#from ipaddress import ip_network, ip_address
#ipu = '147.222.199.75'
#ipu_modified = '147.222.222.147'
#for mask in range(32, 0, -1):
#    network = ip_network(f'{ipu}/{mask}', 0)
#    count = 0
#    if ip_address(ipu_modified) in network:
#        for ip in network:
#            if bin(int(ip)).count('1') == 14:
#                count += 1
#    if count > 0:
#        print(count)
#        break
        
a = []
for x in '012345678':
    for y in '012345678':
        t = int('88'+x+'4'+y,9) + int('7'+x+'44'+y,11)
        if t % 61 ==0:
            a.append(t)
print(min(a)/61)
