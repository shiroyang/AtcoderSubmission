# doubling pow!
MOD = 10**9+7

a, b = map(int, input().split())
dp = [0]*61
dp[0] = a % MOD
for i in range(1, 61):
    dp[i] = (dp[i-1]**2)%MOD

p = 1
for i in range(61):
    if (b>>i)&1 == 1:
        p = (p*dp[i])%MOD

print(p)