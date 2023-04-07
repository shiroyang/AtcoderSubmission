# Maximum Consecutive Sum
# sort＋累積和
# toam様の写経

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))

sm = sum(a)
# 一周できるようにする
a += a
ans = 10**18
# 累積和を求める
cum = [0]
for i in a:
    cum.append(cum[-1]+i)
    
R = 0
for L in range(n):
    R = max(L, R)
    # 不能绕过一圈
    while R - L < n-1 and (a[R+1]-a[R])%m <= 1:
        R += 1
    ans = min(ans, sm-(cum[R+1]-cum[L]))

print(ans)