from itertools import combinations
'''
def rotate_vec(p1, p2):
    x1,y1 = p1[0], p1[1]
    x2,y2 = p2[0], p2[1]
    vec = (x2-x1, y2-y1)
    v_prime = (-vec[1], vec[0])
    p3 = (p2[0]+v_prime[0], p2[1]+v_prime[1])
    return p3    
'''
rotate_vec = lambda p1,p2: (p2[0]+p1[1]-p2[1], p2[1]+p2[0]-p1[0])
'''
def calc_area(p1, p2):
    dx = p2[0]-p1[0]
    dy = p2[1]-p1[1]
    area = dx**2 + dy**2
    return area
'''
calc_area = lambda p1,p2: pow(p2[0]-p1[0], 2)+ pow(p2[1]-p1[1], 2)

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
ref = set(arr)
ans = 0
'''
ref = set()
for _ in range(n):
    p = tuple(map(int, input().split()))
    arr.append(p)
    ref.add(p)
'''

for p1, p2 in combinations(arr, 2):
    p3 = rotate_vec(p1, p2)
    p4 = rotate_vec(p2, p3)
    if p3 in ref and p4 in ref:
        ans = max(ans, calc_area(p3, p4))
print(ans)