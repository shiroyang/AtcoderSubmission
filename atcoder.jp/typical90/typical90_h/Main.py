# dp[i][j]: prev i, completing till letter j, num

MOD = 10**9+7
N = int(input())
S = input()
dp = [[0]*(8) for _ in range(N+1)]
dp[0][0] = 1
ref = 'atcoder'

for i in range(N):
    dp[i+1] = dp[i]
    for j in range(7):
        if S[i] == ref[j]:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD
            
print(dp[-1][-1])