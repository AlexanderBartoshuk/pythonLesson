k = 0
for s in open('112.txt'):
    a = [int(x) for x in s.split()]
    maxi = max(a)
    mini = min(a)
    sred = (maxi + mini) / 2
    if len(a) == len(set(a)) and sred in a:
        k += 1
print(k)




