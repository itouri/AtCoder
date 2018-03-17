N, M = list(map(int, input().split()))
LRD = [list(map(int, input().split())) for i in range(M) ]

G = [[] for _ in range(N+1)]
for lrd in LRD:
    l, r, d = lrd
    G[l][r] = d
    G[r][l] = -d
