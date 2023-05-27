N, M, H, K = map(int, input().split())
S = input()
A = set()
for _ in range(M):
    x, y = map(int, input().split())
    A.add((x, y))

cur = (0, 0)
for i in range(len(S)):
    x, y = cur
    if S[i] == 'R':
        cur = (x+1, y)
    elif S[i] == 'L':
        cur = (x-1, y)
    elif S[i] == 'U':
        cur = (x, y+1)
    elif S[i] == 'D':
        cur = (x, y-1)
    
    H -= 1
    if H < 0:
        exit(print("No"))
        
    if H >= K:
        continue
    
    if cur in A:
        H = K
        A.discard(cur)

print("Yes")
    