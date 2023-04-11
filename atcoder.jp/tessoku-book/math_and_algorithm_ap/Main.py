MOD = 10**9+7

dp = [1, 1]
n = int(input())
if n == 1 or n == 2:
    exit(print(1))
    
for i in range(n-2):
    dp.append((dp[-1]+dp[-2])%MOD)
print(dp[-1])