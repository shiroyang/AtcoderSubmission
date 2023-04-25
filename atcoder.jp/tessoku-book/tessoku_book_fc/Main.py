# 2進法

N = int(input()) - 1
A = []
for i in range(10):
    A.append(N%2)
    N >>= 1
A = A[::-1]
s = ''
for item in A:
    if item == 0:
        s+= '4'
    else:
        s += '7'

print(s)