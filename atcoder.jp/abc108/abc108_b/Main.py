import math
def rotate(x1, y1, x2, y2):
    theta = math.atan((y2-y1)/(x2-x1))
    r = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return(-1*r*math.sin(theta), r*math.cos(theta))

x1, y1, x2, y2 = map(int, input().split())
delta_x = x2 - x1
delta_y = y2 - y1
x3 = x2 - delta_y
y3 = y2 + delta_x
x4 = x3 - delta_x
y4 = y3 - delta_y
print(x3, y3, x4, y4)