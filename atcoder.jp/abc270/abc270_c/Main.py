# DFS, path from s to t
import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True
    path.append(v)
    if v == Y:
        print(*path)
    for nv in G[v]:
        if not visited[nv]:
            dfs(nv)
    visited[v] = False
    path.pop()

N, X ,Y = map(int, input().split())
G = [[] for _ in range(N+1)]
visited = [False]*(N+1)
path = []

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
dfs(X)