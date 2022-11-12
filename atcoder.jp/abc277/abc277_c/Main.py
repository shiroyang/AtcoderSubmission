# defaultdictで隣接リスト、そしてdequeでBFS探索, visitedはすでに訪れたノードを記録する
from collections import defaultdict, deque

n = int(input())
visited = set()
visited.add(1)
d = defaultdict(list)

for i in range(n):
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)

que = deque()
que.append(1)
while len(que) > 0:
    x = que.pop()
    for edge in d[x]:
        if edge not in visited:
            visited.add(edge)
            que.append(edge)

print(max(visited))