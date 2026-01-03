#for x in range(174457,174506):
#    k = 0
#    s = []
#    for y in range(2,x//2+1):
#        if x % y == 0:
#            k += 1
#            s.append(y)
#            if k > 2:
#                break
#    if k == 2:
#        print(*s)


#for x in range(210235,210300+1):
#    k = 0
#    s = []
#    for y in range(2,x//2+1):
#        if x % y == 0:
#            k += 1
#            s.append(y)
#            if k > 4:
#                break
#    if k == 4:
#        print(*s)
#
#for n in range(110203, 110245 + 1):
#    even_divisors = []  
#    for d in range(2, n + 1, 2):
#        if n % d == 0:  # если d - делитель n
#            even_divisors.append(d)
#            if len(even_divisors) > 4:  # оптимизация: если их уже больше 4
#                break
#    if len(even_divisors) == 4:  # если ровно 4 четных делителя и выводим число и его четные делители
#        print(n, *even_divisors)
#

#maxi = 0
#for i in range(84052,84131):
#    num = 0
#    for x in range(1,i+1):
#        if i % x ==0:
#            num += 1
#    if num > maxi:
#        maxi = num
#        mini = i
#print(maxi,mini)

#for x in range(201455,201470):
#    s = []
#    for y in range(1,x+1):
#        if x % y == 0: 
#            s.append(y)
#            if len(s) > 4: break
#    if len(s) == 4:
#        print(*s)

#c = 0
#for n in range(2422000, 2422081):
#    if n > 1 and all(n % d for d in range(2, int(n**0.5) + 1)):
#        c += 1
#        print(c, n)


#for x in range(489421,489440):
#    s = []
#    for y in range(1,x+1):
#        if x % y == 0:
#            s.append(y)
#            if len(s) > 4:
                #break
#    if len(s) == 4:
#        print(*s)


#for x in range(125256,125330):
#    s = []
#    for i in range(2,x+1):
#        if i % 2 == 0 and x % i  == 0:
#            s.append(i)
#            if len(s) > 6:
#                break
#    if len(s) == 6:
#        print(*s)


#maxi = 0
#for x in range(568023,569231):
#    k = 2
#    for i in range(2,x//2+1):
#        if x % i == 0:
#            k+=1
#            
#    if k > maxi:
#        maxi = k
#        mini = x
#print(maxi,mini)


#for i in range (1000000,2000000+1):
#    a = []
#    k = int(i**0.5)+1
#    for j in range (1,k):
#        if i%j==0:
#            if ((i//j)-j)<=100:
#                a.append((i//j)-j)
#    if len(a) >= 3:
#        print(i)

for x in range(0,31,2):
    for i in range(1,19,2):
        if (200000000 <= 2**x * 3**i <= 400000000):
            print(2**x * 3**i)


c = 0
for x in range(452022,1000000):
    d = []
    for i in range(2,x):
        if x % i == 0:
            d.append(i)
            if len(d) >= 2:
                m = d[0] + d[-1]
    if m % 7 == 3:
        c += 1
        print(x,i)
    if c == 5:
        break 



