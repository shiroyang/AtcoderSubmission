from math import ceil
def is_ok(x):
    b = []
    for item in arr:
        cur, speed = item
        t = ceil((x-cur)/speed)
        b.append(t)
    b.sort()
    for idx, num in enumerate(b, 1):
        if  idx > num:
            return False
    return True

n = int(input())
arr = []
for _ in range(n):
    h, s = map(int, input().split())
    arr.append((h, s))
arr.sort()

l = 1
r = 10**16

while r-l > 1:
    mid = (l+r)//2
    if is_ok(mid):
        r = mid
    else:
        l = mid

print(l)