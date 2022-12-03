#　素因数分解、二分探索で答えを探す
from collections import defaultdict
soinsu = defaultdict(int)

k = int(input())
res = k
i = 2
while i**2 <= res:
    if res % i == 0:
        while res % i == 0:
            soinsu[i]+= 1
            res //= i
    i += 1
    
if res > 1:
    soinsu[res] += 1

l = 1
r = k
'''
ここも重要！
if l < r:
l = 1, r = 2
mid = (2+1)// 2 = 1
mid では条件を満たさないとなると
l = mid = 1
l = 1, r = 2
本来はここで２をアウトプットする必要がある
if l+1 < r:
l = 1, mid = 2, r = 3
midでは条件を満たさない
l = mid = 2
2+1 < 3 == Falseであるため
3をアウトプットする
'''
while l+1 < r:
    mid = (l+r)// 2
    flag = True
    for key, value in soinsu.items():
        res = mid
        cnt = 0
        while res > 0:
            cnt += res // key
            res //= key
        if cnt < value:
            flag = False
            break
        
    # まだ改善できる
    if flag:
        r = mid
    else:
        l = mid        
print(r)