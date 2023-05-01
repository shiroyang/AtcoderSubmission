# 木のDP
# dp[v][c]:頂点vを根とする部分木を塗る時、頂点vをc色に塗る時の数
# dp[v][white] = souseki(dp[u][white] + dp[u][black])
# dp[v][black] = souseki(dp[u][white])
# DFSの帰り順で塗って行く（小さい方から塗る）
import sys
sys.setrecursionlimit(10**6)
MOD = 10**9+7

N = int(input())
G = [[] for _ in range(N+1)]
dp = [[0]*(2) for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
def dfs(v, par):
    dp[v][0] = 1
    dp[v][1] = 1
    for nv in G[v]:
        if nv == par: continue
        dfs(nv, v)
        dp[v][0] = dp[v][0] * ((dp[nv][0]+dp[nv][1])%MOD) % MOD 
        dp[v][1] = dp[v][1] * (dp[nv][0]) % MOD
    
dfs(1, -1)
print((dp[1][0] + dp[1][1])%MOD)