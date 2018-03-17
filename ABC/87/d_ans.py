N, M = list(map(int, input().split()))
G = [[] for _ in range(N+1)]
x = [None] * (N+1)

def fail():
    print("No")
    exit()

def dfs(s):
    for t, d in G[s]:
        if x[t] is None:
            x[t] = x[s] + d
            dfs(t)
        else:
            if x[t] != x[s] + d:
                fail()

for _ in range(M):
    L, R, D = map(int, input().split())
    G[L].append([R,  D])
    G[R].append([L, -D])

for i in range(N):
    if x[i] is None:
        x[i] = 0
        dfs(i)

print("Yes")