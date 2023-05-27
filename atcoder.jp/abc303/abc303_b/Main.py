N, M = map(int, input().split())
is_ok = [[False]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    is_ok[i][i] = True

for i in range(M):
    A = list(map(int, input().split()))
    for j in range(len(A)-1):
        is_ok[A[j]][A[j+1]] = True
        is_ok[A[j+1]][A[j]] = True

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if not is_ok[i][j]:
            cnt += 1

print(cnt//2)