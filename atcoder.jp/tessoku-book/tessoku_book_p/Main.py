n = int(input())
INF = 10**8
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [0]
dp.append(a[0])

for i in range(n-2):
    dp.append(min(dp[i+1]+a[i+1], dp[i]+b[i]))
    
print(dp[-1])