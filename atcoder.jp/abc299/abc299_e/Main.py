# Calculate All Paths Shortest Path in O(N(N+M)) = (8*10**6)
# 最も近い黒い頂点の距離がd -> d以内の頂点は全て白で塗る
# {Ini:-1, W:0, B:1}
# 残りの頂点を黒にして、Queryを検証
# 1. At least one black
# 2. when kyori < d: no black
# 3. when kyori == d: at least one black
from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
INF = 10**16
dis = [[INF]*(N) for _ in range(N)]
for i in range(N):
    dis[i][i] = 0

for _ in range(M):
    a, b = map(lambda x:int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

K = int(input())
Q = []

for _ in range(K):
    p, d = map(int, input().split())
    p -= 1
    Q.append((p, d))

for i in range(N):
    que = deque([i])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dis[i][nv] != INF: continue
            
            dis[i][nv] = dis[i][v] + 1
            que.append(nv)

# d以内を白に
col = [-1]*(N)
for p, d in Q:
    for j in range(N):
        if dis[p][j] < d:
            if col[j] == -1: col[j] = 0
# 残りを黒に
for i in range(N):
    if col[i] == -1:
        col[i] = 1     

# 1. At least one black
if col.count(1) == 0:
    exit(print("No"))

# 2. When kyori < d: no black
# 3. When kyori == d: at least one black
for p, d in Q:
    cnt = 0
    for j in range(N):
        if dis[p][j] < d and col[j] == 1:
            exit(print("No"))
        if dis[p][j] == d and col[j] == 1:
            cnt += 1
    if not cnt: exit(print("No"))
    
print("Yes")
print(*col, sep='')