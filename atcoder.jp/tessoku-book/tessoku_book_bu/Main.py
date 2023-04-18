# Dijkstra Heap, ただし木の本数が多い分距離を減らす
# また誤差を減らすため、Decimalを使いたいが、TLEするので
# 距離を全て10000倍にして、木が生えてる道だけ1引く
# 四捨五入 (N+5*(10**k))//(10**(k+1))*(10**k)
# 例えば百の桁で四捨五入をするのなら、　+50, //100, *100

from heapq import heappush, heappop

INF = 10**18
bonus = 1
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
dis = [INF]*(N+1)
dis[1] = 0
kakutei = [False]*(N+1)

for _ in range(M):
    a, b, c, d = map(int, input().split())
    c *= 10**4
    G[a].append((c-d*bonus, b))
    G[b].append((c-d*bonus, a))
    
H = [(0, 1)]
while H:
    _, v = heappop(H)
    if kakutei[v]: continue
    kakutei[v] = True
    
    for w, nv in G[v]:
        if dis[nv] > dis[v] + w:
            dis[nv] = dis[v] + w
            heappush(H, (dis[nv], nv))

kyori = (dis[-1]+5000)//10000*10000
tree_num = abs(kyori-dis[-1])
kyori //= 10000
print(kyori, tree_num)