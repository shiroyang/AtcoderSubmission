from math import sqrt
n = int(input())
ans = 10**10

for i in range(1, round(sqrt(n))+1):
    if n % i == 0:
        left = i
        right = n // i
        tmp = max(len(str(left)), len(str(right)))
        ans = min(ans, tmp)
print(ans)