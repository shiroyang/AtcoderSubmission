s = input()
num = s[1:-1]
if len(num) <= 5:
    print("No")
    exit()
    
if 'A' <= s[0] <= 'Z':
    if 'A' <= s[-1] <= 'Z':
        if num[0] != '0':
            if num.isdigit():
                num = int(num)
                if 100000 <= num <= 999999:
                    print("Yes")
                    exit()
print("No")
        