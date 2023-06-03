import sys
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[px] = py
                if self.rank[px] == self.rank[py]:
                    self.rank[py] += 1

N, M = map(int, input().split())
dsu = DSU(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    dsu.union(u, v)

K = int(input())
restrictions = [tuple(map(int, input().split())) for _ in range(K)]
restricted_pairs = set((dsu.find(x), dsu.find(y)) for x, y in restrictions)

Q = int(input())
for _ in range(Q):
    p, q = map(int, input().split())
    u, v = dsu.find(p), dsu.find(q)
    if (u, v) in restricted_pairs or (v, u) in restricted_pairs:
        print('No')
    else:
        print('Yes')