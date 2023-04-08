from collections import defaultdict

def rec(x):
    if x == 0:
        return 1
    else:
        if d[x]:
            return d[x]
        else:
            d[x] = rec(x//2) + rec(x//3) # type: ignore
            return d[x]

N = int(input())
d = defaultdict(int)
print(rec(N))