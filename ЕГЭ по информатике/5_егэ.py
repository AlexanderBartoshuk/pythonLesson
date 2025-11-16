##for i in range(1,100):
##    s = bin(i)[2:] # перевод в 2-ую систему
##    s += s[-1] # дублируется последняя цифра
##    s += str(s.count('1') % 2) # складываем все цифры и остаток от деленимя на 2
##    r = int(s,2) # переводим в десятичную систему
##    if r > 105:
##        print(r)
##        break
##
##
##for i in range(1,100):
##    s = bin(i)[2:]
##    s += s[-1]
##    s += str(s.count('1') % 2)
##    r = int(s,2)
##    if r > 83:
##        print(r)
##        break
##
#
#
#
#for i in range(100,1,-1):
#    s = bin(i)[2:]
#    if i % 2== 0:
#        s += '10'
#    else:
#        s += '01'
#    r = int(s,2)
#    if r <= 102:
#        print(r)
#        break
#
#
#for i in range(2,10000):
#    s = bin(i)[2:]
#    s = str(s)
#    s = s[:-1]
#    if i % 2 != 0:
#        s += '10'
#    else:
#        s += '01'
#    r = int(s,2)
#    if r == 2018:
#        print(i)
#
#
#for i in range(0,255):
#    s = bin(i)[8:]
#    if len(s) < 8:
#        s = '0' * (8- len(s)) + s 
#    s = s.replace('1', '*')
#    s = s.replace('0','1')
#    s = s.replace('*','0')
#    r = int(s,2)
#    if r-i == 133:
#        print(i)
#
#
#
#for i in range(0,255):
#    s = bin(i)[8:]
#    if len(s) < 8:
#        s = '0' * (8 - len(s)) + s
#    s = s.replace("1", "*")
#    s = s.replace("0","1")
#    s = s.replace('*',"0")
#    r = int(s,2)
#    if r-i == 111:
#        print(i)



a = [] 
for x in range(100, 3001):
    i = int(bin(x)[3:], 2)
    if x - i not in a:
        a.append(x-i)
print(len(a))




d = []
for i in range(10,1001):
    s = int(bin(i)[3:],2)
    if i-s not in d:
        d.append(i-s)
    print(len(d))


for n in range(1, 100):
    s = bin(n)[2:]
    s = s + str(s.count('1') % 2)
    s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r > 123:
        print(r)
        break

for n in range(100,1,-1):
    s = bin(n)[2:]
    s = str(s)
    s= s[::-1]
    s = s[s.find('1'):]
    r = int(s,2)
    if r == 13:
        print(n)
        break


for u in range(80,1,-1):
    s = bin(u)[2:]
    s = str(s)
    s = s[::-1]
    s = s[s.find("1"):]
    r = int(s,2)
    if r > 80:
        print(r)
        break



for i in range(1,1000):
    n = i
    s = ''
    while n > 0:
        s += str(n%3)
        n //= 3
    s = str(i % 3) + s 
    r = 0 
    for j in range(len(s)):
        r += int(s[j]) * 3 ** j
        if r > 999:
            print(r)
            break


def f(n):
    s = ''
    while n > 0:
        s = str(n%3) + s
        n //= 3
    return s
c = []
for n in range(1000):
    s = f(n)
    summa = s.count('1') + s.count('2')*2
    if summa % 3 == 0:
        s = '112'+ s[2:]
    else:
        s = s + f(summa)
    r = int(s,3)
    if r <= 679 and r%2 == 0:
        c.append(r)
print(max(c))