#for x in '0123456789A':
#    t = int("982" + x + "8", 11) + int("194" + x + "7",11)
#    if t % 58 == 0:
#        print(t // 58)
#        break
#
#
#num = 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82
#translantion = hex(num)[2:] # function hex translate to 16 bit sistem
#print(len(set(translantion)))
#
#number = 4**2013 + 2**2012 - 16
#n = bin(number)[2:]
#print(n.count('1'))
#
#
#for x in '012345678':
#    t = int('88' + x + '4' + x, 9) + int('7' + x + '344', 9)
#    if t % 67 == 0:
#        print(t // 67)
#        exit
#
#a = 729**8 - 3**18 +85
#c = bin(a)[2:]
#print(c.count('0'))
#
#
#for x in range(2020+1):
#    t = 3**100 -x 
#    count = 0 
#    while t!= 0:
#        if t%3 == 0:
#            count += 1 
#        t = t // 3
#    if count == 2:
#        print(x)
#        break
#
#count = 216**6 + 216**4 +36**6 -6**14-24
#m = []
#while count > 0:
#    m.append(count % 6)
#    count //= 6 # count = count // 6
#m.reverse()
#print(len(set(m)))
#
#
#b = 49**7 * 7**20 - 7**8 -28
#s = ''
#while b != 0:
#    s += str(b%7)
#    b = b//7
#s = s[::-1]
#print(s.count('6'))
#
#
#for x in '01234567':
#    for y in '01234567':
#        f = int(y + '04' + x + '5', 11) + int('253' + x + y, 8)
#        if f % 117==0:
#            print(f//117)
#            break
#nu = 49**6 + 7**19 -21
#f = ''
#while  nu != 0:
#    f += str(nu%7)
#    nu = nu //7
#f = f[::-1]
#print(f.count('0'))
#
#
#
#число = 8**7 + 4**5 +2**10 -32
#print(bin(число).count('1'))
#
#
#
#for x in '0123456789ABC':
#    f = int('3D' + '4' + x, 16) + int('4' + x +"C4", 14)
#    if f % 154 == 0:
#        print(f//154)
#        break
#
#
#c = 9**12 + 3**8 -3
#s = ''
#while c != 0:
#    s += str(c%3)
#    c = c//3 
#s = s[::-1]
#print(s.count('2'))
#
#for x in '123456789ABCDEF':
#    r = int("1" +x + 'BAD', 16) + int('2C' + x + 'FE', 16)
#    if r % 15 == 0:
#        print(r//15)
#        break
#
#алфавит =sorted("1234567890QWERTYUIOPASDFGHJKLZXCVBNM")
#for p in range(9,36+1):
#    for x in алфавит[:p]:
#        for y in алфавит[:p]:
#            for z in алфавит[:p]:
#                for w in алфавит[:p]:
#                    if int(z+x+y+x+'4', p) + int(x+y+'658',p) == int(w+z+x+'73',p):
#                        print(int(x+y+z+w, p))
#
#n = 6*343**5 + 5*49**7-50
#s = ''
#while n != 0:
#     s += str(n%7)
#     n =n // 7
#s  = s[::-1]
#print(s.count('6'))
#
#s = 3 * 289**2024 + 81 * 49**121 - 9 * 16**81 - 6011
#summa = 0
#while s > 0:
#    digit = s % 31 
#    if digit <= 17:
#        summa += digit
#    s //= 31
#print(summa)
#

a = 216**6 + 216**4 + 36**6 - 6**14 - 24
s = ''
while a != 0:
    s += str(a%6)
    a = a // 6 
s = s[::-1]
b = set()
for i in s:
    b.add(i)
print(len(b))

def a(n):
    if n == 1:
        return 1
    if n >= 2:
        return a(n-1) * n
print(a(6))