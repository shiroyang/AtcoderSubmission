# paint the balls, 0:white, 1:black, 2:blue
from collections import deque

N, X = map(int, input().split())
X -= 1
A = list(input())
col = [-1]*(N)

for i in range(N):
    if A[i] == '#':
        col[i] = 1
    else:
        col[i] = 0
        
que = deque()
que.append(X)
col[X] = 2

while que:
    u = que.popleft()
    if u-1 >= 0 and col[u-1] == 0:
        col[u-1] = 2
        que.append(u-1)
    if u+1 < N and col[u+1] == 0:
        col[u+1] = 2
        que.append(u+1)
        
for item in col:
    if item == 0:
        print(".", end='')
    elif item == 1:
        print("#", end='')
    else:
        print("@", end='')
print()