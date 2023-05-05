# bisect

N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]

l = 0
r = 10**9

def is_ok(x):
    cnt = 0
    cur = 0
    for i in range(len(A)):
        if A[i] - cur >= x:
            cur = A[i]
            cnt += 1
    if cnt > K:
        return True
    else:
        return False

while r - l > 1:
    mid = (r+l)//2
    if is_ok(mid):
        l = mid
    else:
        r = mid
        
print(l)