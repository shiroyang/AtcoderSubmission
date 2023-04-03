# A操作とB操作の順番は入れ替えて良い
# A操作は[0, n-1]回行える
# A操作後にB回数を行う回数も定まる

def calc(tmp, cur):
    l = 0
    r = len(tmp) - 1
    while l < r:
        if tmp[l] != tmp[r]:
            cur += b    
        l += 1
        r -= 1
    return cur

n, a, b = map(int, input().split())
s = list(input())
cur_min = 10**16

for i in range(n):
    cur = a*i
    tmp = s[i:] + s[:i]
    cur_min = min(cur_min, calc(tmp, cur))
    
print(cur_min)