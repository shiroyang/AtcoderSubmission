from collections import defaultdict, deque

n1, n2, m = map(int, input().split())
d1 = defaultdict(list)
d2 = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    if a <= n1 and b <= n1:
        d1[a].append(b)
        d1[b].append(a)
    else:
        a -= n1
        b -= n1
        d2[a].append(b)
        d2[b].append(a)

INF = 10**16
kyori1 = [INF]*(n1+1)
kyori2 = [INF]*(n2+1)

que = deque()
que.append(1)
kyori1[1] = 0

while que:
    v = que.popleft()
    for nv in d1[v]:
        if kyori1[nv] == INF:
            kyori1[nv] = kyori1[v] + 1
            que.append(nv)

que = deque()
que.append(n2)
kyori2[-1] = 0
while que:
    v = que.popleft()
    for nv in d2[v]:
        if kyori2[nv] == INF:
            kyori2[nv] = kyori2[v] + 1
            que.append(nv)


print(max(kyori1[1:]) + max(kyori2[1:])+1)