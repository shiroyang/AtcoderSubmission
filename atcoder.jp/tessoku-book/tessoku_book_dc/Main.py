# 数え上げ
# (1, 1) -> (H, W)
# 割り算があるのでフェルマーの小定理を使う
# {//b} => {*pow(b, MOD-2, MOD)}
MOD = 10**9+7

h, w = map(int, input().split())
# (H+W-2) までの表を作る
table = [0]*(h+w)
table[0] = 1
table[1] = 1
for i in range(2, h+w):
    table[i] = (table[i-1]*i)%MOD

bunsi = table[h+w-2]
bunbo = (table[h-1]*table[w-1])%MOD

ans = (bunsi * pow(bunbo, MOD-2, MOD))%MOD
print(ans)