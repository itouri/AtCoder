N, H = list(map(int, input().split()))
maxA = 0
n = 0
b = []
for _ in range(N):
    ta, tb = list(map(int, input().split()))
    maxA = max(maxA, ta)
    b.append(tb)

b = list(filter(lambda x: x > maxA, b))
b.sort()

while H > 0 and b:
    H -= b.pop()
    n += 1

print(n + max(H-1, -1) // maxA + 1 )