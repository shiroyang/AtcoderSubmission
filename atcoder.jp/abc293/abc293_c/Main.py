# 2^(h+w-2)に対しbit全探索, 1が丁度h-1の数列を取り出す
# 0 going down, 1 going right

h, w = map(int, input().split())
Mat = [list(map(int ,input().split())) for _ in range(h)]

ans = 0

for i in range(1<<(h+w-2)):
    tmp = i
    arr = []
    for j in range(h+w-2):
        arr.append(tmp & 1)
        tmp >>= 1
    arr = arr[::-1]

    if arr.count(0) == h-1:
        x, y = 0, 0
        ref = set()
        ref.add(Mat[0][0])
        flag = True
        for item in arr:
            if item:
                y += 1
            else:
                x += 1
            if Mat[x][y] not in ref:
                ref.add(Mat[x][y])
            else:
                flag = False
                break
        if flag:
            ans += 1
            
print(ans)