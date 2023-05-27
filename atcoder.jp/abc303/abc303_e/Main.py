from collections import defaultdict, OrderedDict

d = defaultdict(int)
dd = defaultdict(int)
N = int(input())
for _ in range(N-1):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1
    
for key, val in d.items():
    dd[val] += 1
    
A = OrderedDict(sorted(dd.items(), key=lambda x:-x[0]))
ans = []

for key, val in A.items():
    if key <= 1: continue
    while dd[key] >= 1:
        ans.append(key)
        dd[key] -= 1
        dd[1] -= (key-1)
        dd[2] -= 2
        dd[1] += 1
    
print(*reversed(ans))