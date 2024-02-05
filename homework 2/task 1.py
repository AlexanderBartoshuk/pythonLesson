def work(x, y):
    work_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for a in range(2, int(i/2)+1):
                if i % a == 0:
                    break
            else:
                work_list.append(i)
    return work_list
print(work(1,746))