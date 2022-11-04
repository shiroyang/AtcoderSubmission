# Array idx starts from 1
n = int(input()) - 1
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
MIN = -10**10
dp = [MIN]*(n+2)
dp[1] = 0
for i in range(1, n+1):
    dp[A[i]] = max(dp[A[i]], dp[i] + 100)
    dp[B[i]] = max(dp[B[i]], dp[i] + 150)
    
print(dp[-1])
    