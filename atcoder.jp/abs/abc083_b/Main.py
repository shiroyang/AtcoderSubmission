n, a, b = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    bit_sum = 0
    num = i
    while num > 0:
        bit_sum += num % 10
        num = num // 10
    if bit_sum >= a and bit_sum <= b:
        cnt += i
print(cnt)