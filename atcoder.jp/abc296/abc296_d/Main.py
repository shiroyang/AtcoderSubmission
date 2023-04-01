from math import sqrt, ceil

n, m = map(int, input().split())
INF = 10**16
X = INF

for a in range(1, ceil(sqrt(m))+1):
    if a > n:
        break
    b = ceil(m/a)
    if b <= n:
        tmp = a*b
        if X > tmp:
            X = tmp
print(X if X != INF else "-1")