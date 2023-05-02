d = set()
N = int(input())
for i in range(N):
    s = input()
    if s not in d:
        d.add(s)
        print(i+1)
    