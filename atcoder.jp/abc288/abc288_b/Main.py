from collections import defaultdict
d = list()


n, k = map(int, input().split())
for _ in range(k):
    s = input()
    d.append(s)
for _ in range(n-k):
    a = input()


sorted_set = sorted(d)
for i in range(k):
    print(sorted_set[i])