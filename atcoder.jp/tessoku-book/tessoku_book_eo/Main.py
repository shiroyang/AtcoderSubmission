# Network Flow But hard!
# Min Cut, Min Cost should calculate from max benefit, and it should be positive
# Dinic's algorithm
# Aを選んだらBも選ぶ : A->B に無限大のフローを流す
# 利益最大化: 特急にしないコストと特急にするコストの最小化
# 利益が負の場合: 直接特急にするコストとして i->T に流す
# 利益が正の場合: 特急にするコストが負になるので、相対的に、特急にしないコストに持っていく、その分offsetも発生する
# Node [0, N-1], S:[N], T:[N+1]

from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0 # type: ignore
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow
    
def main():
    INF  = 10**16
    N, M = map(int, input().split())
    nf = Dinic(N+2)
    P = list(map(int, input().split()))
    
    # Min Cost Flow
    offset = 0
    for i in range(N):
        if P[i] < 0:
            nf.add_edge(i, N+1, -P[i])
        elif P[i] > 0:
            offset += P[i]
            nf.add_edge(N, i, P[i])            
                        
    # Restrictions
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        nf.add_edge(a, b, INF)
    
    max_profit = offset - nf.flow(N, N+1)
    print(max_profit)

if __name__ == '__main__':
    main()