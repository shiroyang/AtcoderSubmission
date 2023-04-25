# 全探索、もしxが当たりくじなら、全ての条件を満たすか
# もし条件を満たすやつが複数存在するとcan't solve
def is_ok(x):

    for i in range(len(ST)):
        s = ST[i][0]
        t = int(ST[i][1])
        if t == 1:
            if x == s: continue
            else: return False
        elif t == 2:
            cnt = 0
            for i in range(4):
                if s[i] == x[i]:
                    cnt += 1
            if cnt == 3: continue
            else: return False
        elif t == 3:
            cnt = 0
            for i in range(4):
                if s[i] == x[i]:
                    cnt += 1
            if cnt < 3: continue
            else: return False
            
    return True

N = int(input())
ST = [list(input().split()) for _ in range(N)]
ans = []

for i in range(10000):
    x = str(i)
    while len(x)< 4: 
        x = '0' + x
    if is_ok(x):
        ans.append(x)
        
if len(ans) == 1:
    print(*ans)
else:
    print("Can't Solve")