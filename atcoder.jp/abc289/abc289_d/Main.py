# dp

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
x = int(input())

dp = [0]*(x+1)
for item in B:
    dp[item] = -1
dp[0] = 1

for i in range(0, x):
    if dp[i] == 1:
        for item in A:
            if i + item <= x and dp[i+item] != -1:
                dp[i+item] = 1

print("Yes" if dp[-1] else "No")