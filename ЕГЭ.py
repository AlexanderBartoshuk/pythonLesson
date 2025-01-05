print('x y z')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            if not((x or y) <= (y==z)):
                print(x, y, z)


a = 9**2016 + 3**2015 - 9
s = ''
while a != 0:
    s += str(a%3)
    a = a//3 
s = s[::-1]
print(s.count('2'))

import sys
sys.setrecursionlimit(10**5)

def F(n):
    if n == 1: 
        return 1 
    elif n > 1: 
        return n-1 + F(n-1)
print(F(2024) - F(2022))
