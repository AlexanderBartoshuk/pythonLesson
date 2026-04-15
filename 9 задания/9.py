# from math import *
# k = 0
# for s in open('8.txt'):
#     a = sorted([int(x) for x in s.split()])
#     if (a[-1] < a[0] + a[1] + a[2]) and (a[0] + a[-1] == a[1] + a[-2]):
#         k += 1
# print(k)
#
#
# kc = 0
# for s in open('2.txt'):
#     a = sorted([int(x) for x in s.split()])
#     p = [x for x in a if a.count(x) == 3]
#     np = [x for x in a if a.count(x) == 1]
#     if len(p) == 3 and len(np) == 3 and (np[0]+np[1]+np[2])* 3 <= (p[0]*p[1]*p[2]):
#         kc += 1
# print(kc)
#
# k = 0
# for s in open('3.txt'):
#     a = sorted([int(x) for x in s.split()])
#     k += 1
#     ct = [x for x in a if x%2 == 0]
#     nct = [x for x in a if x%2 == 1]
#     if len(ct) == len(nct) and (a[0] + a[-1] == a[1] + a[-2] == a[2] + a[-3]):
#         print(k)
#
# k = 0
# for s in open('4.txt'):
#     a = sorted([int(x) for x in s.split()])
#     p = [x for x in a if a.count(x) > 1]
#     np = [x for x in a if a.count(x) == 1]
#     if sum(np) *3 <= prod(p) and len(p) > 0: # prod - произведение
#         k+=1
# print(k)
#
#
# k = 0
# for s in open('5.txt'):
#     a = sorted([int(x) for x in s.split()])
#     if (a[-1] + a[0]) ** 2> (a[1]**2 + a[2]**2 + a[3]**2):
#         k += 1
# print(k)

# k = 0
# for s in open("88.txt"):
#     a = sorted([int(x) for x in s.split()])
#     if (a[0] + a[2]) / 2 == a[1]:
#         k += 1
# print(k)

# f = open('27B.txt')
# s = f.readlines()
# c = 0
# for i in range(1,len(s)):
#     for j in range(i,len(s)):
#         if (int(s[i]) * int(s[j])) % 10000000 == 0 and (int(s[i]) * int(s[j])) % 100000000 != 0 and i != j:
#             c += 1
# print(c)

# k = 0
# for s in open('555.txt'):
#     a = sorted([int(x) for x in s.split()])
#     if a[0] % 5 != 0 and a[1] % 5 != 0 and a[2] % 5 != 0 and a[3] % 5 != 0 and a[4] % 5 != 0 and a[5] % 5 != 0:
#         print(a)


k = 0
for s in open('8989.txt'):
    if s[0] + s[1] + s[2] < s[3]:
        k += 1
print(k)



