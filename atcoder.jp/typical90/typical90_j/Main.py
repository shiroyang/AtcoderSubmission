# Separate two arrays
N = int(input())
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    if a == 1:
        A.append(b)
        B.append(0)
    else:
        A.append(0)
        B.append(b)
        
AccA = [0]
AccB = [0]

for i in range(len(A)):
    AccA.append(AccA[-1]+A[i])
    
for i in range(len(B)):
    AccB.append(AccB[-1]+B[i])
    
Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    ans1 = AccA[r] - AccA[l-1]
    ans2 = AccB[r] - AccB[l-1]
    print(ans1, ans2)
    
