from decimal import Decimal
from collections import defaultdict
N = int(input())
calc = lambda x, y: Decimal (Decimal(x)/ Decimal(x+y))
d = defaultdict()

for i in range(N):
    a, b = map(int, input().split())
    d[i+1] = calc(a, b)


A = sorted(d.items(), key=lambda x:(-x[1], x[0]))


for item in A:
    print(item[0], end=' ')
print()