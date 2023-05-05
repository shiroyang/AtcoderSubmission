# 尺取ほう
from collections import deque

N = int(input())
A = list(map(int, input().split()))
target = 0.1 * sum(A)
A = A + A

idx = 0
que = deque()
cur = 0

while idx < len(A):
    que.append(A[idx])
    cur += A[idx]
    
    while cur > target:
        tmp = que.popleft()
        cur -= tmp
    
    if cur == target:
        exit(print("Yes"))
        
    idx += 1
    
print("No")