from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
dp = []

for item in arr:
    i = bisect_left(dp, item)
    if i == len(dp):
        dp.append(item)
    else:
        dp[i] = item
print(len(dp))