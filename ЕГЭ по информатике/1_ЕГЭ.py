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


table1 = '256 15 4 356 1246 145'.split()
graph = 'аб ав бв бг вг вд гд де'.split()
print('1 2 3 4 5 6')
for p in permutations('абвгде'):
    if all(str(p.index(c2) + 1) in table1[p.index(c1)] for c1,c2 in graph):
        print(*p)
        break