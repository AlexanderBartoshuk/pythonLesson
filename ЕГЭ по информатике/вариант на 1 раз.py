from itertools import * 
from string import *
from functools import *
from fnmatch import * 

a = ('256 159 468 367 127 134 45 39 28').split()
b = ('ад жд аж аб бв вг де жи ик ег ке').split()
print('1 2 3 4 5 6 7 8 9')
for p in permutations('абвгдежик'):
    if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
        print(*p)
        break


s = '9' *  127
while ('333' in s) or ('999' in s):
    if  '333' in s:
        s = s.replace('333','9',1)
    else:
        s = s.replace('999','3',1)
print(s)

print(137&240)

num = 4 ** 34 + 5 * 4**22 + 4 ** 13 + 2 * 4**9 + 82
translated = hex(num)[2:] # функция hex переводит в 16-ую систему счисления
print(len(set(translated)))

def f(x,y):
    return (x * y <100) or (y >= a) or (x > a)

for a in range(0,100):
    if all(f(x,y) == 1 for x in range(0,100) for y in range(0,100)):
        print(a)
def F(n):
    if n == 1: return 2
    if n == 2: return 1 
    if n > 2: return F(n-2) + F(n-1)
print(F(8))





def f(s,m):
    if s >= 54: return m%2 == 0
    if m == 0: return 0 
    h = [f(s+1,m-1),f(s+3,m-1),f(s*2,m-1)]
    return any(h) if m % 2 != 0 else all(h)

print('20)', *[s for s in range(1, 53) if f(s, 3) and (not f(s, 1))])
print('21)', min([s for s in range(1,53) if f(s,4) and (not f(s,2))]))


def d(x, y):
    if x == y:
        return 1

    if x < y or x == 12 or x == 15:
        return 0

    if x > y:
        return d(x - 1, y) + d(x // 2, y) + d(x // 3, y)


print(d(19, 1))



