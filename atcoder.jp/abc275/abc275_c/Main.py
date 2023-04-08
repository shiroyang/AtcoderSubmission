# Counting Squares
# 一点を決めて、右下の点を二つ目の点とみなす
# 真横を含まず、真下を含むことにより一意に定まる
'''
****
*  *
****
'''

s = [list(input()) for _ in range(9)]
cnt = 0

for i1 in range(9):
    for i2 in range(9):
        for j1 in range(9):
            for j2 in range(9):
                if i2 > i1 and j2 <= j1 and s[i1][j1] == '#' and s[i2][j2] == '#':
                    dx = i2 - i1
                    dy = j1 - j2
                    i3 = i2 - dy
                    j3 = j2- dx
                    i4 = i3 - dx
                    j4 = j3 + dy
                    
                    if 0 <= i3 <= 8 and 0 <= j3 <= 8 and 0 <= i4 <= 8 and 0 <= j4 <= 8:
                        if s[i3][j3] == '#' and s[i4][j4] == '#':
                            cnt += 1

print(cnt)