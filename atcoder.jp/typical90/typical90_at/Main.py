# Bucket
def arr_to_bucket(A):
    Bucket = [0]*46
    for item in A:
        Bucket[item%46] += 1
    return Bucket
    
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = arr_to_bucket(A)
B = arr_to_bucket(B)
C = arr_to_bucket(C)

ans = 0
for i in range(46):
    for j in range(46):
        rem = (46 - (i+j)%46) % 46
        ans += A[i] * B[j] * C[rem]
print(ans)