import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.read
    data = input().split()
    it = iter(data)
    N = int(next(it)); M = int(next(it))
    a = [0] + [int(next(it)) for _ in range(N)]  # 1-based
    g = [[] for _ in range(N+1)]
    for _ in range(M):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
    
    # Поиск SCC (алгоритм Тарьяна)
    index = 0
    stack = []
    indices = [-1]*(N+1)
    lowlink = [-1]*(N+1)
    on_stack = [False]*(N+1)
    comp_id = [0]*(N+1)
    comp_sum = []
    comp_graph = []
    comp_index = 0
    
    def strongconnect(v):
        nonlocal index, comp_index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True
        
        for w in g[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])
        
        if lowlink[v] == indices[v]:
            comp_sum.append(0)
            comp_graph.append(set())
            while True:
                w = stack.pop()
                on_stack[w] = False
                comp_id[w] = comp_index
                comp_sum[comp_index] += a[w]
                if w == v:
                    break
            comp_index += 1
    
    for v in range(1, N+1):
        if indices[v] == -1:
            strongconnect(v)
    

    for v in range(1, N+1):
        for w in g[v]:
            if comp_id[v] != comp_id[w]:
                comp_graph[comp_id[v]].add(comp_id[w])
    

    indeg = [0]*comp_index
    for u in range(comp_index):
        for w in comp_graph[u]:
            indeg[w] += 1
    q = []
    for i in range(comp_index):
        if indeg[i] == 0:
            q.append(i)
    topo = []
    while q:
        u = q.pop()
        topo.append(u)
        for w in comp_graph[u]:
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)
    

    dp = [0]*comp_index
    for u in reversed(topo):
        best = 0
        for w in comp_graph[u]:
            if dp[w] > best:
                best = dp[w]
        dp[u] = comp_sum[u] + best
    
    print(max(dp))

if __name__ == "__main__":
    solve()