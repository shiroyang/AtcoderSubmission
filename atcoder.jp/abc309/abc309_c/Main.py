from collections import defaultdict
n, k = map(int, input().split())

d = defaultdict(list)

A = [list(map(int, input().split())) for _ in range(n)]
cur = 0

for item in A:
    cur += item[1]
    d[item[0]].append(item[1])

dd = sorted(d.items(), key=lambda x:(x[0]))

days = 1
if cur <= k:
    exit(print(days))
    
for day, ls in dd:
    days = day+1
    for item in ls:
        cur -= item
        if cur <= k:
            exit(print(days))
