# いイチゴが1 個以上載っているピースそれぞれのイチゴの個数を調べ、その中の最大値を取れば良いです。

from collections import defaultdict
from bisect import bisect_left

w, h = map(int, input().split())
n = int(input())

P = [list(map(int, input().split())) for _ in range(n)]
a_num = int(input())
A = sorted(list(map(int, input().split())))
b_num = int(input())
B = sorted(list(map(int, input().split())))

d = defaultdict(int)

for x, y in P:
    idx = bisect_left(A, x)
    idy = bisect_left(B, y)
    d[(idx, idy)] += 1

    
MI = 10**16
MA = 0

if len(d) < (a_num+1)*(b_num+1):
    MI = 0

for val in d.values():
    if val < MI:
        MI = val
    if val > MA:
        MA = val

print(MI, MA)