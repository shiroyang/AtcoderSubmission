from math import floor

n = int(input())
ans = n // 1.08
for i in range(-1, 2):
    if floor((ans+i)*1.08) == n:
        print(round(ans+i))
        exit()
print(":(")