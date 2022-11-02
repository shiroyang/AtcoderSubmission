n = int(input())
memo = [-1]*(n+1)
memo[0] = 0
memo[1] = 0
memo[2] = 1
INF = 10**8
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [INF]*(n+1)
dp[1] = 0
dp[2] = a[0]
for i in range(3, n+1):
    cost1 = dp[i-1] + a[i-2]
    cost2 = dp[i-2] + b[i-3]
    if cost1 <= cost2:
        dp[i] = cost1
        memo[i] = 1
    else:
        dp[i] = cost2
        memo[i] = 2
        
ans = []
idx = n
while idx > 1:
    ans.append(idx)
    idx -= memo[idx]
ans.append(1)
ans.reverse()
print(len(ans))
for i in ans:
    print(i, end = " ")
print()