# upsolve
_, s = input(), input()
print(max(map(len, s.split('-'))) if '-' in s and 'o' in s else -1)