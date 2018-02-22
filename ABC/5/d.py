N = int(input())
D = [0]*N
for i in range(N):
    D[i] = [int(x) for x in input().split()]
Q = int(input())
P = [0]*Q
for i in range(Q):
    P[i] = int(input())

query = [[i,j] for i in range(1,N+1) for j in range(1,N+1)]
max_values = [0 for i in range(N*N+1)]

for q in query:
    x, y = q[0], q[1]
    for i in range(N-y+1):
        for j in range(N-x+1):
            v = sum([D[k][l] for k in range(i, i+y) for l in range(j, j+x)])
            max_values[x*y] = max(v, max_values[x*y])

for p in P:
    print(max(max_values[:p+1]))