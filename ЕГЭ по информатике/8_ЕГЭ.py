from itertools import *

a = '1234'
ap = []
for i in product(a,repeat=5):
    if i.count('1') == 2:
        ap.append(a)
print(len(ap))

b = '12345'
ao = []
for i in product(b,repeat=5):
    if i.count('1') == 3:
        ao.append(b)
print(len(ao))


#Сколько существует различных трёхзначных чисел, записанных в четверичной 
# системе счисления, в записи которых сумма первой и последней цифры строго больше цифры стоящей по середине?

alpha = '0123'
ap = []
for i in product(alpha,repeat=3):
    if (i[0] != '0') and (int(i[0]) + int(i[2]) > int(i[1])):
        ap.append(i)
print(len(ap))

#Составляют 5-⁠буквенные слова из букв слова ПЯТНИЦА.
#Найти количество слов, которые не начинаются с Н и в которых есть только одна буква Я. Буквы в слове могут повторяться.

count= 0
for i in product('ПЯТНИЦА',repeat=5):
    if i.count('Я') == 1 and i[0] != 'Н':
        count += 1
print(count)

count = 0
for i in product('МАНГУСТ',repeat=6):
    if i[0] != 'А' and i.count("У") >= 1 and i.count('М') == 2:
        count += 1
print(count)

count = 0 
n = 0
a  = 'МУЖЧИНА'
for p in permutations(a, 6):
    if p[0] != "Ч" and p.count('Ж') >= 1:
        n += 1
        if n % 2 != 0:
            count += 1 
print(count )


a = 'ЕГЭ'
b = 0 
for i in product(a,repeat=5):
    if i[0] != "Г":
        b += 1
print(b)

count = 0
for i in product('ABCX',repeat=5):
    if i.count("X") == 1:
        count +=1 
print(count)

count = 0
for i in product('ЖИРАФ',repeat=4):
    if i.count('Р') == 1:
        count += 1
print(count)

count = 0
count1 =0 
for i in product('ABCD', repeat=2 ):
    count +=1 
for i in product('XYZ', repeat=2 ):
    count1 +=1
print(count1*count)


count = 0 
for i in product('ЗИМА',repeat=5):
    if i.count('И') == 1 and i.count('А') == 1:
        count += 1 
print(count )

# Полина составляет 4-⁠буквенные коды из букв П, О, Л, И, Н, А. 
# Каждую букву можно использовать любое количество раз или совсем не использовать, 
# при этом нельзя ставить подряд две гласные или две согласные. Сколько различных кодов может составить Полина?
alphabet = 'ПОЛЯНА'
count = 0
ag = 'ОЯА'
ac = 'ПЛН'
for b1 in alphabet:
    for b2 in alphabet:
        for b3 in alphabet:
            for b4 in alphabet:
                s=b1+b2+b3+b4
                if b1 in ag and b2 in ac and b3 in ag and b4 in ac:
                    count += 1
                if b1 in ac and b2 in ag and b3 in ac and b4 in ag:
                    count += 1
print(count)


#from itertools import product
#count = 0
#for num in product('01234567', repeat=5):
#    if num.count('6') == 1 and num[0] !='0':
#        x = ''.join(num)
#        x = x.replace('1','8').replace('3','8').replace('5','8').replace('7','8')
#        if x.count('86') == 0 and x.count('68') == 0:
#            count+=1
#print(count)


#from itertools import product
#count = 0
#m=[]
#for p in product(sorted("СКАНЕР"), repeat=10):
#    count+=1
#    if count%3==0 and p[0]!= 'А' and p[0]!='Е' and p.count("Р") == 1:
#        m.append(count)
#print(len(m))


words = list(product('AOY', repeat=5))
print(*words[209])

a = list(product('AОУ',repeat=5))
print(*a[100])

letters = ['А', 'К', 'Р', 'У']
words = sorted([''.join(p) for p in product(letters, repeat=5)])
word = 'РУКАА'
index = words.index(word) +1 
print(index)

wor = list(product('ЛНОС', repeat=5))
print(*wor[1019])