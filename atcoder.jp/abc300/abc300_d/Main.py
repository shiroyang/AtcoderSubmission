# a^2 * b * c^2 <= N
# a^5 < Yoshiki <= N => a < pow(N, 1/5)
# b^3 < b * c^2 < N => b < pow(N, 1/3)
# よって、a*b の全探索は N^(1/5)*N^(1/3) = N^(8/15)
# N = 10^12 => O(10**6.4)
# 2**2 * 3 * c**2 <= 10**12
# c <= 288676
# 愚直に計算かよw
from bisect import bisect_right

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table

_, table = sieve(288676)
N = int(input())
cnt = 0
powtable = [i*i for i in table]

limA = pow(N, 1/5)
limB = pow(N, 1/3)

maxi = bisect_right(table, limA)
maxj = bisect_right(table, limB)

for i in range(maxi):
    for j in range(i+1, maxj):
        cur = powtable[i] * table[j]
        if cur >= N: break
        for k in range(j+1, len(table)):
            if cur * powtable[k] > N:
                break
            cnt += 1
            
print(cnt)