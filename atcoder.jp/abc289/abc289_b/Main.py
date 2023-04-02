n, m = map(int, input().split())
A = set(map(int, input().split()))

ans = []
l = 1
while l <= n:
    r = l
    while r in A:
        r += 1
    for k in range(r, l-1, -1):
        ans.append(k)
    l = r+1

print(*ans)