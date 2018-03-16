import functools

N = int(input())
D = [0]*N
for i in range(N):
    D[i] = [int(x) for x in input().split()]
Q = int(input())
P = [int(input()) for i in range(Q)]

max_values = [0 for i in range(N*N+1)]

taste = [[0 for i in range(N)] for j in range(N)]
taste[0][0] = D[0][0]
for i in range(1, N):
    taste[0][i] = D[0][i] + taste[0][i-1]
    taste[i][0] = D[i][0] + taste[i-1][0]

for i in range(1,N):
    for j in range(1,N):
        taste[i][j] = taste[i-1][j] + taste[i][j-1] - taste[i-1][j-1] + D[i][j]
print(taste)

for si in range(N):
    for sj in range(N):
        for ei in range(si, N):
            for ej in range(sj, N):
                row = 0 if si == 0 else taste[ei][sj-1]
                col = 0 if sj == 0 else taste[si-1][ej]
                mid = 0 if si == 0 or sj == 0 else taste[si-1][sj-1] 

                v = mid - col - row + taste[ei][ej]
                size = abs(si-ei+1)*abs(sj-ej+1)
                print(si, sj, ei, ej, size, v)
                max_values[size] = max(max_values[size], v)

for p in P:
    print(max(max_values[:p+1]))