from bisect import bisect_left
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

T = sorted(set(A))
d = defaultdict(int)
for item in A:
    idx = bisect_left(T, item) + 1
    d[len(T) - idx] += 1
    
for i in range(N):
    print(d[i])