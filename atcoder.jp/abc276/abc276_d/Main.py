from math import gcd

N = int(input())
A = list(map(int, input().split()))

g = A[0]
for i in range(N):
    g = gcd(g, A[i])

cnt = 0
for item in A:
    tmp = item // g
    while tmp % 2 == 0:
        tmp //= 2
        cnt += 1
    while tmp % 3 == 0:
        tmp //= 3
        cnt += 1
    if tmp != 1:
        exit(print(-1))

print(cnt)