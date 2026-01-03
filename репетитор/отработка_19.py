def D(x,y,h):
    if x + y >= 46 and h == 2: return True
    if x + y < 46 and h == 2: return False

    d= k= 0
    for b in range(1,x):
        k = x-1
    for e in range(1,y):
        d = y-1
    if x < y:
        return D(x,y,h+1) or D(x+k,y,h+1) 
    if x == y:
        return D(x+k,y,h+1) or D(x+1,y,h+1) or D(x,y+d,h+1) or D(x,y+1,h+1)

for i in range(1,90):
    for x in range(1,90):
        if D(i,x,1):
            print(x+i)
            break
