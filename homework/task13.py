
def function(a,b):
    if b == 0:
        return a
    else:
        return function(b, a%b)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = function(a, b)
print(f"НОД:{c} ")