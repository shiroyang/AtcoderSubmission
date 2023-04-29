# LCS
# dp[i][j]: prev i in s, prev j in t, max val

s = input()
t = input()
ss, tt = len(s), len(t)

dp = [[0]*(tt+1) for _ in range(ss+1)]

for i in range(ss):
    for j in range(tt):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j], dp[i][j+1])
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])


ans = []
slen = dp[-1][-1]
x, y = ss, tt

while slen > 0:
    while dp[x-1][y] == slen:
        x -= 1
    while dp[x][y-1] == slen:
        y -= 1
    
    ans.append(s[x-1])
    slen -= 1
    x -= 1
    y -= 1

print(''.join(ans[::-1]))