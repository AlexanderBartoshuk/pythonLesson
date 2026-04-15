from itertools import * 
from turtle import * 

for i in range(1000, 10000):
    n = str(i)
    n1 = int(n[0]) + int(n[1])
    n2 = int(n[2]) + int(n[3])
    first = str(max(n1, n2))
    second = str((min(n1, n2)))
    g = first + second
    if g == '1311':
        print(i)
        break

for m in range(0,255):
    if 64 == 70 & m:
        print(bin(m),m)

print(70&249)
print(bin(249))


for x in '0123456789':
    t = int('123'+x+'5',15) + int('1'+x+'233',15)
    if t % 14 == 0:
        print(t//14)
        
a = 4**14 + 2**32 -4
s = ''
while a != 0:
    s += str(a%2)
    a = a//2
s = s[::-1]
print(s.count('1'))
