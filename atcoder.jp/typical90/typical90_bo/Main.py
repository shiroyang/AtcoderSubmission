N, K = map(int, input().split())

def oct_to_dec(x):
    num = 0
    digit = 1
    while x != 0:
        num += digit * (x % 10)
        x //= 10
        digit *= 8
    return num

def dec_to_nin(x):
    ans = []
    while x != 0:
        ans.append(x%9)
        x //= 9
    return ans[::-1]


tmp = N
for _ in range(K):
    dec = oct_to_dec(tmp)
    nin = dec_to_nin(dec)
    for i in range(len(nin)):
        if nin[i] == 8:
            nin[i] = 5
    tmp = 0
    for i in range(len(nin)):
        tmp += nin[i]
        tmp *= 10
    tmp //= 10

print(tmp)