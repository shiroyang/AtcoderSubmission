h,w = map(int, input().split())
Mat = [[0]*(w+1) for i in range(h+1)]
Mat_Sum = [[0]*(w+1) for i in range(h+1)]

idx1 = 0
for i in range(h):
    idx1 += 1
    row_list = map(int, input().split())
    idx2 = 0
    for j in row_list:
        idx2 += 1
        Mat[idx1][idx2] = j

for i in range(1, h+1):
    for j in range(1, w+1):
        Mat[i][j] += Mat[i][j-1]

for j in range(1, w+1):
    for i in range(1, h+1):
        Mat[i][j]+= Mat[i-1][j]
q = int(input())
for i in range(q):
    a,b,c,d = map(int, input().split())
    ans = Mat[c][d] + Mat[a-1][b-1] - Mat[a-1][d] - Mat[c][b-1]
    print(ans)