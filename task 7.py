number = int(input("Введите число:"))

sum = 0
count = 1

while count <= number:
    if count % 1 == 0:
        sum = sum + count
        count = count + 1
print(sum)

