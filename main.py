
def homework(n):
    if n == 3:
        return "True"
    else:
        if n % 3 != 0:
            return "False"
        else:
             return homework(n // 3)

input = int(input("Введите число:"))

print(homework(input))

