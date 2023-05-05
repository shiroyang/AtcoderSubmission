# RLE
from collections import defaultdict
def rle(s):
    d = defaultdict(int)
    n = len(s)
    l = 0
    while l < n:
        r  = l + 1
        while r < n and s[r] == s[l]:
            r += 1
        d[r-l] += 1
        l = r
    return d
    

def f(n):
    n -= 1
    a1 = 1
    an = n
    return (a1+an) *n // 2

N = int(input())
S = input()

ans = f(len(S))
d = rle(S)

for key, val in d.items():
    ans -= val * f(key)

print(ans)