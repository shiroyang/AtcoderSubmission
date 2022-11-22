n, q = map(int, input().split())
arr = [i for i in range(1, n+1)]
flag = 1

def get_index(i, flag):
    if flag:
        return i
    else:
        return n-i-1

for _ in range(q):
    li = list(map(int, input().split()))
    if li[0] == 1:
        index = get_index(li[1]-1, flag)
        arr[index] = li[2]
    elif li[0] == 2:
        flag ^= 1
    else:
        index = get_index(li[1]-1, flag)
        print(arr[index])