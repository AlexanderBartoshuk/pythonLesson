num = int(input("Введите свое число:"))


def palindrom(num):
    num_str = str(num)
    return num_str == num_str[::-1]

if palindrom(num):
    print("Это палиндром")
else:
    print("ЭТО ОБМАН, ВВЕДИТЕ ЧИСЛО ЗАНОВО")
