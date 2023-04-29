# dp[i][j]: prev i, last event j, max val
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(3) for _ in range(N+1)]

for i in range(N):
    dp[i+1][0] = max(dp[i+1][0], dp[i][1]+A[i][0], dp[i][2]+A[i][0])
    dp[i+1][1] = max(dp[i+1][1], dp[i][0]+A[i][1], dp[i][2]+A[i][1])
    dp[i+1][2] = max(dp[i+1][2], dp[i][0]+A[i][2], dp[i][1]+A[i][2])

print(max(dp[-1]))