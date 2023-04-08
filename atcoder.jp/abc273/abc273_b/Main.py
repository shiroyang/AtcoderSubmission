# BF
# round 10^i
# floor((x + 5*10^i)/10^(i+1))*10^(i+1)
from math import floor

def f(x, i):
    l = 10 ** i
    h = 10 ** (i+1)
    return floor((x + 5*l)/h) * h

x, k = map(int, input().split())
ans = x
for i in range(k):
    ans = f(ans, i)
print(ans)