# dp[i][s]: prev i, state s (s==0 => healthy ), max val

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(2) for _ in range(N+1)]

for i in range(N):
    dp[i+1][0] = max(dp[i+1][0], dp[i][0])
    dp[i+1][1] = max(dp[i+1][1], dp[i][1])
    if A[i][0] == 0:
        dp[i+1][0] = max(dp[i][0], dp[i][0]+A[i][1], dp[i][1]+A[i][1])
    else:
        dp[i+1][1] = max(dp[i][1], dp[i][0]+A[i][1])
        
print(max(dp[-1]))