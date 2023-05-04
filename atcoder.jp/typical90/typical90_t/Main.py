# blog2c = log2(c**b)
# a < c**b

# a**x = 3 * (101) = 3*1 * 9*0 * 81 * 1 = 243 
def my_pow(a, x):
    num = 1
    while x != 0:
        if x & 1:
            num *= a
        a = a ** 2
        x >>= 1
    return num

a, b, c = map(int, input().split())
if a < my_pow(c, b):
    print("Yes")
else:
    print("No")