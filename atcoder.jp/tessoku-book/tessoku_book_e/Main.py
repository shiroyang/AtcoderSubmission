n, k = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        a = k-i-j
        if a >= 1 and a <=n:
            cnt+=1
print(cnt)
