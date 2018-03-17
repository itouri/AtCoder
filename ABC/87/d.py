N, M = list(map(int, input().split()))
LRD = [list(map(int, input().split())) for i in range(M) ]
x = [-1]*(N+1)
unsolve = LRD

if M == 0:
    print("Yes")
    exit()

def sr(unsolves):
    nextUnsolve = []
    for u in unsolves:
        l, r, d = u
        if x[l] == -1 and x[r] == -1:
            nextUnsolve.append(u)
        elif x[l] == -1:
            x[l] = x[r] - d
        elif x[r] == -1:
            x[r] = x[l] + d
        else:
            if x[r] != x[l] + d:
                print("No")
                exit()
    if len(nextUnsolve) != 0 and unsolves != nextUnsolve:
        sr(nextUnsolve)

x[LRD[0][0]] = 0
sr(unsolve)

print("Yes")