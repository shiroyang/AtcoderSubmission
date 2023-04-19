# Recovery DP
# dp[i][j]: prev i, sum j, doable or not

N, S = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(S+1):
        if dp[i][j] == True:
            l, r  = AB[i]
            if j + l <= S:
                dp[i+1][j+l] = True
            if j + r <= S:
                dp[i+1][j+r] = True

if not (dp[N][S]):
    exit(print("No"))
print("Yes")

rem = S
ans = []
for idx in range(N, 0, -1):
    l, r = AB[idx-1]
    if dp[idx-1][rem-l]:
        ans.append("H")
        rem -= l
    else:
        ans.append("T")
        rem -= r
        
ans = ans[::-1]
print(''.join(ans))