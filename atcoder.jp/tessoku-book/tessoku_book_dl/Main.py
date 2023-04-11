# DP ではタイムアウトする
# 一つの仕事は一日しか続かないので、常に今選べる仕事で一番給料のいいやつを選ぶ
# Priority Que で"可能になったタスクだけ"突っ込む

from sys import stdin
from heapq import heappush, heappop
input = lambda: stdin.readline()[:-1]

N, D = map(int, input().split())
A = [[] for _ in range(D+1)]
que = []
ans = 0

for _ in range(N):
    x, y = map(int, input().split())
    A[x].append(y)

for d in range(1, D+1):
    for val in A[d]:
        heappush(que, -val)

    if que:
        val = -heappop(que)
        ans += val
        
print(ans)