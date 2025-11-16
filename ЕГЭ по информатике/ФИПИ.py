def f(x):
    print(x,end='')
    if x >= 3:
        f(x-1)
        f(x-1)
print(f(4))


print(98&255,81&252,154&0,195&0)

from itertools import *


a = 'аб ав бв вг вд ве де ге гк ек'.split()
b = '24 146 56 1267 36 23457 46'.split()
print('1 2 3 4 5 6 7')
for p in permutations('абвгдек'):
    if all(str(p.index(c2)+1) in b [p.index(c1)] for c1,c2 in a):
        print(*p)
        break


def f(x,y,z,w):
    return ((not(x)) and (not(y))) or (y ==z ) or w

for a,b,c,d in product([0,1],repeat=4):
    table = ((a,b,1,c,0),
             (1,0,d,1,0),
             (0,0,1,1,0))
    if len(table) == len(set(table)):
        for p in permutations('xyzw',r=4):
            if all(f(**dict(zip(p,line))) == line[-1] for line in table):
                print(*p)
                break