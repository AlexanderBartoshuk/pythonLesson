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




def get_m(cluster):
    return min(cluster, key=lambda p:
              sum(dist(p,q) for q in cluster))

clusters = [[],[]]
with open('2702.xlsx') as file:
    next(file)
    for line in file:
        x,y = map(float, line.split())
        if y > 15:
            clusters[0].append((x,y))
        else:
            clusters[1].append((x,y))

medoids = [get_m(cluster) for cluster in clusters]

px = sum(x for x,y in medoids) / len(medoids)
py = sum(y for x,y in medoids) / len(medoids)

print(abs(int(px*10000)), abs(int(py*10000)))

