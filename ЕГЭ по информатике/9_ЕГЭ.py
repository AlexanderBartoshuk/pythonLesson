file = open('егэ.txt')

k = 0
for s in file:
    if len(set(m))==5:
        m = [int(x) for x in s.split()]
        mp = [x for x in m if m.count(x)==2]
        mn = [x for x in m if m.count(x)==1]
        if sum(mn) / 4 <= sum(mp): k+=1
print(k)


#count = 0
#for s in file:
#    m = [int(x) for x in s.split()]
#    m.sort()
#    if (m[0] + m[-1])**2 > m[1]**2 + m[2]**2 + m[3]**2:
#        count += 1
#print(count)


count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len(M) == len(set(M)): # — все числа в строке различны;
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(nechet) > len(chet):
            if sum(nechet) < sum(chet):
                count += 1
print(count)

