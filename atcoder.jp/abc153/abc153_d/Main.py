from functools import lru_cache
import sys
sys.setrecursionlimit(10**8)

cnt = 0

@lru_cache(maxsize=10**8)
def dfs(x):
    if x == 1:
        return 1
    else:
        return 2*dfs(x//2) + 1


    
x = int(input())
print(dfs(x))

