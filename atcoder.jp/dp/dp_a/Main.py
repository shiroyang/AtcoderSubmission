# dp[i]: prev i, min cost

N = int(input())
A = list(map(int, input().split()))

INF = 10**16
dp = [INF]*(N)
dp[0] = 0

for i in range(N):
    if i + 1 < N: 
        dp[i+1] = min(dp[i+1], dp[i]+abs(A[i+1]-A[i]))
    if i + 2 < N:
        dp[i+2] = min(dp[i+2], dp[i]+abs(A[i+2]-A[i]))
        
print(dp[-1])