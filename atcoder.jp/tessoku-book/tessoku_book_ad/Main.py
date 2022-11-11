#　割り算の時だけフェルマーの小定理を使う
from math import factorial
mo = lambda x: x % 1000000007

n, r = map(int, input().split())
ref = {}
ref[0] = 1
ref[1] = 1
for i in range(2, n+1):
    ref[i] = mo(ref[i-1]*i)
bunbo = mo(ref[r]*ref[n-r])
print(ref[n]* pow(bunbo, 1000000007-2, 1000000007) % 1000000007)