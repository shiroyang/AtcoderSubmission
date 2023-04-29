# BF
H, W = map(int, input().split())
A = [list(input().split()) for _ in range(H)]
B = [list(input().split()) for _ in range(H)]

for i in range(H):
    T = []
    T = A[i:] + A[:i]
    for j in range(W):
        TT = []
        for li in T:
            TT.append(li[0][j:] + li[0][:j])
        is_ok = True
        for i in range(H):
            if TT[i] != (B[i][0]):
                is_ok = False
        if is_ok:
            exit(print("Yes"))

print("No")