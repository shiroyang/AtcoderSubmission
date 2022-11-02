import numpy as np
 
def check(arr):
    # check row
    for i in range(3):
        if arr[i][0]+arr[i][1]+arr[i][2] == -3:
            return("Yes")
 
    for j in range(3):
        if arr[0][j]+arr[1][j]+arr[2][j] == -3:
            return("Yes")
 
    if arr[0][0]+arr[1][1]+arr[2][2] == -3:
        return("Yes")
       
    if arr[0][2]+arr[1][1]+arr[2][0] == -3:
        return("Yes")
    
    return("No")
    
        
 
arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))
arr_flat = np.array(arr).reshape(9).tolist()
n = int(input())
for i in range(n):
    a = int(input())
    for idx, item in enumerate(arr_flat):
        if item == a:
            arr_flat[idx] = -1
arr = np.array(arr_flat).reshape(3,3).tolist()
print(check(arr))