# upsolve
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

# Transpose + Reverse = Rotate 90 Deg
def rot(A):
    A = list(map(list, zip(*A[::-1])))
    return A

ans = False
for k in range(4):
    ok = True
    for i in range(N):
        for j in range(N):
            if A[i][j]:
                ok &= B[i][j]
    ans |= ok
    A = rot(A)
    
print("Yes" if ans else "No")