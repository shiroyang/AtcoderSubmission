n, k = map(int, input().split())
tup_arr = []
for i in range(n):
    a, b = map(int, input().split())
    tup_arr.append((a, b))
ans = 0
for i in range(1, 101):
    for j in range(1, 101):
        lower_bound = (i, j)
        tmp = 0
        for tup in tup_arr:
            l = tup[0]
            r = tup[1]
            if i<=l<=i+k and j<=r<=j+k:
                tmp += 1
        ans = max(ans, tmp)
print(ans)