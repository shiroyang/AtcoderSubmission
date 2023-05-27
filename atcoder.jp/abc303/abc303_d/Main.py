# DP
# a, shift+a, caps
# dp[i][j]: prev i-th letters, caps off or on, min time 

X, Y, Z = map(int, input().split())
S = input()

INF = 10**16
dp = [[INF]*2 for _ in range(len(S)+1)]
dp[0][0] = 0

for i in range(len(S)):
    for j in range(2):
        
        if dp[i][j] == INF: continue
        dp[i][1] = min(dp[i][1], dp[i][0]+Z)
        dp[i][0] = min(dp[i][0], dp[i][1]+Z)
        dp[i][1] = min(dp[i][1], dp[i][0]+Z)
        
        Capital = False
        if S[i] == 'A':
            Capital = True
        
        # 目前小写,要打大写，a or shift+a
        if Capital == True:
            dp[i+1][0] = min(dp[i+1][0], dp[i][0] + Y)
            dp[i+1][1] = min(dp[i+1][1], dp[i][1] + X)
        
        else:
            dp[i+1][0] = min(dp[i+1][0], dp[i][0] + X)
            dp[i+1][1] = min(dp[i+1][1], dp[i][1] + Y)
            

print(min(dp[-1]))