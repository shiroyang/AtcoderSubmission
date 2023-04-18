# Frog 問題の改善DP
# dp[i]: 足場iまでの移動数
# [l, r]から現在の足場まで遷移可能だったらdp[l]..dp[r]まで足さないとだめだから累積和も必要
# また現在と距離がLからRまで離れている足場を探す必要があるので、尺取法
from collections import deque

MOD = 10**9+7
N, W, L, R = map(int, input().split())
A = [0] + list(map(int, input().split())) + [W]
N = len(A)
dp = [0]*N
# dpsum[i] = dp[0] + ... dp[i]
# sum(dp[l], dp[r]) = dpsum[r] - dpsum[l-1]
dpsum = [0]*N

dp[0] = 1
dpsum[0] = 1

fst, snd = -1, -1
for i in range(1, N):
    now = A[i]
    # now - R より右にいかないとダメ
    while now - A[fst+1] > R:
        fst += 1
    # now - L  よりは左にいないとだめ    
    while now - A[snd+1] >= L:
        snd += 1
    
    if snd >= 0: dp[i] += dpsum[snd]
    if fst >= 0: dp[i] -= dpsum[fst]
    dp[i] %= MOD
    dpsum[i] = dpsum[i-1] + dp[i]
    dpsum[i] %= MOD

print(dp[-1])