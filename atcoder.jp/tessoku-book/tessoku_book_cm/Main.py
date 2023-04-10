# 複数選んだ値がK
# 2**30 = 10**9 TLE
# 半分全列挙
# 2**15 = 32768, からbisect/set

n, k = map(int, input().split())
A =list(map(int, input().split()))
L = A[:n//2]
R = A[n//2:]
LL = set()
RR = set()

for i in range(1<<len(L)):
    tmp = 0
    for j in range(len(L)):
        if i>>j & 1:
            tmp += L[j]
    LL.add(tmp)

for i in range(1<<len(R)):
    tmp = 0
    for j in range(len(R)):
        if i>>j & 1:
            tmp += R[j]
    RR.add(tmp)
for item in LL:
    if k - item in RR:
        exit(print("Yes"))
print("No")