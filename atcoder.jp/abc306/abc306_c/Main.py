from collections import defaultdict

N = int(input())
d = defaultdict(int)
ans = []
A = list(map(int, input().split()))
for l in A:
    d[l] += 1
    if d[l] == 2:
        ans.append(l)
print(*ans)