n, p, q, r, s = map(lambda x: int(x) - 1, input().split())
A = list(input().split())
ans = A[:p] + A[r:s+1] + A[q+1:r] + A[p:q+1] + A[s+1:]
print(*ans)