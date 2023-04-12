# 数学問題
# Reverse of Euclid

x, y = map(int, input().split())

if x==1 and y==1:
    exit(print(0))

ans = [(x, y)]
while x!= 1 or y != 1:
    if x > y:
        x -= y
    else:
        y -= x
    ans.append((x, y))

ans.pop()
print(len(ans))
while ans:
    print(*ans.pop())