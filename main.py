#def multiply(a,b): return a*b
#
#def print_multiply(a,b,operation):
#    result = operation(a,b)
#    print(result)
#
#a = 5
#b = 4
#print_multiply(a,b,multiply)

a = 36**7 + 6**19 - 18
s = ''
while a!= 0:
    s += str(a%6)
    a //= 6
s = s[::-1]
print(s.count('5'))



def F(n):
    if n == 1:
        return 1
    else:
        if n > 1:
            return(F(n-1) * n)
print(F(5))


def f(x, y):
    if x > y or x == 6 or x == 12:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x + 3, y)
print(f(3, 16))


print((1542613234 - 765432010) //3 +1)

def d(x,y):
    if x > y or x == 16:
        return 0
    if x == y:
        return 1
    else:
        return f(x+1, y) + f(x*2,y)
print(f(1,10) * f(10,21))


for i in range(2000000, 3000001):
    sqrti = i**0.5 
    k = 0
    for j in range(1, round(sqrti)):
        if i % j == 0:
            if (abs(i / j) - j) <= 115:
                k += 1
    if k > 2: print(i)
    k = 0