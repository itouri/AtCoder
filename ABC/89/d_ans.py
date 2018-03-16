H, W, D = list(map(int, input().split()))
A = []
for i in range(H):
    A.append(list(map(int, input().split())))
Q = int(input())
LR = []
for i in range(Q):
    LR.append(list(map(int, input().split())))

d = [0 for i in range(H*W+1)]
sA = [0 for i in range(H*W+1)]

for i in range(len(A)):
        for j in range(len(A[i])):
            sA[A[i][j]] = [i, j]

for i in range(D+1, H*W+1):
    d[i] = d[i-D] + abs(sA[i][0]-sA[i-D][0]) + abs(sA[i][1]-sA[i-D][1])

for lr in LR:
    l, r = lr[0], lr[1]
    print(d[r] - d[l])
    