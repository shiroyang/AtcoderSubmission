# G is adjacency list
# ans means all possbile simple paths
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline()[:-1]

def dfs(x):
    global ans
    if ans == lim:
        return ans

    vis[x] = True
    path.append(x)
    ans += 1
    
    for nx in g[x]:
        if not vis[nx]:
            dfs(nx)
            
    # backtrack, reset the visited node and pop the path
    vis[x] = False
    path.pop()
    

n, m  = map(int, input().split())
g = [[] for _ in range(n+1)]
vis = [False]*(n+1)
lim = 10**6 
path = []
ans = 0

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

dfs(1)
print(ans)