#　没出界的情况下无限制衍生
H, W = map(int, input().split())
A = [input() for _ in range(H)]
ans = [0]*(min(H, W)+1)

is_legal = lambda p: 0 <=p[0]<H and 0<=p[1]<W

def search(i, j):
    size = 0
    lui, luj = i, j
    rui, ruj = i, j
    ldi, ldj = i, j
    rdi, rdj = i, j
    while True:
        lui -= 1; luj +=1
        rui += 1; ruj += 1
        ldi -= 1; ldj += 1
        rdi += 1; rdj -= 1
        lu = (lui, luj)
        ru = (rui, ruj)
        ld = (ldi, ldj)
        rd = (rdi, rdj)
        
        if is_legal(lu) and is_legal(ru) and is_legal(ld) and is_legal(rd):
            if A[lu[0]][lu[1]] == '#' and  A[ru[0]][ru[1]] == '#' and A[ld[0]][ld[1]] == '#' and A[rd[0]][rd[1]] == '#':
                size += 1
            else:
                break
        else:
            break
        
    return size

for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            size = search(i, j)
            if size >= 1:
                ans[size] += 1
                
print(*ans[1:])