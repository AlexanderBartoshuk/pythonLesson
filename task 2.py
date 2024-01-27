n = int()

def homework(n):
    n = n//3
    if n == 3:
        return True
    elif n // 3:
        return(homework(n))
    else:
        return False

input = int(input("Введите число:"))
print(homework(input))

