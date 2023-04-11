# エラトステネスの篩
# 写経

def sieve(n):
    is_prime = [True]*(n+1)
    # 0-index
    is_prime[0] = False

    # 2 から穴埋めをする    
    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:                
                is_prime[j-1] = False
                j += i
    table = [i for i in range(1, n+1) if is_prime[i-1]]
    return table    

N = int(input())
table = sieve(N)
print(*table, sep='\n')