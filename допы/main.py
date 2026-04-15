for n in range(1000):
    i = bin(n)[2:]
    summa = str(i.count('1') % 2) 
    i = i + summa 
    summa = str(i.count('1') % 2)
    i = i + summa
    
    r = int(i,2)
    if r >= 123:
        print(r)
        break


for n in range(100,1,-1):
    i = bin(n)[2:]
    x = int(str(i)[::-1],2)
    if x == 13: 
        print(n)
        break

for n in range(400):
    i = bin(n)[2:]
    if int(i) % 2 == 0: 
        i = '1' + i + '0'
    if int(i) % 2 != 0:
        i = '11' + i + '11'
    
    r = int(i,2)
    if r >= 52:
        print(n)
        break


for i in range(100):
    n = i 
    s = ''
    while n > 0:
        s += (str(n%3))
        n //= 3
    s = s[::-1]
    s += str(i % 3)
    s = int(s,3)
    if s > 99:
        print(s)
        break


for i in range(2,200):
    n = bin(i)[2:]
    n = str(n)
    n = n + n[-2]
    n = n + n[1]

    r = int(n,2)
    if r > 150:
        print(i)
        break









