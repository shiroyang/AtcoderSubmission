# simple path using dfs

import sys
input = lambda: sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
visited = [False]*(N+1)
path = []

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

def dfs(v):
    path.append(v)
    visited[v] = True
    if v == N:
        print(*path)
        exit()
    for nv in G[v]:
        if visited[nv]: continue
        dfs(nv)
           
    if path: path.pop()
    visited[v] = False

    
dfs(1)