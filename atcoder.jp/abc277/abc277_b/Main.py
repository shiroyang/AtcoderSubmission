n = int(input())
flag = True
ref = {}
for i in range(n):
    s = input()
    if s[0] == 'H' or s[0] == 'D' or s[0] == 'C' or s[0] == 'S':
        if s[1] == 'A' or s[1] == '2' or s[1] == '3' or s[1] == '4' or s[1] == '5' or s[1] == '6' or s[1] == '7' or s[1] == '8' or s[1] == '9' or s[1] == 'T' or s[1] == 'J' or s[1] == 'Q' or s[1] == 'K':
            if ref.get(s, -1) == -1:
                ref[s] = 1
            else:
                flag = False
        else:
            flag = False
    else:
        flag = False
if flag:
    print("Yes")
else:
    print("No")