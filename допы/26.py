f = open('263.txt')
sn = f.readline().split()
s = int(sn[0])
n = int(sn[1])

a = []

for i in range(n):
    x = int(f.readline())
    a.append(x)

a.sort()

b = []

for i in range(n):
    if sum(b) + a[i] <= s:
        b.append(a[i])
    else:
        break

b = b[:-1]

for i in range(len(a)-1,-1,-1):
    if sum(b) + a[i] <= s:
        b.append(a[i])
        break

print(len(b),b[-1])



f = open('262.txt')
n = int(f.readline())

a = [0]*100001
for i in range(0,100001):
    a[i] = []

for i in range(0,n):
    s = f.readline()
    b=s.split()
    a[int(b[0])].append(int(b[1]))

for i in range(0,len(a)):
    a[i].sort()

flag = 0
for i in range(len(a)-1,-1,-1):
    for j in range(0,len(a[i])-1):
        if a[i][j+1] -a[i][j] == 3:
            print(i,a[i][j]+1)
            flag = 1
            break
    if flag == 1:
        break
