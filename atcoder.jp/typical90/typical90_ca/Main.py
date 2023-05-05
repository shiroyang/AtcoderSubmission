# 片端から愚直に処理

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

cnt = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == B[i][j]: continue
        delta = B[i][j] - A[i][j]
        if i+1 < H and j+1 < W:
            cnt += abs(delta)
            A[i][j] += delta
            A[i+1][j] += delta
            A[i][j+1] += delta
            A[i+1][j+1] += delta

is_ok = True
for i in range(H):
    if not is_ok: break
    for j in range(W):
        if A[i][j] != B[i][j]:
            is_ok = False
            break

if is_ok:
    print("Yes")
    print(cnt)
else:
    print("No")