MOD = 10**9+7

N, K = map(int, input().split())
if N == 1:
    exit(print(K))
elif N == 2:
    exit(print(K*(K-1)))

ans =  (K * (K-1) % MOD * pow(K-2, N-2, MOD))%MOD
print(ans)