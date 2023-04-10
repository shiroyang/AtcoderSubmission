# 区間DP
# dp[l][r]: l文字目からr文字目が範囲になっている時、最大何文字を回文として追加できるか
# Sliding Windowみたいにし、区間を少しずつ拡張する

n = int(input())
s = input()

dp = [[0]*(n) for _ in range(n)]

# Initialize
for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if s[i] == s[i+1]:
        dp[i][i+1] = 2
    else:
        dp[i][i+1] = 1

for interval in range(2, n):
    for l in range(n - interval):
        r = l + interval
        # Ignore left, right, or taking both
        if s[l] == s[r]:
            dp[l][r] = max(dp[l][r-1], dp[l+1][r], dp[l+1][r-1]+2)
        else:
            dp[l][r] = max(dp[l+1][r], dp[l][r-1])

print(dp[0][n-1])