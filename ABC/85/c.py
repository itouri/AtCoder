# 31'24"
N, Y = list(map(int, input().split()))
Y //= 1000
for x in range(0, Y//10+1):
    for y in range(0, (Y-10*x)//5+1):
        z = N-x-y
        if (9*x + 4*y) == Y-N and z >= 0:
            print(x, y, N-x-y)
            exit()
print(-1, -1, -1)
