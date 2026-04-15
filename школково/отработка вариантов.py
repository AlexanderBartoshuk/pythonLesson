from itertools import *
from functools import lru_cache
from fnmatch import *
# a = '47 37 26 17 67 357 12456'.split()
# b = 'ab ac be ce cd de ef fg eg'.split()
# print('1 2 3 4 5 6 7')
# for p in permutations('abcdefg'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)
#
# print('x y z')
# for x,y,z in product([0,1],repeat=3):
#     if (x and (not(y)) and z) or (x <= y):
#         print(x,y,z)
#
# mx = 0  # Инициализация переменной для хранения максимального результата R, удовлетворяющего условию
# for n in range(1, 300):  # Перебор всех натуральных чисел от 1 до 299 включительно
#     f = ""  # Пустая строка для формирования записи числа в четверичной системе счисления
#     while n > 0:  # Цикл для перевода числа n в четверичную запись
#         f = str(n % 4) + f  # Добавляем остаток от деления на 4 в начало строки f
#         n = n // 4  # Целочисленное деление n на 4 для перехода к следующей цифре
#     f += f[-1]  # Дублируем последнюю цифру четверичной записи, добавляя её в конец строки
#     b = bin(int(f, 4))[2:]  # Переводим четверичное число в десятичное, затем в двоичную строку без префикса ’0b’
#     b += b[-1]  # Дублируем последнюю цифру двоичной записи, добавляя её в конец строки
#     r = int(b, 2)  # Переводим полученную двоичную строку обратно в десятичное число R
#     if r < 280:  # Проверяем, что R меньше 280
#         mx = max(r, mx)  # Обновляем максимальное значение R, если текущее больше
# print(mx)
#
from turtle import *
# #
# # x,y = 0,0
# # tracer(0)
# # penup()
# # m = 40
# # goto(x*m,y*m)
# # pendown()
# # screensize(2000,2000)
# #
# # for i in range(20):
# #     new_x = x+4
# #     new_y = y+3
# #     goto(new_x*m,new_y*m)
# #     x,y = new_x,new_y
# #
# #     new_x = x-4
# #     new_y = y-3
# #     goto(new_x*m,new_y*m)
# #     x, y = new_x, new_y
# #
# #     new_x = x-12
# #     new_y = y-5
# #     goto(new_x*m,new_y*m)
# #     x,y = new_x,new_y
# #
# #     new_x = x +12
# #     new_y = y + 5
# #     goto(new_x*m,new_y*m)
# #     x,y = new_x,new_y
# #
# # pu()
# #
# # for x in range(-50,25):
# #     for y in range(-25,25):
# #         goto(x*m,y*m)
# #         dot(3)
# # done()
#
#
# c = 1
# for x in product('СУМКА',repeat=8):
#     s = ''.join(x)
#     if s[4] == 'К' or s[4] == 'У' and s[5] == "С" or s[5] == "М" or s[5] == "К":
#         if s[-2] == 'М' and s[-1] == 'С' or s[-1] == 'У' or s[-1] == 'А':
#             c += 1
# print(c)
#
# s = '9' * 406 + '1' * 188 + '5' * 707
# while '9' in s or '11' in s or '555' in s:
#     if '9' in s:
#         s = s.replace('9','11',1)
#     if '11' in s:
#         s = s.replace('11','1',1)
#     if '555' in s:
#         s = s.replace('555','9',1)
# print(s)
#
#
# def f(x):
#     if x == 0: return 1
#     if x > 0: return x * (x+1) + f(x-1)
# print(f(10))
#
# s = 5 * 512**3 + 2*64**6 - 7 * 8**4 - 111
# print(oct(s).count('7'))
#
#
# # def f(x,y):
# #     return ((x <= 9) <= (x * x <= a)) and ((y**2 <=a) <= (y <= 9))
# #
# # for a in range(1,1000):
# #     if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
# #         print(a)
#
#
# # def f(x,y):
# #     if x > y: return 0
# #     if x == y: return 1
# #     else:
# #         return f(x+2,y) + f(x*3,y)
# # print(f(2,42))
# #
# #
# # for x in range(387,10**7,387):
# #     if fnmatch(str(x), '*16*9?0?'):
# #         print(x,x//387)
#
# def f(x,y):
#     if x <= 34: return y % 2 == 0
#     if y == 0: return 0
#     h = [f(x-1,y-1), f(x-2,y-1)]
#     return any(h) if y % 2 != 0 else all(h)
# print('19)', min([s for s in range(36, 100) if f(s, 2)]))
# print('20)', *[s for s in range(36,100) if f(s,3) and (not f(s,1))])
# print('21)', *[s for s in range(36,100) if f(s,4) and (not f(s,2))])


# def f(x,y,z,w):
#     return (x == (not(y))) <= (z == (y or w))
#
# for a,b,c,d,e in product([0,1],repeat=5):
#     table = ((0,a,0,b,0),
#              (0,0,c,0,0),
#              (0,d,e,0,0))
#
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw',r=4):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)
#                 break


#
# tracer(0)
# lt(90)
# k = 20
#
# screensize(2000,2000)
#
#
# for i in range(10):
#     fd(10*k)
#     rt(60)
#
# up()
# for x in range(-25,25):
#     for y in range(-25,25):
#         goto(x*k,y*k)
#         dot(3)
#
# done()
#
# c= 0
# for x in product('КВАС',repeat=6):
#     s = ''.join(x)
#     if s.count('А') == 1:
#         c += 1
# print(c)
#
# x = 5**11 + 5**6 - 344
# s = ''
# while x > 0:
#     s = str(x%5) + s
#     x //= 5
#     print(s)
#
# def f(x,y):
#     if x > y or x == 12: return 0
#     if x == y: return 1
#     else:
#         return f(x+1,y) + f(x+2,y) + f(x*3,y)
#
# print(f(3,40))
#
# c = m = 0
# for x in range(2077,8276):
#     if x % 6 == 0:
#         if x % 4 != 0 and  x % 9 != 0 and  x % 20 != 0 and  x % 36 != 0:
#             c += 1
#             m = max(x,m)
#             print(c,m)
#
#
# p = list(range(20,31))
# q = list(range(5,15))
# c = list(range(35,50))
# a = []
# for x in range(1000):
#     if ((x in p) <= (x in q)) or ((not(x in a)) <= (x in c)):
#         a.append(x)
#         print(len(a))

# def f(s,m,n):
#     if s + m >= 49: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s+1,m,n-1), f(s*3,m,n-1), f(s,m+1,n-1), f(s,m*3,n-1)]
#     return any(h) if n % 2 != 0 else all(h)
#
# #print('19)', min([s for s in range(1,44) if f(5,s,2)]))
# print('21)', *[s for s in range(1,44) if f(5,s,4) and (not f(5,s,2))])

#
# for i in range(1,1000):
#     s = str(bin(i)[2:])
#     sum1 = sum(map(int,s)) % 2
#     s += str(sum1)
#     sum2 = sum(map(int,s)) % 2
#     s += str(sum2)
#
#     r = int(s,2)
#     if r > 91:
#         print(i)
#         break
#
# x = 26
# s = ''
# while x > 0:
#     s = str(x%4) + s
#     x//=4
# print(s)
#
# x = open('93.txt')
# n = 3200
# ans = 0
# for i in range(n):
#
#     a = sorted([int(s) for s in x.readline().split()])
#     if a[3] < (a[0] + a[1] + a[2]):
#         k = (a[0] == a[1]) + (a[0] == a[2]) + (a[0] == a[3]) + \
#             (a[1] == a[2]) + (a[1] == a[3]) + (a[2] == a[3])
#         if k == 1:
#             ans += 1
# print(ans)



# def f(x,y,z):
#     return not(z or (not(x) and y))
#
# table = ((0,0,0,1),
#          (1,0,0,1),
#          (1,0,1,1))
#
# if len(table) == len(set(table)):
#     for p in permutations('xyz',r=3):
#         if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#             print(*p)


# for i in range(100,1000):
#     n = str(i)
#     per = int(n[0]) + int(n[1])
#     wt = int(n[1]) + int(n[2])
#     naim = min(per,wt)
#     naib = max(per,wt)
#     chislo = str(naib) + str(naim)
#
#     if chislo == '178':
#         print(i)
#         break
# tracer(0)
# screensize(2000,2000)
# lt(90)
# k=20
#
# for i in range(6):
#
#     rt(45)
#     fd(5*k)
#
# for i in range(4):
#
#     fd(12*k)
#     rt(270)
#
# up()
#
# for x in range(-22,25):
#     for y in range(-25,25):
#         goto(x*k,y*k)
#         dot(3)
# done()
#
#
# count = 0
# for x in product('квас',repeat=6):
#     s = ''.join(x)
#     if s.count('а') == 1:
#         count += 1
#         print(count)
#
# s = '3' * 20 + '6' * 26 + '9' * 31
# c = 0
# while ('36' in s) or ('63' in s) or ('69' in s):
#     if '69' in s:
#         s = s.replace('69','63',1)
#         c += 1
#     if '36' in s:
#         s = s.replace('36','3',1)
#         c += 1
#     if '63' in s:
#         s = s.replace('63','9',1)
#         c += 1
#
# print(c)
#
#
# x = 25**20 + 4 * 5 **11 - 2
# s = ''
# while x != 0:
#     s = str(x % 5) + s
#     x //= 5
# print(s.count('3'))
#
#
# # def f(n):
# #     if n == 1: return 1
# #     if n > 1:
# #         return f(n-1) + 1 * g(n-1)
#
# # def g(n):
# #     if n == 1: return 2
# #     if n > 1: return f(n-1) - 2 * g(n-1)
# #
# # print(f(20) + g(10))
#
# # def f(x,y):
# #     if x > y: return 0
# #     if x == y: return 1
# #     else:
# #         return f(x+3,y) + f(x*2,y) + f(x+1,y)
# #
# # print(f(2,10)*f(10,30))
#
# ma = 10**100
# c = 0
# for i in range(1532858,1922980):
#     if i % 13 == 0:
#         if i % 21 != 0 and i % 25 != 0 and i % 41 != 0 and i % 77 != 0:
#             c += 1
#             ma = min(ma,i)
# print(c,ma)
#
# def f(x,y,s):
#     if x + y <= 40: return s % 2 == 0
#     if s == 0: return 0
#     h = [f(x-1,y,s-1),f(x,y-1,s-1), f((x//2)+(x%2),y,s-1), f(x,(y//2)+(y%2),s-1)]
#     return any(h) if s % 2 != 0 else any(h)
#
# print('19)', *[s for s in range(20, 59) if f(20, s, 0)])
# print('20)', *[s for s in range(21, 100) if f(20, s, 3) and (not f(20, s, 1))])
# print('21)', *[s for s in range(21, 100) if f(20, s, 4) and (not f(20, s, 2))])
#
#
# def d(a,b,c):
#     return (a + b +c) == 180
#
# for a in range(1,1000):
#     f = 0
#     for x in range(1,1000):
#         if (d(a,15,x+25) == d(x,a,60) and (not(a+10 < 100))) == False:
#             f =1
#             break
#     if f == 0:
#         print(a)
#         break
#
# from ipaddress import ip_address, ip_network
#
# # Задаем IP-адрес и адрес сети
# ip = ip_address("7.120.112.5")
# network = ip_network("7.120.96.0/255.255.224.0")
#
# # Получаем номер компьютера в сети
# host_number = int(ip) - int(network.network_address)
#
# print(host_number)


from ipaddress import *

# def f(x,y,z):
#     return (x <= y) and (y <= z)
#
# table = ((0,0,1,1),
#          (1,0,1,1),
#          (0,0,0,1))
#
# if len(table) == len(set(table)):
#     for p in permutations('xyz',r=3):
#         if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#             print(*p)

# for i in range(1,1000):
#     n = str(bin(i)[2:])
#
#     if n[0] == '1':
#         n = n[1:]
#         n = '1' + list(reversed(n))

# c = 0
# for x in product('МАШИН',repeat=6):
#     s = ''.join(x)
#     if (s.count('А') == 1 and s.count('И') == 0) or (s.count('А') == 0 and s.count('И') == 1):
#         c += 1
#         print(c,s)
#
# def f(n):
#     if n < 100: return 5 + n + f(n+2)
#     else:
#         return n + 2
# print(f(90)-f(101))
#
#
# print(int('11110000',2))
# print(148&240)
#
# p = list(range(5,35))
# q = list(range(20,52))
# a = []
# for x in range(1,100):
#     if (x in p) <= (((x in q) and not(x in a)) <= (not x in p)):
#         a.append(x)
#         print(len(a))
#
# a = 12 ** 34  + 7 * 12 ** 26 - 3*12**16 + 2 * 12**5 + 552
# s = ''
# while a > 0:
#     s = str(a % 12) + s
#     a //= 12
# print(s)
#
#
# def f(x,y,z,w,m):
#     if x+y+z+w >= 70: return m % 2==0
#     if m == 0: return 0
#     h = [f(x+2,y,z,w,m-1), f(x*3,y,z,w,m-1),f(x,y+2,z,w,m-1), f(x,y*3,z,w,m-1),f(x,y,z+2,w,m-1), f(x,y,z*3,w,m-1),f(x,y,z,w+2,m-1), f(x,y,z,w*3,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(1,40) if f(9,6,8,s,2)])
# print('20)', *[s for s in range(1,40) if f(9,6,8,s,3) and not f(9,6,8,s,1)])
# print('20)', *[s for s in range(1,40) if f(9,6,8,s,4) and not f(9,6,8,s,2)])

# lt(90)
# k = 20
# tracer(0)
# screensize(2000,2000)
#
#
# lt(45)
# fd((6*(2**0.5))*k)
# rt(45)
#
# for i in range(2):
#     seth(90)
#     circle(-3*k,180)
#
#
# rt(45)
# fd((6*(2**0.5))*k)
#
# up()
#
# for x in range(-25,25):
#     for y in range(-25,25):
#         goto(x*k,y*k)
#         dot(3)
# done()
#
# a = [] # Список для хранения подходящих N
# for n in range(1000): # Перебираем все числа N от 1 до 999
#     r = bin(n)[2:] # Получаем двоичную запись N (без префикса ’0b’)
#     first = r[0] # Сохраняем первую цифру числа
#     r = r[1:] # Берем срез числа без первой цифры
#     r = r.replace(’0’, ’*’) # Заменяем все нули в строке на *
#     r = r.replace(’1’, ’0’) # Заменяем все единицы в строке на 0
#     r = r.replace(’*’, ’1’) # Заменяем все * (старые нули) в строке на 1
#     r = first + r # Приписываем слева первую цифру исходного числа
#     rez = int(r, 2) + n # Преобразуем полученную двоичную строку в десятичное число R и складываем с N
#     if n % 2 != 0 and rez > 85: # Проверяем, что N нечетное и что полученный результат > 85
#         a.append(n) # Добавляем текущее N в список
# print(min(a)

# a = '45 347 27 125 146 57 236'.split()
# b = 'ab bc ac ec eg gd de df fa'.split()
# print('1 2 3 4 5 6 7')
# for p in permutations('abcdefg'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)
#         break
#
# def f(x,y,z,w):
#     return (x and not(y)) or (x == z) or (not(w))
#
# for a,b,c,d in product([0,1],repeat=4):
#     table = ((0,1,1,0,0),
#              (0,a,b,c,0),
#              (c,1,0,1,0))
#
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw',r=4):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)

# tracer(0)
# lt(90)
# screensize(2000,2000)
# k = 20
#
# for i in range(4):
#
#     fd(9*k)
#     rt(90)
#     fd(7*k)
#     rt(90)
#
# up()
#
# for x in range(-25,25):
#     for y in range(-25, 25):
#         goto(x*k,y*k)
#         dot(3)
#
# done()

# for x in range(1, 2030):
#     s = 3**100 - x
#     a = ''
#     while s != 0:
#         a = str(s % 3) + a
#         s//=3
#     if a.count('0') == 2:
#         print(x)
#         break
#
#
#
#
# def f(x,y,m):
#     if x + y <= 40: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x-1,y,m-1), f(x,y-1,m-1), f(x//2,y,m-1), f(x,y//2,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(20,100) if f(20,s,1)])
# print('20)', *[s for s in range(20,100) if f(20,s,3) and (not f(20,s,1))])
# print('21)', *[s for s in range(20,100) if f(20,s,4) and (not f(20,s,2))])
#
# def f1(x,y):
#     if x > y or x == 9: return 0
#     if x == y: return 1
#     else:
#         return f1(x+1,y) + f1(x*2,y)
#
#
# def f(x,y):
#     if x > y or x == 10: return 0
#     if x == y: return 1
#     else:
#         return f(x+1,y) + f(x*2,y)
#
# print(f(1,9) * f(9,20) + f1(1,10) * f1(10,20))
#
#
# def f(x,y):
#     return (48 != y + x*2) or (A < x) or (A < y)
#
# for A in range(1,100):
#     if all(f(x,y) for x in range(1,100) for y in range(1,100)):
#         print(A)
#
# c = 0
# for x in product('0123456789ABCDEF',repeat=8):
#     s = ''.join(x)
#     if s.count('0') == 2:
#         if s.count('A') + s.count('B') + s.count('C') + s.count('D') + s.count('E') <= 2:
#             c += 1
#             print(c,s)

# for i in range(105,1000):
#     n = (bin(i)[2:])
#     ed = n.count('1')
#     nol = n.count('0')
#     for x in range(3):
#         if ed > nol:
#             n += '0'
#         if ed == nol:
#             n += n[-1]
#         else:
#             n += '1'
#
#     r = int(n,2)
#
#     if r % 4 == 0:
#         print(i)
#         break

#
# a = '256 15 4 356 1246 145'.split()
# b = 'аб бг ва вд гд де бв вг'.split()
# print('1 2 3 4 5 6')
# for p in permutations('абвгде'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)
#         break
#
# def f(x,y,z):
#     return (x == y) or ((y or z) <= x)
#
# for a,b,c in product([0,1],repeat=3):
#     table = ((a,1,1,0),
#              (b,c,1,0))
#
#     if len(table) == len(set(table)):
#         for p in permutations('xyz',r=3):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)
#
# for i in range(2,1000):
#     n = int(bin(i)[2:])
#     if n % 5 == 0:
#         n = str(n) + '11'
#     else:
#         res = n // 5
#         dv = bin(res)[2:]
#         n = str(n) + str(dv)
#
#     r = int(n,2)
#     if r > 896:
#         print(i)
#         break
# c = 0
# for x in product('ТИМОФЕЙ',repeat=5):
#     s = ''.join(x)
#     if s.count('Т') >= 1:
#         if s.count('Й') < 1:
#             c += 1
#             print(c)
#
# s = '1' + '9' * 100
# while ('19' in s) or ('299' in s) or ('3999' in s):
#     if '19' in s:
#         s = s.replace('19','2',1)
#     if '299' in s:
#         s = s.replace('299','3',1)
#     if '3999' in s:
#         s = s.replace('3999','1',1)
#
# print(s)
#
# s = 25**5 + 5**14 - 5
# a = ''
# while s != 0:
#     a = str(s%5) + a
#     s //=5
# print(a.count('4'))
#
#
#
# def f(x):
#     if x <= 2:
#         return x+1
#     else:
#         return f(x-1) + 3 * f(x-2)
#
# print(f(4))
#
#
# # c = m = 0
# # f = open('17uu.txt')
# # l = [int(x) for x in f]
# # for i in range(len(l)-1):
# #     for j in range(i+1,len(l)):
# #         if l[i] * l[j] % 10 == 0:
# #             c += 1
# #             m = max(m,l[i]+l[j])
# # print(c,m)
#
# def f(x,y):
#     if x > y or x == 9: return 0
#     if x == y: return 1
#     else:
#         return f(x+1,y) + f(x+2,y)
# print(f(1,7) * f(7,13))
#
# def f(x,y,m):
#     if x + y <= 40: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x-1,y,m-1), f(x,y-1,m-1), f(x//2,y,m-1), f(x,y//2,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(20,100) if f(20,s,1)])
# print('20)', *[s for s in range(20,100) if f(20,s,3) and (not f(20,s,1))])
# print('21)', *[s for s in range(20,100) if f(20,s,4) and (not f(20,s,2))])


from sys import *
# setrecursionlimit(6000)
#
# def f(x):
#     if x >= 10_000:
#         return x
#     if x < 10_000 and x % 3 == 0:
#         return x + f(x/3)
#     if x < 10_000 and x % 3 == 1:
#         return 2 * x+f(x+3)
#
# print(f(999) - f(46))
#
# s = 16807 ** 35 + 2401**2 * 343**9 - 49**52 + 7**3 -2005
# a = ''
# c = 0
# while s > 0:
#     a = str(s%49) + a
#     s //=49
# print(int(a))
# for i in range(1,len(a)-1):
#     if a[i] + a[i+1] > '0':
#         c += 1
# print(c)
#
# c = 0
# for x in permutations('амфибрахий'):
#     s = ''.join(x)
#     if s[4] == 'б' and s[5] == 'р':
#         c += 1
#         print(c,s)
# co = 0
# net = ip_network('192.168.248.176/255.255.255.240',0)
# for ip in net:
#     s = f'{ip:b}'
#     if s.count('0') == s.count('1'):
#         co += 1
# print(co)
#
#
# def f(x,y,m):
#     if x + y >= 200: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x+6,y,m-1), f(x,y+6,m-1), f(x**2,y,m-1), f(x,y**2,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(1,194) if f(3,s,1)])
# print('20)', *[s for s in range(1,194) if f(3,s,3) and (not f(3,s,1))])
# print('21)', *[s for s in range(1,194) if f(3,s,4) and (not f(3,s,2))])

# a = '458 37 26 178 168 357 246 145'.split()
# b = 'ab bf fg gh hc ce ea ef cd dg dh'.split()
# print('1 2 3 4 5 6 7 8')
# for p in permutations('abcdefgh'):
#     # if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)
#         break

# def f(a,b,c):
#     return (a and not(c)) or (not(b) and not(c))
#
# table = ((0,0,0,1),
#          (0,0,1,0),
#          (0,1,0,0),
#          (0,1,1,0),
#          (1,0,0,1),
#          (1,0,1,0),
#          (1,1,0,1),
#          (1,1,1,0))
#
# if len(table) == len(set(table)):
#     for p in permutations('abc',r=3):
#         if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#             print(*p)

# s = 3*1024**75 + 2*256**76 - 16**77 -2023
# a = ''
# while s > 0:
#     a = str(s%32) + a
#     s //=32
# print(a.count('0'))


# def f(x):
#     return (not(x % a == 0)) <= ((x % 6 == 0) <= (not(x % 9 == 0)))
#
# for a in range(10000,1,-1):
#     if all(f(x) for x in range(1,20000)):
#         print(a)
#         break
#
# def f(x,y,m):
#     if x + y >= 123: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x+1,y,m-1), f(x,y+1,m-1), f(x*2,y,m-1), f(x,y*2,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(1,109) if f(13,s,1)])
# print('20)', *[s for s in range(1,109) if f(13,s,3) and (not f(13,s,1))])
# print('21)', *[s for s in range(1,109) if f(13,s,4) and (not f(13,s,2))])
#
# from ipaddress import *
#
# ip1 = ip_address('112.117.107.70')
# ip2 = ip_address('112.117.121.80')
# otv = []
# for mask in range(1,33):
#     net = ip_network(f'112.117.121.80/{mask}',0)
#     count = 0
#     if (ip1 in net) and (ip2 in net):
#         count += 1
#     otv.append(count)
# print(len(otv))

# a = '235 1457 148 237 126 578 2468 367'.split()
# b = 'аб бк ки ие еа вг гд дв ав бг гк де ди'.split()
# print("1 2 3 4 5 6 7 8")
# for p in permutations('абвгдеки'):
#     if all(str(p.index(c2)+1) in  a[p.index(c1)] for c1,c2 in b):
#         print(*p)
#         break


# def f(x,y,z,w):
#     return (w <= y) and ((x <= z) == (y <= x))
#
# for a,b,c,d in product([0,1],repeat=4):
#     table = ((a,1,b,0,1),
#              (0,c,1,d,1),
#              (0,1,0,1,1))
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw',r=4):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)
#                 break

# def f(x,y,a):
#     return ((x*y) > a) or (x > y) or (74 >x)

# for a in range(20000,1,-1):
#     if all(f(x,y,a) for x in range(1,1500) for y in range(1,1500)):
#         print(a)
#         break
    

# c = 0
# for x in product('тихорецк',repeat=4):
#     s = ''.join(x)
#     if s[0] == 'т' or s[0] == 'и' or s[0] == 'х' or s[0] == 'о':
#         if s.count('и') + s.count('о') + s.count('е') == 2:
#             if s[0] != s[1] != s[2] != s[3]:
#                 c += 1
#                 print(s,c)
#
# for i in range(1,1000):
#     n = str(bin(i)[2:])
#     ba = 3*(n.count('1')%3)
#     bu = bin(ba)[2:]
#     if n.count('1') % 3 == 0:
#         n += n[:2]
#     else:
#         n = n + str(bu)
#
#     r = int(n,2)
#     if r < 60:
#
#         print(i)


# a = '235 1457 148 237 126 578 2468 367'.split()
# b = 'аб бк ки ие еа вг гд дв ав бг гк ди де'.split()
# print('1 2 3 4 5 6 7 8')
# for p in permutations('абвгдеки'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)
#         break

# def f(x,y,z):
#     return ((y or z) <= x) or (x == z)
#
# for a,b,c in product([0,1],repeat=3):
#     table = ((0,a,0,0),
#              (b,c,0,0))
#
#     if len(table) == len(set(table)):
#         for p in permutations('xyz',r=3):
#             if all(f(**dict(zip(p,line)))==line[-1] for line in table):
#                 print(*p)
#                 break

# for x in range(100,1000):
#     for y in range(100,1000):
#         x1 = str(x)
#         y1 = str(y)
#         sot = int(x1[0]) + int(y1[0])
#         des = int(x1[1]) + int(y1[1])
#         ed = int(x1[2]) + int(y1[2])
#
#         chislo = str(ed) + str(sot) + str(des)
#
#         if chislo == '002':
#             print(x,y)

# v = 0
# for x in permutations('одеколон'):
#     s = ''.join(x)
#     if s[0] != s[1] != s[2] != s[3] != s[4] != s[5] != s[6] != s[7]:
#         v += 1
#         print(v,s)

#
# def f(x,y):
#     if x >= 129: return y % 2 == 0
#     if y == 0: return 0
#     h = [f(x+1,y-1),f(x*2,y-1)]
#     return any(h) if y % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(1,129) if f(s,2)])
# print('20)', *[s for s in range(1,129) if f(s,4) and (not f(s,2))])
# print('21)', *[s for s in range(1,129) if f(s,5) and (not f(s,3))])
#
#
# c = m = 0
# f = open('17_1998.txt')
# a = [int(x) for x in f]
# for i in range(len(a)-2):
#     k = str(a[i] + a[i+1] + a[i+2])
#     d = int(k)
#     p = a[i] * a[i+1] * a[i+2]
#     if str(k[-1]) == '5':
#         if p % 7 == 0:
#             c += 1
#         m = max(m,d)
# print(c,m)
#
# def f(x,y):
#     if x > y or x == 14: return 0
#     if x == y: return 1
#     else:
#         return f(x+1,y) + f(x+3,y)
# print(f(2,9)*f(9,18))
#
# for i in range(2291,10**10,2291):
#     if fnmatch(str(i), '*222132?'):
#         print(i,i/2291)


# a = '234 156 17 15 246 257 36'.split()
# b = 'bc cd de ef fg gb ga ad ab'.split()
# print('1 2 3 4 5 6 7 ')
# for p in permutations('abcdefg'):
#     if all(str(p.index(c2)+1) in a[p.index(c1)] for c1,c2 in b):
#         print(*p)
#         break

# s = 5*216**1156  - 4*36**1147 + 6**1153 - 875
# a = ''
# while s > 0:
#     a = str(s%6) + a
#     s//=6
# print(a.count('5')-a.count('0'))

# F = [0] *3000
# g = [0] *3000
#
# for n in range(len(F),len(g)):
#     if n < 10:
#         F[n] = n
#     else:
#         F[n] = g[F[n-1]%10] + F[g[n%10]-1] - F[n-3]
#
#     if n < 10:
#         g[n] = n
#     else:
#         g[n] = F[g[n-1]%10] + g[F[n-1]-1] + g[n-2]
#
# print(F[1111]+g[1111])
#
# f = open('17_18045.txt')
# a = [int(x) for x in f]
# c = 0
# mini = 10**6
# dlina = [int(x) for x in f if len(a) == 2]
# dli = len(dlina)
# for i in range(len(a)-1):
#     if (a[i] % 10) + (a[i+1]%10) == dli:
#         c += 1
#         mini = min(mini, a[i]+a[i+1])
# print(c,mini)
#
#
# def f(x,y,s):
#     if x+y >= 79: return s % 2 == 0
#     if s == 0: return 0
#     h = [f(x+1,y,s-1),f(x,y+1,s-1),f(x+y,y,s-1),f(x,y+x,s-1)]
#     return any(h) if s % 2 != 0 else all(h)
#
# print('19)', *[s for s in range(1,70) if f(9,s,2)])
# print('20)', *[s for s in range(1,70) if f(9,s,3) and not(f(9,s,1))])
# print('21)', *[s for s in range(1,70) if f(9,s,4) and not(f(9,s,2))])
#
# def F(A, x):
#     return (not (x % A == 0)) <= ((x % 28 == 0) <= (not (x % 49 == 0)))
#
# for A in range(1, 1000):
#     if all(F(A, x) for x in range(1, 1000)):
#         print(A)

# f = open('17_5916.txt')
# a = [int(x) for x in f]
# c = m = 0
# for i in range(len(a)-1):
#     if (a[i] % 2 == 0 and a[i+1] %2 == 1) or (a[i] % 2 == 1 and a[i+1] %2 == 0):
#         c += 1
#         m = max(m,a[i]+a[i+1])
# print(c,m)
#
# net = ip_network('192.168.32.64/255.255.255.192',0)
# cnt = 0
# for ip in net:
#     s = f'{ip:b}'
#     if s[-3:] == '101':
#         cnt += 1
# print(cnt)


# def f(a,b,c,d):
#     return (not(a) and (not(b))) or (b== c) or d
#
# for a,b,c,d in product([0,1],repeat=4):
#     table= ((a,b,1,c,0),
#             (1,0,d,1,0),
#             (0,0,1,1,0))
#     if len(table) == len(set(table)):
#         for p in permutations('abcd',r=4):
#             if all(f(**dict(zip(p,line)))==line[-1] for line in table):
#                 print(*p)
# c = 0
# for x in product(sorted(list('муха')), repeat=4):
#     s = ''.join(x)
#     c += 1
#     if s == 'хухх':
#         print(c)
#
# for x in '0123456789ABCDEF':
#     a = int(f'2{x}84',19)
#     b = int(f'2B3{x}',16)
#     c = a+b
#     if c % 88 == 0:
#         print(c//88)
#         break


# def f(x,y):
#     if x > y or x == 17: return 0
#     if x == y: return 1
#     else: return f(x+1,y) + f(x*2,y)
# print(f(1,10)*f(10,21))
#
#
# for i in range(1000,10_000):
#     n = str(i)
#     per = int(n[0]) + int(n[1])
#     vtor = int(n[2]) + int(n[3])
#     perv = str(min(per,vtor))
#     vtoro = str(max(per,vtor))
#     chislo = perv + vtoro
#     if chislo == '117':
#         print(i)
