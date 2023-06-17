A = list(map(int, input().split()))
ans = 0
for i in range(64):
    bit = 2**i
    ans += bit*A[i]
print(ans)