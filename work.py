from itertools import * 
from sys import * 
from turtle import * 
from functools import * 
from fnmatch import * 
from ipaddress import * 






#def f(s,m):
#    if s >= 125: return m % 2 == 0
#    if m == 0: return 0
#    h = [f(s+2,m-1), f(s+4,m-1), f(s*2,m-1)]
#    return any(h) if m % 2 != 0 else all(h)
#print('19)', min([s for s in range(1, 124) if f(s, 2)]))
#print('20)', *[s for s in range(1,124) if f(s,3) and (not f(s,1))])
#print('19)', min([s for s in range(1, 124) if f(s, 4) and (not f(s,2))]))

#cnt = 0
#for num in range(1_350_050,10**20):
#    for dev in range(2,num):
#        if num % dev == 0 and dev != 11 and dev % 100 == 11:
#            print(num,dev)
#            cnt += 1
#    if cnt == 5:
#        break
