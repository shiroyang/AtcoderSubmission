n,q = map(int, input().split())
A = list(map(int, input().split()))
B = []
B.append(0)
for num in A:
    B.append(B[-1]+num)
for i in range(q):
    l,r = map(int, input().split())
    print(B[r] - B[l-1])