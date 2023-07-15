n, p, q = map(int,input().split())
A = list(map(int, input().split()))

ans = p
for item in A:
    if item + q < ans:
        ans = item + q
print(ans)