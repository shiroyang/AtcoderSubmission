def calc(x):
    speed = pow(2, x/1.5)
    t = x + p / speed
    return t

p = float(input())

l = 0
r = 2000
err = 10**-8

while r-l > err:
    delta = (r - l) / 3
    lc = l + delta
    rc = r - delta
    if calc(lc) < calc(rc):
        r = rc
    else:
        l = lc

print(calc(r))