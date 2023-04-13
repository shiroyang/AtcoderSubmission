# Laterns
# bit dp + BFS で最短距離を求めよう

from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
XYZ = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
INF = 10**16

dp  = [INF]*(1<<N)
now = 0

for i in range(N):
    if A[i] == 1:
        now += (1<<i)

dp[now] = 0
que = deque()
que.append(now)

while que:
    now = que.popleft()
    for x, y, z in XYZ:
        switch = (1<<x) | (1<<y) | (1<<z)
        nxt = now ^ switch
        if dp[nxt] == INF:
            dp[nxt] = dp[now] + 1
            que.append(nxt)
            
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])