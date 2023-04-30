# dp[i]: 体力がiから0以下になる期待値
# dp[i] = ((dp[max(i-2, 0)]*critical + dp[i-1]*normal) + 1)%MOD

MOD = 998244353
inv100 = pow(100, MOD-2, MOD)

N, p = map(int, input().split())
dp = [0]*(N+1)

critical = (p * inv100)%MOD
noraml = (1 - p * inv100)%MOD

for i in range(1, N+1):
    dp[i] = ((dp[max(i-2, 0)]*critical + dp[i-1]*noraml) + 1) % MOD 

print(dp[-1])