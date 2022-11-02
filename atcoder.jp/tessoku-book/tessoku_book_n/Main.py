def merge(P, Q, set0):
    for i in P:
        for j in Q:
            set0.add(i+j)
    return set0

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
set1 = set()
set2 = set()
set1 = merge(A, B, set1)
set2 = merge(C, D, set2)

for item in set1:
    if k - item in set2:
        print("Yes")
        exit()
print("No")