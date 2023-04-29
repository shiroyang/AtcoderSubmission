# memo DP
# dp[i]: curren at i, the prob of reaching N
# dp[i] = 1/5(dp[2*i]+dp[3*i]+dp[4*i]+dp[5*i]+dp[6*i])
from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)
MOD = 998244353 
inv5 = pow(5, MOD-2, MOD)

N = int(input())

@lru_cache(10**6)
def rec(x):
    if x == N:
        return 1
    elif x > N:
        return 0
    tmp = 0
    for k in range(2, 7):
        tmp += rec(k*x)
    tmp = tmp * inv5 % MOD
    return tmp
    
print(rec(1))