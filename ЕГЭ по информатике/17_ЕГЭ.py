#f = open('1-7.txt')
#b = [int(i) for i in f]
#c = [int(x) for x in b if int(x)%2 == 0]
#t1 = sum(c) / len(c)
#n, max1 = 0,0
#for j in range(0,len(b)-1):
#    if ((b[j] % 3 == 0) or (b[j + 1] % 3 == 0)) and ((b[j] < t1) or (b[j + 1] < t1)):
#        n += 1
#        max1 = max(max1,b[j]+b[j+1])
#print(n,'',max1)

#count = 0
#m = -20001
#f = open('17.txt')
#l = [int(i) for i in f]
#for i in range(len(l)-1):
#    if (l[i] % 3 == 0) or (l[i+1]%3== 0):
#        count += 1
#        m = max(m,l[i] + l[i+1])
#print(count,m)
#
#count = m = 0
#f = open('17-1.txt')
#l = [int(i) for i in f]
#for i in range(len(l)-1):
#    for j in range(i+1,len(l)):
#        if (l[i] + l[j]) % 8 == 0:
#            count +=1 
#            m = max(m,l[i] + l[j])
#print(count,m)
#
#
#count = m = 0
#f = open('17-2.txt')
#l = [int(i) for i in f]
#for i in range(len(l)-1):
#    for j in range(i+1,len(l)):
#        if (l[i] % 160 != l[j]%160) and ((l[i] % 7 == 0) or (l[j] % 7 ==0)):
#            count += 1
#            m = max(m,l[i]+l[j])
#print(count,m)



#count = m = 0
#f= open('17-3.txt')
#l = [int(i) for i in f]
#for i in range(len(l)-1):
#    for j in range(i+1,len(l)):
#        if (l[i] - l[j]) % 2 == 0 and (l[i] % 19 == 0 or l[j] % 19 == 0):
#            count += 1 
#            m = max(m,l[i] + l[j])
#print(count,m       )


#count = m = 0
#f = open('17-10.txt')
#l = [int(i) for i in f]
#for i in range(len(l)-1):
#    for j in range(i+1,len(l)):
#        if ((l[i]+l[j]) % 2 != 0) and (l[i]*l[j] % 3 == 0):
#            count += 1
#            m = max(m,l[i]+l[j])
#print(count,m)


#count = m = 0
#f = open('17-17.txt')
#l = [int(i) for i in f]
#for i in range(len(l) - 1):
#    for j in range(i + 1, len(l)):
#        if (l[i] + l[j]) % 120 == 0:
#            count += 1
#            m = max(m, l[i] + l[j])
#print(count, m)



#count = m = 0
#f = open('17-25.txt')
#l = [int(i) for i in f]
#for i in range(len(l)-1):
#    if (l[i] - l[i+1]) % 36 == 0 and (l[i] % 13 == 0 or l[i+1] % 13 == 0):
#        count += 1
#        m = max(m,l[i]-l[i+1])
#print(count,m)


#M = [int(x) for x in open('17.txt')]
#D = [x for x in M if str(x)[-1] == '5']
#R = []
#for i in range(len(M)-1):
#    x, y = M[i], M[i+1]
#    if str(min(x, y))[-1] == '5':
#        if (x ** 2 + y ** 2) < min(D) ** 2:
#            R.append(x ** 2 + y ** 2)
#print(len(R), max(R))


#m = [int(x) for x in open('17-40.txt')]
#d = [x for x in m if str(x)[-1] == '3']
#r = []
#for i in range(len(m)-1):
#    x,y = m[i],m[i+1]
#    if str(min(x,y))[-1] == '3':
#        if (x**2 + y**2 ) < min(d) ** 2:
#            r.append(x**2 + y**2)
#print(len(r),max(r))



#def good(x,y,m):
#    return (str(x)[-2] == str(y)[-1] or str(x)[-1]==str(y)[-2]) and (x%13==0) != (y%13==0) and x**2+y**2 < m**2
#a = [int(s) for s in open('17-42.txt')]
#m = min([x for x in a if str(x)[-1]==str(x)[-2]])
#b = [a[i]**2+a[i+1]**2 for i in range(len(a)-1) if good(a[i],a[i+1],m)]
#print(len(b),max(b))


def god(x,y,m):
    return (str(x)[-1] == str(y)[-1]) and (x%3==0) != (y%3==0) and x**2+y**2 < m**2
a = [int(s) for s in open('17-44.txt')]
m = min([x for x in a if abs(x)%10==3])
b = [a[i]**2+a[i+1]**2 for i in range(len(a)-1) if god(a[i],a[i+1],m)]
print(len(b),max(b))


def f(x,y,m):
    return (str(x)[-1]==str(y)[-1]) and (x%7==0) != (y%7==0) and x**2 + y **2 < m**2

a  = [int(s) for s in open('17-45.txt')]
m = min([x for x in a if abs(x)%10==7])
b = [a[i]**2+a[i+1]**2 for i in range(len(a)-1) if f(a[i],a[i+1],m)]
print(len(b),max(b))

"""
M = [int(x) for x in open('1_17.txt')]
A = [x for x in M if str(x)[-2:] == '17']
cnt = 0
for i in range(len(M)-2):
    x, y, z = M[i:i+3]
    D = [a for a in (x, y, z) if len(str(abs(a))) == 3]
    if len(D) == 1:
        if (x + y + z) < max(A):
            cnt += 1
print(cnt)
"""

sp = [int(x) for x in open('17-53.txt')]
m24 = max(x for x in sp if abs(x) % 100 == 24)
answer = []
for i in range(len(sp) - 2):
    a, b, c = sp[i:i + 3]
    dop = (100 <= a <= 999) + (100 <= b <= 999) + (100 <= c <= 999)
    if dop == 1 and (a + b + c) > m24:
        answer.append(a + b + c)
print(len(answer), min(answer))


a = [int(s) for s in open('17-54.txt')]
m = max([x for x in a if abs(x)%100==29])
b = [sum(a[i:i+3]) for i in range(len(a)-2) if sum([(10000 <= abs(x) < 100000) for x in a[i:i+3]]) == 2 and sum(a[i:i+3]) <= m]
print(len(b),max(b))

a = [int(s) for s in open('17-56.txt')]
me19 = max([x for x in a if x%100 == 19])
b = [a[i:i+3] for i in range(len(a)-2)]
c = [sum(x) for x in b if sum([1000 <= n < 10000 for n in x]) == 2 and sum([n%3 == 0 for n in x]) > 0 and sum(x) > me19]
print(len(c),max(c))

a = [int(s) for s in open('17-58.txt')]
a123 = max([x for x in a if x % 1000 == 123])
count = 0
s3 = []
for i in range (len(a) - 2):
    if ((a[i] + a[i+1] + a[i+2]) > a123):
        if ((a[i] % 3 == 0) + (a[i + 1] % 3 == 0) + (a[i + 2] % 3 == 0)) == 1:
            if (((len(str(a[i])) == 5) + (len(str(a[i + 1])) == 5) + (len(str(a[i + 2])) == 5))) > 1:
                s3.append(a[i] + a[i+1] + a[i+2])
print(len(s3),max(s3))


a = [int(s) for s in open('17-60.txt')]
b238 = max([x for x in a if x%1000 == 238])
v = []
for i in range(len(a)-2):
    troika = [a[i], a[i + 1], a[i + 2]]
    a3 = [x for x in troika if x % 3 == 0]
    a5 = [x for x in troika if x % 5 == 0]
    raz = [x for x in troika if len(str(x)) == 5]
    if sum(troika) > b238:
        if len(a3) > len(a5):
            if 0 < len(raz) < 3:
                v.append(sum(troika))
print(len(v),max(v))

a = [int(s) for s in open('17-61.txt')]
b832 = max([x for x in a if x%1000 == 832])
d = []
for i in range(len(a)-2):
    troia = [a[i],a[i + 1],a[i + 2]]
    a3 = [x for x in troia if x%3 == 0]
    a5 = [x for x in troia if x%5 == 0]
    raz = [x for x in troia if len(str(x))== 4]
    if sum(troia) > b832:
        if len(a5) > len(a3):
            if 0 < len(raz) < 3:
                d.append(sum(troia))
print(len(d),max(d))


count = maxi = 0 
a = [int(s) for s in open('17-64.txt')]
b = min([x for x in a if x%19 == 0])
for i in range(len(a)-1):
    if (a[i]% b == 0) or (a[i+1]% b == 0):
        count += 1
        maxi = max(maxi,a[i]+a[i + 1])
print(count,maxi)


a = [int(x) for x in open('17-66.txt')]
count_delit_32 = 0
for i in range(len(a)):
    if a[i]%32==0:
        count_delit_32 += 1
answer = []
for j in range(len(a)-1):
    if (a[j] < 0 or a[j+1] <0) and ((a[j] + a[j+1]) < count_delit_32):
        answer.append(a[j] + a[j+1])
print(len(answer),max(answer))


a = [int(s) for s in open('17-67.txt')]
mini = min(a)
c = []
for i in range(1,len(a)):
    if a[i] % 16 == mini or a[i - 1] % 16 == mini:
        c.append(a[i]+a[i - 1])
print(len(c),max(c))

a = [int(s) for s in open('17-68.txt')]
mini = min(a)
maxi = max(a)
b = []
for i in range(1,len(a)):
    if ((a[i]%3 == mini%3) or (a[i - 1]%3 == mini%3)) and ((a[i]%7==maxi%7) or (a[i-1]%7==maxi%7)):
        b.append(a[i] + a[i - 1])
print(len(b),max(b))


a = [int(s) for s in open('17-72.txt')]
amax7 = max(a) % 7
amin5 = min(a) % 5 
s3 = []
for i in range (len(a) - 2):
    troika = [a[i] , a[i+1] , a[i+2]]
    alen4 = [x for x in troika if len(str(x)) == 4]
    a7 = [x for x in troika if x % 7 == amax7]
    a5 = [x for x in troika if x % 5 == amin5]
    if len(a5) <= 1 and len(a7) >= 2 and len(alen4) > 0:
        s3.append(sum(troika))
print(len(s3),max(s3))


a = [int(s) for s in open('17-74.txt')]
maxi = max([x for x in a if x%10 == 7])
s3 = []
for i in range(len(a)-2):
    troika = [a[i] , a[i+1] , a[i+2]]

    abdsum = abs(sum(troika))
    alen = [x for x in troika if (abs(x)%10 == 7 and len(str(abs(x)))==3)]
    arax = [str(abs(x))[0] for x in troika]
    if arax[0] == arax[1] == arax[2]:
        if abdsum < maxi and len(alen) > 0:
            s3.append(abs(sum(troika)))
print(len(s3),max(s3))





