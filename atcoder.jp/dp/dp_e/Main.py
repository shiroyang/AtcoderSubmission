# reverse knapsack
# dp[i][j]: prev i, val j, min weight

INF = 10**16

N, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[INF]*(10**5+1) for _ in range(N+1)]
for i in range(N):
    dp[i][0] = 0
    
for i in range(N):
    for j in range(10**5+1):
        if dp[i][j] == INF: continue
        w, v = A[i]
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i+1][j+v] = min(dp[i+1][j+v], dp[i][j]+w)

maxval = 0
for i in range(10**5+1):
    if dp[N][i] <= W:
        maxval = i

print(maxval)