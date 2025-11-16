#from fnmatch import *

#for x in range(0,10**9,23):
#   if fnmatch(str(x), '12345?7?8'):
#       print(x, x//23)


#for i in range(0,10**10,2023):
#    if fnmatch(str(i), '1?2139*4'):
#        print(i, i//2023)
#
#
#for x in range(0,10**10,3013):
#    if fnmatch(str(x), '1?3948*5'):
#        print(x)
#
#
#for b in range(0,10**8,273):
#    if fnmatch(str(b), '12??36*1'):
#        print(b, b//273)
#
#for x in range(0,10**9,9117):
#   if fnmatch(str(x), '4*64*9?7'):
#       print(x)
#
# 2 тип задания 

#for x in range(174457,174505+1):
#    k = 0
#    s = []
#    for y in range(2, x//2+1):
#        if x%y == 0:
#            k +=1 
#            s.append(y)
#            if k > 2:
#                break
#    if k ==2 :
#        print(s)
#
#for x in range(210235,210300+1):
#    k = 0
#    s = []
#    for y in range(2,x//2+1):
#        if x%y == 0:
#            k +=1 
#            s.append(y)
#            if k > 4:
#                break
#    if k ==4:
#        print(s)
#

#for x in range(312614,312651):
#    k = 0
#    s = []
#    for y in range(2,x//2+1):
#        if x%y ==0:
#            if y%2 ==0:
#                k +=1 
#                s.append(y)
#    if k == 6:
#        print(x,s)
#
#for n in range(95632,95700+1):
#    c = 0
#    de = []
#    for j in range(1,n+1):
#        if n % j == 0:
#            if j % 2 == 0:
#                c += 1
#                de.append(j)
#    if c == 6:
#        print(n,de)

#
#maxi = 0
#for i in range(120115, 120201):
#    numdel = 0
#    for j in range(1, i + 1):
#        if i % j == 0:
#            numdel += 1
#    if numdel >= maxi:
#        maxi = numdel
#        maxinum = i
#print(maxi, maxinum)
#
#
#mn =  0
#m = 0
#for i in range(568023,569231):
#    n = 2
#    for j in range(2,i//2+1):
#        if i%j ==0:
#            n +=1 
#    if n > m:
#        m=n
#        mn = i
#print(m,mn)
#
#
#for x in range(2422000,2422080):
#    k = 0
#    for j in range(2,int(x**0.5) +1):
#        if not x%j:
#            break
#    else:
#        k +=1 
#        print(k,x)
#
#
#for n in range(1,100):
#    s = bin(n)[2::]
#    s = s + str(s.count('1') % 2)
#    s  = s +str(s.count('1') % 2)
#    r = int(s,2)
#    if r > 123:
#        print(r)
#        break
#
print(192*200)