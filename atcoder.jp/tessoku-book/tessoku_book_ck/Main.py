n = int(input())
err = 0.00009
l = 0
r = 10**6

def calc(x):
    p = pow(x,3)+x
    return p

mid = 0
while r-l > 0.001:
    mid = (r+l)/2
    if abs(calc(mid)-n) < err:
        print(mid)
        exit()
    elif calc(mid) < n:
        l = mid
    else:
        r = mid
        
print(mid)