from collections import defaultdict

def calc_comb(x):
    if x < 2:
        return 0
    return x*(x-1)//2

N = int(input())
d = defaultdict(int)
for _ in range(N):
    a = int(input())
    d[a] += 1
    
ans = 0
for key, val in d.items():
    ans += calc_comb(val)
print(ans)