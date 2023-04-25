# 二分探索でボーダーを探す

N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 1
r = 10**9

def is_ok(x):
    cnt = 0
    for item in A:
        cnt += item // x
    if cnt >= K:
        return True
    else:
        return False
    
while r-l > 1e-6:
    mid = (l+r) / 2
    if is_ok(mid):
        l = mid
    else:
        r = mid

for item in A:
    print(int(item // l), end=' ')
print()