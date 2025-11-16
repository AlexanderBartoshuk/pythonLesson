from turtle import * 

#k = 40
#speed(10)
#for i in range(10):
#    forward(5 * k)
#    right(60)
#
#up()
#
#for x in range(-10*k,10*k,k):
#    for y in range(-10 *k,10*k,k):
#        goto(x,y)
#        dot(3,'red')
#
#done()

"""
x1 = xcor()
y1 = ycor()

speed(10)
for i in range(11):
    forward(36)
    right(72)

x2 = xcor()
y2 = ycor()

print(round(((x2-x1)**2 + (y2-y1)**2)) ** 0.5)

done()



k = 40
speed(10)
for i in range(4):
    forward(8*k)
    right(150)
    forward(8*k)
    right(30)

up()

for x in range(-10*k,10*k,k):
    for y in range(-10*k,10*k,k):
        goto(x,y)
        dot(3,'red')

done()


"""
k = 40
speed(115)
for i in range(5):
    forward(7*k)
    right(120*k)

up()

for x in range(-10*k,10*k,k):
    for y in range(-10*k,10*k,k):
        goto(x,y)
        dot(3,'red')

done



tracer(0)
screensize(100000,100000)
lt(90)

r = 20

down()

for i in range(9):
    fd(29 * r)
    rt(90)
    fd(17*r)
    rt(90)

up()

fd(5*r)
rt(90)
fd(1*r)
lt(90)

down()

for i in range(9):
    fd(64*r)
    rt(90)
    fd(48*r)
    rt(90)

up()

for x in range(-10,100):
    for y in range(-10,250):
        goto(x*r,y*r)
        dot(3,'red')
update()
exitonclick()