# 合計10**4以内で終わるので、BF

N = int(input())
A, B, C = map(int, input().split())

ans = 10**16
for i in range(10**4):
    for j in range(10**4):
        tmp = A*i + B*j
        if tmp > N: break
        if (N-tmp) % C != 0: continue
        cnum = (N-tmp) // C
        num = i + j + cnum
        if ans > num:
            ans = num
            
print(ans)