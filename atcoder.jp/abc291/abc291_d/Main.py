# DP
# dp[i][j]: prev i-th cards, 

MOD = 998244353
n = int(input())
Mat = []
for _ in range(n):
    a, b = map(int, input().split())
    Mat.append([a, b])

dp = [[0]*(2) for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(n-1):
    if Mat[i+1][0] != Mat[i][0]:
        dp[i+1][0] += dp[i][0]
        dp[i+1][0] %= MOD
        
    if Mat[i+1][0] != Mat[i][1]:
        dp[i+1][0] += dp[i][1]
        dp[i+1][0] %= MOD
        
    if Mat[i+1][1] != Mat[i][0]:
        dp[i+1][1] += dp[i][0]
        dp[i+1][1] %= MOD
        
    if Mat[i+1][1] != Mat[i][1]:
        dp[i+1][1] += dp[i][1] 
        dp[i+1][1] %= MOD   

print(sum(dp[-1])%MOD)