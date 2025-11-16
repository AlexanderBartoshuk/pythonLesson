# x - количество камней в куче, p-позиция игры.
#
#def F(x,p):
#    if x >= 29 and p == 3: return True 
#    if x < 29 and p == 3: return False 
#    if x >= 29: return False
#
#    if p%2 == 1:
#        return F(x+1, p+1) and F(x*2,p+1)
#    else:
#        return F(x+1, p+1) or F(x*2,p+1)
#    
#for i in range(1,29):
#    if F(i,1):
#        print(i)
#
#
#def M(x,p):
#    if x >= 63 and p == 3: return True 
#    if x < 63 and p == 3: return False
#    if x >= 63 : return False 
#
#
#    if p % 2 == 0:
#        return M(x+1,p+1) or M(x+4,p+1) or M(x*5, p+1)
#    else:
#        return M(x+1,p+1) or M(x+4,p+1) or M(x*5, p+1)
#    
#for i in range(1,68):
#    if M(i,1):
#        print(i)
#        break  
#
#def C(x,p):
#    if x >= 42 and p==3: return True
#    if x < 42 and p==3 : return False
#    if x > 42: return False
#
#    if p%2 == 0:
#        return C(x+1,p+1) or C(x+3,p+1) or C(x*2,p+1)
#    else:
#        return C(x+1,p+1) or C(x+3,p+1) or C(x*2,p+1)
#    
#for i in range(1,42):
#    if C(i,1):
#        print(i)
#        break
#
#
#def X(x,p):
#    if x >= 64 and p == 3: return True
#    if x < 64 and p ==3: return False
#    if x > 64: return False
#
#    if p % 2 == 0: return X(x+1,p+1) or X(x*3, p+1)
#    else: return X(x+1,p+1) and X(x*3, p+1)
#
#for i in range(1,64):
#    if X(i,1):
#        print(i)
#        break
#
#def f(x,n):
#    if n==2 and x>=132:
#        return 1
#    if n==2 and x<132:
#        return 0
#    if n==1 and x>=132:
#        return 0
#    else:
#        a=0
#        if x%2==0:
#            a=x//2
#        if x%3==0:
#            a=x//3
#        if x%2!=0 and x%3!=0 :
#            a=x
#        if n%2==0:
#            return f(x+1,n+1) and f(x+a,n+1)
#        if n%2==1:
#            return f(x+1,n+1) or f(x+a,n+1)
#for s in range(1,132):
#    if f(s,0):
#        print(s)
#        break

#
#
#def f(x,p):
#    if x >= 37 and p == 3: return True 
#    if x < 37 and p == 3: return False
#    if x > 37: return False
#
#    if p%2 == 0: return f(x+1,p+1) or f(x+2,p+1) or f(x*2,p+1)
#    else:
#        return f(x+1,p+1) or f(x+2,p+1) or f(x*2,p+1)
#    
#for i in range(1,38):
#    if f(i,1):
#        print(i)
#        break
#
#
#
#def s(x,p):
#    if x >= 46 and p ==3: return True
#    if x < 46 and p ==3: return False
#    if x > 46: return False
#
#    if p % 2 == 0: return s(x+1,p+1) or s(x+2,p+1) or s(x*3,p+1)
#    else:
#        return s(x+1,p+1) or s(x+2,p+1) or s(x*3,p+1)
#    
#for i in range(1,45):
#    if s(i,1):
#        print(i)
#        break
#


#def f(x,p):
#    if x >= 47 and p == 3: return True 
#    if x < 47 and p ==3 : return False
#    if x > 47: return False
#
#    if p % 2 == 0: return f(x+1,p+1) or f(x+4,p+1) or f(x*2,p+1)
#    else: return f(x+1,p+1) or f(x+4,p+1) or f(x*2,p+1)
#
#for i in range(1,47):
#    if f(i,1):
#        print(i)
#        break
#
#def b(s,m):
#    if s >= 29: return m%2 == 0
#    if m == 0: return 0     
#    h = [b(s+1,m-1), b(s*2,m-1)]
#    return any(h) if m%2 == 0 else all(h)
#
#print(min(s for s in range(1,100) if b(s,2)))
#
#def f(x,p):
#    if x >= 364 and p == 3: return True
#    if x < 364 and p ==3: return False
#    if x >= 364: return False
#
#    if p%2 == 0: return f(x+1,p+1) or f(x*6, p+1)
#    else: return f(x+1,p+1) or f(x*6, p+1)
#
#for i in range(1,361):
#    if f(i,1):
#        print(i)
#        break
#

#def f(s,m):
#    if s <= 19: return m %2 == 0
#    if m == 0: return 0 
#    h = [f(s-2,m-1),f(s-5,m-1),f(s//3, m-1)]
#    return any(h) if m % 2 != 0 else all(h)
#
#print('19)', min([s for s in range(20, 100) if f(s, 2)]))
#print('20)', *[s for s in range(20, 100) if f(s, 3) and (not f(s, 1))])
#print('21)', min([s for s in range(20, 100) if f(s, 4) and (not f(s, 2))]))

def f(x,y):
    if x >= 64: return y%2 == 0
    if y == 0: return 0 

    h = [f(x+1,y-1),f(x*3,y-1)]
    return any(h) if y%2 != 0 else all(h)

print(min(s for s in range(1,63) if f(s,2)))
print(*[s for s in range(1, 63) if f(s, 3) and (not f(s, 1))])
print(*[s for s in range(1, 63) if f(s, 4) and (not f(s, 2))])


def f(s,m):
    if s >= 63: return m % 2 == 0
    if m == 0: return 0 
    h = [f(s+1,m-1),f(s+4,m-1),f(s*5,m-1)]
    return any(h) if m % 2 != 0 else all(h)
print('19)', min([s for s in range(1, 62) if f(s, 2)]))
print('20)', *[s for s in range(1, 62) if f(s, 3) and (not f(s, 1))])
print('21)', min([s for s in range(1, 62) if f(s, 4) and (not f(s, 2))]))




def f(x, h):
    if h == 3 and x >= 63: 
        return 1
    elif h == 3 and x < 63:
        return 0
    elif x >= 63 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)   # стратегия победителя
        else:
             return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)   # стратегия проигравшего(неудачный ход)

for x in range(1, 63):
    if f(x, 1) == 1:
        print("Задача 19: ", x)
        break