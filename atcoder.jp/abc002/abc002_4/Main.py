## TLE WA?

from itertools import combinations

ans = 1
n, m  = map(int, input().split())
relation = [tuple(map(int, input().split())) for _ in range(m)]
ref = set(relation)

for num in range(1<<n):
    ppl = set()
    idx = 1
    while num!= 0:
        c = num & 1
        if c:
            ppl.add(idx)
        num >>= 1
        idx += 1
    ppl = list(ppl)
    flag = True
    for kumi in combinations(ppl, 2):
        x, y = kumi[0], kumi[1]
        if (x, y) not in ref and (y, x) not in ref:
            flag = False
            break
    if flag:
        ans = max(ans, len(ppl))

print(ans)