n = int(input())
pp = [-1]
aa = [-1]
dp = [[0]*(n+2) for _ in range(n+2)]
for i in range(n):
    a, b = map(int, input().split())
    pp.append(a)
    aa.append(b)

for i in range(1, n+1):
    for j in range(n, 0, -1):
        score1 = 0 
        score2 = 0
        # 左の箱を取った時にもらえるボーナス
        # 1. make sure there is a box on the left
        # 2. make sure it satisfies the condition of the bonus
        if i > 1 and i <= pp[i-1] <= j:
            score1 = aa[i-1]
        if j < n and i <= pp[j+1] <= j:
            score2 = aa[j+1]
        dp[i][j] = max(dp[i-1][j]+score1, dp[i][j+1]+score2)
        
print(max(dp[i][i] for i in range(n+1)))