s = '8' * 68 
while('222' in s) or ('888' in s):
    if('222' in s):
        s = s.replace('222','8',1)
    else:
        s = s.replace('888','2',1)
print(s)

a = '9' * 127
while('333' in a) or ('999' in a):
    if('333' in a):
        a = a.replace('333','9',1)
    else:
        a = a.replace('999','3',1)
print(a)


b = '1' + '8'*80
while('18' in b) or ('288' in b) or ('3888' in b):
    if('18' in b):
        b = b.replace('18','2',1)
    elif ('288' in b):
        b = b.replace('288','3',1)
    else:
        b = b.replace('3888','1',1)
print(b)

s = '>' + '1' * 26 + '2' * 10 + '3' * 14
while ('>1' in s) or ('>2' in s) or ('>3' in s):
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)
print('сумма цифр:', s.count('1') + s.count('2')  * 2)

for a in range(50):
    for b in range(50):
        for c in range(50):
            s='0'+'1'*a+'2'*b+'3'*c
            while '01' in s or '02' in s or '03' in s:
                s=s.replace('01','2302',1)
                s=s.replace('02','10',1)
                s=s.replace('03','201',1)
            if s.count('1')==50 and s.count('2')==12 and s.count('3')==7:
                print(a)
                break
 
minn = 1000
index = 0
for i in range(201, 1000):
    s = '1' * i
    while ('1111' in s):
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    if minn > s.count('1'):
        minn = s.count('1')
        index = i
print(index)

for n in range(4,100):    
    s = '3' + '5' * n 
    while ('25' in s) or ('355' in s) or ('555' in s):
        s = s.replace('25', '3', 1)
        s = s.replace('355', '52', 1)
        s = s.replace('555', '23', 1)
    if 5*s.count("5") +3*s.count("3") + 2*s.count("2") == 27:
        print(n)
        break

for n in range(1000, 3,-1): # -1 определяет максимальное число 
    s = '5' + '2' * n
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    if  s.count('1') + s.count('2') * 2 + s.count('5') * 5  == 64:
        print(n)
        break