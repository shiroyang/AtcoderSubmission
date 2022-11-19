def is_legal(h, m):
    if 0 <= h <= 23 and 0 <= m <= 59:
        return True
    return False

def swap_time(h, m):
    h0 = h // 10
    h1 = h % 10
    m0 = m // 10
    m1 = m % 10
    p = h0*10+m0
    q = h1*10+m1
    return (p,q)
    

h, m = map(int, input().split())
while True:
    p, q = swap_time(h, m)
    if is_legal(p, q):
        print(h, m)
        exit()
        
    m += 1
    if m >= 60:
        m -= 60
        h += 1
    if h >= 24:
        h -= 24