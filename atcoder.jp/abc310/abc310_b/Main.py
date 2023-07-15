n, m = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]

ans = False

for i in range(len(A)):
    for j in range(len(A)):
        if i == j: continue
        pi, ci, *fi = A[i]
        pj, cj, *fj = A[j]
        if pi >= pj:
            flag1 = True
            flag2 = False
            for item in fi:
                if item not in fj: 
                    flag1 = False
            if pi > pj:
                flag2 = True
            cnt = 0
            for item in fj:
                if item not in fi: cnt += 1
            if cnt >= 1: flag2 = True

            if flag1 and flag2: exit(print("Yes"))
print("No")