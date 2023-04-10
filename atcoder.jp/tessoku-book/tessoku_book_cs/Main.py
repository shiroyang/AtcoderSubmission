# min edit distance
# dp[i][j]: S[:i] => T[:j], min cos

s = input()
t = input()
INF = 10**16

dp = [[INF]*(len(t)+1) for _ in range(len(s)+1)]
# CAUTION, NEED TO FULLY INITIAZLIZE
for i in range(len(s)+1):
    dp[i][0] = i
for j in range(len(t)+1):
    dp[0][j] = j


for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i+1][j+1] = min(dp[i][j], dp[i+1][j]+1, dp[i][j+1]+1)
        else:
            dp[i+1][j+1] = min(dp[i][j]+1, dp[i+1][j]+1, dp[i][j+1]+1)

print(dp[len(s)][len(t)])