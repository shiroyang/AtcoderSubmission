def gcd(a, b):
    if a < b: a, b = b, a
    if b == 0: return a
    else: return gcd(b, a%b)
    
a, b = map(int ,input().split())
gg = gcd(a, b)
ll = a * b // gg

print(ll if ll <= 10**18 else "Large")