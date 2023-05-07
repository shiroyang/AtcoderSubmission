# topo sortして、leafを全部塗る、そして、条件を満たしている分を上にbottom-upで塗って行く

import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True
    for nv in G[v]:
        if visited[nv]: continue
        dfs(nv)
    path.append(v)

N = int(input())
G = [[] for _ in range(N+1)]
col = [0]*(N+1)
path = []
visited = [False]*(N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
dfs(1)

cnt = 0
for i in range(N):
    v = path[i]
    is_ok = True
    for nv in G[v]:
        if col[nv] == 1: 
            is_ok = False
            break
    if is_ok: 
        col[v] = 1
        cnt += 1
    if cnt == N//2:
        break

for i in range(N+1):
    if col[i]: print(i, end=' ')
print()