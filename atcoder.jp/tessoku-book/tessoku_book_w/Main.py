# 1D bit DP is easier to implement and comprehend
n ,m = map(int, input().split())
# 直接２進法に変換して、bit DPの準備をする
coupon = [int(''.join(input().split()), 2) for _ in range(m)]
INF = 10**16
dp = [INF]*(1<<n)
dp[0] = 0
for i in range(m):
    dp[coupon[i]] = 1
# Outer Iteration is for all the status
for i in range(1<<n):
    # Inner Iteration is for all the coupons, to use or not to use
    for j in range(m):
        # new status after using coupon j
        status = i | coupon[j]
        dp[status] = min(dp[status], dp[i]+1)
ans = dp[-1]
if ans == INF:
    print("-1")
else:
    print(ans)