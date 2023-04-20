# Rank, bottom to up dfs
# dfs をして、帰りがけ順にランクを設定する

from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    visited[x] = True
    for nx in G[x]:
        if visited[nx]: continue
        ret = dfs(nx)
        rk[x] = max(rk[x], ret+1)

    return rk[x]

N, T = map(int, input().split())
G = [[] for _ in range(N+1)]
visited = [False]*(N+1)
rk = [0]*(N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dfs(T)
print(*rk[1:])