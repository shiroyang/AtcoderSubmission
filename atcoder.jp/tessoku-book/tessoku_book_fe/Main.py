# Greedy + 累積和 + 二分探索
from bisect import bisect_right

N = int(input())
A = sorted(list(map(int, input().split())))
Accum = [0]
for i in range(len(A)):
    Accum.append(Accum[-1]+A[i])

ans = []
Q = int(input())
for _ in range(Q):
    X = int(input())
    ans.append(bisect_right(Accum, X)-1)
    
print(*ans, sep='\n')