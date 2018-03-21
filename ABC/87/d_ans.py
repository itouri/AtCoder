# コレがないせいでずっと RE になってた
import sys
sys.setrecursionlimit(200002)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
x = [None] * N

def fail():
    print("No")
    exit()

def dfs(s):
    global x, G
    for t, d in G[s]:
        if x[t] is None:
            x[t] = x[s] + d
            dfs(t)
        else:
            if x[t] != x[s] + d:
                fail()

for _ in range(M):
    L, R, D = map(int, input().split())
    G[L-1].append([R-1,  D])
    G[R-1].append([L-1, -D])

for i in range(N):
    if x[i] is None:
        x[i] = 0
        dfs(i)

print("Yes")