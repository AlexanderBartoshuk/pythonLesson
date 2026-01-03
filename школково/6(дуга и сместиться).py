from turtle import *
#                                СМЕСТИТЬСЯ НА
#
# x,y = 0,0
# tracer(0)
# penup()
# m = 40
# goto(x*m,y*m)
# pendown()
#
# for i in range(20):
#     new_x = x+4
#     new_y = y+3
#     goto(new_x*m,new_y*m)
#     x,y = new_x,new_y
#
#     new_x = x-4
#     new_y = y-3
#     goto(new_x*m,new_y*m)
#     x, y = new_x, new_y
#
#     new_x = x-12
#     new_y = y-5
#     goto(new_x*m,new_y*m)
#     x,y = new_x,new_y
#
#     new_x = x +12
#     new_y = y + 5
#     goto(new_x*m,new_y*m)
#     x,y = new_x,new_y
#
# pu()
#
# for x in range(-25,25):
#     for y in range(-25,25):
#         goto(x*m,y*m)
#         dot(3)
# done()


#                       ДУГА

lt(90)
tracer(0)
k = 20


rt(180)
fd(3*k)
rt(90)
fd(48*k)
rt(90)
fd(3*k)

for i in range(6):
    seth(90)
    circle(-4*k,180)
penup()

for x in range(-250,25):
    for y in range(-25,25):
        goto(x*k,y*k)
        dot(3,'red')
done()

