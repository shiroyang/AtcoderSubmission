# dp[i]: prev i-th, min cost

N, K = map(int, input().split())
A = list(map(int, input().split()))

INF = 10**16
dp = [INF]*N
dp[0] = 0

for i in range(N):
    for j in range(1, K+1):
        if i + j < N:
            dp[i+j] = min(dp[i+j], dp[i] + abs(A[i+j] - A[i]))
            
print(dp[-1])