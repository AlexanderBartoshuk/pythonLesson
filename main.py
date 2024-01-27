#Implement a program that finds the sum of the digits of a given number

n = int(input("Введите число:"))
list = []
while n > 0 :
    list.insert(0, n % 10)
    n = n // 10

print(list)

