h, w = map(int, input().split())
ans = 0
for i in range(h):
    s= input()
    for ele in s:
        if ele == '#':
            ans += 1
            
print(ans)