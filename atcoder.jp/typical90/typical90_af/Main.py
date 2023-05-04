# BF
from itertools import permutations
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
G = [[False]*(N) for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a-=1; b-=1
    G[a][b] = True
    G[b][a] = True
    
tmp = [i  for i in range(N)]
INF = 10**16
min_cos = INF

for ls in permutations(tmp):
    is_ok = True
    for i in range(len(ls)-1):
        if G[ls[i]][ls[i+1]]: 
            is_ok = False
            break
    if is_ok == False: continue
    cur_cos = 0
    for i in range(len(ls)):
        cur_cos += A[ls[i]][i]
    if min_cos > cur_cos:
        min_cos = cur_cos

print(min_cos if min_cos!= INF else -1)