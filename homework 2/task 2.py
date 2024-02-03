number = int(input("Введите число:"))

sum = 0
count = 2

while count <= number:
    if count % 2 == 0:
        sum = sum + count
        count = count - 2
    else:
        count = count + 1

print(sum)

