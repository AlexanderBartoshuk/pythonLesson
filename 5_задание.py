def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    xs = []
    ys = []
    idx = 1
    for _ in range(n):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        xs.append(x)
        ys.append(y)
    
    xs.sort()
    ys.sort()
    
    if n % 2 == 1:
        # Нечётное N
        med_x = xs[n // 2]
        med_y = ys[n // 2]
        total_dist = 0
        for i in range(n):
            total_dist += abs(xs[i] - med_x) + abs(ys[i] - med_y)
        print(total_dist, 1)
    else:
        # Чётное N
        m = n // 2
        med_x1, med_x2 = xs[m - 1], xs[m]
        med_y1, med_y2 = ys[m - 1], ys[m]
        
        # Любая точка между медианами даёт минимум
        count_x = med_x2 - med_x1 + 1
        count_y = med_y2 - med_y1 + 1
        
        # Сумму расстояний можно вычислить для любой точки в прямоугольнике, например (med_x1, med_y1)
        total_dist = 0
        for i in range(n):
            total_dist += abs(xs[i] - med_x1) + abs(ys[i] - med_y1)
        
        print(total_dist, count_x * count_y)

if __name__ == "__main__":
    solve()