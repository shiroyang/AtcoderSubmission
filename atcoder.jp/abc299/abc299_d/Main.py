N = int(input())

l = 1
r = N

def que(mid):
    print('?  {}'.format(mid), flush=True)
    return input()

for i in range(20):
    mid = (l+r)//2
    c = que(mid)
    if int(c) == 1:
        r = mid
    else:
        l = mid

print('! {}'.format(l))