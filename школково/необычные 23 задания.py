# Исполнитель ДЮ преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
#
# Удвоить
# Удвоить и прибавить 1
# Утроить и прибавить 1
# Первая команда умножает число на экране на 2  , вторая - умножает его на 2  , а затем прибавляет 1  ,
# а третья - умножает его на 3  , а затем прибавляет 1  .
#
# Программа для исполнителя ДЮ — это последовательность команд.
# Сколько различных результатов можно получить из исходного числа 1
# после выполнения программы, содержащей ровно 7   команд?



a = set()
for i in range(3**7):
    t = i
    n = 1
    for j in range(7):
        if t % 3 == 0:
            n*=2
        if t % 3 == 1:
            n = n*2 +1
        if t % 3 == 2:
            n = n*3 + 1
        t //=3
    a.add(n)
print(len(a))

ans = set()
def f(start,com):
    if com == 0:
        ans.add(start)
        return 0
    f(start+2, com-1)
    f(start*2+1,com-1)
f(6,12)
print(len(ans))

# Исполнитель Щелчок преобразует число на экране.
# У исполнителя есть три команды:
#
# 1. Прибавить 1
# 2. Умножить на 2
# 3. Прибавить 4
#
# Программа для исполнителя — это последовательность команд.
#
# Сколько существует различных результатов выполнения программ,
# содержащих 8 команд и начинающих свою работу из 2.


a = set()
def f(start,count,end_count):
    if count == end_count:
        a.add(start)
    else:
        f(start+1,count+1,end_count)
        f(start*2,count+1,end_count)
        f(start+4,count+1,end_count)
f(2,0,8)
print(len(a))

a = set()

def f(start,co,end):
    if co == end:
        a.add(start)
    else:
        if start >0 :
            f(start * (-2),co+1,end)
            if start - 10 < 0:
                f(start-10,co+1,end)
        if start < 0:
            f(abs(start),co+1,end)
            f(start * (-2),co+1,end)
f(1,0,10)
print(len(a))

# Исполнитель Щелчок преобразует число на экране. У исполнителя есть три команды:
#
# 1. Прибавить 1
#
# 2. Прибавить 3
#
# 3. Умножить на 3
#
# Программа для исполнителя — это последовательность команд.
#
# Сколько существует различных результатов выполнения программ, содержащих 10
# команд и начинающих свою работу из 2  . При этом траектория вычислений исполнителя
# содержит не более трех нечетных чисел.

a = set()

def f(start, cnt_step, cnt_nch, max_step):
    if cnt_step == max_step and cnt_nch <= 3:
        a.add(start)
    if cnt_step > max_step or cnt_nch > 3:
        return
    f(start+1,cnt_step+1,cnt_nch + ((start +1) % 2), max_step)
    f(start+3,cnt_step+1,cnt_nch + ((start+3) % 2) , max_step)
    f(start *3 , cnt_step +1, cnt_nch +((start *3) % 2) , max_step)

f(2,0,0,10)
print(len(a))

from functools import *
@lru_cache(None)

def f(a,k,last=0):
    if k == 20:
        s.add(a)
    if k < 20:
        if last == 0:
            f(a + 1, k + 1, 1)
            f(a - 2, k + 1, 2)
            f(a * 3, k + 1, 3)
        if last == 1:
            f(a - 2, k + 1, 2)
            f(a * 3, k + 1, 3)
        if last == 2:
            f(a + 1, k + 1, 1)
            f(a * 3, k + 1, 3)
        if last == 3:
            f(a + 1, k + 1, 1)
            f(a - 2, k + 1, 2)

s = set()

f(2,0)
print(len(s))


# Исполнитель Пробник преобразует число на экране. У исполнителя есть две команды:
#
# 1. Прибавить 3
#
# 2. Умножить на 4
#
# Программа для исполнителя - это последовательность команд.
# Сколько существует значений, в которые можно прийти не менее чем за 1,
# но не более чем за 8 команд из числа 2?

s = set()

def f(a,k=0):
    if 1<= k <= 8:
        s.add(a)
    elif k > 8:
        return
    f(a+3,k+1)
    f(a*4,k+1)

f(2)

print(len(s))


s = set()

def f(a,c=0.5,k=0):
    if 1 <= k <= 8:
        s.add(a)
    if k > 8:
        return 0

    if c % 2 != 0:
        f(a+7,2,k+1)
        f(a*2,4,k+1)
        if a % 2 == 0:
            f(int(a*1.5), 6, k+1)
    if c % 2 != 1:
        f(a+3,1,k+1)
        f(a+1,3,k+1)
        f(a*4,5,k+1)
f(10)
print(len(s))

s =set()

def f(a,c=0,k=0):
    if k == 18:
        s.add(a)
        return
    if c != 1 and c != 2:
        f(a + 3, 1, k + 1)
        f(a + 5, 2, k + 1)
    if c != 3 and c != 4:
        f(a * 2, 3, k + 1)
        f(a * 3, 4, k + 1)

f(35)

print(len(s))


s = set()

def f(a,b,c=0):
    if a > b:
        return 0
    if a == b:
        return 1
    if c == 2:
        return f(a*3,b,3)

    return f(a + 1, b, 1) + f(a * 2, b, 2) + f(a * 3, b, 3)

print(f(8,123))


#               ПРОЧИЕ ПРОТОТИПЫ


def f(x,y):
    if x >y: return 0
    if x == y: return 1
    else:
        return f(x + 2, y) + f(x + 4, y) + f(x + 5, y)

for y in range(32,72):
    if f(31,y) == 1001:
        print(y)

def f(x,y):
    if x > y:
         return 0
    if x == y:
         return 1
    else:
        return f(x+2,y) + f(x+5,y)

for y in range(6,30):
    if f(5,y) == 34:
        print(y)


count = 0

def f(st):
    global count
    if len(st) == 10:
        count += 1
    if len(st) < 10:
        f(st + '0')
        f(st + st[::-1])

f('7')
print(count)

def f(st,fn,co2,co3):
    if st == fn and co3 > co2:
        return True
    if st > fn:
        return False

    x = f(st+3,fn,co2,co3)
    y = f(st*2,fn,co2+1,co3)
    z = [0] * 10
    for i in range(10):
        z[i] = f(st*10 + i, fn,co2,co3+1)
    return x + y + sum(z)

print(f(1,48,0,0))

# Исполнитель Щелчок преобразует число на экране. У исполнителя есть две команды:
#
# 1. Прибавить 4
# 2. Вычесть 5
#
# Сколько существует программ, для которых при исходном числe 1 результатом является число 20.
# При этом исполнитель не может посетить одно и то же число дважды и может двигаться пока не перейдет
# границы отрезка [-20; 40], при переходе границ исполнитель разрушается.


def f(st,con,lim,vi):
    if st == con:
        return 1
    if (st < lim[0]) or (st > lim[1]):
        return 0
    if st in vi: return 0
    vis = vi.copy()
    vis.add(st)
    x = f(st+4,con,lim,vis)
    y = f(st-5,con,lim,vis)
    return x + y

print(f(1,20,(-20,40),set()))







