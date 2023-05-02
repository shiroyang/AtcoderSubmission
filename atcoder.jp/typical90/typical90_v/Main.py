def gcd(a, b):
    if a < b: a,b=b,a
    if b == 0: return a
    return gcd(b, a%b)

a, b, c = map(int, input().split())
min_len = gcd(gcd(a,b), c)

cnt = a // min_len + b // min_len + c // min_len -3
print(cnt)