N = input()
W = list(input().split())
ck = ['and', 'not','that','the', 'you']

for item in W:
    if item in ck:
        print("Yes")
        exit()
print("No")