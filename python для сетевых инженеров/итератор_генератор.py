# Итерируемый объект

# Примеры итерируемых объектов:

#все последовательности: список, строка, кортеж

#словари

#файлы

numbers = [1,2,3,4,5,6,8]
a = iter(numbers)
next(a)


for item in numbers:
    print(item)

f = open('r1.txt')
f.__next__()


with open("r1.txt") as f:
    for line in f:
        print(line.rstrip())
