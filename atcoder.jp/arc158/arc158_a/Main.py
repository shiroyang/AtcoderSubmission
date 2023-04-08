t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    if (a+b+c)%3 == 0 and (a%2 == b%2) and(b%2 == c%2):
        d = (a+b+c) // 3
        ans = (abs(d-a) + abs(d-b) + abs(d-c)) // 4
        print(ans)
    else:
        print(-1)