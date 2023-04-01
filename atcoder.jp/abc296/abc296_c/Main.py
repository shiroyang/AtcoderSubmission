from bisect import bisect_left

n, x = map(int, input().split())
A = list(map(int, input().split()))
B = A
A.sort()

for item in B:
    looking_for = item + x
    po = bisect_left(A, looking_for)
    if po >= n:
        continue
    num = A[po]
    if num == looking_for:
        print("Yes")
        exit()
        
print("No")