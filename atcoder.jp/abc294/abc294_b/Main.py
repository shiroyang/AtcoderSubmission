h, w = map(int, input().split())
Mat = [list(map(int, input().split())) for _ in range(h)]
Ans = [[] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if Mat[i][j] == 0:
            Ans[i].append('.')
        else:
            Ans[i].append(chr(Mat[i][j]+64))
for li in Ans:
    for ele in li:
        print(ele, end='')
    print()
        