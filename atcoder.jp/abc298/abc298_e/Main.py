# satama6 様のコード写経
# dfs による確率問題, メモ化再帰
from collections import defaultdict
import sys
input = lambda: sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**6)
MOD = 998244353

n, a, b, p, q = map(int, input().split())

memo = defaultdict(int)

# 高橋、青木、手番
def dfs(a, b, t):
    if a == n: return 1
    elif b == n: return 0
    elif (a, b, t) in memo: return memo[(a, b, t)]
    
    res = 0
    
    # 高橋の手番
    if t:
        for i in range(1, p+1):
            na = min(n, a+i)
            res += dfs(na, b, 0)

        # res // p
        res = res * pow(p, MOD-2, MOD) % MOD

    else:
        for j in range(1, q+1):
            nb = min(n, b+j)
            res += dfs(a, nb, 1)
            
        # res // q
        res = res * pow(q, MOD-2, MOD) % MOD
        
    memo[(a, b, t)] = res
    return res

print(dfs(a, b, 1))