from itertools import *
from string import printable 
from functools import * 

#
#
#a = '2459 16 4579 138 136 25 38 47 13'.split()
#b = 'аб бв вг аг гд де ев еж гж ек жи ик'.split()
#print('1 2 3 4 5 6 7 8 9')
#for p in permutations('абвгдежик'):
#    if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#        print(*p)
#        break
#
#def f(x,y,z,w):
#    return (x and (not(y))) or (y == z) or (not(w))
#
#for a,b,c,d,e in product([0,1],repeat=5):
#    table = ((a,0,b,c),
#             (1,0,d,0),
#             (1,e,0,0))
#    
#    if len(table) == len(set(table)):
#        for p in permutations('xyzw',r=4):
#            if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                print(*p)
#                break
#
#for n in range(99,10000):
#    i = bin(n)[2:]
#    for s in range(3):
#        a0 = i.count('0')
#        a1 = i.count('1')
#        if a0 == a1:
#            i = i + i[-1]
#        if a1 > a0:
#            i += '0'
#        else:
#            i += '1'
#    
#    r = int(i,2)
#    if r % 4 == 0:
#        print(n)
#        break
#
#print(131&192,64&0)
#
#
#for x in '012345678':
#    t = int('88' + x + '4' + x, 9) + int('7' + x + '344', 9)
#    if t % 67 == 0:
#        print(t // 67)
#        
#
#def f(x,y):
#    return (3*x + 4*y != 70) or (a > x) or (a > y)
#
#for a in range(100):
#    if all(f(x,y) for x in range(0,100) for y in range(0,100)):
#        print(a)

@lru_cache()
def f(n):
    if n <= 7:
        return n 
    else:
        return g(n-3) * 3 

@lru_cache()
def g(n):
    if n <= 7:
        return n   
    else:
        return g(n-1) + 4

for n in range(43000+1):
    g(n)
    f(n)


print(f(43000))



p = [a for a in product('бкф',repeat=6)]
print(*p[344])

def f(x,y):
    if x > y or x == 13: return 0
    if x == y: return 1 
    else:
        return f(x+1,y) + f(x+2,y) + f(x*3,y)

print(f(3,8)*f(8,18))
