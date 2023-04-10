# Bit DP, TSP
# dp[i][j]: visited set i, current pos j, min dis
# {1, 3} + {2}
# 1010 | 0100
# i | (1<<k)
def calc_dis(j, k):
    x1, y1 = A[j]
    x2, y2 = A[k]
    dis = pow((x1-x2)**2 + (y1-y2)**2, 0.5)
    return dis

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

INF = 10**16
dp = [[INF]*N for _ in range(1<<N)]
# TSP could start from any point, let's start from 0
dp[0][0] = 0
                                
for i in range(1<<N):
    for j in range(N):
        # not reachable
        if dp[i][j] == INF: continue
        
        # kにまだ行ってなかったら行ってみる, j->k
        for k in range(N):
            if i & (1<<k) != 0: continue
            
            dp[i|(1<<k)][k] = min(dp[i|(1<<k)][k], dp[i][j] + calc_dis(j, k))
            
# 答えはdp[(1<<N)-1][0]にある
print(dp[(1<<N)-1][0])