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


# |S0| == |S1|
# No cycle, Union Find
from collections import defaultdict

n = int(input())
uf = UnionFind(2*n)
name_to_num = defaultdict(int)
idx = 0
recorded = set()

for _ in range(n):
    a, b = input().split()
    if a not in recorded:
        recorded.add(a)
        name_to_num[a] = idx
        idx += 1
    if b not in recorded:
        recorded.add(b)
        name_to_num[b] = idx
        idx += 1
        
    if uf.same(name_to_num[a], name_to_num[b]):
        exit(print("No"))
    uf.union(name_to_num[a], name_to_num[b])
    
print("Yes")