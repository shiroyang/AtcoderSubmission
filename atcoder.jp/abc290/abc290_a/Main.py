n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

for item in B:
    ans += A[item]
print(ans)