H, W = map(int, input().split())
Mat = [list(input()) for _ in range(H)]

Mat = map(list, zip(*Mat))


for li in Mat:
    cnt = 0
    for item in li:
        if item == '#':
            cnt += 1
    print(cnt, end=' ')
print()