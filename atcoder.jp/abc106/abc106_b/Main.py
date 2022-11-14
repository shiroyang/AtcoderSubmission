def check_prime(x):
    num = 0
    for i in range(1, x+1):
        if x % i == 0:
            num += 1
    return num

n = int(input())
ans = 0
for i in range(1, n+1, 2):
    if check_prime(i) == 8:
        ans += 1
print(ans)
