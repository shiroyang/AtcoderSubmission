def check(mid, k):
    sum = 0
    for item in arr:
        sum += mid // item
    if sum >= k:
        return True
    else:
        return False

n, k = map(int, input().split())
arr = list(map(int, input().split()))
l = 1
r = 10**9
while(l < r):
    mid = (l+r) // 2
    # 看看用mid天能不能完成任务
    ans = check(mid, k)
    # 完成不了就向右搜索
    if ans == False:
        l = mid + 1
    else:
        r = mid
print(l)