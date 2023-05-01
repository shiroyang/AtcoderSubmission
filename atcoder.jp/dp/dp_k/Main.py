'''
勝ち負け情報遷移
dp[i] = prev i, 0 to lose, 1 to win
'''

N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0]*(K+1)
dp[0] = 0
for i in range(K+1):
    if dp[i] == 1: continue
    for j in range(N):
        if i + A[j] > K: continue
        dp[i+A[j]] = dp[i] ^ 1
        
print("First" if dp[-1] else "Second")