H, W, D = list(map(int, input().split()))
A = []
for i in range(H):
    A.append(list(map(int, input().split())))
Q = int(input())
LR = []

memo = [[0 for i in range(H*W)] for j in range(H*W)]

def calcMp(start, end):
    if memo[start][end] != 0:
        return memo[start][end]
    si, sj = sA[start]
    ei, ej = sA[end]
    mp = abs(si-ei) + abs(sj-ej)
    
    if start+D == end:
        memo[start][end] = mp
        return mp
    memo[start][end] = calcMp(start+D, end)
    return memo[start][end]


for i in range(Q):
    LR.append(list(map(int, input().split())))

sA = [0 for i in range(H*W+1)]

for i in range(len(A)):
        for j in range(len(A[i])):
            sA[A[i][j]] = [i, j]

for lr in LR:
    l, r = lr[0], lr[1]
    mp = calcMp(l, r)
    print(mp)
