# 尺取法
from collections import deque

que = deque()
n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
que = deque([A[0]])

for i in range(1, n):
    while que and A[i] - que[0] > k:
        que.popleft()
    ans += len(que)
    que.append(A[i])
    
print(ans)