# upsolveその2
# ランレングス圧縮　RLE
s = input()

ans = ''
cur = s[0]
cnt = 0

for item in s:
    if item == cur:
        cnt += 1
    else:
        ans += str(cur) + str(cnt)
        cur = item
        cnt = 1
        
ans += str(cur) + str(cnt)
print(ans)