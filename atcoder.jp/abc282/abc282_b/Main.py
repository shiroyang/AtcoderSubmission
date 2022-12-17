n, m = map(int, input().split())
Mat = []
for i in range(n):
    s = input()
    tmp = []
    for letter in s:
        if letter == 'o':
            tmp.append(1)
        else:
            tmp.append(0)
    Mat.append(tmp)

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        tmp1 = Mat[i]
        tmp2 = Mat[j]
        tmp3 = []
        flag = True
        for k in range(len(tmp1)):
            tmp3.append(tmp1[k] or tmp2[k])
        for k in range(len(tmp3)):
            if tmp3[k] == 0:
                flag = False
        if flag:
            ans += 1
            
print(ans)