for i in range(1000,100_000):
    s = str(i)
    t1 = int(s[0]) + int(s[1])
    t2 = int(s[2]) + int(s[3])
    if str(min(t1,t2)) + str(max(t1,t2)) == '1718':
        print(i)
        break


for i in range(10000,10**5):
    s = str(i)
    nechet = (int(s[0]) ** 2) + (int(s[2]) ** 2) + (int(s[4]) ** 2)
    chet = (int(s[1]) ** 2) + (int(s[3]) ** 2)
    if str(min(chet,nechet)) + str(max(chet,nechet)) == '7590':
        print(i)

