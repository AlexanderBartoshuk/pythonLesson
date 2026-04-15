# f = open('2401.txt').readline()
# k = 1
# m = 0
# for i in range(1, len(f)):
#     if f[i] == f[i-1] == "X":
#         k += 1
#     else:
#         m = max(k,m)
#         k = 1
# m = max(m,k)
# print(m)
#
# f = open('2403.txt').readline().split('E')
# k = 0
# for i in f:
#     if len(i) >= 10 and i.count('F') == 0:
#         k += 1
# print(k)
#
# f = open('2404.txt')
# n = f.readline()
# n = n.replace('CA','x')
# n = n.replace('CO','x')
# n = n.replace('DA','x')
# n = n.replace('DO','x')
# n = n.replace('FA','x')
# n = n.replace('FO','x')
# n = n.replace('A','y')
# n = n.replace('C','y')
# n = n.replace('D','y')
# n = n.replace('F','y')
# n = n.replace('O','y')
# s = n.split('y')
# print(max([len(x) for x in s]))
#
# f = open('2405.txt').readline().split('F')
# k = 1
# m = 0
# for i in range(len(f)):
#     if f[i].count('A') <= 2:
#         k += len(f[i]) +1
#         m = max(k,m)
#     else:
#         k = 1
# print(m)

f = open('24_2425.txt')
s = f.read()
s1 = 'DBAC'
a = s.split(s1)
while len(a) > 1:
    s2 = s1
    s1 += 'DBAC'
    a = s.split(s1)
if s2 + 'D' in s:
    s2 += 'D'
    if s2 + 'B' in s:
        s2 += 'B'
        if s2 + 'A' in s:
            s2 += 'A'
print(len(s2))