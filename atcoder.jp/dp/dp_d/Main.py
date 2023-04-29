# dp[i][j]: prev i, using j, max val

N, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    for j in range(W):
        dp[i+1][j] = dp[i][j]
        if j + A[i][0] <= W:
            dp[i+1][j] = max(dp[i][j], dp[i][j+A[i][0]]+A[i][1])
            
print(max(dp[-1]))