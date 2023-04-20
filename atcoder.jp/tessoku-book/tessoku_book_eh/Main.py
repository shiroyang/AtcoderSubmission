from sys import stdin
input = lambda: stdin.readline()[:-1]

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
ans = 0
idx = 0
for i in range(1, N+1):
    if ans < len(G[i]):
        ans = len(G[i])
        idx = i

print(idx)