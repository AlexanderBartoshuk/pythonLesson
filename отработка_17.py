#f = open('17555.txt')
#cnt = 0
#m = 0
#l = [int(i) for i in f]
#for i in range(len(l) - 1):
#    for j in range(i + 1, len(l)):
#        if (l[i] - l[j]) % 2 == 0 and (l[i] % 31 == 0 or l[j] % 31 == 0):
#            cnt += 1
#            m = max(m, l[i] + l[j])
#print(cnt, m)


f = open('17777.txt')
cnt = 0
m = 0
a = [int(i) for i in f]
for i in range(len(a)-1):
    if (a[i] % 5 == 0 or a[i+1] % 5 == 0) and ((a[i]+a[i+1]) % 7 == 0):
        cnt += 1
        m = max(m,a[i]+a[i+1])
print(cnt,m)


M = [int(x) for x in open('17554.txt')]
D = [x for x in M if str(x)[-1] == '5']
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if str(min(x, y))[-1] == '5':
        if (x ** 2 + y ** 2) < min(D) ** 2:
            R.append(x ** 2 + y ** 2)
print(len(R), max(R))

x = 14
print(x//5)