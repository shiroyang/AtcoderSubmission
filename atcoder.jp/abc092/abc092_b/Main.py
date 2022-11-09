n = int(input())
d, x = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
cnt = 0
day = 1
while day <= d:
    for i in range(n):
        if arr[i] == 1:
            cnt += 1
        elif day % arr[i] == 1:
            cnt += 1
    day += 1
    
print(cnt+x)