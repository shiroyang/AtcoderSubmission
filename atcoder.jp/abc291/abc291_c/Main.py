from collections import defaultdict



d = set()
d.add((0, 0))
Cur = (0, 0)
_ = input()
s = input()
for i in s:
    x, y = Cur
    if i == "U":
        y+=1
    elif i == "D":
        y-=1
    elif i == "L":
        x -= 1
    elif i == "R":
        x += 1
    Cur = (x, y)
    if Cur in d:
        print("Yes")
        exit()
    else:
        d.add(Cur)
print("No")