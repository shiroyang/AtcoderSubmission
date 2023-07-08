a, b = map(int, input().split())
if a > b:
    a, b = b, a

if b - a == 1 and a%3!=0:
    print("Yes")
else:
    print("No")