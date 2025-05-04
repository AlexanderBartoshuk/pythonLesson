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


def f(x,p):
    if x >= 364 and p == 3: return True
    if x < 364 and p ==3: return False
    if x >= 364: return False

    if p%2 == 0: return f(x+1,p+1) or f(x*6, p+1)
    else: return f(x+1,p+1) or f(x*6, p+1)

for i in range(1,361):
    if f(i,1):
        print(i)
        break



