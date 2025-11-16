def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    events = []
    
    idx = 1
    for _ in range(n):
        start_str = data[idx]; idx += 1
        end_str = data[idx]; idx += 1
        
        h1, m1 = map(int, start_str.split(':'))
        h2, m2 = map(int, end_str.split(':'))
        start_min = h1 * 60 + m1
        end_min = h2 * 60 + m2
        
        events.append((start_min, 1))
        events.append((end_min, -1))
    
    events.append((0, 0))
    events.append((1440, 0))
    events.sort()
    
    T = [0] * (n + 2)
    current = 0
    last_time = 0
    max_visitors = 0
    
    for time, delta in events:
        duration = time - last_time
        T[current] += duration
        current += delta
        if current > max_visitors:
            max_visitors = current
        last_time = time
    
    print(max_visitors)
    print(' '.join(map(str, T[:max_visitors + 1])))

if __name__ == "__main__":
    solve()



