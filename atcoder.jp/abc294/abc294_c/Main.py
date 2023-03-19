n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans_a = []
ans_b = []
idx_a = 0
idx_b = 0
cnt = 0

for i in range(n+m):
    cnt += 1
    if idx_a == n:
        ans_b.append(cnt)
        idx_b += 1
    elif idx_b == m:
        ans_a.append(cnt)
        idx_a += 1
    else:
        if A[idx_a] <= B[idx_b]:
            ans_a.append(cnt)
            idx_a += 1
        else:
            ans_b.append(cnt)
            idx_b += 1

print(*ans_a)
print(*ans_b)