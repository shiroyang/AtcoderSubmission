from collections import defaultdict, deque

ans = deque()
d = defaultdict(set)
n, q = map(int, input().split())
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if b not in d[a]:
            d[a].add(b)
    if t == 2:
        if b in d[a]:
            d[a].remove(b)
    if t == 3:
        if b in d[a] and a in d[b]:
            ans.append("Yes")
        else:
            ans.append("No")
while len(ans) > 0:
    print(ans.popleft())