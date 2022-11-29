from collections import deque

m = int(input())
pattern = [tuple(map(int, input().split())) for _ in range(m)]
n = int(input())
G = [tuple(map(int, input().split())) for _ in range(n)]
G = set(G)

relation = deque()
origin = pattern[0]
for ele in pattern:
    dx = ele[0] - origin[0]
    dy = ele[1] - origin[1]
    relation.append((dx, dy))
relation.popleft()

for ele in G:
    flag = True
    for rel in relation:
        dx, dy = rel[0], rel[1]
        x, y = ele[0]+rel[0], ele[1]+rel[1]
        if (x, y) not in G:
            flag = False
            break
    if flag:
        print(ele[0]-origin[0], ele[1]-origin[1])
    

    