# 桁DPポイけど違う解決法
# Xは9の倍数 -> 各桁の和が9の倍数
# 従って、Kが9の倍数じゃないと0通り
MOD = 10**9+7
K = int(input())

if K % 9 != 0:
    exit(print(0))

dp = [0]*(100001)
dp[0] = 1

for i in range(1, K+1):
    lim = min(9, i)
    for j in range(lim+1):
        dp[i] += dp[i-j]
        dp[i] %= MOD

print(dp[K])