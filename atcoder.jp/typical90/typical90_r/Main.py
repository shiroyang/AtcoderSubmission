from math import sin, cos, pi, atan, sqrt
T = int(input())
L, X, Y = map(int, input().split())


def get_coordinate(t):
    t %= T
    ratio = t / T
    theta = ratio * 2 * pi
    x = - L/2 * sin(theta)
    y = L/2 - L/2 * cos(theta) 
    return (x, y)

def solve(x):
    p = get_coordinate(x)
    u, v = p
    soko = sqrt(X**2 + (Y-u)**2)
    return atan(v/soko) / pi * 180


Q = int(input())
for _ in range(Q):
    x = int(input())
    print(solve(x))