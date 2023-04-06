# DP, scheduling problem
# dp[i][j]: prev i-th items, consumed time j, max cnt

N = int(input())
Task = []
lim = 0
for _ in range(N):
    t, d = map(int, input().split())
    if d > lim:
        lim = d
    Task.append((t, d))
Task.sort(key=lambda x: x[1])

dp = [[-1]*(lim+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(lim+1):
        # reachable
        if dp[i][j] == -1: continue
        # do nothing
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        # If the task is still in time
        if j + Task[i][0] <= Task[i][1]:
            dp[i+1][j+Task[i][0]] = max(dp[i+1][j+Task[i][0]], dp[i][j]+1)

print(max(dp[-1]))