n, l = map(int, input().split())
ans = 0
for i in range(n):
    num, direction = input().split()
    num = int(num)
    tmp = None
    if direction == 'E':
        tmp = l - num
    else:
        tmp = num
    ans = max(ans, tmp)
print(ans)