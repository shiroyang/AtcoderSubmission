# グラフdpは順序がないので、まずtopological sort
# BFS topological sort, record indegree

from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]
deg = [0]*(N)

for _ in range(M):
    a, b = map(lambda x:int(x)-1, input().split())
    G[a].append(b)
    deg[b] += 1
    
que = deque()
# topological sort
path = []
# longest path
dp = [0]*(N)

for i in range(N):
    if deg[i] == 0:
        que.append(i)

while que:
    v = que.popleft()
    path.append(v)
    for nv in G[v]:
        deg[nv] -= 1
        if deg[nv] == 0:
            que.append(nv)
            dp[nv] = max(dp[nv], dp[v]+1)

print(max(dp))