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


a = '01234567'
for x in a:
    for y in a:
        f = int(f'{y}04{x}5',11) + int(f"253{x}{y}",8)
        f = int(f'{y}04{x}5', 11) + int(f'253{x}{y}', 8)
        if f%117 == 0:
            print(f//117)

def траекториявычислений(x,y):
    if x > y or x == 31:
        return 0
    if x == y:
        return 1
    else:
        return траекториявычислений(x + 1,y) + траекториявычислений(x*2,y)
print(траекториявычислений(2,15) * траекториявычислений(15,35))

from fnmatch import *
for x in range(0, 10**10, 3147):
# Перебираем все числа от 0 с шагом 3147, будут получены числа кратные 3147
    if fnmatch(str(x), '1*4302?1'):
    # Проверяем полученное число соответствию заданию
        print(x)


print('x y w z')
for x in range(0,2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if not (x == (w or y) or (w <= z) and (y <= w)):
                    print(x,y,w,z)

def mi(x,y):
    if x > y or x == 18:
        return 0
    if x == y:
        return 1
    else :
        return mi(x+1,y) + mi(x*2,y)
print(mi(1,10) * mi(10,21))

print('x y z w')
for x in range(0,2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if (x == (y <= z)) and ((not(w)) <= (x == y)):
                    print(x,y,z,w)

m = 4 ** 12 + 2 **32 - 16
s = bin(m)[2:]
print(s.count('1'))


def F(n):
    if n < 15:
        return F(n)
    else:
        return F(n)


def f(x,y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 2, y) + f(x + 3, y)
print(f(1, 8) * f(8, 15))


s = '1' + '9' * 98
while ('19' in s) or ('299' in s) or ('3999' in s):
    s = s.replace('19','2',1)
    s = s.replace('299', '3', 1)
    s = s.replace('3999', '1', 1)
print(s)

def print_multiply(a,b,operation):
    result = operation(a,b)
    print(result)

a = 5
b = 4
print_multiply(a,b,multiply)

a = 36**7 + 6**19 - 18
s = ''
while a!= 0:
    s += str(a%6)
    a //= 6
s = s[::-1]
print(s.count('5'))


def f(x, y):
    if x > y or x == 6 or x == 12:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x + 3, y)
print(f(3, 16))


print((1542613234 - 765432010) //3 +1)

def d(x,y):
    if x > y or x == 16:
        return 0
    if x == y:
        return 1
    else:
        return f(x+1, y) + f(x*2,y)
print(f(1,10) * f(10,21))


for i in range(2000000, 3000001):
    sqrti = i**0.5
    k = 0
    for j in range(1, round(sqrti)):
        if i % j == 0:
            if (abs(i / j) - j) <= 115:
                k += 1
    if k > 2: print(i)
    k = 0