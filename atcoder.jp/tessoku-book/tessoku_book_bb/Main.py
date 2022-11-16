from collections import defaultdict

d = defaultdict(str)
n = int(input())
for _ in range(n):
    s = input()
    if s[0] == '1':
        idx, name, score = s.split()
        d[name] = score
    if s[0] == '2':
        idx, name = s.split()
        print(d[name])