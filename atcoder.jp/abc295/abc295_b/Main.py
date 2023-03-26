# B問題なのでDFSしなくていい
# ただし、爆弾を吹き飛ばさないようにする必要があるため、一回記録する

def kyori(p1, p2):
    return abs(p2[0]-p1[0])+abs(p2[1]-p1[1])

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))

bomb = []
for i, li in enumerate(board):
    for j, ele in enumerate(li):
        if ele.isdigit():
            bomb.append((i, j, int(ele)))

for i, li in enumerate(board):
    for j, ele in enumerate(li):
        for b in bomb:
            p1 = (i, j)
            if kyori(p1, b) <= b[2]:
                board[i][j] = '.'

for li in board:
    print(''.join(li))