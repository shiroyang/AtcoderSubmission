n, k = map(int, input().split())
if (k%2 == 0 and 2*n-2 <= k):
    print("Yes")
else:
    print("No")