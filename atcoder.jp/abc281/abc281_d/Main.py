# DP
# dp[i][j][k]: prev i-th numbers, selecting j numbers, sum mod D == k, maximum num

N, K ,D = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[-1]*(D) for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N): 
    # 别取多了, 但是循环别漏了，要转到K+1保证当前状态能往下传下去
    for j in range(min(K+1, i+1)):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
            # Take A[i]
            if j != K:
                dp[i+1][j+1][(k+A[i])%D] = max(dp[i+1][j+1][(k+A[i])%D], dp[i][j][k] + A[i])
    
print(dp[-1][K][0])