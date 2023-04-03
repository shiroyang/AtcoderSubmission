a, b = map(int, input().split())

if a > b: a, b = b, a
print("Yes" if b == 2*a or b == 2*a+1 else "No")