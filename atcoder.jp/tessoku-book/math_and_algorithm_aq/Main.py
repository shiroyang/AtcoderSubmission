# Upsolve
MOD = 10**9+7
# x^n
def my_pow(x, n):
    ans = 1
    while n:
        if n & 1:
            ans = ans * x % MOD
        x =  x ** 2 % MOD
        n >>= 1
    return ans

a, b = map(int, input().split())
print(my_pow(a, b))