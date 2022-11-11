n, m = map(int, input().split())
adj_lis = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj_lis[a-1].append(b)
    adj_lis[b-1].append(a)


for idx, arr in enumerate(adj_lis):
    print(len(arr), end=' ')
    print(*sorted(arr))
    