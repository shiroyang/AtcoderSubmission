# bit全探索

def is_ok(li):
    t = set()
    for idx, num in enumerate(li):
        if num:
            t = t | Mat[idx]
    if len(t) == n:
        return 1
    else:
        return 0


n, m = map(int, input().split())
Mat = []

for _ in range(m):
    c = int(input())
    Mat.append(set(map(int, input().split())))
    
cnt = 0    
for i in range(1<<m):
    tmp = i
    li = []
    for j in range(m):
        li.append(tmp&1)
        tmp >>= 1
    li = li[::-1]
    cnt += is_ok(li)
    
print(cnt)