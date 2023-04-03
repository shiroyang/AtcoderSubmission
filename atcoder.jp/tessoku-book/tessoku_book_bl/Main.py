# Shortest Path on a DAG
# DAG can be topologically sorted
# Dijkstra-Radix-Heap
# d[u].append((w, v))
from collections import deque, defaultdict
from heapq import heappush, heappop

N, M = map(int, input().split())
d = defaultdict(list)
INF = 10**16
cur = [INF]*(N)
cur[0] = 0
kakutei = [False]*(N)

for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    d[u].append((w, v))
    d[v].append((w, u))
    
h = []
heappush(h, (0, 0))

while h:
    tmp = heappop(h)
    u = tmp[1]
    # 未確定の頂点で最小を求めるため、確定している頂点はパスする    
    if kakutei[u]:
        continue
    kakutei[u] = True
    
    for w, v in d[u]:
        # 更新されたらヒープに追加

        if cur[v] > cur[u] + w:
            cur[v] = cur[u] + w
            heappush(h, (cur[v], v))

for kyori in cur:
    print(kyori if kyori !=INF else "-1")