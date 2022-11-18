from math import factorial
def calc_comb(x):
    if x == 3:
        return 1
    return x*(x-1)*(x-2)/6


n = int(input())
ans_lis = [0]*110
ans = 0
arr = list(map(int, input().split()))

for i in range(n):
    ans_lis[arr[i]] += 1

for i in range(1, len(ans_lis)):
    if ans_lis[i] >= 3:
        ans += calc_comb(ans_lis[i])
print(round(ans))