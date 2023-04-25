# 12 * (7**(N-1))
# 累乗

def my_pow(n, x):
    ans = 1
    while x != 0:
        if x & 1:
            ans = ans * n % MOD
        n = n ** 2 % MOD
        x >>= 1
    return ans

MOD = 10**9+7
W = int(input())
if W == 1:
    exit(print(12))
else:
    ans = (12*my_pow(7, W-1))%MOD
    print(ans)