from collections import defaultdict
import numpy as np
h, w = map(int, input().split())
Mat1 = []
Mat2 = []
ref1 = defaultdict(int)
ref2 = defaultdict(int)

for i in range(h):
    s = input()
    tmp = []
    for i in s:
        if i == '#':
            tmp.append(1)
        else:
            tmp.append(0)
    Mat1.append(tmp)

for i in range(h):
    s = input()
    tmp = []
    for i in s:
        if i == '#':
            tmp.append(1)
        else:
            tmp.append(0)
    Mat2.append(tmp)

Mat1 = np.array(Mat1).transpose()
Mat2 = np.array(Mat2).transpose()
for li in Mat1:
    tmp = tuple(li)
    ref1[tmp] += 1

for li in Mat2:
    tmp = tuple(li)
    ref2[tmp] += 1

for key1, value1 in ref1.items():
    if key1 in ref2 and ref2[key1] == ref1[key1]:
        pass
    else:
        print("No")
        exit()
print("Yes")