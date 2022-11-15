n = int(input())
arr = list(map(int, input().split()))

ans = 0
for num in arr:
    ans ^= num
if (ans == 0):
    print("Second")
else:
    print("First")