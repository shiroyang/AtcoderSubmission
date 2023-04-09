# Warshall-Floyd

n, k = map(int, input().split())
INF = 10**16
dp = [[INF]*(n) for _ in range(n)]

A = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            dp[i][j] = 1

for x in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][x]+dp[x][j])

q = int(input())
for _ in range(q):
    s, t = map(lambda x:int(x)-1, input().split())
    s %= n
    t %= n
    print(dp[s][t] if dp[s][t]!= INF else -1)