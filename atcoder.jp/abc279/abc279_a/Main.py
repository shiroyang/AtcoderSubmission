s = input()
ans = 0
for i in s:
    if i == 'v':
        ans += 1
    elif i == 'w':
        ans += 2
print(ans)