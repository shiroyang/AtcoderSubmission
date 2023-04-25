# Divisor Enumeration

def make_divisor(n):
    lower_divisor, upper_divisor = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisor.append(i)
            if i * i != n:
                upper_divisor.append(n//i)
        i += 1
        
    return lower_divisor + upper_divisor[::-1]

N = int(input())
print(*make_divisor(N), sep='\n')