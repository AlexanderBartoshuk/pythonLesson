# Напишите программу, которая ищет среди целых чисел,
# принадлежащих числовому отрезку [55556;55776]  , простые числа.
# Программа должна вывести количество таких чисел.

def f(x): # функция для проверки, что число - простое
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
k = 0
for i in range(55556,55776):
    if f(i):
        k += 1
print(k)

def f(x):
    if x == 1: return False
    for i in range(2,int(x**0.5)+1):
        if x % i ==0: return  False
    return True

k = 0
for i in range(25432, 45432):
    if f(i):
        k += 1
print(k)


count = 0
for i in range(12345,12426):
    has = False
    for j in range(1,i+1):
        if i % j == 0:
            if str(j) == str(j)[::-1] and len(str(j)) > 1:
                has = True
                break
            if str(i//j) == str(i//j)[::-1]  and len(str(i//j)) > 1:
                has = True
                break
    if has:
        count += 1
print(count)


