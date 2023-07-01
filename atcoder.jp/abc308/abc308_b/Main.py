from collections import defaultdict

N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))
d = defaultdict(int)

for i in range(len(D)):
    d[D[i]] = P[i+1]

tmp = P[0]
ans = 0

for item in C:
    if d.get(item) == None:
        ans += tmp
    else:
        ans += d.get(item)
        
print(ans)