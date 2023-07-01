A = list(map(int, input().split()))
B = sorted(A)
if B!= A:
    exit(print("No"))
for i in range(8):
    if A[i] % 25 != 0:
        exit(print("No"))
    if A[i] < 100 or A[i] > 675:
        exit(print("No"))
print("Yes")