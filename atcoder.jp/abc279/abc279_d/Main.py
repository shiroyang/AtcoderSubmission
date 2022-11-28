# 凸関数の極値を求めるときに三分探索を使う
from math import sqrt, floor, ceil

def f(x):
    t = x*b+ a/(sqrt(1+x))
    return t

a, b = map(int, input().split())
l, r = 0, 10**18
c1, c2 = 0, 0

while l+pow(10, -1) < r:
    delta = (r-l)/3
    c1 = l + delta
    c2 = r - delta

    if f(c1) < f(c2):
        r = c2
    else:
        l = c1

print(min(f(floor(c1)), f(ceil(c2))))