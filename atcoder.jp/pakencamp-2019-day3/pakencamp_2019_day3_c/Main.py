n, m = map(int, input().split())
Mat = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(m-1):
    for j in range(i+1, m):
        tmp = 0 
        for k in range(n):
            tmp += max(Mat[k][i], Mat[k][j])
        ans = max(ans, tmp)
print(ans)