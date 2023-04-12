# Only have to record the row that being switched

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Perm = [i for i in range(N)]
ans = []

Q = int(input())
for _ in range(Q):
    idx, x, y = map(int, input().split())
    x-= 1; y-= 1
    if idx == 1:
        Perm[x], Perm[y] = Perm[y], Perm[x]
    elif idx == 2:
        ans.append(A[Perm[x]][y])

for item in ans:
    print(item)