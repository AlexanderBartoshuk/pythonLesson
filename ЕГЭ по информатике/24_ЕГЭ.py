"""
f = open('24_demo.txt').readline()
k = 1 
m = 0 
for i in range(1,len(f)):
    if f[i] != f[i-1]:
        k += 1

    else:
        m = max(m,k)
        k = 1
m = max(m,k)
print(m)

f = open('241.txt').readline()
k = 1
m = 0 
for i in range(1,len(f)):
    if f[i] == f[i-1] == 'X':
        k += 1
    else:
        m = max(m,k)
        k = 1
m = max(m,k)
print(m)



f = open('243.txt').readline()
k = 1
m = 0 
for i in range(1,len(f)):
    if f[i] == f[i-1] == "Y":
        k += 1
    else:
        m = max(m,k)
        k = 1
m = max(m,k)
print(m)        



f = open('245.txt').readline()
k = 0
m = 0
for  i in range(1,len(f)):
    if f[i-1:i+1] in 'XYZX' and k:
        k += 1
    else:
        m = max(m,k)
        k = 1
m = max(m,k)
print(m)


f = open('246.txt').readline()
k-= 1
m = 0 
for i in range(1,len(f)):
    if f[i] != f[i-1]:
        k += 1
    else:
        m = max(m,k)
        k = 1 
m = max(m,k)
print(m)


f = open('248.txt').readline()
k = 0
m = 0
for i in range(1,len(f)):
    if f[i] == f[i-1] == "B":
        k += 1
    else:
        m = max(m,k)
        k = 1 
m = max(m,k)
print(m)


f = open('2416.txt')
k = 0
for string in f:
    if(string.count('A') < string.count('E')):
        k +=1 
print(k)

f = open('2418.txt').readline()
l = ''
for  i in range(len(f)-1):
    if f[i] == "A":
        l += f[i+1]
print(max(set(l), key=l.count))


f = open('2419.txt').readline()
l = ''
for i in range(len(f)-1):
    if f[i] == "E":
        l += f[i+1]
print(max(set(l), key=l.count))

f = open('2420.txt').readline()
l = ''
for i in range(len(f)-1):
    if f[i] == f[i-2]:
        l += f[i-1]
print(max(set(l), key=l.count))



f = open('2420.txt').readline()
l = ''
for i in range(len(f)-1):
    if f[i-1] == f[i-2]:
        l += f[i]
print(max(set(l), key=l.count))

f = open('2422.txt')
a = [str(i) for i in f]
mini = 1000000
for i in range(len(a)):
    k = a[i].count('G')
    if k < mini:
        mini = k
        t = i
print(max(set(a[t]),key = a[t].count))


f = open('2426.txt').readlines()
mx = 0 
for a in f:
    if a.count('G') < 25:
        m = 0
        for i in range(len(a)):
            if a.count(a[i]) > 1:
                r = a.rfind(a[i]) - a.find(a[i])
                m = max(m,r)
        mx = max(mx,m)
print(mx)



f = open('2427.txt').readline()
f = f.replace('KL','K L').replace('LK','L K')  
print(max([len(x) for x in f.split()]))

s = open('2429.txt').readline()
while 'PP' in s:
    s = s.replace('PP', 'P P')
print(max([len(x) for x in s.split()]))


f = open('2430.txt')
ans = 0
s = f.readline().split('A')
for i in range (len(s)-1):
    ans = max(len(s[i])+len(s[i+1])+1,ans)
print(ans)


f = open('2432.txt')
s = f.readline().split('A')
s = list(filter(lambda x: x.count('E') >= 3,s))
print(len(max(s,key=len)))


f = open('2433.txt')
s = f.readline().split('E')
s = list(filter(lambda x: x.count('A') >= 3, s))
print(len(max(s, key=len)))

f = open('2434.txt').readline()
f = f.replace('CB', '*')
f = f.replace('AB', '*')
f = f.replace('A', ' ')
f = f.replace('B', ' ')
f = f.replace('C', ' ')
a = f.split()
print(len(max(a,key=len)))


f = open('2435.txt').readline().split('E')
c = 0
for i in f:
    if len(i) >= 10 and i.count('F') == 0:
        c += 1
print(c)

f = open('2436.txt').readline().split('A')
c = 0 
for i in f:
    if len(i) >= 8 and i.count('B') == 0:
        c += 1
print(c)


a = open('2437.txt')
y = a.readline()
y = y.replace('CA','0')
y = y.replace('CO','0')
y = y.replace('FA','0')
y = y.replace('FO','0')
y = y.replace('DA','0')
y = y.replace('DO','0')
y = y.replace('A','1')
y = y.replace('C','1')
y = y.replace('D','1')
y = y.replace('F','1')
y = y.replace('O','1')
print(len((max(y.split('1'),key=len))))

s = open('24.txt').readline()
s = s.replace('C', 'D').replace('F', 'D')
s = s.replace('O', 'A')
s = s.replace('DDA', '*')
s = s.replace('D', ' ').replace('A', ' ')
print(max([len(x) for x in s.split()]))


s = open('24.txt').readline().split('F')[1:-1]
mx = 0
count = 1 
for i in range(len(s)):
    if s[i].count('A') <= 2:
        count += len(s[i]) + 1 
        mx = max(mx, count)
    else:
        count = 1
print(mx)



f = open('2441.txt').readline().split('D')[1:-1]
mx = 0 
k =1 
for  i in range(len(f)):
    if f[i].count('O') <= 2:
        k += len(f[i])+1
        mx = max(mx,k)
    else:
        k = 1 
print(mx)


f = open('2442.txt').readlines()
li = []
for j in f:
    st = ''
    for x, y in zip(j, j[1:]):
        if x == 'A':
            st += y
    maxi = max(st.count(i) for i in set(st))
    for s in set(st):
        if st.count(s) == maxi:
            li += [s]
print(max(li.count(l) for l in set(li)))



s = open('2444.txt').readline()
count = mx = 1
for i in range(len(s)-1):
    if s[i] not in'QRS' or s[i+1] not in'QRS':
        count+= 1
        mx= max(count, mx)
    else:
        count = 1
print(mx)



f = open('2445.txt')
mx=-1
mxall=-1
for s in f:
    k=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            k+=1
            if k>mx:
                mx=k
                mxall=s.count(s[i])
            if k==mx:
                mxall = max(s.count(s[i]), mxall)
        else:
            k=1
print(mxall)






f = open('2446.txt')
mx = mxall = -1
for s in f:
    k =1 
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            k +=1

            if k > mx:
                mx = k 
                mxall = s.count(s[i])
            if k == mx:
                mxall = min(s.count(s[i]),mxall)
        else:
            k = 1
print(mxall)


f = open('2447.txt')
count = m =1
s = f.readline()
for i in range(1, len(s)):
    if s[i-1] not in 'ABC' or s[i] not in 'ABC':
        count +=1
        m = max(count, m)
    else:
        count =1
print(m)


f = open('2448.txt').readline()
k = mx = 1 
for i in range(1,len(f)):
    if f[i-1] > f[i]:
        k +=1 
        mx = max(k,mx)
    else:
        k =1 
print(mx)


f = open('2451.txt').readline()
k = 1 
mx = 0
for i in range(1,len(f)):
    if int(f[i - 2]) + int(f[i - 1]) > int(f[i]):
        k += 1
        mx = max(k,mx)
    else:
        k =1 
print(mx)



s = open('2453.txt').readline()
ds=0
mds=0
for i in range(len(s)-3):
    s1 = s[i+1]+s[i+2]+s[i+3]
    ds += 1
    mds = max(mds,ds)
    if s1.count('X')==1 and s1.count('Y')==1 and s1.count('Z')==1:
        ds=0
print(mds - 3)

s = open('2454.txt').readline()[:-1]
a = [i for  i in range(len(s)) if s[i] == "Y"]
mx = 0
for i in range(150,len(a)):
    mx = max(a[i]-a[i-150],mx)
print(mx)


s = open('2457.txt').readline().split('T')
mini = 10**9
for i in range(len(s)-208):
    r = 'T' + 'T'.join(s[i:i+209]) + 'T'
    mini = min(mini, len(r))
print(mini)

s = open('24.txt').readline()
s = s.split('W')[1:-1]
mini = 10**10
for i in range(len(s)-129):
    r = 'W' + 'W'.join(s[i:i+128]) + 'W'
    mini = min(mini, len(r))
print(mini)

s = open('24.txt').readline().split('T')
mini = 10**9
for i in range(len(s)-98):
    r = 'T' + 'T'.join(s[i:i+99]) + 'T'
    mini = min(mini, len(r))
print(mini)




s = open('2460.txt').readline().split('V')
mini = 10**10
for i in range(1,len(s)-119):
    mini = min(len('V'.join(s[i:i+119]))+2,mini)
print(mini)

s = open('2461.txt').readline().split('U')
mini = 10**10
for i in range(1,len(s)-109):
    mini = min(len('U'.join(s[i:i+109]))+2,mini)
print(mini)


f = open('2462.txt')
s = f.read()
count, maxi = 1,0
for i in range(1,len(s)):
    if s[i-1] not in 'ABC' or s[i] not in 'ABC':
        count += 1
    else:
        maxi = max(maxi,count)
        count = 1
print(maxi)


s = open('2465.txt').readline()
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[26:]:
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))

s = open('2466.txt').readline().split('T')
mini = 0
for i in range(1,len(s)-99):
    mini = max(len('T'.join(s[i:i+99]))+2,mini)
print(mini)


s = open('24.txt').readline()
p = [-1]+[i for i in range(len(s)) if s[i] in 'AB'] + [len(s)]
print(max([p[i+3]-p[i]-1 for i in range(len(p)-3) if s[p[i+1]] != s[p[i+2]]]))
"""


s = open('2470.txt').readline()
s = s.replace('C','C ').replace('D','D ').split()
maxi = 0 
for i in range(len(s)-4):
    r  = s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4][:-1]
    if r.count('C') == 2 and r.count('D') ==2: 
        maxi = max(maxi,len(r))
print(maxi)


s = open('2473.txt').readline()
maxi = 0 
alf = ''.join(sorted('QWERTYUIOPASDFGHJKLZXCVBNM'))[:13]
for i in alf:
    maxi = max(maxi,len(max(s.split(i)[1:-1],key=len)+i*2))
print(maxi)


f = open('2474.txt').readline()
f = f.replace('R','Q').replace('W','Q').replace('2','1').replace('4','1').replace('QQQ','QQ').replace('111','11').replace('QQ','Q Q').replace('11','1 1').split(' ')
maxi = 0 
for i in range(0,len(f)):
    maxi = max(len(f[i]),maxi)
print(maxi)

f = open('2478.txt').readline()
f = f.replace('CD','C D').split()
maxi = 0
for i in range(len(f)):
    r = ''.join(f[i:i+141])
    maxi = max(maxi,len(r))
print(maxi)


import re 
text = open('2482.txt').read()
matches = re.findall(r'(?:[1-9][0-9]*|0)(?:[+-](?:[1-9][0-9]*|0))*',text)
print(max(map(len,matches)))

string = open('2484.txt').readline()
pattern = r'[123456789ABCD][0123456789ABCD]*[02468AС]'
iterator = re.finditer(pattern, string)
otv = max([i.group() for i in iterator], key=len)
print(len(otv))



















