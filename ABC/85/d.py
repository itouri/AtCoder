import math
N, H = list(map(int, input().split()))
maxA = 0
b = []
for _ in range(N):
    ta, tb = list(map(int, input().split()))
    maxA = max(maxA, ta)
    b.append(tb)

b = list(filter(lambda x: x > maxA, b))
b.sort()
b.reverse()
if not b:
    print(math.ceil(H / maxA))
    exit()

slashNum = math.ceil( (H - sum(b)) / maxA )
dmg = slashNum * maxA
for i in range(N):
    dmg += b[i]
    if dmg >= H:
        print(slashNum + i + 1)
        exit()