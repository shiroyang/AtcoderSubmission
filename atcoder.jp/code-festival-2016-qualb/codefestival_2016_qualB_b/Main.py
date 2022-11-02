n, a, b = map(int, input().split())
s = input()
cnt = 0
cnt2 = 0

for i in s:
    if i == 'c':
        print("No")
    elif i == 'a' and cnt < a+b:
        cnt += 1
        print("Yes")
    elif i == 'b' and cnt < a+b and cnt2 < b:
        cnt += 1
        cnt2 += 1
        print("Yes")
    else:
        print("No")