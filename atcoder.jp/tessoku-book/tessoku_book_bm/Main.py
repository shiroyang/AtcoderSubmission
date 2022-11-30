from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
d = defaultdict(list)
dp = [0]*(n+1)

# 上司→部下の順番で追加する
for idx, num in enumerate(arr, 2):
    d[num].append(idx)
    
for i in reversed(range(1, n+1)):
    for buka in d[i]:
        dp[i] += dp[buka] + 1
        
for i in range(1, len(dp)):
    print(dp[i], end=' ')
print()