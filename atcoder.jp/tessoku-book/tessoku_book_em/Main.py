# Union Find, erase the edge!
# ただし、UnionFindでは辺を消すことができないので、逆に考えて、
# 辺を徐々に追加する！
# また最後まで運休しない路線があるので、そこはあらかじめ接続しておく

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    

def main():
    N, M = map(int, input().split())
    E = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
    q = int(input())
    Q = [list(map(lambda x: int(x)-1, input().split())) for _ in range(q)] 
    ans = []

    Ini = [True]*(M)
    for li in Q:
        if li[0] == 0:
            Ini[li[1]] = False
            
    uf = UnionFind(N)
    for i in range(M):
        if Ini[i]:
            a, b = E[i]
            uf.union(a, b)
    
    # reverse the query and solve        
    Q = Q[::-1]
    for i in range(q):
        li = Q[i]
        if li[0] == 0:
            idx = li[1]
            a, b = E[idx]
            uf.union(a, b)
        elif li[0] == 1:
            _, a, b = li
            if uf.same(a, b):
                ans.append("Yes")
            else:
                ans.append("No")
    
    ans = ans[::-1]
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()