# 尺取法
from collections import deque, defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
ans = 0
que = deque()
for idx in range(len(A)):
    d[A[idx]] += 1
    que.append(A[idx])
    while len(d) > K:
        tmp = que.popleft()
        d[tmp] -= 1
        if d[tmp] == 0:
            d.pop(tmp)
    ans = max(ans, len(que))

print(ans)