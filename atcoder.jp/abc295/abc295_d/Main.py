# dp[i]: 先頭からi文字目にxが出現した回数MOD2
# if dp[i] == dp[j], s[i, j-1] satisfies
# use dic to record the same array
from collections import defaultdict

def bi_to_dec(ls):
    keta = 1
    dec = 0
    for item in ls:
        dec += item * keta
        keta *= 2
    return dec

def calc(x):
    if x == 1:
        return 0
    else:
        return (x-1)*(x)//2

s = input()
ls = [0]*10
d = defaultdict(int)
d[bi_to_dec(ls)] += 1

for letter in s:
    ls[int(letter)] ^= 1
    d[bi_to_dec(ls)] += 1

ans = 0
# d = sorted(d.items(), key= lambda x: (x[1], -x[0]), reverse=True)
for key, val in d.items():
    ans += calc(val)
print(ans)