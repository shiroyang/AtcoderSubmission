# 貰うDP
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+val)
# But J could be extremely big
# ヒント：dp[i][j]: prev i, val j, min weight

N, W = map(int, input().split())
INF = 10**16
MAXV = pow(10, 5)
wv = [list(map(int, input().split())) for _ in range(N)]
dp = [[INF]*(MAXV+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    wei, val = wv[i-1]
    for j in range(MAXV+1):
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        if j - val >= 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j-val]+wei)

idx = MAXV
while idx >= 0 and dp[-1][idx] > W:
    idx -= 1

print(idx)