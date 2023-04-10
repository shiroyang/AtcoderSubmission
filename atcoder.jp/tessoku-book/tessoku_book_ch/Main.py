# imos法

CONS = 1500
imos = [[0]*(1+CONS) for _ in range(1+CONS)]

N = int(input())
for _ in range(N):
    a, b, c, d = map(int, input().split())
    imos[a][b] += 1
    imos[c][d] += 1
    imos[a][d] -= 1
    imos[c][b] -= 1

# update, which should loop for twice
# AND IT SHOULD START FROM THE VERY BEGINNING
for i in range(1, 1+CONS):
    for j in range(0, 1+CONS):
        imos[i][j] += imos[i-1][j]

for i in range(0, 1+CONS):
    for j in range(1, 1+CONS):
        imos[i][j] += imos[i][j-1]

cnt = 0
for li in imos:
    for num in li:
        if num > 0:
            cnt += 1
            
print(cnt)