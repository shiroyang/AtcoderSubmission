d = set()
n = int(input())

for _ in range(n):
    s = input()
    d.add(min(s, s[::-1]))

print(len(d))