# OK 1:01'57
import math
N = int(input()) - 1
CSF = [list(map(int, input().split())) for _ in range(N)]

def station(time, i):
    if i == N:
        print(time)
        return
    c, s, f = CSF[i]
    nextTime = s + c if time <= s else math.ceil(time / f) * f + c
    station(nextTime, i+1)

for i in range(N):
    station(0, i)
print(0)