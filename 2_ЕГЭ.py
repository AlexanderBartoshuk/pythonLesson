#print('x y z w')
#for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            for w in 0,1:
##                F =(not(x) or y or (z and not(w)))
##                if not(F):
##                    print(x,y,x,w)
#
#
##a = {0: "А", 1: "К", 2: "Р", 3: "У"}
##k = 0
##for i in range(0, len(a)):
##    for j in range(0, len(a)):
##        for g in range(0, len(a)):
##            for m in range(0, len(a)):
##                for n in range(0, len(a)):
##                    k += 1
##                    if a[i] == "К":
##                        print(k) # Возьмем первое число, которое выведет программа
##                        break
#
#def f_1(x, y, z, w):
#    if ((x <= y) == (w or not(z))) == 1:
#        return 1
#    else:
#        return 0
#def f_2(x, y, z, w):
#    if ((x <= y) and (not(w) == z)) == 1:
#        return 1
#    else:
#        return 0
#print('x y z w  f1 f2')
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            for w in range(2):
#                print(x, y, z, w, ' ', f_1(x, y, z, w), ' ',f_2(x, y, z, w))
#
#
#def f(x, y):
#    if x > y:
#        return 0
#    if x == y:
#        return 1
#    else:
#        return f(x + 1, y) + f(x + 2, y) + f(x + 3, y)
#print(f(1, 8) * f(8, 15))
#


#for i in range(2000000,3000001):
#    a = i**0.5
#    k = 0
#    for b in range(1, round(a)):
#        if i % b == 0:
#            if(abs(i / b) - b) <= 115:
#                k += 1
#    if k > 2: print(i)
#    k = 0



#maxlen = 0
#for i in a.split('E'):
#    if i.count('A') > 2:
#        maxlen = max(maxlen,len(i))
#print(maxlen)
#
#
#print((1542613234-765432010) // 3 + 1)


