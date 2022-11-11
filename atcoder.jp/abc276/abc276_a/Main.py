s = input()
idx = len(s)-1
while s[idx] != 'a' and idx >= 1:
    idx-=1
if s[idx] == 'a':
    print(idx+1)
else:
    print("-1")