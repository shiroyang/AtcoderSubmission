from collections import defaultdict, deque
d = defaultdict(list)

n, m = map(int, input().split())
comp = {i for i in range(1, n+1)}
edge_lis = []
ans = 0

for i in range(m):
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)
    edge_lis.append((u, v))
  
for pairs in edge_lis:
    u, v = pairs
    # 从顶点u开始BFS
    visited = set()
    visited.add(u)
    que = deque()
    que.append(u)
    while len(que) > 0:
        x = que.popleft()
        for edge in d[x]:
            if (u, v) != (x, edge) and (u, v) != (edge, x) and edge not in visited:
                visited.add(edge)
                que.append(edge)
    if visited != comp:
        ans += 1

print(ans)
