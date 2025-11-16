from itertools import *

#table = '67 346 24 235 47 127 156'.split()
#graph = 'ГД ГВ ВД АК АБ КБ КЕ ДЕ ВБ'.split()
#print('1 2 3 4 5 6 7')
#for p in permutations('АБВГДЕК'):
#    if all(str(p.index(c2)+1) in table[p.index(c1)] for c1,c2 in graph):
#        print(*p)
#        break   


#table = '56 347 257 26 136 145 23'.split()
#graph = 'AF AB BF BD DC FG EC EG CG'.split()
#print('1 2 3 4 5 6 7')
#for p in permutations('ABCDEGF'):
#    if all(str(p.index(c2)+1) in table[p.index(c1)] for c1,c2 in graph):
#        print(*p)
#        break

#table1 = '478 356 248 1378 268 25 14 1345'.split()
#g1 = 'АБ АИ БИ БВ ИЖ БЖ ЖВ ВГ ЖЕ ГЕ ДЕ ДГ'.split()
#print('12345678')
#for p in permutations('АБВГДЕЖИ'):
#    if all(str(p.index(c2)+1) in table1[p.index(c1)] for c1,c2 in g1):
#        print(*p)
#        break

#table = '24 146 56 1267 36 23457 46'.split()
#graph = 'аб ав бв вд вг де ве ге ек гк'.split()
#print('1 2 3 4 5 6 7')
#for p in permutations('абвгдек'):
#    if all(str(p.index(c2)+1) in table[p.index(c1)] for c1,c2 in graph):
#        print(*p)
#        break







from itertools import *

a = 'аб бв вг аж ад дж де жи ик гк ге ек'.split()
b = '256 159 468 367 127 134 45 39 28'.split()
print('1 2 3 4 5 6 7 8 9')
for p in permutations('абвгдежик'):
    if all(str(p.index(c2)+1 ) in b[p.index(c1)] for c1,c2 in a):
        print(*p)
        
def f(x,y,z,w):
    return ((x and y) or (y and z)) == ((x <= w) and (w <= z))
for a,b in product([0,1],repeat=2):
    table = ((0,1,1,1,1),
             (0,1,0,a,1),
             (0,1,0,b,1))
    if len(table) == len(set(table)):
        for p in permutations('xyzw',r=4):
            if all(f(**dict(zip(p,line))) == line[-1] for line in table):
                print(*p)
                break
