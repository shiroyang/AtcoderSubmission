a, b = map(int, input().split())
a = a % b
print(min(a, abs(a-b)))