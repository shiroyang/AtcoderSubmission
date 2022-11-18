from collections import defaultdict
from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(2, n+1)]
d = defaultdict(set)

for i in range(m):
    u ,v = map(int, input().split())
    d[u].add(v)
    d[v].add(u)
    
ans = 0
for idx, arrangement in enumerate(permutations(arr)):
    flag = True
    arrangement = list(arrangement)
    arrangement.insert(0, 1)
    for j in range(len(arrangement)-1):
        if arrangement[j+1] in d[arrangement[j]]:
            pass
        else:
            flag = False
            break
    if flag:
        ans += 1

print(ans)