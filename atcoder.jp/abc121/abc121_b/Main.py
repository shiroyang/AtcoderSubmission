n, m ,c = map(int, input().split())
b = list(map(int, input().split()))
a = []
cnt = 0
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    sigma = c
    for j in range(m):
        sigma += a[i][j] * b[j]
    if sigma > 0:
        cnt += 1
        
print(cnt)