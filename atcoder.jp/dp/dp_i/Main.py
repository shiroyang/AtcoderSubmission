# dp[i][j]: prev i-th, nums of up, prob
# dp[i+1][j] = dp[i][j-1]*P[i] + dp[i][j]*(1-P[i])
# dp[]

N = int(input())
P = list(map(float, input().split()))

dp = [[0.0]*(N+1) for _ in range(N+1)]
dp[1][0] = 1-P[0]
dp[1][1] = P[0]

for i in range(1, N):
    for j in range(i+2):
        dp[i+1][j] = dp[i][j-1]*(P[i]) + dp[i][j]*(1-P[i])

prob = sum(dp[-1][len(dp[-1])//2:])
print(prob)