H, W, D = list(map(int, input().split()))
A = []
for i in range(H):
    A.append(list(map(int, input().split())))
Q = int(input())
LR = []
for i in range(Q):
    LR.append(list(map(int, input().split())))

for lr in LR:
    mp = 0
    l, r = lr[0], lr[1]
    while l != r:
        for i range(len(A))
            for j range(len(A[i]))
                if A[i][j] == l+D:
                    index = A.index(l+D)
