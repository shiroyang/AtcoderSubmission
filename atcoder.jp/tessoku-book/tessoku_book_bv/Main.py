# 列と行の転倒数の総和

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

R = []
C = []

def inversion_number(A):
    cnt = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[j] < A[i]:
                cnt += 1
    return cnt
    
for i in range(N):
    for j in range(N):
        if A[i][j] != 0:
            R.append(A[i][j])
            break

for j in range(N):
    for i in range(N):
        if A[i][j] != 0:
            C.append(A[i][j])
            break

ans = inversion_number(R) + inversion_number(C)
print(ans)