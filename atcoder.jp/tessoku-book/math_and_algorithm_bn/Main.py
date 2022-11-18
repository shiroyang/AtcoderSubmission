n = int(input())
tup_arr = []
for i in range(n):
    l ,r = map(int, input().split())
    tup_arr.append((l ,r))
tup_arr = sorted(tup_arr, key=lambda x: x[1])
now = 0
ans = 0
for tup in tup_arr:
    if now <= tup[0]:
        now = tup[1]
        ans += 1
        
print(ans)