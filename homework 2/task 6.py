import math

n = int(input("Введите число"))

a = 2
b = int(math.sqrt(n))

def main():
    for x in range(a, b):
        if n // x == 0:
            print("True")
        else:
            print("False")
main()