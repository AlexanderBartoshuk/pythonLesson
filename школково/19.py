


def f(x,s):
    if x >= 63: return s % 2 == 0
    if s == 0: return 0
    h  = [f(x+1,s-1), f(x*3,s-1), f(x+3,s-1)]
    return any(h) if s % 2 != 0 and x % 2 != 0 else all(h)

print('19)', *[s for s in range(1,63) if f(s,1)])



















# def f(x,y,m):
#     if x + y <= 12: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x-1,y,m-1), f(x,y-1,m-1),f(x//2,y,m-1),f(x,y//2,m-1)]
#     return any(h) if m % 2 != 0 else any(h)
#
# print('19)' , *[s for s in range(1,100) if f(25,s,2)])