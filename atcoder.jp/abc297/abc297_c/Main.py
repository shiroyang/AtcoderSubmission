# Greedy

h, w = map(int, input().split())
ans = []
for _ in range(h):
    s = list(input())
    for i in range(len(s)-1):
        if s[i] == 'T' and s[i+1] == 'T':
            s[i] = 'P'
            s[i+1] = 'C'
    ans.append(s)

for li in ans:
    print(''.join(li))