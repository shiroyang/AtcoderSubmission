from bisect import bisect_left
d = int(input())
n = int(input())
m = int(input())
tenpo = [0, d]
for _ in range(n-1):
    tenpo.append(int(input()))
takuhai = [int(input()) for _ in range(m)]

tenpo.sort()
takuhai.sort()
ans = 0
for item in takuhai:
    pos = bisect_left(tenpo, item)
    if pos == 0 or pos == len(tenpo) - 1:
        ans += min(abs(tenpo[0]-item), abs(tenpo[-1]-item), abs(tenpo[-2]-item), abs(tenpo[1]-item))
    else:
        ans += min(abs(tenpo[pos]-item), abs(tenpo[pos+1]-item), abs(tenpo[pos-1]-item))

print(ans)