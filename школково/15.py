# def f(x,a):
#     return (x % a != 0) <= ((x % 21 != 0) and (x % 35 != 0))
#
# for a in range(10000,1,-1):
#     b = False
#     for x in range(1000):
#         if not(f(x,a)):
#             b = True
#     if not(b):
#         print(a)
#         break
#
# def f(x):
#     return (x % a != 0) <= ((x % 21 != 0) and (x % 35 != 0))
#
# for a in range(10000,1,-1):
#     if all(f(x) for x in range(1,10000)):
#         print(a)
#         break

# def f(x):
#     return ((x % 34 == 0) and (x % 51 != 0)) <= ((x % a != 0) or (x % 51 == 0))
#
# for a in range(1,10000):
#     if all(f(x) for x in range(1,10000)):
#         print(a)
#         break


p = [i for i in range(2,21,2)]
q = [x for x in range(5,51,5)]
a = [i for i in range(100)]
for i in range(100):
    for x in range(1000):
        if (((x == i) <= (x in p)) or ((x not in q) <= (x != i))) == 0:
            a.remove(i)

print(len(a))


# def f(x):
#     return x & 51 == 0 or ((x &42 == 0) <= (x & a != 0))
#
# for a in range(1,1000):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break

# def f(x):
#     return (x & a != 0) <= ((x & 11 == 0) <= (x & 17 != 0))
#
# for a in range(1000,1,-1):
#     if all(f(x) for x in range(1,1000)):
#         print(a)

def f(x):
    return ((x & 47 != 0) or (x & 24 !=0)) <= ((x & 29 == 0) <= (x & a != 0))
for a in range(1,1000):
    if all(f(x) for x in range(1,1000)):
        print(a)
        break

                                    # ОТРЕЗКИ

# p = list(range(55,100))
# q = list(range(66,130))
# a = []
# for x in range(1,1001):
#     if (x in p) <= (((x in q) and not(x in a)) <= (not(x in p))):
#         a.append(x)
# print(len(a))


# p = list(range(15,50))
# q = list(range(36,60))
# a = list(range(100))
# for x in range(100):
#     if (((not (x in a)) <= (x in p)) <= ((x in a) <= (x in q))):
#         a.remove(x)
# print(len(a))

#                                         CМЕШАННОЕ

# def f(x,y):
#     return (x < a) or (y < a) or ((x * y ) % 4 == 0) or ((2*x + 3*y) != 100)
#
# for a in range(1,1000):
#     if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
#         print(a)
#         break
#

# def f(x):
#     return ((x % 3 == 0) and (x % 7 == 0)) <= ((x & 13 != 0) or (x & 32 == 0) or (a*x <= 120834))
#
# for a in range(1001,1,-1):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break
#
# def inn(x,b):
#     return b[0] <= x <= b[1]
#
# def f(x,a):
#     b = [50,70]
#     return (x % a != 0) <= (inn(x,b) <= (x % 15 != 0))
#
# maxim =  0
# for a in range(1,500):
#     flag= True
#     for x in range(1,760):
#         if not(f(x,a)):
#             flag= False
#             break
#     if flag:
#         maxim = a
# print(maxim)

# for a in range(1,10000):
#     flag = True
#     for x in range(5,(4095+1)*2+1,2):
#         for y in range(2,4095+1,2):
#             if x * y % a == 0:
#                 flag = False
#                 break
#         if not flag:
#             break
#     if flag:
#         print(a)
#         break

# def f(x):
#     return ((x % 13 == 0) <= (not x + 25 > 0)) or (x+a >= 245)
#
# for a in range(1,1000):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break

minlen = 10**6

def tup(a,b,c):
    if (a <= b <= c) and (a+b > c) and (a**2 + b**2 < c**2):
        return True
    else:
        return False

def ostr(a,b,c):
    if (a <= b<=c) and (a+b > c) and (a**2 + b**2 < c**2):
        return True
    else:
        return False

def f(x,a1,a2):
    return (ostr(39, 80, x) or tup(65, 72, x) or ((x <= 80 or x >= 119) or (a1 <= x <= a2)))

for a1 in range(100):
    for a2 in range(100):
        if all(f(x,a1,a2) for x in range(1,130)):
            minlen = min(minlen,a2-a1)
print(minlen)


def treugolnik(a,b,c):
    a,b,c = sorted([a,b,c])
    return a+b > c

summa = 0

for a in range(1,1000):
    flag= True
    for x in range(1,1000):
        if (not(not treugolnik(x, 333, a) and not treugolnik(879, x, a)) or (x > 600)) == False:
            flag = False
    if flag:
        summa += a
print(summa)
