# 区間DP
# dp[l][r]: from l to r-1, min cost
# l and r is separator, 0 <= l < r <= N
# dp[l][r] = min(dp[l+1][r], dp[l][r-1]) + sum(A, l, r-1)

INF = 10**16
N = int(input())
A = list(map(int, input().split()))
Acc = [0]
for i in range(len(A)):
    Acc.append(Acc[-1]+A[i])
    
dp = [[INF]*(N+1) for _ in range(N+1)] 

for i in range(N):
    dp[i][i+1] = 0
    
# Warshall Floyd のように中継地点を決める
for interval in range(2, N+1):
    for l in range(N):
        if l + interval > N: break
        r = l + interval
        
        for k in range(l+1, l+interval):
            dp[l][r] = min(dp[l][r], dp[l][k] + dp[k][r] + Acc[r] - Acc[l])

print(dp[0][N])