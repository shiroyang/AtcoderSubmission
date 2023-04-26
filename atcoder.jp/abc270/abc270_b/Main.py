x, y, z =map(int, input().split())

# 常に壁を正にしておく
if y < 0:
    x, y, z = -x, -y, -z

# 直接ゴールに行く
if x < y:
    exit(print(abs(x)))
    
else:
    if z > y:
        exit(print(-1))
    # ハンマーを拾う
    else:
        exit(print(abs(z) + abs(x-z)))