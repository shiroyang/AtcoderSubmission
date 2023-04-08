# 考え方が少し難しいDP
# 0インデックスから考えると
# 奇数かいの時はx座標を＋ーA[i]移動でき
# 偶数回の時はy座標を＋ーA[i]移動できる
# 最後に(x, y)に届けばオッケー
# dpa[i][j]: vertical move, prev i, reaching coord j, doable or not

N, x, y = map(int, input().split())
x += 10000
y += 10000
L = list(map(int, input().split()))
A = []
B = []
for i in range(N):
    if i % 2 == 0:
        A.append(L[i])
    else:
        B.append(L[i])
        
# 座標がマイナスになるかもしれないので、真ん中に持ってくる、原点を10000にする
dpa = [[False]*(40040) for _ in range(len(A)+1)]
dpb = [[False]*(40040) for _ in range(len(B)+1)]

dpb[0][10000] = True
for i in range(len(B)):
    # 防止坐标越界并节约时间
    for j in range(B[i], 20001):
        dpb[i+1][j] = dpb[i][j-B[i]]| dpb[i][j+B[i]]            

dpa[1][10000+A[0]] = True
for i in range(1, len(A)):
    for j in range(A[i], 20001):
        dpa[i+1][j] = dpa[i][j-A[i]] | dpa[i][j+A[i]]

if dpa[-1][x] and dpb[-1][y]:
    print("Yes")
else:
    print("No")