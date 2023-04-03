# knapsack with item limitation
# dp[i][j]=i種類目の硬貨まででj円ちょうどにできるか？
# また直接bitに情報を持たせて、管理することもできる
n, x = map(int, input().split())
s = 1 << x
for i in range(n):
    a, b = map(int, input().split())
    for j in range(b):
        s |= s >> a
print("Yes" if s & 1 else "No")
'''
n, x = map(int, input().split())
Mat = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(x+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(x+1):
        if dp[i][j]:
            cost, lim = Mat[i]
            for k in range(lim+1):
                if j + cost * k <= x:
                    dp[i+1][j+cost*k] = 1
                    
print("Yes" if dp[-1][-1] else "No")
'''