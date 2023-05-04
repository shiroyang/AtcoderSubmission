N, Q = map(int, input().split())
A = list(map(int, input().split()))
shift = 0
ans = []

for _ in range(Q):
    t, x, y = map(int, input().split())
    x-=1; y-=1
    if t == 1:
        A[(x-shift)%N], A[(y-shift)%N] = A[(y-shift)%N], A[(x-shift)%N]
    elif t == 2:
       shift += 1
       shift %= N
    elif t == 3:
        ans.append(A[(x-shift)%N])

print(*ans, sep='\n')