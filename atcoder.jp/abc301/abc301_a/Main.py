from collections import defaultdict
n = int(input())
s = input()
d = defaultdict(int)
for item in s:
    d[item] += 1
    if d[item] >= n//2:
        print(item)
        exit()