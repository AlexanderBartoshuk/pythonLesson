def f(a,b,m):
    if a + b >= 65: return m%2 == 0
    if m == 0: return 0
    h = [f(a+1,b,m-1), f(a,b+1,m-1), f(a*3,b,m-1),f(a,b*3,m-1)]
    return any(h) if m % 2 != 0 else all(h)
    #return any(h) if m %2 != 0 else any(h)   это для 19 номера
# print('19)', *[s for s in range(1, 59) if f(6, s, 2)])
print('20)', *[s for s in range(1, 59) if f(6, s, 3) and (not f(6, s, 1))])
print('21)', *[s for s in range(1, 59) if f(6, s, 4) and (not f(6, s, 2))])


def d(a,b,m):
    if a + b >= 75: return m%2 == 0 
    if m == 0: return 0 

    h = [d(a+1,b,m-1), d(a+b,b,m-1),d(a,b+a,m-1),d(a,b+1,m-1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', *[s for s in range(1, 67) if d(7, s, 2)])
print('20)', *[s for s in range(1, 67) if d(7, s, 3) and (not d(7,s,1))])
print('21)', *[s for s in range(1, 67) if d(7, s, 4) and (not d(7,s,2))])
