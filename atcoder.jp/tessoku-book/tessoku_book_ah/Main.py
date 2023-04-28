# Grundy数

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

# まずは個数によるグランディー数を計算,X個かY個しかとれないので、最大で2
grundy = [0]*100001
mex = [False]*3

def find_mex(M):
    for i in range(len(M)):
        if M[i] == False:
            return i

for i in range(100001):
    mex = [False]*3
    if i >= X:
        mex[grundy[i-X]] = True
    if i >= Y:
        mex[grundy[i-Y]] = True
    grundy[i] = find_mex(mex) # type: ignore

cond = 0
for item in A:
    cond ^= grundy[item]
print("Second" if cond == 0 else "First")