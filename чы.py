from itertools import * 
from turtle import * 
from string import * 
from functools import *

a = '28 148 57 25 346 58 38 1267'.split()
b = 'аб аж бз же зе ег вг ве гд бд'.split()
print("1 2 3 4 5 6 7 8")
for p in permutations('абвгдежз'):
    if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
        print(*p)
        break

def j(x,y,z,w):
    return (x or (not(y))) and (y == (not(z))) and w

for a,b,c,d,e,f in product([0,1],repeat=6):
    table = ((0,a,b,0,1),
             (c,d,e,0,1),
             (1,1,0,f,1))

    if len(table) == len(set(table)):
        for p in permutations('xyzw',r=4):
            if all(j(**dict(zip(p,line))) == line[-1] for line in table):
                print(*p)
                break
k = 0
for i in range(1,1000):
    r = int(bin(i)[2:])
    if r % 2 == 0:
        r = str(r) + '00'
    else:
        r = str(r) + '10'

    if r.count("1") % 2 == 0:
        r = str(r) + '0'
    else:
        r = str(r) + '1'

    n = int(r,2)

    if n in range(160,630):
        k += 1
        print(k)

#k = 20
#screensize(2000,2000)
#tracer(0)
#lt(90)
#
#for i in range(5):
#    lt(60)
#    fd(4*k)
#    lt(120)
#    fd(4*k)
#
#up()
#
#for x in range(-20,30):
#    for y in range(-20,30):
#        goto(x*k,y*k)
#        dot(3)
#done()


k = 0

for i in set(permutations('ИДИЛЛИЯ')):
    k += 1
print(k)

def f(x):
    if x == 1: return 1
    if x % 2 == 0: return x + f(x/2)
    if x > 1 and x % 2 != 0:
        return x * f(x-1)

print(f(37))

for x in range(1,100000):
    s = 243**5 + 3**7 - 2 - x
    temp = ''
    while s != 0:
        temp = str(s%3) + temp
        s //= 3
    if temp.count('2') == 20:
        print(x)
        break

m = list(range(10,94))
n = list(range(4,72))
z = []
for i in range(1,101):
    if (i in n) <= ((i in m) and not(i in z) <= (i in n)):
        z.append(i)
print(len(z))


print(bin(128))

def f(x,y):
    if x > y: return 0
    if x == y: return 1
    else: return f(x+1,y) + f(x*2,y) + f(x*3,y)

print(f(1,7) * f(7,14) * f(14,30))


def f(s,n):
    if s >= 78: return n % 2 == 0
    if n == 0: return 0
    h = [f(s+1,n-1),f(s+3,n-1),f(s*4,n-1)]
    return any(h) if n % 2 != 0 else all(h)

print('19)', min([s for s in range(1, 77) if f(s, 2)]))
print('20)', *[s for s in range(1,77) if f(s,3) and (not f(s,1))])
print('21)', min([s for s in range(1,77) if f(s,4) and (not f(s,2))]))


a = minn = 0
f = open('еггег.txt')
l = [int(i) for i in f]
for i in range(len(l)-1):
    if l[i] % 2 != 0 or l[i+1] % 2 != 0:
        a += 1
        minn = min(minn,l[i]+l[i+1])
print(a,minn)

#for i in range(50_000_000,60_000_000):
#    s = []
#    for y in range(2,i+1,2):
#        if i % y == 0 or i % 911 == 0:
#            s.append(y)
#            if len(s) > 6:
#                break
#    if len(s) == 6:
#        print(n,*s)

for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            s = '0' + '2' * x + '4' * y + '6' * z
            while ('02' in s) or ('04' in s ) or ('06' in s):
                if '02' in s:
                    s = s.replace('02','6404',1)
                if '04' in s:
                    s = s.replace('04','2206',1)
                if '06' in s:
                    s = s.replace('06','440',1)

                if ('2' * 30 + '4' * 54 + '6' * 10) in s:
                    print(min(z))
                    break


