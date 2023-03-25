from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for item in A:
    d[item] += 1

ans = 0
for key, val in d.items():
    ans += val // 2
print(ans)