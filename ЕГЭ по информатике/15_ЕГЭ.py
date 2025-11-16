
def F(x,A):
    return (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))
for A in range(0,1000):
    if all(F(x,A) for x in range(0,10000)):
           print(A)
           break
    


def F(x, A):
    return (x & 25 != 0) <= ((x & 19 == 0) <= (x & A != 0))
 
for A in range(0, 1000):
    if all(F(x, A) for x in range(10000)):
        print(A)
        break

p = list(range(25, 50))
q = list(range(32, 47))

A = list(range(60))

for x in range(60):
    if ((not(x in A)) <= (x in p)) <= ((x in A) <= (x in q)):
        A.remove(x)
print(A)








