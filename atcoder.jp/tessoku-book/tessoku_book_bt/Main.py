# Tile Painting
# 塗る順番は関係ないので、小さいHを全列挙して、Wは貪欲法で残り分を塗ります、そこで黒ますの数カウントする
from copy import deepcopy as dc
H, W, K = map(int, input().split())
A = [list(input()) for _ in range(H)]
wht_cnt = 10**16

for i in range(1<<H):
    tmp = []
    for j in range(H):
        if (i >>j) & 1:
            tmp.append(j)

    T = dc(A)
    if len(tmp) > K: continue
    
    for item in tmp:
        for j in range(W):
            T[item][j] = '#'
    
    li = []
    for q in range(W):
        c = 0
        for p in range(H):
            if T[p][q] == '.':
                c += 1
        li.append(c)
    li.sort()
    for p in range(K-len(tmp)):
        li.pop()
    
    wht_cnt = min(wht_cnt, sum(li))

print(H*W - wht_cnt)