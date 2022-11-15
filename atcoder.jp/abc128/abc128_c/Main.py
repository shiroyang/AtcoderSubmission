from collections import defaultdict
# d is light -> switch
# d_rev is switch -> light

d = defaultdict(list)
d_rev = defaultdict(set)
n, m = map(int, input().split())
for i in range(m):
    tmp = list(map(int, input().split()))
    for j in range(1, len(tmp)):
        d[i].append(tmp[j])
        d_rev[tmp[j]-1].add(i)
ref_arr = list(map(int, input().split()))
ans = 0

for i in range(1<<n):
    trial = [0]*m
    idx = 0
    tmp = i
    while tmp != 0:
        bit = tmp & 1
        tmp = tmp >> 1
        if bit:
            for element in d_rev[idx]:
                trial[element] ^= 1
        idx += 1
    if trial == ref_arr:
        ans += 1
print(ans)