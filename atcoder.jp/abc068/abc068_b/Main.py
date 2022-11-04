n = int(input())
if n == 1:
    print("1")
    exit()
ans = 1
while ans <= n:
    ans <<= 1
ans >>= 1
print(ans)