f = open("27b.txt")  # для файла A замените название
s = f.readlines()
n = int(s[0])  # количество пар
summi = 0
d = 10**6
for i in range(1, n + 1):
    x, y = map(int, s[i].split())
    summi += max(x, y)
    if abs(x - y) % 3 != 0:
        d = min(d, abs(x - y))
if summi % 3 != 0:
    print(summi)
else:
    print(summi - d)


# f = open('27-B_2.txt')
# s = int(f.readline())
# n = [int(x) for x in f]
# n14 = [0]
# n2 = [0]
# n7 = [0]
# proiz = max(n)
# for i in range(s):
#     if n[i] % 14 == 0 and n[i] != proiz:
#         n14.append(n[i])
#     elif n[i] % 7 == 0:
#         n7.append(n[i])
#     elif n[i] % 2 == 0:
#         n2.append(n[i])
# print(max(max(n2)*max(n7),max(n14)*proiz))


n = [int(s) for s in open('27989_A.txt')][1:]
n2= len([int(x) for x in f if x % 2 == 0 and x % 13 != 0])
n13= len([int(x) for x in f if x % 13 == 0 and x % 2 != 0])
n26= len([int(x) for x in f if x % 26 == 0])
a = len(n)
print(n26*(n26-1)//2 + n26*(a-n26)//2 + n2*n13)

f = open('27989_A.txt')
s = int(f.readline())
k26 = 0
k13 = 0
k2 = 0
k0 = 0

for _ in range(s):
    x = int(f.readline())
    if x % 26 == 0:
        k26 += 1
    elif x % 13 == 0:
        k13 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        k0 += 1

# Количество пар
count = k26 * (k26 - 1) // 2 + k26 * (k13 + k2 + k0) + k13 * k2
print(count)


f = open('27k.txt')
n = int(f.readline())
a = list(map(int, f.readlines()))
a.sort()
b_0 = [i for i in a if i % 3 == 0][-3:]
b_1 = [i for i in a if i % 3 == 1][-3:]
b_2 = [i for i in a if i % 3 == 2][-3:]
print(max(sum(b_0), sum(b_1), sum(b_2), b_1[-1] + b_2[-1] + b_0[-1]))
