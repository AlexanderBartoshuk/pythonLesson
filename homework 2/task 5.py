a = int(input("Введите число: "))
b = int(input("Введите степень числа"))

power = 1
i = 1

while i <= b:
    power = power * a
    i = i + 1
print(power)