s = input()
idx = 0
ans = 0
while idx < len(s):
    if '1' <= s[idx] <= '9':
        ans += 1
        idx += 1
    elif s[idx] == '0':
        if idx + 1 < len(s) and s[idx+1] == '0':
            idx += 2
            ans += 1
        else:
            idx += 1
            ans += 1
                
print(ans)