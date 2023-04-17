n = hex(int(input()))
ans = n[2:].upper()
if len(ans) < 2:
    ans = '0'+ans
print(ans)