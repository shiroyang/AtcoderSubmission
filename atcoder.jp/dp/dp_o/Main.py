# dp[i][s]: 左のi人の男性と、右の女性の0-1集合(1<<N)でのマッチング数
# OPT -> dp[s]: i == s.bitcnt(1)のため、持たなくていい
# dp[0] = 1
# dp[s] = sigma(dp[s / l] * A[bitcnt[s]-1][l])
MOD = 10**9+7
    
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [0]*(1<<N)
dp[0] = 1

for s in range(1<<N):
    tmp = 0
    for j in range(N):
        if (1<<j) & s:
            tmp += 1
    man_cnt = tmp - 1
    for l in range(N):
        # Sからl人目の女性を取り除いて、マッチング数をカウントする
        if (s>>l) & 1 == 0: continue
        if A[man_cnt][l] == 0: continue     
        dp[s] += dp[s^(1<<l)]
        dp[s] %= MOD

print(dp[(1<<N) - 1]%MOD)