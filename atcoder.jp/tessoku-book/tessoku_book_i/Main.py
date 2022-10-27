h, w, n = map(int, input().split())
Mat = [[0]*(w+2) for _ in range(h+2)]

for i in range(n):
    a, b, c, d = map(int, input().split())
    Mat[a][b] += 1
    Mat[c+1][d+1] += 1
    Mat[a][d+1] -= 1
    Mat[c+1][b] -= 1

for i in range(1, h+1):
    for j in range(1, w+1):
        Mat[i][j] += Mat[i][j-1]

for j in range(1, w+1):
    for i in range(1, h+1):
        Mat[i][j] += Mat[i-1][j]

for i in range(1, h+1):
    for j in range(1, w+1):
        print(Mat[i][j], end=' ')
    print()