# xor
# changing two lights at one time, thus number of odd/even will not change

n, k = map(int, input().split())
s = input()
cnt = s.count('1')
if cnt % 2 == k % 2:
    print("Yes")
else:
    print("No")