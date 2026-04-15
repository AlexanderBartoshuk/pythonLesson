# for i in range(174457,174505+1):
#     k = []
#     s = 0
#     for x in range(2,i//2+1):
#         if i % x == 0:
#             s += 1
#             k.append(x)
#             if s > 2:
#                 break
#     if s == 2:
#         print(*k)

# for i in range(101000000,102000001):
#     if i % 2 == 0:
#         s = 1
#         for x in range(2,round(i**0.5)+1):
#             if i % x == 0:
#                 if x % 2 == 0:
#                     s += 1
#             if s > 3:
#                 break
#         if s == 3:
#             print(i)


# for x in range(210235,210300+1):
#     k = []
#     s = 0
#     for y in range(2,x//2+1):
#         if x % y == 0:
#             s += 1
#             k.append(y)
#             if s > 4:
#                 break
#     if s == 4:
#         print(k)


for x in range(110203,110245+1):
    k = []
    for y in range(2,int(x**0.5)+1):
        if x % y == 0 and y % 2 == 0:
            k.append(y)
        if x % y == 0 and (x//y) % 2 == 0:
            k.append(x//y)
        if len(k) > 4:
            break
    if len(k) == 4:
        print(sorted(k))


for x in range(110203,110245):
    n = {x}
    for y in range(2,round(x**0.5)+1):
        if x % y == 0 and y % 2 == 0:
            n.add(y)
        if x % y == 0 and (x//y) % 2 == 0:
            n.add(x//y)
        if len(n) > 4:
            break
    if len(n) == 4:
        print(sorted(n))
