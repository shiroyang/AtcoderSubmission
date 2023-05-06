# Union Find
# 如果周围也有红色的格子，就相连

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
    
    def to1dim(x, y):
        return W*x+y
    
    H, W = map(int, input().split())
    uf = UnionFind(H*W)
    col = [[0]*(W) for _ in range(H)]
    dirc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    Q = int(input())
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            _, r, c = q
            r-=1; c-=1
            col[r][c] = 1
            for dx, dy in dirc:
                nx = r + dx
                ny = c + dy
                if 0 <= nx < H and 0 <= ny < W:
                    if col[nx][ny] == 1:
                        uf.union(to1dim(r,c), to1dim(nx, ny))
                        
        if q[0] == 2:
            _, ra, ca, rb, cb = q
            ra-=1; ca-=1; rb-=1; cb-=1
            if col[ra][ca] == 0 or col[rb][cb] == 0:
                print("No")
                continue
            if uf.same(to1dim(ra,ca), to1dim(rb,cb)):
                print("Yes") 
            else: print("No")

            
if __name__ == '__main__':
    main()