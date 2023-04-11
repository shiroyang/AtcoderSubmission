# 勝つ状態を記録するDP

n, k  = map(int, input().split())
A = list(map(int, input().split()))

# 最初は全部負けの状態,そこから勝ち状態を上塗りするだけ
dp  = [0]*(n+1)

for i in range(n+1):
    if dp[i]: continue
    for item in A:
        if item + i <= n:
            dp[item+i] = 1    

print("First" if dp[n] else "Second")