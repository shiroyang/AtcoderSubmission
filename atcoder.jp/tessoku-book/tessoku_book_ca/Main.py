a,b = map(int, input().split())
flag= False
for i in range(a,b+1):
    if 100 % i == 0:
        if flag == False:
            print("Yes")
            flag = True
if not flag:
    print("No")