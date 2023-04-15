n = int(input())
s = input()

cnt1 = 0
cnt2 = 0

for i in s:
    if i == 'o':
        cnt1 += 1
    elif i == 'x':
        cnt2 += 1
        
if cnt1 >0 and cnt2 == 0:
    print("Yes")
else:
    print("No")