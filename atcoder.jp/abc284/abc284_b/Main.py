n = int(input())
for _ in range(n):
    q = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for item in arr:
        if item % 2 == 1:
            ans += 1
    print(ans)