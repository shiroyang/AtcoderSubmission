from collections import deque, defaultdict
flag = True
visited = set()
d = defaultdict(set)

n, m = map(int, input().split())

for _ in range(m):
    u, v = map(int, input().split())
    d[u].add(v)
    d[v].add(u)

que = deque()
que.append(1)
visited.add(1)

while len(que) > 0:
    tmp = que.pop()
    for node in d[tmp]:
        if node not in visited:
            visited.add(node)
            que.append(node)

if len(visited) < n:
    print("The graph is not connected.")
else:
    print("The graph is connected.")