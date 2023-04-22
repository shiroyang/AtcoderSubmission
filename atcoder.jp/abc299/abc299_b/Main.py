from collections import defaultdict
d = defaultdict(list)
n, t = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
for i in range(n):
    d[C[i]].append((R[i], i+1))

if d[t]:
    A = d[t]
    print(max(A)[1])
else:
    A = d[C[0]]
    print(max(A)[1])