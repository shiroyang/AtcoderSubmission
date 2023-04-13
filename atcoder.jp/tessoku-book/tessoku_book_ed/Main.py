# Doubling
# dp[k][i]: 整数iから2^(k)回操作した後の整数
# 1<<30 > 10*9
# 大きい順に先に遷移する

def solve(N, K):
    cur = N
    rem = K
    for k in range(29, -1, -1):
        if (1<<k) <= rem:
            rem -= (1<<k)
            cur = dp[k][cur]
    print(cur)
    

N, K = map(int, input().split())
dp = [[0]*(N+1) for _ in range(30)]
for i in range(N+1):
    t1 = i
    t2 = i
    while t2 != 0:
        t1 -= t2 % 10
        t2 //= 10
    dp[0][i] = t1

for k in range(1, 30):
    for i in range(1, N+1):
        dp[k][i] = dp[k-1][dp[k-1][i]]

for i in range(1, N+1):
    solve(i, K)    