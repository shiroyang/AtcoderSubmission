a = input()
b = input()
l = max(len(a), len(b))

# 要为dp多留一个空位
dp = [[0]*(l+1) for _ in range(l+1)]

for i in range(len(a)+1):
    for j in range(len(b)+1):
        if i >= 1 and j >= 1:
            if a[i-1] == b[j-1]:
                dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        elif i >= 1:
            dp[i][j] = dp[i-1][j]
        elif j >= 1:
            dp[i][j] = dp[i][j-1]
            
print(dp[len(a)][len(b)])