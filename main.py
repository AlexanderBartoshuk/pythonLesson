#from itertools import * 
#
#def F(x,y,z,w):
#    return ((x <= y) <= z) or not(w)
#
#for a,b,c,d,e,f,g in product([0,1], repeat=7):
#    table = ((a,0,b,0,0),
#             (1,c,d,e,0),
#             (0,1,f,g,0))
#    
#    if len(table) == len(set(table)):
#        for p in permutations('xyzw',r=4):
#            if all(F(**dict(zip(p,line))) == line[-1] for line in table):
#                print(*p)
#
#
#s = 45*'1' + 45*'2'
#while '111' in s:
#    s = s.replace('111','2',1)
#    s = s.replace('222','1',1)
#print(s)
#
#def f(x):
#    if x <=2 : return 1 
#    if x > 2: return f(x-1) + 3* f(x-2)
#print(f(7))
#
#from fnmatch import *
#
##for i in range(3013,10**10,3013):
##    if fnmatch(str(i),'1?3948*5'):
##        print(i)
#
#a = []
#for x in '01234567':
#    for y in '01234567':
#        t = int(x+'01'+y+'4',9) + int(x+y+'544',8)
#        if t % 89 == 0: a.append(t)
#
#    if a: print(min(a)// 89)
#
#
#def f(x,y):
#    if x < y: return 0
#    if x == y: return 1 
#    else: return f(x-2,y) + f(x-5,y)
#print(f(22,2))

#def F(n):
#    if n == 1: return 0
#    elif n > 1: return F(n-1) + n
#
#def G(n):
#    if n == 1: return 1
#    elif n > 1: return G(n-1) * n
#
#print(F(5) + G(5))


#from functools import * 
#
#@lru_cache(None)
#
#def f(n):
#    if n == 1: return 1 
#    if n > 1: return n * f(n-1)
#
#for n in range(1,2025): f(n)
#
#print((f(2024)//4 + f(2023))//f(2022))




from itertools import *



a = 'ба бв ав аг ве гд де дж еж'.split()
b = '67 346 24 235 47 127 156'.split()
print('1 2 3 4 5 6 7')
for p in permutations('абвгдеж'):
    if all(str(p.index(c2)+1) in b[p.index(c1)] for c1,c2 in a):
        print(*p)



a = 343**6 - 7**10 + 47
s = ''
while a != 0:
    s += str(a % 7)
    a //= 7
s = s[::-1]
print(s.count('6'))

"""
def f(x,y):
    return (2*x + 3*y < 30) or (x + y >= A)

for A in range(0,100):
    if all(f(x,y) for x in range(1,100) for y in range(1,100)):
        print(A)
"""

def F(n):
    if n == 1: return 1
    if n >1: 
        return 2 * F(n-1)+1
print(F(5))


def f(x,y):
    if x > y or x == 14: 
        return 0 
    if x == y: 
        return 1
    else:
        return f(x+1,y) + f(x*2,y) + f(x*3,y)
    
print(f(1,12) * f(12,40))


counter = 0
for i in range(245690, 245756 + 1):
    counter += 1
    ost = 0
    for d in range(2, i):
        if i % d == 0:
            ost += 1
    if ost == 0:
        print(counter, i)



#f = open('24.txt').readline().split('W')
mini = 10**10
for i in range (1,len(f)-129):
    mini = min(len('W'.join(f[i:i+129]))+2,mini)
print(mini)
