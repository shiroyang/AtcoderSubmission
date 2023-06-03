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


if __name__ == '__main__':
    from math import sqrt
    n, d = map(int, input().split())
    covid = [False]*(n)

    def kyori(x1, y1, x2, y2):
        dx = x2-x1
        dy = y2-y1
        return sqrt(dx**2 + dy**2)

    A = [list(map(int, input().split())) for _ in range(n)]
    uf = UnionFind(n)

    for i in range(n-1):
        for j in range(i+1, n):
            x1, y1 = A[i]
            x2, y2 = A[j]
            if kyori(x1, y1, x2, y2) <= d:
                uf.union(i, j)

    for i in range(n):
        if uf.find(i) == uf.find(0):
            print("Yes")
        else:
            print("No")