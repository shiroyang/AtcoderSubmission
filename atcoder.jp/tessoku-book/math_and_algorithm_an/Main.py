from collections import defaultdict, deque
n, m = map(int, input().split())
visited = set()
INF = 10**10
kyori = [INF]*(n+1)
kyori[1] = 0
d = defaultdict(set)

for _ in range(m):
    u, v = map(int, input().split())
    d[u].add(v)
    d[v].add(u)
    
que = deque()
que.append(1)
visited.add(1)

while len(que) > 0:
    tmp = que.popleft()
    for node in d[tmp]:
        if node not in visited:
            visited.add(node)
            que.append(node)
            kyori[node] = min(kyori[node], kyori[tmp]+1)

for i in range(1, n+1):
    if kyori[i] == INF:
        print("-1")
    else:
        print(kyori[i])