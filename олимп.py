from itertools import *
from fnmatch import *
from turtle import *
from sys import setrecursionlimit
from functools import lru_cache



s = '8' * 1000
while ('888' in s) or ('999' in s):
    if '888' in s:
        s = s.replace('888','9',1)
    else:
        s = s.replace('999','8',1)

print(163&240)

# @lru_cache(None)
# def f(n):
#     if n == 0: return 2
#     if n == 1: return 3
#     if n > 1:
#         return n * (n-1) + f(n-2) - f(n-3)
#
#
# for i in range(100000000):
#     f(i)
#
# print(f(7429) + f(7426) - f(7427))


print("x y z")
# Генерируем все возможные комбинации из 0 и 1 длины 3 (для x,y,z)
for x, y, z in product([0, 1], repeat=3):
    # Проверяем, что логическое выражение с текущим набором переменных дает истину
    if (not (x or (not y)) <= (z and x)):
        # Выводим подходящую комбинацию
        print(x, y, z)




