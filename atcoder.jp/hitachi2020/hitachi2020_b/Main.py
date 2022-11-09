a ,b, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Coupons = [list(map(int, input().split())) for _ in range(m)]
min_ans = min(i for i in A) + min (j for j in B)


for coupon in Coupons:
    x ,y, c = coupon
    tmp = A[x-1] + B[y-1] - c
    min_ans = min(min_ans, tmp)

print(min_ans)