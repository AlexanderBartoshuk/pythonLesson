a = input("Введите слово : ")
b = input("Введите слово : ")
c = input("Введите слово : ")
d = input("Введите слово : ")
e = input("Введите слово : ")
f = input("Введите слово : ")
g = input("Введите слово : ")
h = input("Введите слово : ")
j = input("Введите слово : ")
k = input("Введите слово : ")

words = {
    1: a,
    2: b,
    3: c,
    4: d,
    5: e,
    6: f,
    7: g,
    8: h,
    9: j,
    10: k,
}

list = []
for key in words.values():
    list.append(key)

count = 0

for word in words:
    if word == word[-1]:
        count += 1

print(count)