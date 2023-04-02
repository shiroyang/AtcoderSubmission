# MEX
n, k = map(int, input().split())
A = list(map(int, input().split()))
A = set(A)

idx = 0
while idx < k:
    if idx not in A:
        exit(print(idx))
    idx += 1
print(idx)