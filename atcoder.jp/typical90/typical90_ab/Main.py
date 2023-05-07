# 二次元imos法
# 座標からグリッドにするとき、rx, ry を共に1引く
from collections import defaultdict
d = defaultdict(int)
N = int(input())
A = [[0]*(1010) for _ in range(1010)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    rx -= 1; ry -= 1
    A[lx][ly] += 1
    A[lx][ry+1] -= 1
    A[rx+1][ly] -= 1
    A[rx+1][ry+1] += 1

# add up the row
for i in range(1010):
    for j in range(1, 1010):
        A[i][j] += A[i][j-1]
        
# add up the col
for j in range(1010):
    for i in range(1, 1010):
        A[i][j] += A[i-1][j]
        
for i in range(1010):
    for j in range(1010):
        if A[i][j] == 0: continue
        d[A[i][j]] += 1

for i in range(1, N+1):
    print(d[i])