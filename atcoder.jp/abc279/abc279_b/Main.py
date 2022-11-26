s = input()
t = input()

if s == t:
    print("Yes")
    exit()
if t in s:
    print('Yes')
else:
    print("No")