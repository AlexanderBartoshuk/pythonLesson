def homework(n):
    if n > 1:
        homework(n-1)
    print(n, end="")

n = int(input("Введенные числа:"))
homework(n)