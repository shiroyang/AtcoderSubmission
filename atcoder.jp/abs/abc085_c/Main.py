n,y = map(int, input().split())
flag = False
for i in range(n+1):
    if flag:
        break
    for j in range(n-i+1):
        if flag:
            break
        k = n - i - j
        if 10000*i+5000*j+1000*k == y:
            print(f'{i} {j} {k}')
            flag = True
if not flag:
    print("-1 -1 -1")