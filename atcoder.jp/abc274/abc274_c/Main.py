from collections import deque
INF=float("INF")

N=int(input())
A=list(map(int,input().split()))
 
G=[[] for _ in range(2*N+1)]
for i in range(N):
  G[A[i]-1].append((i+1)*2-1)
  G[A[i]-1].append((i+1)*2)

dist=[INF]*(2*N+1); dist[0]=0
D=deque(); D.append(0)
while D:
  now=D.popleft()
  for nxt in G[now]:
    if dist[nxt]!=INF:
      continue
    dist[nxt]=dist[now]+1
    D.append(nxt)

print(*dist,sep="\n")