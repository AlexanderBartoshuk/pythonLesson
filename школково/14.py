from math import *
#                         Арифметические выражения

# a = 2**43 + 2**14 + 2
# s = ''
# while a > 0:
#     s = str(a%4) + s
#     a//=4
#
# count = 0
# s1 = int(s)
# while s1 > 0:
#     if s1 % 10 != 0:
#         count += 1
#     s1 //=10
# print(count)

# a = 5**14 + 25**3 - 117
# s = ''
# while a > 0:
#     s = str(a%5) + s
#     a //=5
#
# print(s.count('4'))

# a = 9**6 + 81**8 - 32
# s = ''
# while a > 0:
#     s = str(a%9) + s
#     a//=9
#
# print(s.count('0'))


# a = 16**6 + 16**13 - 289
# s= ''
# while a > 0:
#     s = str(a%16) + s
#     a//=16
# print(s.count('15'))
#
#
# a = 2**43 + 2**14 + 2
# print(bin(a).count('1'))

#                          Поиск цифр(-ы) числа

# for x in range(1,1000000):
#     a = 343**5 + 7**3 -1 -x
#     counter = 0
#     while a != 0:
#         counter += a % 7 == 6
#         a//=7
#
#     if counter == 12:
#         print(x)
#         break

# for x in range(1,100):
#     a = int(f'20{x}3',4)
#     b = int(f"1{x}32",4)
#     c = a + b
#     if c % 3 == 0:
#         print(c//3)
#         break

# for x in range(1,100):
#     a = int(f"1{x}34",6)
#     b = int(f"23{x}1",4)
#     c = a+b
#     if c % 7 == 0:
#         print(c//7)
#
# for x in range(11):
#     a = int(f'348{x}5',11)
#     b = int(f"1{x}111",11)
#     c = a+b
#     if c % 8 == 0:
#         print(c // 8)
#         break
#
# for x in range(7):
#     a = int(f'1213{x}6',7)
#     b = int(f'51{x}431',7)
#     c = a+b
#     if c % 91 == 0:
#         print(c//91)
#         break
#
#
# for x in range(25, 0, -1):
#     t = [(1 * 26**4 + 3 * 26**3 + y * 26**2 + x * 26 + 5 +
#            2 * 26**4 + 4 * 26**3 + y * 26**2 + 1 * 26 + 3) % 8 == 0
#             for y in range(26)]
#     if all(t):
#         print((1 * 26**4 + 3 * 26**3 + 2 * 26**2 + x * 26 + 5 +
#            2 * 26**4 + 4 * 26**3 + 2 * 26**2 + 1 * 26 + 3) // 8)
#         break
#
# def four(num):
#     n = num
#     s= ""
#     while n>0:
#         s = str(n%4) + s
#         n //=4
#     return s
#
# for x in range(1,4999):
#     hx = hex(x)[2:]
#     ot = oct(x)[2:]
#     f = four(x)
#     if (len(hx) == 3 and hx[1] == "3"  # Средняя цифра в шестнадцатеричной записи равна ’3’
#     and len(ot) == 3 and ot[0] == '4' and ot[2] == '1'  # Первая и последняя цифры в восьмеричной записи
#     and len(f) == 5 and f[-1] == '1'):  # Последняя цифра в четверичной записи равна ’1’
#         print(x)  # Если все условия выполняются, выво
#
# ans = 0
# for x in range(121):
#     s1 = 5*121**4 + 6*121**3 + 1*121**2 + x*121 + 4
#     s2 = 1*121**4 + x*121**3 + 2*121**2 + 9*121
#     c = s1 + s2
#     if c % 17 == 0:
#         ans += c//17
#
# print(ans)
#
# maxim =0
# for x in '0123456789ABC':
#     s = 17**200 - int(f'365{x}2',13)
#     sum_digit = 0
#     while s > 0:
#         sum_digit += s%17
#         s//=17
#     maxim = max(maxim,sum_digit)
# print(maxim)
#
#
#
# for x in range(17):
#     a = int(f'11{x}586',17)
#     b = int(f'5{x}211',17)
#     c = a+b
#     if c % 49 == 0:
#         print(c//49)
#         break
#
# for x in range(21):
#     a = int(f'12{x}AC',21)
#     b = int(f'90F{x}E',21)
#     c= a+b
#     if c % 53 == 0:
#         print(c/53)
#         break



