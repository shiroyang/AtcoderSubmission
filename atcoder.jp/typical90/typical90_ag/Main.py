H, W = map(int, input().split())
if H == 1 or W == 1:
    exit(print(max(H, W)))

ans = ((H+1)// 2) * ((W+1) // 2)

print(ans)