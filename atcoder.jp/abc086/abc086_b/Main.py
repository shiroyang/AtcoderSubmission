from math import sqrt
a = list(input().split())
s = int("".join(a))
if (sqrt(s) == int(sqrt(s))):
    print("Yes")
else:
    print("No")