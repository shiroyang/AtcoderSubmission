# kyopro_friends
# ずらさないバージョンはGCD(D, K)を一通り塗るだけ

def gcd(a, b):
    if b > a: a, b = b, a
    if b == 0: return a
    else: return gcd(b, a%b)

def solve(n, d, k):
    k -= 1
    g = gcd(n, d)
    perimeter = n // g
    shifting = (k) // perimeter
    rem = k - perimeter * shifting
    # optimize!
    '''
    for i in range(rem):
        shifting = (shifting + d) % n
    '''
    shifting = (shifting + d*rem) % n 
    return shifting

t = int(input())
for _ in range(t):
    n, d, k = map(int, input().split())
    print(solve(n, d, k))