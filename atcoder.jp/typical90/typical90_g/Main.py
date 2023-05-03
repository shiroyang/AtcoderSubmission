from bisect import bisect_right

N = int(input())
INF = 10**16
A = [-INF] + sorted(list(map(int, input().split()))) + [INF]

Q = int(input())
B = [int(input()) for _ in range(Q)]

for item in B:
    idx = bisect_right(A, item)
    l = A[idx-1]
    r = A[idx]
    print(min(abs(l-item), abs(r-item)))