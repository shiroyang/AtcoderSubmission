# dp[i][j]: prev i, using j candies, vals
# dp[i+1][j] = dp[i][j] + dp[i][j-1] + ... dp[i][max(j-A[i], 0)]
# sum(dp[i], j, max(j-A[i], 0)) = Acc[j] - Acc[max(j-A[i]-1, 0)]

MOD = 10**9+7
N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0]*(K+1) for _ in range(N+1)]

dp[0][0] = 1

for i in range(N):
    Acc = [0]
    for j in range(len(dp[i])):
        Acc.append((Acc[-1] + dp[i][j])%MOD)
    for j in range(K+1):
        dp[i+1][j] = (Acc[j+1] - Acc[max(j-A[i], 0)])%MOD
        '''
        for k in range(A[i]+1):
            if j - k < 0: continue
            dp[i+1][j] += dp[i][j-k]
            dp[i+1][j] %= MOD
        '''
print(dp[-1][-1])