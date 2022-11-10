mo = lambda x: x % 10000

n = int(input())
ans = 0
for i in range(n):
    sig, num = input().split()
    num = int(num)
    if sig == '+':
        ans = mo(ans + mo(num))
    if sig == '*':
        ans = mo(ans * mo(num))
    if sig == '-':
        ans = mo(ans - mo(num))
        if (ans < 0):
            ans = ans + 10000
    print(ans)