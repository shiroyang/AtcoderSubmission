from copy import deepcopy as dc
N = int(input())
A = [[0]*(N) for _ in range(N)]

for i in range(N):
    s = input()
    for j in range(N):
        A[i][j] = int(s[j])

B = dc(A)

for i in range(N):
    for j in range(N):
        if i == 0 and j != N-1:
            B[0][j+1] = A[0][j]
        elif j == N-1 and i != N-1:
            B[i+1][N-1] = A[i][N-1]
        elif i == N-1 and j != 0:
            B[N-1][j-1] = A[N-1][j]
        elif j == 0 and i != 0:
            B[i-1][0] = A[i][0]

for li in B:
    print(*li, sep='')