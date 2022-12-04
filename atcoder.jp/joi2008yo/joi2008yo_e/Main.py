from copy import deepcopy
h, w = map(int, input().split())
Mat = [list(map(int, input().split())) for _ in range(h)]
ans = 0

for i in range(1<<h):
    # flip the row 
    num = i
    idx = 0
    arr = deepcopy(Mat)
    while num > 0:
        bit = num & 1
        if  bit:
            for j in range(w):
                arr[idx][j] ^= 1
        idx += 1
        num >>= 1
    # trial on column   
    cnt = 0    
    for q in range(w):
        tmp = 0
        for p in range(h):
            tmp += arr[p][q]
        cnt += max(tmp, h-tmp)
    ans = max(ans, cnt)
    
print(ans)