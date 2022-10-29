n = int(input())
cur_time = 0
cur_x = 0
cur_y = 0
flag = True

for i in range(n):
    t, x, y = map(int, input().split())
    delta_time = abs(t - cur_time)
    delta_dis = abs(cur_x - x) + abs(cur_y - y)
    if (delta_time >= delta_dis and (delta_time-delta_dis) % 2 == 0):
        cur_time = t
        cur_x = x
        cur_y = y   
    else:
        flag = False
        print("No")
        exit()

print("Yes")