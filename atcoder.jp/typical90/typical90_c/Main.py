# diameter of a tree
# dfs 2 times
from collections import deque

N = int(input())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    a-=1; b-=1
    G[a].append(b)
    G[b].append(a)

def bfs(p):
    dis = [-1]*(N)
    dis[p] = 0
    que = deque([p])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dis[nv] != -1: continue
            dis[nv] = dis[v]+1
            que.append(nv)
            
    return dis

def furthest(dis):
    p, tmp = 0, 0
    for i in range(N):
        if dis[i] > tmp:
            tmp = dis[i]
            p = i
    return p
  
dis = bfs(0)
p = furthest(dis)  
dis = bfs(p)
q = furthest(dis)

print(dis[q]+1)