import sys
from functools import lru_cache
import time
sys.setrecursionlimit(10**8)

@lru_cache(maxsize=10**8)
def exchange(a, b, c):
    a, b, c = (b+c)/2, (a+c)/2, (a+b)/2
    return [a, b, c]

def check(a, b, c):
    if (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0):
        return True
    return False 

a ,b ,c = map(int, input().split())
cnt = 0
now = time.time()
while (time.time() - now <= 1):
    if not check(a, b, c):
        print(cnt)
        exit()
    else:
        a, b, c = exchange(a, b, c)
        cnt += 1

print("-1")
        