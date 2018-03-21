# AC 23'39
N = int(input())
txys = [list(map(int, input().split())) for _ in range(N) ]
txys.insert(0, [0, 0, 0])

for i in range(N):
    t1, x1, y1 = txys[i]
    t2, x2, y2 = txys[i+1]
    dt = t2 - t1
    tIsEven = dt % 2 == 0
    dist = abs(x1 - x2) + abs(y1 - y2)
    xyIsEven = dist % 2 == 0
    if tIsEven != xyIsEven or dist > t2:
        print("No")
        exit()
print("Yes")

