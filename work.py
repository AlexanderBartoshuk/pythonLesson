from itertools import * 
from sys import * 
from turtle import * 


for n in range(3,50):
    s = '>' + '1'* 30  + '2' * n + '3'*35
    while ('>1'in s) or (">2" in s) or (">3" in s):
        if ">1 " in s:
            s = s.replace('>1','1>',1)
        if '>2' in s:
            s = s.replace('>2','>3',1)
        if '>3' in s:
            s = s.replace('>3','>1',1)
        
        
        print(n,s)
        