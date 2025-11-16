import statistics
"""
В кондитерской есть N круглых форм для коржей. Специализация кондитерской – многоярусные торты,
в которых диаметр каждого верхнего коржа меньше диаметра предыдущего. Один корж можно поместить на другой,
если его диаметр хотя бы на 4 единицы меньше диаметра другого коржа. Определите наибольшее количество коржей,
которое можно использовать для создания многоярусного торта, и максимально возможный диаметр самого маленького коржа
"""

with open('2601.txt') as file:
    N = int(file.readline())
    data = list(map(int,file))

data = sorted(data,reverse=True)
res = [data[0]]
for i in data[1:]:
    if res[-1] - i >= 9:
        res.append(i)

print(len(res),res[-1])


"""
Отбор кандидатов в матросы происходит по сумме баллов трех экзаменов. 
На заранее известное количество мест отбираются кандидаты, набравшие большую сумму баллов по результатам трех экзаменов. Все кандидаты, 
набравшие определенную сумму баллов или больше, 
зачисляются на имеющиеся места. Такой балл называется проходным. 
Если после заполнения имеющихся мест кандидатами с проходным баллом остаются незаполненные места, но кандидатов, 
набравших следующую сумму баллов, больше, чем вакантных мест, набранная этими кандидатами сумма баллов называется полупроходным баллом. 
Из числа кандидатов, набравших 
полупроходной балл, на имеющиеся места принимаются кандидаты, имеющие более высокий балл за собеседование, а при равенстве баллов за собеседование – 
приоритет имеют кандидаты с наименьшими ID.

Для данного множества кандидатов следует определить ID последнего кандидата с набранным проходным баллом, а также каково количество кандидатов, набравших полупроходной балл
"""

data = []
with open('2603.txt') as file:
    N, S = map(int, file.readline().split())

    for line in file:
        parts = line.strip().split()
        candidate = {
            'id': int(parts[0]),
            'exam_1':int(parts[1]),
            'exam_2': int(parts[2]),
            'exam_3': int(parts[3]),
            'interview': int(parts[4])}

        candidate['result'] = candidate['exam_1'] + candidate['exam_2'] + candidate['exam_3']
        data.append(candidate)

data = sorted(data,key=lambda x: (-x['result'],
                                  -x['interview'],
                                  x['id']))
half_pass_mark = data[S]['result']

answer_1 = {}
answer_2 = 0

for candidate in data:
    if candidate['result'] > half_pass_mark:
        answer_1 = candidate
    if candidate['result'] == half_pass_mark:
        answer_2 += 1
    if candidate['result'] < half_pass_mark:
        break
print(f'ID последнего кандидата:{answer_1['id']}')
print(f'Набрали полупроходной балл:{answer_2}')


data = []
with open('2604.txt') as file:
    N = int(file.readline())

    for line in file:
        parts = line.strip().split()
        student = {
            'id': int(parts[0]),
            'm_1': int(parts[1]),
            'm_2': int(parts[2]),
            'm_3': int(parts[3]),
            'm_4': int(parts[4])}

        marks = (student['m_1'],student['m_2'],
                 student['m_3'],student['m_4'])
        student['twos'] = marks.count(2)
        student['mean'] = statistics.mean(marks)
        data.append(student)

data = sorted(data,key=lambda x: (-x['mean'],
                                  x['twos'],
                                  x['id']))

quart = N // 4
answer_1 = data[quart-1]['id']
print(answer_1)

for student in data:
    if student['twos'] > 2:
        print(student['id'])
        break


"""
При онлайн-покупке билета на концерт известно, какие места в зале уже заняты. 
Необходимо купить два билета на такие соседние места в одном ряду, чтобы 
перед ними все кресла с такими же номерами были свободны, 
а ряд находился как можно дальше от сцены. Если в этом ряду таких пар мест несколько,
найдите пару с наименьшими номерами. В ответе запишите два целых числа: искомый номер ряда и 
наименьший номер места в найденной паре. Нумерация рядов и мест ведётся с 1. 
Гарантируется, что хотя бы одна такая пара в зале есть.
"""

with open('2602.txt') as file:
    N, M, K = map(int,file.readline().split())
    data = [list(map(int, line.split())) for line in file]

max_row = 0
min_seat = 0

min_row = [M + 1] * (K + 2)

for row,seat in data:
    if row < min_row[seat]:
        min_row[seat] = row



for seat in range(1,K):

    accept_row = min(min_row[seat], min_row[seat+1]) - 1

    if (accept_row > max_row or
            (accept_row == max_row and seat < min_seat)):
        max_row = accept_row
        min_seat = seat

print(f'Наибольший размер ряда: {max_row}')
print(f'Наименьший размер места: {min_seat}')


data = []
with open('2609.txt') as file:
    N = int(file.readline())

    for line in file:
        parts = line.strip().split()
        event = {
            'start':int(parts[0]),
            'end': int(parts[1])
        }
        data.append(event)

events = sorted(data, key=lambda event: (event['end'],
                                         -event['start']))
approved_events = [events[0]]

for event in events[1:]:
    if event['start'] >= approved_events[-1]['end']:
        approved_events.append(event)

longest_break = 0
for event in events:
    if event['start'] >= approved_events[-2]['end']:
        longest_break = max(longest_break,event['start']-approved_events[-2]['end'])
print(len(approved_events),longest_break)



f = open('26_1.txt')
s,n = list(map(int,f.readline().split()))
files = sorted([int(line) for line in f])
filessum = [files[0]]
for x in files[1:]: filessum.append(filessum[-1]+x)
ndx = max([i for i in range(len(filessum)) if filessum[i] <= s])
freespace = s-filessum[ndx-1]
maxfile = max([x for x in files if x <= freespace])
print(ndx+1,maxfile)



a = [int(s) for s in open('26_16.txt')][1:]
b50 = sorted([x for x in a if x > 50])
skidka = sum(b50[:len(b50)//2])//4
print(sum(a) - skidka,b50[len(b50)//2-1])


a = [int(s) for s in open('26_17.txt')][1:]
b = sorted([x for x in a if x > 100])
skidkaa = sum(b[:len(b)//2])*0.3
print(sum(a)-skidkaa, b[len(b)//2-1])


f = open('26-22.txt')
k = f.readlines()
n = list(map(int,k))
m= 0
s = 0
c = 0
ns = set(n)
for i in range(1,len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]%2== 0 and n[j]%2==0:
            s = (n[j]+n[i]) // 2
            if s in ns:
                c +=1
                if s > m:
                    m = s
print(c,m)


f = open('26-25.txt')
s,n = list(map(int,f.readline().split()))
a = sorted([int(x) for x in f])
k = 0
for x in a:
    if x > s: break
    s -=x
    last = x
    k += 1
s += last
m = max([x for x in a if x <= s])
print(k,m)



a = sorted([list(map(int,s.split())) for s in open('26.txt')][1:])
lefts = [a[i] for i in range(len(a) - 1) if a[i][0] == a[i+1][0] and a[i+1][1] - a[i][1] == 3]
print(lefts[-1][0],lefts[-1][1] + 1)


"""
f = open('26.txt')
n, m = map(int, f.readline().split())
f = [i.split() for i in f]
f = sorted([[int(i[0]), i[1]] for i in f])
a = []
b = []
for i in range(len(f)):
    if sum(a+b) + f[i][0] <= m:
        if f[i][1] == 'A':
            a.append(f[i][0])
            f[i] = []
        elif f[i][1] == 'B':
            b.append(f[i][0])
            f[i] = []
f = [i for i in f if i != []]
for i in f:
    if i[1] == 'A':
        if sum(a+b) - b[-1] + i[0] <= m:
            a.append(i[0])
            b.pop(-1)
print(len(a), m - sum(a + b))
"""


f = open('107_26.txt')
n = int(f.readline())
nums = sorted([int(i) for i in x.split()] for x in f)
rmax = 0
for i in range(1,n):
    r,m = nums[i-1]
    if r == nums[i][0] and nums[i][1] - m == 14:
        if r > rmax: rmax, mmin = r,m
print(rmax,mmin+1)


f = open('26 (1).txt')
n = f.readline()
sytki = [0]*86400
start = 8*60*60
end = 14*60*60
zapros = 0
for s in f:
    t1,t2 = map(int,s.split())
    for i in range(t1,t2):
        sytki[i] += 1
zapros = max(sytki[start:end+1])
time_zapros = sytki.count(zapros)
print(zapros, time_zapros)




















