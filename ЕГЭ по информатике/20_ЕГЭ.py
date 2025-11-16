#Петя не может выиграть за один ход;

#Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.

#def f(x,p):
#    if x >= 37 and p == 4: return True 
#    if x < 37 and p == 4: return False
#    if x > 37: return False
#
#    if p%2 != 0:
#        return f(x+1,p+1) or f(x+2,p+1) or f(x*2,p+1)
#    else:
#        return f(x+1,p+1) and f(x+2,p+1) and f(x*2,p+1)
#    
#for i in range(1,38):
#    if f(i,1):
#        print(i)
#


#def s(x,p):
#    if x >= 46 and p ==4: return True
#    if x < 46 and p ==4: return False
#    if x > 46: return False
#
#    if p % 2 != 0:
#        return s(x+1,p+1) or s(x+2,p+1) or s(x*3,p+1)
#    else:
#        return s(x+1,p+1) and s(x+2,p+1) and s(x*3,p+1)
#    
#for i in range(1,46):
#    if s(i,1) == 1:
#        print(i)
#


 
def f(x, h):
    if (h == 3 or h == 5) and x >= 361:
        return 1
    elif h == 5 and x < 361:
        return 0
    elif x >= 361 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x * 6, h + 1)   # стратегия победителя
        else:
            return f(x + 1, h + 1) and f(x * 6, h + 1)  # стратегия проигравшего
 
def f1(x, h):
    if h == 3 and x >= 361:
        return 1
    elif h == 3 and x < 361:
        return 0
    elif x >= 361 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f1(x + 1, h + 1) or f1(x * 6, h + 1)   # стратегия победителя
        else:
            return f1(x + 1, h + 1) and f1(x * 6, h + 1)  # стратегия проигравшего(любой ход)
 
for x in range(1, 361):
    if f(x, 1) == 1:
        print(x)
print("====")
for x in range(1, 361):
    if f1(x, 1) == 1:
        print(x)  # Исключим эти значения из списка выше


# method from book 
def f(s, m): # s-количество камней, m-осталось ходов до конца игры
 if s <= 19: return m % 2 == 0 # условие победы
 if m == 0: return 0
 h = [f(s - 2, m - 1), f(s - 5, m - 1), f(s // 3, m - 1)] # ходы
 return any(h) if m % 2 != 0 else all(h)
print('19)', min([s for s in range(20, 100) if f(s, 2)]))
print('20)', *[s for s in range(20, 100) if f(s, 3) and (not f(s, 1))])
print('21)', min([s for s in range(20, 100) if f(s, 4) and (not f(s, 2))]))