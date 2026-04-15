import sys
from functools import *
from fnmatch import fnmatch
from itertools import *
from ipaddress import  ip_network, ip_address
from turtle import *
from string import *
from sys import setrecursionlimit
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
        
# a = []
# for x in '012345678':
#     for y in '012345678':
#         t = int('88'+x+'4'+y,9) + int('7'+x+'44'+y,11)
#         if t % 61 ==0:
#             a.append(t)
# print(min(a)/61)

#
# a = '234 136 12 157 467 25 45'.split()
# b = 'ad db bf fg gc ce ea ge fd'.split()
# print('1 2 3 4 5 6 7')
# for p in permutations('abcdefg'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in  b):
#         print(*p)


#
# def f(x,y,z,w):
#     return (y or x) == ((y <= w) or not(z))
#
# table = ((1,0,0,0,0),
#          (0,1,0,0,0),
#          (1,0,1,0,0))
#
# if len(table) == len(set(table)):
#     for p in permutations('xyzw',r=4):
#         if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#             print(*p)

# def troich(f,osn):
#     a = ''
#     while f > 0:
#         a = (f % osn) + a
#         f //= osn
#     return a
#
#
# for i in range(1,1000):
#     x = troich(i,3)
#     if x % 3 == 0:
#

# setrecursionlimit(50000)
#
#
# def f(x,y):
#     if x > y or x == 27:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x+3,y) + f(x+5,y) + f(x**2,y)
#
# print(f(3,16) * f(16,51))
#
#
# def f(x,y,m):
#     if x + y >= 133:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#
#     h = [f(x+1,y,m-1), f(x*4,y,m-1),f(x,y+1,m-1), f(x,y*4,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print('20)', *[s for s in range(1,126) if f(7,s,3) and not f(7,s,1)])
# print('21)', *[s for s in range(1,126) if f(7,s,4) and not f(7,s,2)])


# def f(x):
#     return not(x % a == 0) <= ((x % 28 == 0) <= (not(x % 49 ==0)))
#
# for a in range(10000000000000,0,-1):
#     if all(f(x) for x in range(1,10000)):
#         print(a)

# a = '2346 16 1678 17 68 1235 34 35'.split()
# b = 'ab bd dg ge eh hf fc ac bc be ec'.split()
# print('1 2 3 4 5 6 7 8')
# for p in permutations('abcdefgh'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)

# def f(x,y,z,w):
#     return not(w == y) and (z <= w) and not(x)
#
# for a,b,c,d,e,g in product([0,1],repeat=6):
#     table = ((a,b,c,1,1),
#              (1,d,1,e,1),
#              (0,g,1,0,1))
#
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw',r=4):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)
#
#
#
#
#
# s = 3 * 256**320 - 2*64**290 + 4**250 - 1023
# a = ''
# while s > 0:
#     a = str(s % 4) + a
#     s //= 4
# print(len(a))
#




# def f(x,y):
#     if x <= 19: return y % 2 == 0
#     if y == 0: return 0
#     h = [f(x-4,y-1), f(x-6,y-1), f(x//2,y-1)]
#     return any(h) if y % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(20,100) if f(s,2)])
# print('20)', *[s for s in range(20, 100) if f(s, 3) and (not f(s, 1))])
# print('21)', *[s for s in range(20,100) if f(s,4) and not f(s,2)])
#
# print(bin(167).count('0'))

#
# a = '3567 3467 12 26 17 124 125'.split()
# b = 'аб ав ве бд дк ек вг гд бв де'.split()
# print('1 2 3 4 5 6 7')
# for p in permutations('абвгдек'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)
#
# def f(x,y,z,w):
#     return ((w <= y) <= x) or not(z)
#
# for a,b,c,d,e,g,h in product([0,1],repeat=7):
#     table = ((a,b,1,c,0),
#              (d,0,e,g,0),
#              (h,1,0,0,0))
#
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw',r=4):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)
#                 break


# tracer(0)
# lt(90)
# screensize(20000,20000)
# k = 20
#
# for i in range(95):
#     fd(95*k)
#     rt(72)
#     back(5*k)
#
# up()
#
# for x in range(-100,150):
#     for y in range(-100,150):
#         goto(x*k,y*k)
#         dot(3)
# done()
#
# s = 3*16**8 - 4**5 + 3
# a = ''
# while s >0:
#     a = str(s % 4) + a
#     s //= 4
#
# print(a.count('3'))
#
#
# c = 0
# for x in product('01234',repeat=5):
#     s = ''.join(x)
#     if s[0] != '0':
#         if (s.count('0') + s.count('2') + s.count('4')) <= 3:
#             c += 1
# print(c)
#



#
# for x in range(1,1000):
#     n = str(bin(x)[2:])
#     if int(n[-1]) == int(n[-1]):
#         n += '0'
#     else:
#         n += '1'
#     if n[-1] == n[-2]:
#         n += '0'
#     else:
#         n += '1'
#
#     r = int(n,2)
#     if r > 93:
#         print(x)
#         break
#
#
#
# def f(x,y,m):
#     if x * y >= 123:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#
#     h = [f(x+2,y,m-1), f(x*2,y,m-1),f(x,y+2,m-1), f(x,y*2,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(1,41) if f(3,s,2)])
# print('20)', *[s for s in range(1,41) if f(3,s,3) and not f(3,s,1)])
# print('21)', *[s for s in range(1,41) if f(3,s,4) and not f(3,s,2)])
#


# a = '58 34 28 268 17 478 568 13467'.split()
# b = 'ав ае ез зж жб бг гд дв ед зд жд'.split()
# print('1 2 3 4 5 6 7 8')
# for p in permutations('абвгдежз'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)
#
# def f(x,y,z):
#     return (x or y) <= (x == z)
#
# for a,b,c in product([0,1],repeat=3):
#     table = ((a,0,b,0),
#              (c,0,0,0))
#
#     if len(table) == len(set(table)):
#         for p in permutations('xyz',r=3):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)
#
#
#
#
# coun = 0
# for x in product('012345',repeat=5):
#     s = ''.join(x)
#     if (s[0] == '024' and s[1] == '135') or (s[0] == '135' and s[1] == '024') or (s[1] == '024' and s[2] == '135') or (s[1] == '024' and s[2] == '135') or (s[2] == '024' and s[3] == '135') or (s[2] == '135' and s[3] == '024') or(s[3] == '024' and s[4] == '135') or (s[3] == '135' and s[4] == '024') or (s[4] == '024' and s[5] == '135') or (s[4] == '135' and s[5] == '024'):
#         coun += 1
#         print(coun)
#
# co = 0
# ip_net = ip_network('228.117.236.0/255.255.240.0',0)
# for x in ip_net:
#     ip = f"{x:b}"
#     if ip.count('1') % 5 != 0:
#         co += 1
# print(co)
#
# p = list(range(3,15))
# q = list(range(14,26))
# a = list(range(200))
# for x in range(1,100):
#     if ((x in p) == (x in q)) <= (not(x in a)):
#         a.remove(x)
#         print(len(a))
#
#
#
# def f(x,y):
#     if x < y: return 0
#     if x == y: return 1
#     else:
#         return f(x-2,y) + f(x//2,y)
# print(f(32,14)*f(14,1))
#
#
# def f(x,y,m):
#     if x + y >= 131: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x+2,y,m-1), f(x*2,y,m-1),f(x,y+2,m-1), f(x,y*2,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(1,123) if f(11,s,2)])
# print('20)', *[s for s in range(1,123) if f(11,s,3) and (not(f(11,s,1)))])
# print('21)', *[s for s in range(1,123) if f(11,s,4) and (not(f(11,s,2)))])
#
#
# a = 5 * 7**3 + 2*5**2*7**2 + 3*5**3*7
# s = ''
# while a > 0:
#     s = str(a % 7) + s
#     a //= 7
# print(s)

# a = '247 148 578 126 38 47 136 235'.split()
# b = 'bh hf fd dc ce ea ab ah fg eg gc'.split()
# print('1 2 3 4 5 6 7 8')
# for p in permutations('abcdefgh'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)
#         break
#
# def f(x,y,z,w):
#     return ((not(x) and w) <= y) and (y <= (z and (not(y))))
#
# for     a,b,c,d in product([0,1],repeat=4):
#     table = ((0,a,1,1,1),
#              (1,0,b,0,1),
#              (1,c,d,0,1))
#
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)
#                 break
#
#
#
# for i in range(27,100):
#     n = bin(i)[2:]
#     if n.count('1') % 2 == 0:
#         n = '0' + n[:-2] + '10'
#     else:
#         n = '1' + n[:-2] + '11'
#
#     r = int(n,2)
#     if i > 27:
#         print(r)
#         break
#
#
#
# c = 0
# for x in product('0123456',repeat=7):
#     s = ''.join(x)
#     if s[0] != '0':
#         if (s.count('2') + s.count('4') + s.count('6') + s.count('0'))  == 2:
#             c += 1
# print(c)
#
# a = 81**5 + 3**30 - 27
# s = ''
# while a > 0:
#     s = str(a % 9) + s
#     a//=9
# print(s.count('8'))
#
# def f(x):
#     if x < 0: return -x
#     if x % 2 == 0:
#         return 2*x + 1 + f(x-3)
#     if x % 2 == 1:
#         return 4*x + 2*f(x-4)
# print(f(33))
#
# def f(x,y):
#     if x > y: return 0
#     if x == y: return 1
#     else:
#         return f(x+1,y) + f(x+2,y) + f(x*2,y)
#
# print(f(5,13) * f(13,25))
#
# p = list(range(66,67))
# o = list(range(32,125))
# t = list(range(30,492))
# a = []
# for x in range(501):
#     if (x not in a) <= ((x in p) or (x not in o) or (x not in t)):
#         a.append(x)
# print(len(a))
#
# def f(x,y):
#     if x >= 512: return y % 2 == 0
#     if y == 0: return  0
#     h = [f(x+2,y-1), f(x+3,y-1), f(x+4,y-1), f(x+5,y-1), f(x*2,y-1), ]
#     return any(h) if y % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(1,512) if f(s,2)])
# print('20)', *[s for s in range(1,512) if f(s,3) and not(f(s,1))])
# print('20)', *[s for s in range(1,512) if f(s,4) and not(f(s,2))])
#

# a = '568 36 247 368 178 124 35 145'.split()
# b = 'ба аж жд дк ке еб бг га гв ев вд'.split()
# print('1 2 3 4 5 6 7 8')
# for p in permutations('абвгдежк'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)


# def f(x,y,z,w):
#     return ((x <= y) == (y <= z)) and (y or w)
#
# for a,b,c,d,e,g in product([0,1],repeat=6):
#     table = ((0,a,0,b,1),
#              (0,0,c,0,1),
#              (d,e,g,0,1))
#
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw',r=4):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)
#                 break
# maxi = 0
# c = 0
# for x in product(sorted('АЛГОРИТМ'),repeat=5):
#     s = ''.join(x)
#     c += 1
#     if c % 2 == 1:
#         if s[0] != 'Г' and s.count('И') >= 2:
#             maxi += 1
# print(maxi)

# for x in '0123456789AB':
#     for y in '0123456789AB':
#         a = int(f'{y}AA{x}',12)
#         b = int(f'{x}02{y}',14)
#         c = a + b
#         if c % 80 == 0:
#             print(c//80)


# f = open('Задание 17.txt')
# a = [int(x) for x in f]
# count = ma = 0
# for i in range(len(a)-1):
#     for j in range(i + 1, len(a)):
#         if (a[i] + a[j]) % 7 == 0:
#             count += 1
#             ma = max(ma,a[i]+a[j])
# print(count,ma)


# def f(x,y,m):
#     if x + y >= 49: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x+1,y,m-1),f(x*3,y,m-1),f(x,y+1,m-1),f(x,y*3,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(1,44) if f(5,s,2)])
# print('20)', *[s for s in range(1,44) if f(5,s,3) and not(f(5,s,1))])
# print('21)', *[s for s in range(1,44) if f(5,s,4) and not(f(5,s,2))])
#
#
# def tro(num):
#     result = ''
#     while num:
#         result += str(num % 3)
#         num //= 3
#     return result[::-1]
#
#
# for N in range(1, 300):
#     N_tern = tro(N)
#
#     remainder = N % 3
#     if remainder == 0:
#         N_tern += N_tern[-2:]
#     else:
#         sum_d = sum(map(int, N_tern))
#         N_tern += tro(sum_d * 3)
#     R = int(N_tern, 3)
#     if R > 900:
#         print(R)
#         break
#
# for a in range(1,2000):
#     k = 0
#     for x in range(1,2000):
#         if (x % 1905 != 0) <= ((x % 1000 == 0) <= (x & a != 0)):
#             k += 1
#     if k == 2000:
#         print(a)
#         break
#
#
# from ipaddress import *
#
# ip1 = ip_address('157.220.185.237')
# ip2 = ip_address('157.220.184.230')
# otv = []
# for mask in range(15, 33):
#     net = ip_network(f'157.220.185.237/{mask}', 0)
#     if (ip1 in net) and (ip2 in net):
#         count = 0
#         for ip in net:
#             if f'{ip:b}'.count('1') == 15:
#                 count += 1
#         otv.append(count)
# print(min(otv))
#
# for a in range(0, 10**5):
#     k = True
#     for x in range(0, 10**5):
#         if ((x & 20777 != 0) <= ((x & 12332 == 0) <= (x & a != 0)))==0:
#             k = False
#             break
#     if k == True:
#         print(a)
#         break


#
# a = '378 8 147 3 67 5 1358 127'.split()
# b = 'ac cd de eb cf fe fd fg gh'.split()
# print('1 2 3 4 5 6 7 8')
# for p in permutations('abcdefgh'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)

# def f(p,y,h,n):
#     return y and not(y or h) or not(y <= h) and (n <= p)
#
# for a,b,c,d,e,g in product([0,1],repeat=6):
#     table = ((a,b,c,1,1),
#              (d,1,e,1,1),
#              (g,1,1,1,1))
#
#     if len(table) == len(set(table)):
#         for p in permutations('pyhn',r=4):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)
#                 break
# c = 0
# for x in product('метро',repeat=4):
#     s = ''.join(x)
#     if s[0] != "е" and s[0] == "о":
#         if s[-1] != "м" and s[-1] == "р" and s[-1] != 'т':
#             c += 1
#         print(c,s)


# ip1 = ip_address('95.24.2.9')
# ip2 = ip_address('95.24.3.10')
# otv = []
# for mask in range(1,33):
#     net = ip_network(f'95.24.3.10/{mask}',0)
#     if (ip1 in net) and (ip2 in net):
#         count = 0
#         for ip in net:
#             if f'{ip:b}'.count('0') % 2 == 0:
#                 count += 1
#             otv.append(count)
# print(min(otv))




# p = list(range(2,21,2))
# q = list(range(5,51,5))
#
# def f(x):
#     return ((x in a) <= (x in p)) and ((x in q) >= (x in a))
#
# for a in range(1,1000):
#     if all(f(x) for x in range(1,1000)):
#         print(a)

# def f(x,y,m):
#     if x + y >= 231: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x+1,y,m-1),f(x*2,y,m-1),f(x,y+1,m-1),f(x,y*2,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(1,214) if f(17,s,2)])
# print('20)', *[s for s in range(1,214) if f(17,s,3) and not(f(17,s,1))])
# print('21)', *[s for s in range(1,214) if f(17,s,4) and not(f(17,s,2))])
#
# def f(x,y):
#     if x > y: return 0
#     if x == y: return 1
#     else:
#         return f(x+2,y) + f(x+3,y) + f(x+int('1'),y)
#
# print(f(3,12) * f(12,25))
#
# for x in range(1,1000):
#     n = bin(x)[2:]
#     if n.count('1') % 2 == 0:
#         n = '101' + n[3:] + '0'
#     if n.count('1') % 2 == 1:
#         n = '10' + n[2:] + '11'
#
#     r = int(n,2)
#     if r > 68:
#         print(x)
#         break
#
# count = 0
# f = open('9.txt')
# for s in f:
#     a = [int(x) for x in s.split()]
#     a.sort()
#     if a[0] + a[1] + a[2] == 180:
#         if a[0] < a[1] + a[2] or a[1] < a[0] + a[2] or a[2] < a[0] + a[1]:
#             count += 1
# print(count)


a = '37 57 147 37 26 57 12346'.split()
b = 'ac cd ag gd db bf ad de ef'.split()
for p in permutations('abcdefg'):
    if all(str(p.index(c2) + 1) in a[p.index(c1)] for c1, c2 in b):
        print(*p)



# def f(x,y,z,w):
#     return z or (z == w) or not(y <= x)
#
# for a,b,c,d,e,g,h in product([0,1],repeat=7):
#     table = ((a,b,0,1,0),
#              (c,1,d,0,0),
#              (e,0,g,h,0))
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw',r=4):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)
#
# for i in range(1,1000):
#     n = str(bin(i)[2:])
#     n1 = sum(map(int,n))
#     ost1 = n1 % 2
#     n2 = str(n) + str(ost1)
#     n3 = sum(map(int,n2))
#     ost2 = n3 % 2
#     n4 = str(n2) + str(ost2)
#
#     r = int(n4, 2)
#     if r < 100:
#         print(r)
#
# k = 0
# for x in product('abcdef',repeat=5):
#     s = ''.join(x)
#     if s[0] != 'f' and s[-1] == 'a':
#         k += 1
#         print(k,s)
#
# for x in range(3,10_001):
#     s = '5' + '2'*x
#     while '52' in s or '1122' in s or '2222' in s:
#         if '52' in s:
#             s = s.replace('52','11',1)
#         if '2222' in s:
#             s = s.replace('2222','5',1)
#         if '1122' in s:
#             s = s.replace('1122','25',1)
#
#     if sum(map(int,s)) == 64:
#         print(x)
#         break
#
# for x in '01234567':
#     for y in '01234567':
#         a = int(f'{y}04{x}5',11)
#         b = int(f'253{x}{y}',8)
#         if (a + b) % 117 == 0:
#             print((a+b)/117)
#
#
# def f(x,y):
#     return (x * y < 120) or (y > a) or (x > a)
#
# for a in range(1000):
#     if all(f(x,y) for x in range(1000) for y in range(1000)):
#         print(a)

def f(x,y):
    if x > 200: return y % 2 == 0
    if y == 0: return 0
    h = [f(x+1,y-1),f(x*5,y-1)]
    return any(h) if y% 2 != 0 else all(h)
print('19)', *[s for s in range(1,201) if f(s,2)])
print('20)', *[s for s in range(1,201) if f(s,3) and not(f(s,1))])
print('21)', *[s for s in range(1,201) if f(s,4) and not(f(s,2))])

otv = []
f = open('255555.txt')
a = [int(x) for x in f]
minip = min(x for x in a if abs(x) % 100 == 15 and abs(x) in range(99,1000))
for i in range(len(a)-2):
    troiki = [a[i], a[i+1], a[i+2]]
    troikisplusom = [x for x in troiki if x >= 0]
    troikisminusom = [x for x in troiki if x < 0]
    if len(troikisplusom) == 3 or len(troikisminusom) == 3:
        if min(troiki) * max(troiki) > minip**2:
            otv.append(min(troiki)*max(troiki))
print(len(otv),min(otv))

k = 0
for x in product('abcdef',repeat=5):
    s = ''.join(x)
    if s[0] != 'f' and s[-1] != 'a':
        k += 1
        print(k,s)

