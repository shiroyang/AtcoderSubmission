N, K = map(int, input().split())
A = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(b)
    A.append(a-b)
A.sort(reverse=True)
print(sum(A[0:K]))