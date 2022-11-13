n = int(input())
k = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in arr:
    ans += min(i, k-i)
print(2*ans)