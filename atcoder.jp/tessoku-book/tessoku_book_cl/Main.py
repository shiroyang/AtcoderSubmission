# まず単純に尺取法
# その次にsum(que)を累積和で高速化
# その際stackにはindexを保存する

from collections import deque

n, k = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
for item in A:
    S.append(S[-1]+item)
    
calc = lambda i, j: S[j]-S[i-1]
que = deque()
ans = 0

for i in range(1, n+1):
    que.append(i)
    # sum(que) = calc(que[0], que[-1])
    while que and calc(que[0], que[-1]) > k:
        que.popleft()
    ans += len(que)

print(ans)