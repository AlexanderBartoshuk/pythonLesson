# def f(s,n):
#     if s <= 537: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s-4,n-1),f(s//5,n-1)]
#     return any(h) if n % 2 != 0 else all(h)
#
# print('19)', min([s for s in range(538, 1000000) if f(s, 2)]))
# print('20)', *[s for s in range(538,100000) if f(s,3) and (not f(s,1))])
# print('21)', *[s for s in range(538,100000) if f(s,4) and (not f(s,2))])
#







#def f(a,b,s):
#    if a + b >= 77: return s % 2 == 0
#    if s == 0: return 0
#    h = [f(a+1,b,s-1),f(a*2,b,s-1),f(a,b+1,s-1),f(a,b*2,s-1)]
#    return any(h) if s % 2 != 0 else all(h)
#
#
#print('19)', *[s for s in range(1,70) if f(6,s,2)])
#print('20)', *[s for s in range(1, 70) if f(7, s, 3) and (not f(7, s, 1))])
#print('21)', *[s for s in range(1, 70) if f(7, s, 4) and (not f(7, s, 2))])



