# Union Find
class UnionFind:
    # 1-indexed 
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)
    
    # find the root using path compression
    def find_root(self, x):
        if x == self.parent[x]:
            return x
        while self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])  # type: ignore
            return self.parent[x]
                
    def is_same(self, x, y):
        return self.find_root(x) == self.find_root(y)
    
    def merge(self, x, y):
        root_x = self.find_root(x)
        root_y = self.find_root(y)
        if root_x == root_y:
            return
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x  # type: ignore
        self.size[root_x] += self.size[root_y]


def main():
    from collections import deque
    ans = deque()
    n, q = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(q):
        a, b, c = map(int, input().split())
        if a == 1:
            uf.merge(b, c)
        elif a == 2:
            ans.append("Yes") if uf.is_same(b, c) else ans.append("No")
    
    while len(ans) > 0:
        print(ans.popleft())        
    

main()