from itertools import * 
from turtle import *


def f(x,h):
    if h == 3 and x >= 65: return 1 
    if h == 3 and x < 65: return 0 
    if x >= 65 and h < 3: return 0
    else:
        if h % 2 == 0:
            return f(x+1,h+1) or f(x*3,h+1)
        else: return f(x+1,h+1) or f(x*3,h+1)

for x in range(1,65):
    if f(x,1) == 1:
        print(x)
        break


def f(x,y):
    if x >= 65: return y % 2==0
    if y == 0: return 0 
    h = [f(x+1,y-1),f(x*3,y-1)]
    return any(h) if y % 2 != 0 else all(h)
print('20)', *[x for x in range(1,64) if f(x,3) and (not f(x,1))])
print('21)', min([x for x in range(1,64) if f(x,4) and (not f(x,2))]))
