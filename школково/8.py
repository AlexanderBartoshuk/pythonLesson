from itertools import *
# from sys import setrecursionlimit
#
# from functools import lru_cache
# t = product('НРДО',repeat=4)
# c= 0
# for i in t:
#     s = ''.join(i)
#     c += 1
#     if s == 'ДРОН':
#         print(c)
#
#
#
# t = product('МАЕЛ',repeat=5)
# c = 0
# for i in t:
#     s = ''.join(i)
#     c += 1
#     if s == 'ЛЕММА':
#         print(c)
#
# t = product('КАМЕО', repeat=5)
# c = 0
# d = 0
# for i in t:
#     s = ''.join(i)
#     c += 1
#     if c in range(571,2148):
#         if s[-2:] == 'ОМ':
#             d += 1
#             print(d)
#
# # Все 4-буквенные слова, составленные из букв А, Л, П, К, записаны в алфавитном порядке. Вот начало списка
# # Запишите слово, которое стоит на 226-м месте от начала списка.
#
# t = list(product(sorted('АЛПК'),repeat=4))
# print(t[225])
#
# c = 0
# t = list(product(sorted('ДВЕРЬ'), repeat=7))
# for i in t:
#     s = ''.join(i)
#     c += 1
#     if 'В' not in s:
#         print(c)
#         break
#
# # Под каким номером в списке идёт последнее слово, которое содержит сочетание букв АМБАР?
#
# s = "АБМР"  # Алфавитный порядок букв
# n = 1  # Счётчик для нумерации слов
# ans = ""  # Для номера последнего слова, содержащего подстроку АМБАР
#
# # Генерируем все возможные 6-буквенные комбинации
# for x in product(s, repeat=6):
#     w = "".join(x)  # Преобразуем кортеж символов в строку
#     if "АМБАР" in w:
#         ans = n  # Запоминаем номер, если слово содержит подстроку АМБАР
#     n += 1  # Увеличиваем счётчик на 1 для каждого нового слова
# print(ans)
#
#
# #`                              Подсчет количества слов/чисел
#
# #count = 0
#
# # for x in permutations('ПРАВНУК'):
# #     s = ''.join(x)
# #     if s[0] == "П" and s[-1] == 'Р':
# #         count += 1
# # print(count)
#
# count = 0
# for x in permutations('САМОРЗВИТЕ',r=4):
#     s = ''.join(x)
#     count += 1
# print(count)
#
# a = 0
# for x in permutations('ПИКСЕЛЬ',r=4):
#     s = ''.join(x)
#     a += 1
# print(a)
#
#
# a = 0
# for x in permutations('напиток',r=7):
#     s=''.join(x)
#     if s[-1] == 'к' and s[0] == 'п':
#         a += 1
# print(a)




def conv(n):
    alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = ''
    while n:
        ans = alph[n % 27] + ans
        n //= 27
    return ans

for x in range(1, 27001):
    n = 3 * 27**9 + 2 * 27**6 + 27**3 - x
    if conv(n).count('0') == 6:
        print(x)
        break


