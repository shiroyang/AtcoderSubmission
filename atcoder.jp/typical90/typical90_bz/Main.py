N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
ans = 0
for v in range(1, N+1):
    cnt = 0
    for nv in G[v]:
        if nv < v:
            cnt += 1
    if cnt == 1:
        ans += 1
        
print(ans)