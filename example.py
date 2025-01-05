def f(n):
    if n <= 2:
        return 2
    else:
        return 2 * f(n-1) + f(n-2)
    
f(5)


print("x","y","w","z")
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                F = (not(z == w) <= (w and not(x)) or (x and not(y)))
                if not(F):
                    print(x,y,w,z)

print(bin((4 **8) + (2 ** 8) - 8).count('1')) # task 14 ЕГЭ 
print(bin((9**8) + (3**8) - 2).count('1'))








print('x',"y","z","w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((not(y)) <= (z==w)) and ((z <= x) == w):
                    print(x,y,z,w)



def x(n):
    if n ==1 :
        return 1
    else:
        if n > 1:
            return x(n-1) + n
x(30)
    

import turtle as t
t.left(90)
t.speed(1000)
k=10
t.down()
for i in range(3):
    t.forward(7*k)
    t.right(90)
t.forward(8*k)
for i in range(3):
    t.left(90)
    t.forward(5*k)
t.up()
for x in range(-1, 8):
    for y in range(-5, 8):
        t.goto(x*k,y*k)
        t.dot('red')