# Make Bipartite
# 在检查的时候要防止回流,也就是除了父节点可以同色以外，颜色必须是取反的
# 要用par数组记录每个节点的父节点
# 可能还有没上色的点，所以方法数有 N(N-1)/2, 再减去红色不能连的点和蓝色不能连的点和现在已经有的边数
# 也就是 R(R-1)/2, B(B-1)/2
# また、連結成分が一つではない可能性もある

# toam 様のコード写経
# seen が-1の時は訪問してない、０か1で色分け
# 連結成分が複数あるかもしれないので、一度全てのVを回して、seen[i]が-1の時だけスタックでDFS


n, m = map(int, input().split())
G = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)
    
seen = [-1]*(n)
ans = n*(n-1)//2 - m
res = 0

for i in range(n):
    if seen[i] != -1:
        continue
    c0 = 0
    c1 = 0
    seen[i] = 0
    todo = [i]
    while todo:
        v = todo.pop()
        if seen[v] == 0:
            c0 += 1
        else:
            c1 += 1
        for nv in G[v]:
            if seen[nv] == -1:
                seen[nv] = seen[v] ^ 1
                todo.append(nv)
            elif seen[nv] != seen[v]^1:
                exit(print(0))
    ans = ans - c0*(c0-1)// 2 - c1*(c1-1)//2

print(ans)