'''
min-maxの区間DP
dp[l][r]: A[l, r) から始まった時のans
outer-loop: the length of interval from 1 to N

相手は常に自分と反対のことをしているからポイントはマイナス

'''

from collections import deque

N = int(input())
A = list(map(int, input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]

for interval in range(1, N+1):
    for l in range(N):
        if l + interval <= N:
            r = l + interval
            dp[l][r] = max(-dp[l][r-1] + A[r-1], -dp[l+1][r] + A[l])

print(dp[0][N])