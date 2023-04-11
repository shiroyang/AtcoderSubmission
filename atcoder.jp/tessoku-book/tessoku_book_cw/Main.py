# Box in box の最大個数
# First, we have to sort x, then if we pick up the boxes from left to right
# Each box with at least satisfy xi < xj
# Then we have to calculate the LIS from y

# LIS O(n^2)
# dp[i][j]: using prev i, last used j(index) and it should be smaller than i, longest length
# ans = max(dp[-1])
# 貰うDP

# LIS 改善版
# 二分探索!!
# listでLISの数字を管理する
# もしbisect_leftが最後尾だったら、listにアペンドする
# それ以外の時は、その添え字と交換する、すなわち前に選んで数字を改ざんできる
from bisect import bisect_left

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]

A.sort(key=lambda x: (x[0], -x[1])) 
ls = [A[i][1] for i in range(N)]

dp = []

# Initialize
for item in ls:
    idx = bisect_left(dp, item)
    if idx == len(dp):
        dp.append(item)
    else:
        dp[idx] = item

ans = len(dp)
print(ans)