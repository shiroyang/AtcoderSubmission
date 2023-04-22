_ = input()
s = input()

cnt1 = 0
cnt2 = 0
for i in s:
    if i == '|':
        cnt1 += 1
    if i == '*' and cnt1 == 1:
        exit(print('in'))

print('out')