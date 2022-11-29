n = int(input())
A, B = [], []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 10 ** 16
for i in A:
    for j in B:
        l, r = i, j
        tmp = 0
        for k in range(len(A)):
            m = A[k]
            n = B[k]
            tmp += abs(m-l)+abs(m-n)+abs(r-n)
        ans = min(ans, tmp)
print(ans)