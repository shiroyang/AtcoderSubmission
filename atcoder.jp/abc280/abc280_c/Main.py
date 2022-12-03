s = input()
t = input()

flag = True
idx = min(len(s), len(t))

for i in range(idx):
    if s[i] == t[i]:
        pass
    elif flag:
        print(i+1)
        flag = False
        
if flag:
    print(idx+1)

