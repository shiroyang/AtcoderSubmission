H, W = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(H)]
RSUM = []
CSUM = []
B = [[0]*(W) for _ in range(H)]

for i in range(H):
    tmp = 0
    for j in range(W):
        tmp += A[i][j]
    RSUM.append(tmp)

for j in range(W):
    tmp = 0
    for i in range(H):
        tmp += A[i][j]
    CSUM.append(tmp)
    
for i in range(H):
    for j in range(W):
        B[i][j]  = RSUM[i] + CSUM[j] - A[i][j]
        
for li in B:
    print(*li)