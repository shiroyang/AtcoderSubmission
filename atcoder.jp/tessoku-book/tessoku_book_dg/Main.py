# Grundy数, X=2, Y=3 なので、他のコツでGrundy数を計算す
# 0, 0, 1, 1, 2 のループ
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
ref = [0, 0, 1, 1, 2]
# まずは個数によるグランディー数を計算,X個かY個しかとれないので、最大で2
def calc_grundy(x):
    return ref[x%5]

cond = 0
for item in A:
    cond ^= calc_grundy(item)

print("Second" if cond == 0 else "First")