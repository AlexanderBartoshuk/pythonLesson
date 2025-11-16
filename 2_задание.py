def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    L = int(data[1])
    A = int(data[2])
    B = int(data[3])
    b = list(map(int, data[4:4+N]))
    
    INF = 10**18
    dp = [INF] * (N+1)
    dp[0] = 0
    
    for i in range(1, N+1):
        if b[i-1] == 0:
            dp[i] = dp[i-1]
        else:
            dp[i] = min(dp[i], A + dp[i-1])
            if i >= L:
                dp[i] = min(dp[i], B + dp[i-L])
            else:
                dp[i] = min(dp[i], B)
    
    print(dp[N])

if __name__ == "__main__":
    solve()