def f(x,y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2,y)
print(f(1,10) * f(10,21) * f(21,30))

def e(x,y):
    if x > y:
        return 0
    if x == y:
        return 1 
    else:
        return e(x+1,y) + e(x *2, y) + e(x+3,y)
print(e(2,10) * e(10,14))


def d(x,y):
    if x > y or x == 26:
        return 0
    if x == y:
        return 1 
    else:
        return d(x+1,y) + d(x*2+1,y)
print(d(1,27))


def g(x,y):
    if x > y or x == 12 or x == 6:
        return 0
    if x == y:
        return 1 
    else:
        return g(x+1,y) + g(x*2, y) + g(x+3, y)
print(g(3,16))


def f(start, end, k):
    if start > end + 1:
        return 0
    if start == end:
        return 1 
    else:
        if k==1:
            return f(start + 3, end, k-1) + f(start *2, end, k-1)
        else:
            return f(start-1, end, k+1) + f(start+3, end, k) + f(start*2, end, k)
print(f(3,12,0))
        

def f(x,y):
    if x < y or x==10 or x== 15:
        return 0 
    if x == y:return 1
    if x%2 ==0 and x%3==0:
        return f(x-1,y) + f(x//2,y) + f(x//3,y)
    if x%2 == 0 and x%3 != 0:
        return f(x-1,y) + f(x//2,y)
    if x%2 != 0 and x%3==0:
        return f(x-1,y) + f(x//3,y)
    if x%2 != 0 and x%3 != 0:
        return f(x-1,y)

print(f(22,1))

def f(x,y):
    if x>y or x == 17:
        return 0
    if x == y: return 1
    else:
        return f(x+1,y) + f(x*2,y)
print(f(1,10) * f(10,21))


def f(x,y):
    if x > y or x == 15 or x == 9: return 0
    if x == y: return 1 
    else:
        return f(x+1,y) + f(x+3,y) + f(x*3,y)
print(f(3,18))



def f(x,y):
    if x > y: return 0
    if x == y: return 1 
    else:
        return f(x+1,y) + f(x+3,y)
print(f(2,15))


def f(x,y):
    if x > y: return 0
    if x == y: return 1 
    else:
        return f(x+1,y) + f(x+3,y) + f(x+(x-1), y)
print(f(2,10))


def f(start,end,s):
    if start == end and '+++' not in s and '***' not in s:
        return 1
    elif start > end: return 0
    return f(start+1,end,s + '+') + f(start*2,end, s + '*')
print(f(1,16, ''))


def f(start, end, d):
    if start > end: return 0
    if start == end and d==1: return 1
    else:
        return f(start +1,end, d) + f(start + 2,end, d) + f(start * 2, end, d+1) + f(start*3, end, d+1)
print(f(1,10,0))






def f(x,y):
    if x>y or x == 25: return 0
    if x == y: return 1 
    else:
        return f(x+1,y) + f(x*2,y)
print(f(2,14) * f(14,29))



def F(n):
    if n <= 2: return 2
    else: 
        return F(n-1)+2 * F(n-2)
F(5)


for i in range(100,0,-1):
    s = bin(i)[2::]
    s = str(s)
    if i % 2 == 0:
        s += '00'
    else:
        s += '11'
    r = int(s,2)
    if r < 94:
        print(i)
        break


print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(not((x or not(y)) and (not(z) == w)) or (y and z)):
                    print(x, y, z, w,)  