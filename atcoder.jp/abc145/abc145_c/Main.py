from itertools import permutations
from math import sqrt
from math import factorial

def dist(cor1, cor2):
    x1 = cor1[0]
    y1 = cor1[1]
    x2 = cor2[0]
    y2 = cor2[1]
    kyori = sqrt((x2-x1)**2 + (y2-y1)**2)
    return kyori

n = int(input())
li = [i for i in range(n)]

cor = []

for _ in range(n):
    x, y = map(int, input().split())
    cor.append((x, y))

ans = 0
for arragement in permutations(li):
    for i in range(len(arragement)-1):
        ans += dist(cor[arragement[i]], cor[arragement[i+1]])
print(ans/factorial(n))
        