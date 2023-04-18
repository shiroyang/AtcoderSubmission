# Yokan Party!
# 切る長さを二分探索で求めて、貪欲できる

N, L = map(int, input().split())
K = int(input()) + 1
A = [0] + list(map(int, input().split())) + [L]

l = 0
r = 10**16

def is_ok(x):
    cnt = 0
    prev = 0
    for item in A:
        cur = item
        if cur - prev >= x:
            cnt += 1
            prev = cur
        if cnt >= K:
            return True
    return False

while r-l > 1:
    mid = (r+l)//2
    if is_ok(mid):
        l = mid
    else:
        r = mid
        
print(l)