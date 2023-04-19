# 二分探索、X巻まで読めるか
N = int(input())
A = set(map(int, input().split()))

# x冊まで集めれるか
def is_ok(x):
    c = len(set(range(1, x+1)) & A)
    if c + (N-c)//2 >= x:
        return True
    else:
        return False
    
l = 0
r = N+1
while r - l > 1:
    mid = (r+l) // 2
    if is_ok(mid):
        l = mid
    else:
        r = mid

print(l)