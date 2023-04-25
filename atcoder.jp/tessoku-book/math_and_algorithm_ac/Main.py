# dp[i][j]: prev i-th days, studied or not, max val

N = int(input())
A = list(map(int, input().split()))
dp = [[0]*(2) for _ in range(N+1)]

for i in range(N):
    dp[i+1][1] = max(dp[i+1][1], dp[i][0] + A[i])
    dp[i+1][0] = max(dp[i+1][0], dp[i][0], dp[i][1])

print(max(dp[-1]))