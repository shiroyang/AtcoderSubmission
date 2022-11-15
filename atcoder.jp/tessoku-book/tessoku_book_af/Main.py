n, a, b = map(int, input().split())
dp = [-1]*(n+1)
for i in range(a):
    dp[i] = 0
for i in range(a, n+1):
    sol1 = dp[i-a]^1
    sol2 = 0
    if i >= b:
        sol2 = dp[i-b]^1
    dp[i] = max(sol1, sol2)

if dp[-1]:
    print("First")
else:
    print("Second")
    