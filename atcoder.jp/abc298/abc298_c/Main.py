from collections import defaultdict

N = int(input())
Q = int(input())
A = [[] for _ in range(N+1)]
d = defaultdict(list)
dr = defaultdict(list)

for _ in range(Q):
    li = list(map(int, input().split()))
    if li[0] == 1:
        i, j = li[1], li[2]
        d[j].append(i)
        dr[i].append(j)
        
    elif li[0] == 2:
        j = li[1]
        d[j].sort()
        print(*d[j])
    elif li[0] == 3:
        i = li[1]
        dr[i].sort()
        print(*set(dr[i]))
    