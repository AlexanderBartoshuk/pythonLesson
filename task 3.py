def homework(n):
    if n < 10:
        return n
    else:
        return n % 10 + homework(n // 10)
input = int(input("Введите число:"))
print(homework(input))
