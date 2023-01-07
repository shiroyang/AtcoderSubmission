from math import sqrt
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

is_prime, table = sieve(4000000)
n = int(input())
for _ in range(n):
    num = int(input())
    idx = 0
    while idx < len(table):
        if num % table[idx] != 0:
            idx += 1
            continue
        else:
            #case1, p == table[idx]            
            if num % (table[idx]**2) == 0:
                print(table[idx], num // (table[idx]**2))
                break
            else: 
                print(round(sqrt((num // table[idx]))), table[idx])
                break