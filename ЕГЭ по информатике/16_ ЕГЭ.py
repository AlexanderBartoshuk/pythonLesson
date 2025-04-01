# Задание 16

def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n/2)
    if n % 2 != 0:
        return 1 + f(n-1)
k = 0
for n in range(1, 1001):
    if f(n) == 3:
        k += 1
print(k)



def d(n):
    if n <= 1:
        return 0
    if n >1 and n%2 == 1:
        return d(n-1) + 3*n*n
    if n > 1 and n%2 == 0:
        return n/2 + d(n-1)+2
    
print(d(49))

def g(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + g(n-1)
    if n > 1 and n % 2 == 1:
        return 2 * g(n-2)
    
def a(n):
    if n ==1 :
        return 1 
    if n>1:
        return n * a(n-1)
    
print(a(2023)/a(2020))


def s(n):
    if n ==1 :
        return 1
    if n == 2:
        return 2 
    if n > 2 and n%2 ==0:
        return (3*n+s(n-3)) // 3
    if n > 2 and n%2 == 1:
        return (7*n+s(n-1)-s(n-2)) // 5
    
s(35)

def y(n):
    if n < 11:
        return 10
    if n >= 11:
        return n + y(n-1)

print(y(2024)-y(2022))


def fin(n):
    if n ==1 :
        return 1 
    if n == 2:
        return 3 
    if n > 2:
        return fin(n-1) *n + fin(n-2)*(n-1)
fin(5)

def fun(n):
    if n <=2:
        return n+4
    if n > 2:
        return fun(n-1) + fun(n-2)
fun(6)

def l(n):
    if n == 0:
        return 0
    if n > 0 and n%3 ==0:
        return n + l(n-3)
    if n % 3 > 0:
        return n + l(n-(n%3))
l(22)

def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 != 0:
        return F(n-1)+3*F(n-2)
    if n > 2 and n % 2 == 0:
        return sum(F(i) for i in range (1,n)) 
print(F(28))



def under( n):
    if n == 1:
        return 1 
    if n > 1:
        return n * under(n-1)
print((under(2024)-under(2023)) / under(2022))



a = 7**48
print(a)