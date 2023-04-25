# 変化量だけ保管する

D = int(input())
X = int(input())
A = [int(input()) for _ in range(D-1)]
Accum = [0]

for i in range(len(A)):
    Accum.append(Accum[-1] + A[i])
    
Q = int(input())
for _ in range(Q):
    s, t = map(lambda x: int(x)-1, input().split())
    if Accum[s] > Accum[t]:
        print(s+1)
    elif Accum[s] < Accum[t]:
        print(t+1)
    else: print("Same")