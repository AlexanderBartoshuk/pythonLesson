from math import dist
#def get_medoid(cluster):
#    return min(cluster, key=lambda p:
#               sum(dist(p,q) for q in cluster))
#
#clusters = [[],[]]
#with open('2701_A.txt') as file:
#    next(file)
#    for line in file:
#        x,y = map(float,line.split())
#        if y < 0 :
#            clusters[0].append((x,y))
#        else:
#            clusters[1].append((x,y))
#
#medoids = [get_medoid(cluster) for cluster in clusters]
#
#px = sum(x for x,y in medoids) / len(medoids)
#py = sum(y for x,y in medoids) / len(medoids)
#
#print(abs(int(px*10000)), abs(int(py*10000)))

#
#
#def get_medoid(cluster):
#    return min(cluster, key=lambda p:
#               sum(dist(p,q) for q in cluster))
#
#clusters = [[],[],[]]
#with open('2701_B.txt') as file:
#    next(file)
#    for line in file:
#        x,y = map(float,line.split())
#        if x < 10:
#            clusters[0].append((x,y))
#        if x > 20:
#            clusters[1].append((x,y))
#        else:
#            clusters[2].append((x,y))
#
#medoids = [get_medoid(cluster) for cluster in clusters]
#
#px = sum(x for x,y in medoids) / len(medoids)
#py = sum(y for x,y in medoids) / len(medoids)
#
#print(abs(int(px*10000)), abs(int(py*10000)))




f = open('27_A_2024.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(x) for x in f]
st= 0 
fin = 0 
summa = 0 
for i in range(2 * k,n):
    st = max(st, a[i-2*k])
    fin = max(fin, st + a[i-k])
    summa = max(summa, fin + a[i])
print(summa)


f = open('1_27_A.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(x) for x in f]
summa = 0
maxi = 0
for i in range(n):
    maxi = max(maxi, a[i])
    if i + k < len(a):
        summa = max(summa, maxi+a[i+k])
print(summa)

