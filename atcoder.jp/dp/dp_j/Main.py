# Sushi
# dp[i][j][k]: すし１つ皿i枚 ... を全部食べる時の期待値
# dp[i][j][k] = dp[i][j-1][k+1] * k * invN +
#               dp[i-1][j+1][k] * j * invN +
#               dp[i+1][j][k]   * i * invN +
#               dp[i][j][k] * (N-i-j-k) * invN  

# この式を整理する、このやり方では寿司が減るように更新されているけど、bottom-upで更新しつつ、
# dp[-1][-1]に答えを保存したいので、状態遷移の符号を反転する、そうすると
# dp[i][j][k] = invIJK * (dp[i-1][j][k]*i + dp[i+1][j-1][k]*j + dp[i][j+1][k-1]*k + N)
# 状態更新が {-1,+1}でバラバラなので、メモ化する
# また、添え字がバラバラだから i+j+k <= N　まで全部更新する

from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)

for item in A:
    d[item] += 1

dp = [[[0.0]*(N+1-i-j) for j in range(N+1-i)] for i in range(N+1)]

# 一すし皿がインナーループ!
for k in range(N+1):
    for j in range(N+1-k):
        for i in range(N+1-j-k):
            if i == j == k == 0: continue
            invIJK = 1/(i+j+k)
            tmp = N
            if i > 0:
                tmp += dp[i-1][j][k]*i
            if j > 0:
                tmp += dp[i+1][j-1][k]*j
            if k > 0:
                tmp += dp[i][j+1][k-1]*k
            tmp *= invIJK
            dp[i][j][k] = tmp
            # dp[i][j][k] = invIJK * (dp[i-1][j][k]*i + dp[i+1][j-1][k]*j + dp[i][j+1][k-1]*k + N)
print(dp[d[1]][d[2]][d[3]])