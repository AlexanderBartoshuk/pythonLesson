from itertools import * 

def f(x,y,z,w):
    return ((y or z) <= (z and w)) == (not(( x and z) <= (w or y)))

for a, b, in product([0,1], repeat=2):
    table = ((a,1,1,1,1),
             (0,0,0,b,1),
             (1,1,0,0,1))
    
    if len(table) == len(set(table)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)



def f(x,y,z,w):
    return (x <= (y == w) and (y == (w <= z)))

for a,b in product([0,1], repeat=2):
    table = ((1,a,0,1,1),
             (0,0,b,0,1),
             (0,0,0,1,0))
    
    if len(table) == len(set(table)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p,line))) == line[-1] for line in table):
                print(*p)

def f(x,y,z,w): 
    return (x == (y <= z)) and ((not(w)) <= (x == y))



for a,b in product([0,1], repeat=2):
    table = ((1,0,1,1,1),
             (0,1,1,1,1),
             (0,a,0,b,1))
    
    if len(table) == len(set(table)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p,line))) == line[-1] for line in table):
                print(*p)