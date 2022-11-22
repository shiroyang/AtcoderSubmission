n, c = input().split()
s = input()
ans = 0
for letter in s:
    if letter == 'W':
        ans += 0
    elif letter == 'B':
        ans += 1
    else:
        ans += 2

ans %= 3
if ans == 0:
    ans = 'W'
elif ans == 1:
    ans = 'B'
else:
    ans = 'R'

if ans == c:
    print("Yes")
else:
    print("No")