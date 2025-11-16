from itertools import * 
from turtle import * 

a = '24 146 567 1267 36 23457 346'.split()
b = 'аб ав бв вд бд ве де вг ге ек гк'.split()
print('1 2 3 4 5 6 7')
for p in permutations('абвгдек'):
    if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
        print(*p)
        
def f(x,y,z):
    return (x == z ) or (x <= (y and z))

for a,b,c in product([0,1],repeat=3):
    table = ((0,0,a,0),
             (1,b,c,0))
    
    if len(table) == len(set(table)):
        for p in permutations('xyz',r=3):
            if all(f(**dict(zip(p,line))) == line[-1] for line in table):
                print(*p)
                break


for i in range(1000,10001):
    n = str(i)
    st1 = int(n[0]) + int(n[1])
    st2 = int(n[2]) + int(n[3])
    per = str(min(st1,st2))
    vtor = str(max(st1,st2))
    b = per + vtor
    if b == '117':
        print(i)
        
tracer(0)
screensize(10000,10000)
lt(90)

r = 20

for i in range(4):
    fd(10 * r)
    rt(90)

up()

for x in range(-10,10):
    for y in range(-10,25):
        goto(x*r,y*r)
        dot(3,'red')
update()
exitonclick()



