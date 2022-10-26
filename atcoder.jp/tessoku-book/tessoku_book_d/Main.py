import math
a = int(input())
b = 1 << 9
while(b != 0):
    if a >= b:
        a -= b
        b = b >> 1
        print("1", end='')
    else:
        b = b >> 1
        print("0", end='')