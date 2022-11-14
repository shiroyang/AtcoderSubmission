a, b, c, x, y = map(int, input().split())

first = min(a+b, 2*c)
second = min(a, 2*c)
third = min(b, 2*c)
cost = min(x, y) * first
if x > y:
    cost += second*(x-y)
elif x < y:
    cost += third*(y-x)
print(cost)