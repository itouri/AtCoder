def add_grid(I, J, x, y):
    v = 0
    for i in range(I, I+y):
        for j in range(J, J+x):
            v = v + D[i][j]
    return v

N = input()
D = []
for i in range(N):
    D.append(map(int, raw_input().split()))
Q = input()
P = []
for i in range(Q):
    P.append(input())

query = []
for i in range(N):
    for j in range(i, N):
        query.append([i+1, j+1])

max_values = [0 for i in range(N*N+1)]
for q in query:
    x = q[0]
    y = q[1]
    for i in range(N-y+1):
        for j in range(N-x+1):
            v = add_grid(i, j, x, y)
            if v > max_values[x*y]:
                max_values[x*y] = v
max = 0
for i in range(len(max_values)):
    if max_values[i] > max:
        max = max_values[i]
    else:
        max_values[i] = max

# search
for p in P:
    #print(str(max_values))
    print(max_values[p])