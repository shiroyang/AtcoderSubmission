## dp[i][j] represents if you can reach j with following i numbers
n, s = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0]*(s+1) for _ in range(n+1)]


for i in range(n+1):
    dp[i][0] = 1
    
for i in range(1, n+1):
    for j in range(1, s+1):
        idx = i - 1
        if j >= arr[idx]:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[idx]]
        else:
            if dp[i-1][j]:
                dp[i][j] = True
        
if dp[n][s] == True:
    print("Yes")
else:
    print("No")

