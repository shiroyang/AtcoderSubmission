n =  int(input())
cnt = 0

for _ in range(n):
    if input() == 'For':
        cnt += 1

if cnt * 2 >= n:
    print("Yes")
else:
    print("No")