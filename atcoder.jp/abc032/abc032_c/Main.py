# 尺取法
from collections import deque

que = deque()
p = 1
ans = 0

n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]
for item in A:  
    if item == 0:
        exit(print(n))
    que.append(item)
    p *= item
    while p > k and que:
        p //= que.popleft()
    ans = max(ans, len(que))

print(ans)