# Naive Matching Takes O(n^2)
# Make a prefix and suffix table in O(n), so that matching could be done in O(1)
s = list(input())
t = list(input())
delta = len(s) - len(t)
pre = [True]*(len(t)+1)
suf = [True]*(len(t)+1)

# make prefix table
for idx in range(len(t)):
    if pre[idx] == False:
        pre[idx + 1] = False
        continue
    if s[idx] == t[idx] or s[idx] == '?' or t[idx] == '?':
        continue
    else:
        pre[idx+1] = False

s = s[::-1]
t = t[::-1]

# make suffix table
for idx in range(len(t)):
    if suf[idx] == False:
        suf[idx + 1] = False
        continue
    if s[idx] == t[idx] or s[idx] == '?' or t[idx] == '?':
        continue
    else:
        suf[idx+1] = False

# prev i-th letters from s
for i in range(len(t)+1):
    if pre[i] and suf[len(t) - i]:
        print("Yes")
    else:
        print("No")