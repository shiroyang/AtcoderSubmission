MOD = 10**9+7
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 1
for li in A:
    tmp = sum(li)
    ans *= tmp
    ans %= MOD
    
print(ans)