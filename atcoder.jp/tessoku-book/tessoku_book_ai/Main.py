from collections import defaultdict
n = int(input())
arr = list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]
for idx, num in enumerate(arr):
    dp[n][idx+1] = num
for i in range(n-1, 0, -1):
    if i % 2 == 1:
        for j in range(1, i+1):
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
    else:
        for j in range(1, i+1):
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])

print(dp[1][1])