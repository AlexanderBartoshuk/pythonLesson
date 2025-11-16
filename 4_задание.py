import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    h = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(int(data[idx])); idx += 1
        h.append(row)
    
    
    dirs = [(-1,0), (0,-1), (0,1), (1,0)]
    
    
    def next_cell(i, j):
        min_h = h[i][j]
        next_i, next_j = i, j
        found = False
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if h[ni][nj] < h[i][j]:
                    if not found or h[ni][nj] < min_h:
                        min_h = h[ni][nj]
                        next_i, next_j = ni, nj
                        found = True
        return (next_i, next_j)
    
    
    next_map = [[(0,0)] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            next_map[i][j] = next_cell(i, j)
    
    
    sinks = []
    sink_id = [[-1] * M for _ in range(N)]
    sink_counter = 0
    for i in range(N):
        for j in range(M):
            ni, nj = next_map[i][j]
            if ni == i and nj == j:
                sink_id[i][j] = sink_counter
                sinks.append((i, j))
                sink_counter += 1
    
    final_sink = [[(-1,-1)] * M for _ in range(N)]
    
    def find_sink(i, j):
        if final_sink[i][j] != (-1,-1):
            return final_sink[i][j]
        ni, nj = next_map[i][j]
        if ni == i and nj == j:
            final_sink[i][j] = (i, j)
            return (i, j)
        res = find_sink(ni, nj)
        final_sink[i][j] = res
        return res
    
    for i in range(N):
        for j in range(M):
            find_sink(i, j)
    
    from collections import defaultdict
    basin_size = defaultdict(int)
    for i in range(N):
        for j in range(M):
            si, sj = final_sink[i][j]
            basin_size[(si, sj)] += 1
    
    sizes = sorted(basin_size.values(), reverse=True)
    print(len(sizes))
    print(' '.join(map(str, sizes)))

if __name__ == "__main__":
    solve()