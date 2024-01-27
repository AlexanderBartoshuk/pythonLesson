
def Fibonachi(n):
    if n <= 0:
        input = int(input("Введите новое число:"))
        Fibonachi(input)
    else:
        if n == 1:
            return 0
        else:
            if n == 2:
                return 1
            else:
                return Fibonachi(n-1) + Fibonachi(n-2)


input = int(input("Введите число:"))
print(Fibonachi(input))
print(Fibonachi(input))