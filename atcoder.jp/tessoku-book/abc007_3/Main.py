# BFS-Maze
import sys
input = lambda:sys.stdin.readline()[:-1]
from collections import deque

N, M = map(int, input().split())
sx, sy = map(lambda x:int(x)-1, input().split())
gx, gy = map(lambda x:int(x)-1, input().split())
INF = 10**16
dis = [[INF]*(M) for _ in range(N)]
dis[sx][sy] = 0
A = [list(input()) for _ in range(N)]

direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

que = deque([(sx, sy)])

while que:
    x, y = que.popleft()
    for dx, dy in direc:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N or 0 <= ny < M:
            if A[nx][ny] == '#': continue
            if dis[nx][ny] != INF: continue
            
            dis[nx][ny] = dis[x][y] + 1
            que.append((nx, ny))
        
print(dis[gx][gy])