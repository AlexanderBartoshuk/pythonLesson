print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not (((not (x) or z) == (y and not (w))) <= (z and y)):
                    print(x, y, z, w)

for x in range(0,100):
    s = bin(x)[2:]
    s = str(s)
    if x % 2 == 0:
        s += '01'
    else:
        s += '10'
    r = int(s,2)
    if r > 102:
        print(r)
        break

#224.23.253.138 IP-адрес узла
#Маска: 255.255.240.0
print(255&224,255&23,240&253,0&138)


for a in range(300):
    k = 0
    for x in range(300):
        for y in range(0, 300):
            if ((3*x + 7*y < a) or (x >= y) or (y>6)):
                k += 1
    if k == 90_000:
        print(a)
        break


def F(n):
    if n <= 2:
        return 1
    else:
        return 2 * F(n-1) + F(n-2)
print(F(7))

def F(x,y):
    if x > y or x == 14:
        return 0
    if x == y:
        return 1
    else:
        return F(x+1,y) + F(x*2,y) + F(x*3,y)
print(F(1,12) * F(12,40))

from fnmatch import *

for x in range(0,10**9,9117):
    if fnmatch(str(x), '4*64*9?7'):
        print(x)