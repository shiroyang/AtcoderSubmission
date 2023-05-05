MOD = 10**9+7
l, r  = map(int, input().split())

l_keta = len(str(l))
r_keta = len(str(r))
cnt = 0

def my_sum(a, b):
    return (a+b)*(b-a+1)//2%MOD

if l_keta == r_keta:
    cnt += l_keta * my_sum(l ,r) % MOD
else:
    cnt += l_keta * my_sum(l, 10**l_keta - 1) % MOD
    cnt += r_keta * my_sum(10**(r_keta-1), r) % MOD   
    for i in range(l_keta+1, r_keta):
        cnt += i * my_sum(10**(i-1), 10**i - 1)
        cnt %= MOD
    
print(cnt % MOD)