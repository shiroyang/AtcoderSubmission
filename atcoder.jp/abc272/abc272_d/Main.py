# BFS
# a**2 + b**2 = M
# BF + set

from collections import deque
from bisect import bisect_left
from math import sqrt, ceil

N, M = map(int, input().split())
d = set()

for i in range(ceil(sqrt(M))+1):
    d.add(i**2)

dirc = []
for a in d:
    if M-a in d:
        rem = M-a
        a = ceil(sqrt(a))
        b = ceil(sqrt(rem))
        dirc.append((a, b))

tmp = []
for x, y in dirc:
    tmp.append((x, y))
    tmp.append((-x, y))
    tmp.append((x, -y))
    tmp.append((-x, -y))

dirc = tmp

dis = [[-1]*(N) for _ in range(N)]
dis[0][0] = 0

que = deque()
que.append((0, 0))

while que:
    x, y = que.popleft()
    for dx, dy in dirc:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if dis[nx][ny] != -1: continue
            dis[nx][ny] = dis[x][y] + 1
            que.append((nx, ny))
            
for li in dis:
    print(*li)