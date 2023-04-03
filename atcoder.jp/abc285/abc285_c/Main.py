# 26進法 -> decimal

s = input()
cnt = 0
for idx in range(len(s)):
    c = s[idx]
    num = ord(c) - 64
    cnt = cnt * 26 + num
print(cnt)