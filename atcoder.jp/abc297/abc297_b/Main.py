ans = 1
s = input()
cnt = 0
C = []
D = []
idx = 0
for i in range(len(s)):
    if s[i] == 'B':
        C.append(i+1)
    elif s[i] == 'K':
        idx = i+1
    elif s[i] == 'R':
        D.append(i+1)
if C[0] % 2 == 0 and C[1] % 2 == 0:
    ans = 0
if C[1] % 2 == 1 and C[0] % 2 == 1:
    ans = 0
    
if idx > D[1] or idx < D[0]:
    ans = 0
    
print("Yes" if ans else "No")