n, w = map(int, input().split())
ww = [0]
vv = [0]
MIN = -10**10
dp = [[MIN]*(w+1) for i in range(n+1)]

for i in range(w+1):
    dp[0][i] = 0

for i in range(n):
    a ,b = map(int, input().split())
    ww.append(a)
    vv.append(b)
    
for i in range(1, n+1):
    for j in range(w+1):
        max_ans = dp[i-1][j]
        if j - ww[i] >= 0:
            max_ans = max(max_ans, dp[i-1][j-ww[i]]+vv[i])
        dp[i][j] = max_ans

print(dp[n][w])