# Dijkstra with heap
from heapq import heappop, heappush

N, M = map(int, input().split())
kakutei = [False]*(N+1)
INF = 10**16
dis = [INF]*(N+1)
dis[1] = 0
G = [[] for _ in range(N+1)]
prev = [-1]*(N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
    G[b].append((c, a))
    
h = [(0, 1)]

while h:
    _, v = heappop(h)
    if kakutei[v]: continue
    kakutei[v] = True
    
    for w, nv in G[v]:
        if dis[nv] > dis[v] + w:
            dis[nv] = dis[v] + w
            prev[nv] = v
            heappush(h, (dis[nv], nv))
            
cur = N
ans = []
while cur != -1:
    ans.append(cur)
    cur = prev[cur]
    
ans = ans[::-1]
print(*ans)