N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
S = [0]*4

for i in range(N):
    a, b = AB[i]
    if a+b > 0:
        S[0] += a+b
    if a-b > 0:
        S[1] += a-b
    if -a+b > 0:
        S[2] += -a+b
    if -a-b > 0:
        S[3] += -a-b
        
ans = 0
for i in range(4):
    ans = max(ans, S[i])
print(ans)