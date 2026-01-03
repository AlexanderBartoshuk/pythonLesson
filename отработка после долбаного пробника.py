from sys import *

setrecursionlimit(100000000)

# def f(x):
#     if x == 1: return 1
#     if x > 1: return 2 * x * f(x-1)
#
# print((f(2024) // 16 - f(2023)) // f(2022))
#
#
# def f(x):
#     if x == 1: return 1
#     if x > 1: return x * f(x-1)
#
# print((f(2024)//4+f(2023)) // f(2022))
#
# def f(x):
#     if x < 20: return x
#     else: return (x-6) * f(x-7)
#
# print((f(47872) - 290 * f(47865)) // f(47858))
#
#
# def f(x):
#     if x < 31054: return f(x+4) + 3020
#     if x >= 31054: return 3 * (g(x-2) - 15)
#
# def g(x):
#     if x >= 28: return g(x-5) - 15
#     if x < 28: return 3 * x - 4
#
# print(f(15))

def f(n):
    if n < 10: return n
    if n > 9: return  f(n)* f(n-2)
def g(n):
    if n < 11: return n*3
    if n > 10 and n % 7 == 1: return f(n**2) + f(n**2+1) + f(n**n)

print(g(10)**f(2) + f(5))

def f(n):
    if n <= 10: return n
    if n > 10 and n % 10 == 0: return f(n%5) +1
    if n > 10 and n % 10 == 1: return n * f(n-1)

def f(x):
    if x < 5: return 1
    if x > 4 and x % 5 == 0: return f(x//5)
    if x > 4 and x % 5 == 1: return (x - 5) * (x//5) + f((x-5)*(x//5))

def g(x):
    if x < 7: return 1
    if x > 6 and x % 7 ==0: return g(x//7)
    if x > 6 and x % 7 == 1: return (x-7) * (x//7) + g((x-7) * (x//7))

for x in range(1,10000):
    if g(x) + f(x) < 3:
        print(x)
