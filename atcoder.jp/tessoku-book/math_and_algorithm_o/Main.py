from functools import lru_cache
import sys
sys.setrecursionlimit(10**8)

@lru_cache(maxsize= 10**8)
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        print(a)
        return a
    else:
        tmp = a % b
        gcd(b, tmp)


a, b = map(int, input().split())
gcd(a, b)